import psycopg2
from otree.api import *
from datetime import *
from datetime import time
import time


class C(BaseConstants):
    NAME_IN_URL = 'phase_3'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Seite 1
    # Daten runterladen
    Geschlecht = models.StringField()
    NettoEinkommen = models.FloatField()
    Wohnungskosten = models.FloatField()
    Verpflegungskosten = models.FloatField()
    Mobilitaetskosten = models.FloatField()
    Resteinkommen = models.FloatField()
    KontoPhase3Anfang = models.FloatField() #für die Tabelle
    IDPlayer = models.StringField()

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
    S3P8Zeit = models.FloatField()
    UnixTimeP3S1 = models.FloatField()
    UnixTimeP3S2 = models.FloatField()
    UnixTimeP3S3 = models.FloatField()
    UnixTimeP3S4 = models.FloatField()
    UnixTimeP3S5 = models.FloatField()
    UnixTimeP3S6 = models.FloatField()
    UnixTimeP3S7 = models.FloatField()
    UnixTimeP3S8 = models.FloatField()

    # ------------------------------------------
    # Info, ob diese Runde schon gespielt worden ist
    # ------------------------------------------
    Runde_3_erledigt = models.StringField()


class Waiting_Site(Page):
    @staticmethod
    def is_displayed(player: Player):
        Zeit = 0 * 60 * 60
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
            player.UnixTimeP3S1 = time.time()

    @staticmethod
    def vars_for_template(player: Player):
        connection3 = psycopg2.connect(user='aipclfonwuiort',
                                       password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                       host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                       port='5432',
                                       database='dcoubsit8jsig0')

        cursor3 = connection3.cursor()
        IDValue = [player.participant.label]

        Geschlecht = '''SELECT Geschlecht FROM Novaland WHERE nutzer_id = %s'''
        cursor3.execute(Geschlecht, IDValue)
        player.Geschlecht = (str(str(cursor3.fetchone()).replace("(", "").replace(")", "").replace(",", "")).replace("[", "").replace("]", "").replace("'", ''))

        NettoEinkommen = '''SELECT Netto_Einkommen FROM Novaland WHERE nutzer_id = %s'''
        cursor3.execute(NettoEinkommen, IDValue)
        player.NettoEinkommen = float((str(cursor3.fetchone()).replace("(", "").replace(")", "").replace(",", "")).replace("[", "").replace("]", "").replace("'", ''))

        Wohnungskosten = '''SELECT Wohnungskosten FROM Novaland WHERE nutzer_id = %s'''
        cursor3.execute(Wohnungskosten, IDValue)
        player.Wohnungskosten = float((str(str(cursor3.fetchone()).replace("(", "").replace(")", "").replace(",", "")).replace("[", "").replace("]", "").replace("'", '')))

        Verpflegungskosten = '''SELECT Verpflegungskosten FROM Novaland WHERE nutzer_id = %s'''
        cursor3.execute(Verpflegungskosten, IDValue)
        player.Verpflegungskosten = float((str(str(cursor3.fetchone()).replace("(", "").replace(")", "").replace(",", "")).replace("[", "").replace("]", "").replace("'", '')))

        Mobilitaetskosten = '''SELECT Mobilitaetskosten FROM Novaland WHERE nutzer_id = %s'''
        cursor3.execute(Mobilitaetskosten, IDValue)
        player.Mobilitaetskosten = float((str(str(cursor3.fetchone()).replace("(", "").replace(")", "").replace(",", "")).replace("[", "").replace("]", "").replace("'", '')))

        Resteinkommen = '''SELECT Rest_Einkommen FROM Novaland WHERE nutzer_id = %s'''
        cursor3.execute(Resteinkommen, IDValue)
        player.Resteinkommen = float((str(str(cursor3.fetchone()).replace("(", "").replace(")", "").replace(",", "")).replace("[", "").replace("]", "").replace("'", '')))

        connection3.commit()
        cursor3.close()
        connection3.close()

        player.KontoPhase3Anfang = player.Resteinkommen * 2

        ##########################

        if player.Wohnungskosten == 1100:
            Wohnung_satz = "einem großen Haus zu wohnen"
        elif player.Wohnungskosten == 950:
            Wohnung_satz = "einem Reihenhaus zu wohnen"
        elif player.Wohnungskosten == 700:
            Wohnung_satz = "in einer geräumigen Wohnung zu wohnen"
        elif player.Wohnungskosten == 500:
            Wohnung_satz = "einer normal großen Wohnung zu wohnen"

        if player.Verpflegungskosten == 400:
            Verpflegungssatz = "regelmäßig in Restaurants Essen zu gehen"
        elif player.Verpflegungskosten == 300:
            Verpflegungssatz = "häufig etwas Essen zu bestellen"
        elif player.Verpflegungskosten == 200:
            Verpflegungssatz = "häufig selber zu kochen"

        if player.Mobilitaetskosten == 200:
            Mobilitaetssatz = "hauptsächlich mit dem eigenen Auto zu fahren"
        if player.Mobilitaetskosten == 150:
            Mobilitaetssatz = "das Sie bei Bedarf ein Auto mieten und öffentliche Verkehrsmittel nutzen"
        if player.Mobilitaetskosten == 50:
            Mobilitaetssatz = "das sie Fahrrad fahren und bei Bedarf öffentliche Verkehrsmittel verwenden"

        return {
            "Wohnung": Wohnung_satz,
            "Verpflegung": Verpflegungssatz,
            "Mobilitaet": Mobilitaetssatz
        }


