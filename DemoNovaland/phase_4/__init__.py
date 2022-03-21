import psycopg2
from otree.api import *
from datetime import *
from datetime import time


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


class Waiting_Site(Page):
    def is_displayed(player: Player):
        Zeit = 16 * 60 * 60
        ProgrammTagZeit = (datetime.now().time().hour * 60 * 60) + (datetime.now().time().minute * 60) + datetime.now().time().second
        differenz = Zeit - ProgrammTagZeit
        if differenz > 0:
            return True
        else:
            return False


class Phase_4_Page_1_Bar_Chart(Page):
    @staticmethod
    def vars_for_template(player: Player):
        player.IDPlayer = player.participant.code
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
        connection.close()


page_sequence = [Waiting_Site, Phase_4_Page_1_Bar_Chart]
