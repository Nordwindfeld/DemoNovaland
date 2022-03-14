import psycopg2
from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'phase_3'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Login
    IdAlle = models.StringField()
    IDPlayer = models.StringField()
    ID_korrekt = models.IntegerField()

    # Seite 6
    Partei = models.StringField()

    # Zeit
    S3P1Zeit = models.FloatField()
    S3P2Zeit = models.FloatField()
    S3P3Zeit = models.FloatField()
    S3P4Zeit = models.FloatField()
    S3P5Zeit = models.FloatField()
    S3P6Zeit = models.FloatField()
    S3P7Zeit = models.FloatField()

    # ------------------------------------------
    # Info, ob diese Runde schon gespielt worden ist
    # ------------------------------------------
    Runde_3_erledigt = models.StringField()


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


class Phase_3_Page_1(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP3S1" in data:
            player.S3P1Zeit = data["ZeitP3S1"]


class Phase_3_Page_2(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP3S2" in data:
            player.S3P2Zeit = data["ZeitP3S2"]


class Phase_3_Page_3(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP3S3" in data:
            player.S3P3Zeit = data["ZeitP3S3"]


class Phase_3_Page_4(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP3S4" in data:
            player.S3P4Zeit = data["ZeitP3S4"]


class Phase_3_Page_5(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP3S5" in data:
            player.S3P5Zeit = data["ZeitP3S5"]


class Phase_3_Page_6(Page):
    form_model = 'player'
    form_fields = ['Partei']

    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP3S6" in data:
            player.S3P6Zeit = data["ZeitP3S6"]


class Phase_3_Page_7(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP3S7" in data:
            player.S3P7Zeit = data["ZeitP3S7"]

    @staticmethod
    def vars_for_template(player: Player):
        player.Runde_3_erledigt = "Ja"


class Phase_3_Page_8(Page):
    @staticmethod
    def vars_for_template(player: Player):
        connection3 = psycopg2.connect(user='aipclfonwuiort',
                                       password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                       host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                       port='5432',
                                       database='dcoubsit8jsig0')

        cursor3 = connection3.cursor()

        update_rows = '''UPDATE Novaland SET Partei = %s, Runde_3_Erledigt = %s, Zeit_P3S1 = %s, Zeit_P3S2 = %s, Zeit_P3S3 = %s, Zeit_P3S4 = %s, Zeit_P3S5 = %s, Zeit_P3S6 = %s, Zeit_P3S7 = %s WHERE nutzer_id = %s'''
        update_values = (
        player.Partei, player.Runde_3_erledigt, player.S3P1Zeit, player.S3P2Zeit, player.S3P3Zeit, player.S3P4Zeit,
        player.S3P5Zeit, player.S3P6Zeit, player.S3P7Zeit, player.IDPlayer)
        cursor3.execute(update_rows, update_values)

        connection3.commit()
        cursor3.close()
        connection3.close()


page_sequence = [Login, Phase_3_Page_1, Phase_3_Page_2, Phase_3_Page_3, Phase_3_Page_4, Phase_3_Page_5, Phase_3_Page_6,
                 Phase_3_Page_7, Phase_3_Page_8]
