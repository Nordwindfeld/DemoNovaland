import psycopg2
from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'phase_4'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # --------------------------
    # Login
    # -------------------------

    IdAlle = models.StringField()
    IDPlayer = models.StringField()
    ID_korrekt = models.IntegerField()

    # ---------------------------
    # Ergebnis
    # --------------------------
    LPNStimmen = models.FloatField()
    LPNProzent = models.FloatField()
    SPNStimmen = models.FloatField()
    SPNProzent = models.FloatField()
    KPNStimme = models.FloatField()
    KPNProzent = models.FloatField()
    PPNStimmen = models.FloatField()
    PPNProzent = models.FloatField()


# PAGES
class Login(Page):
    form_model = 'player'

    @staticmethod
    def live_method(player: Player, data):
        if 'IdEingabe' in data:
            player.IDPlayer = data['ID']

        if player.IDPlayer in player.IdAlle:
            player.ID_korrekt = 1
            response = dict(type='IDKORREKT')
            return {0: response}

    @staticmethod
    def vars_for_template(player: Player):
        player.ID_korrekt = 0
        connection5 = psycopg2.connect(user='aipclfonwuiort',
                                       password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                       host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                       port='5432',
                                       database='dcoubsit8jsig0')

        cursor5 = connection5.cursor()
        id_script = 'SELECT Nutzer_ID from Novaland'
        cursor5.execute(id_script)
        id_value = cursor5.fetchall()
        player.IdAlle = str(id_value)
        cursor5.close()
        connection5.close()

        player.IDPlayer = ""


class Phase_4_Page_1_Bar_Chart(Page):
    @staticmethod
    def vars_for_template(player: Player):
        player.ID_korrekt = 0
        connection = psycopg2.connect(user='aipclfonwuiort',
                                       password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                       host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                       port='5432',
                                       database='dcoubsit8jsig0')

        cursor = connection.cursor()

        id_script = 'SELECT Partei FROM Novaland'
        cursor.execute(id_script)
        Abstimmen = cursor.fetchall()
        AlleStimmen = str(Abstimmen)
        player.KPNStimme = AlleStimmen.count("Konservative Partei Novaland")
        player.SPNStimmen = AlleStimmen.count("Soziale Partei Novaland")
        player.LPNStimmen = AlleStimmen.count("Liberale Partei Novaland")
        player.PPNStimmen = AlleStimmen.count("Partei Progressives Novaland")
        AlleStimmenZahl = player.KPNStimme + player.SPNStimmen + player.LPNStimmen + player.PPNStimmen
        player.KPNProzent = (player.KPNStimme/AlleStimmenZahl) * 100
        player.SPNProzent = (player.SPNStimmen / AlleStimmenZahl) * 100
        player.LPNProzent = (player.LPNStimmen / AlleStimmenZahl) * 100
        player.PPNProzent = (player.PPNStimmen / AlleStimmenZahl) * 100

        return{
            "LPNProzent": int(player.LPNProzent),
            "SPNProzent": int(player.SPNProzent),
            "KPNProzent": int(player.KPNProzent),
            "PPNProzent": int(player.PPNProzent)
        }

        cursor.close()
        connection.close()


page_sequence = [Login, Phase_4_Page_1_Bar_Chart]