class Phase_3_Page_2(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP3S2" in data:
            player.S3P2Zeit = data["ZeitP3S2"]
            player.UnixTimeP3S2 = time.time()

    @staticmethod
    def vars_for_template(player: Player):
        player.IDPlayer = player.participant.label


class Phase_3_Page_3(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP3S3" in data:
            player.S3P3Zeit = data["ZeitP3S3"]
            player.UnixTimeP3S3 = time.time()


class Phase_3_Page_4(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP3S4" in data:
            player.S3P4Zeit = data["ZeitP3S4"]
            player.UnixTimeP3S4 = time.time()


class Phase_3_Page_5(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP3S5" in data:
            player.S3P5Zeit = data["ZeitP3S5"]
            player.UnixTimeP3S5 = time.time()


class Phase_3_Page_6(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP3S6" in data:
            player.S3P6Zeit = data["ZeitP3S6"]
            player.UnixTimeP3S6 = time.time()


class Phase_3_Page_7(Page):
    form_model = 'player'
    form_fields = ['Partei']

    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP3S7" in data:
            player.S3P7Zeit = data["ZeitP3S7"]
            player.UnixTimeP3S7 = time.time()


class Phase_3_Page_8(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP3S8" in data:
            player.S3P8Zeit = data["ZeitP3S8"]
            player.UnixTimeP3S8 = time.time()

    @staticmethod
    def vars_for_template(player: Player):
        player.Runde_3_erledigt = "Ja"


class Phase_3_Page_9(Page):
    @staticmethod
    def vars_for_template(player: Player):
        connection3 = psycopg2.connect(user='aipclfonwuiort',
                                       password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                       host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                       port='5432',
                                       database='dcoubsit8jsig0')

        cursor3 = connection3.cursor()

        update_rows2 = '''UPDATE Novaland SET Partei = %s, KontoPhase3Anfang = %s, Runde_3_Erledigt = %s, Zeit_P3S1 = %s, Zeit_P3S2 = %s, Zeit_P3S3 = %s, Zeit_P3S4 = %s, Zeit_P3S5 = %s, Zeit_P3S6 = %s, Zeit_P3S7 = %s, Zeit_P3S8 = %s, UnixTime_P3S1 = %s, UnixTime_P3S2 = %s, UnixTime_P3S3 = %s, UnixTime_P3S4 = %s, UnixTime_P3S5 = %s, UnixTime_P3S6 = %s, UnixTime_P3S7 = %s, UnixTime_P3S8 = %s WHERE nutzer_id = %s'''
        update_values2 = (
            player.Partei, player.KontoPhase3Anfang, player.Runde_3_erledigt, player.S3P1Zeit, player.S3P2Zeit, player.S3P3Zeit, player.S3P4Zeit,
            player.S3P5Zeit, player.S3P6Zeit, player.S3P7Zeit, player.S3P8Zeit, player.UnixTimeP3S1,
            player.UnixTimeP3S2, player.UnixTimeP3S3, player.UnixTimeP3S4, player.UnixTimeP3S5, player.UnixTimeP3S6,
            player.UnixTimeP3S7, player.UnixTimeP3S8, player.IDPlayer)
        cursor3.execute(update_rows2, update_values2)

        connection3.commit()
        cursor3.close()
        connection3.close()


page_sequence = [Waiting_Site, Phase_3_Page_1, Phase_3_Page_2, Phase_3_Page_3, Phase_3_Page_4, Phase_3_Page_5,
                 Phase_3_Page_6,
                 Phase_3_Page_7, Phase_3_Page_8, Phase_3_Page_9]
