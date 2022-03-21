import psycopg2
from otree.api import *
from datetime import *
from datetime import time


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


class Waiting_Site(Page):
    def is_displayed(player: Player):
        Zeit = 14 * 60 * 60
        ProgrammTagZeit = (datetime.now().time().hour * 60 * 60) + (
                    datetime.now().time().minute * 60) + datetime.now().time().second
        differenz = Zeit - ProgrammTagZeit
        if differenz > 0:
            return True
        else:
            return False


class Phase_3_Page_1(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP3S1" in data:
            player.S3P1Zeit = data["ZeitP3S1"]

    @staticmethod
    def vars_for_template(player: Player):
        player.IDPlayer = player.participant.code


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


page_sequence = [Waiting_Site, Phase_3_Page_1, Phase_3_Page_2, Phase_3_Page_3, Phase_3_Page_4, Phase_3_Page_5,
                 Phase_3_Page_6,
                 Phase_3_Page_7, Phase_3_Page_8]
