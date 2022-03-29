import psycopg2
from otree.api import *
from datetime import *
from datetime import time
import time

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'phase_5'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Seite 1
    Geschlecht = models.StringField()
    NettoEinkommen = models.FloatField()
    Wohnungskosten = models.FloatField()
    Verpflegungskosten = models.FloatField()
    Mobilitaetskosten = models.FloatField()
    Resteinkommen = models.FloatField()
    Spende = models.FloatField()
    KontoPhase5Anfang = models.FloatField() ###################
    KontoPhase5Ende = models.FloatField()

    # Seite 2
    SpendenInsgesamt = models.FloatField()

    # Seite 4
    BrandBetroffen = models.StringField()
    BrandSchadenKosten = models.FloatField()
    KontoNachBrandSchaden = models.FloatField()

    # Seite 6
    ZufriedenheitsFrage4 = models.StringField(
        choices=[["Sehr zufrieden", "Sehr zufrieden"], ["zufrieden", ""], ["Mitte", ""], ["Nicht zufrieden", ""],
                 ["Überhaupt nicht zufrieden", "Überhaupt nicht zufrieden"]],
        label="",
        widget=widgets.RadioSelect
    )

    # Seite 7
    Spende2 = models.FloatField()

    # Zeit
    S5P1Zeit = models.FloatField()
    S5P2Zeit = models.FloatField()
    S5P3Zeit = models.FloatField()
    S5P4Zeit = models.FloatField()
    S5P5Zeit = models.FloatField()
    S5P6Zeit = models.FloatField()
    S5P7Zeit = models.FloatField()
    S5P8Zeit = models.FloatField()
    S5P9Zeit = models.FloatField()
    UnixTimeP5S1 = models.FloatField()
    UnixTimeP5S2 = models.FloatField()
    UnixTimeP5S3 = models.FloatField()
    UnixTimeP5S4 = models.FloatField()
    UnixTimeP5S5 = models.FloatField()
    UnixTimeP4S6 = models.FloatField()
    UnixTimeP5S7 = models.FloatField()
    UnixTimeP5S8 = models.FloatField()
    UnixTimeP5S9 = models.FloatField()
    Runde_5_Erledigt = models.StringField()


# PAGES
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


class Phase_5_Page_1(Page):
    @staticmethod
    def vars_for_template(player: Player):
        connection3 = psycopg2.connect(user='aipclfonwuiort',
                                       password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                       host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                       port='5432',
                                       database='dcoubsit8jsig0')

        cursor3 = connection3.cursor()
        IDValue = [player.participant.code]

        Geschlecht = '''SELECT Geschlecht FROM Novaland WHERE nutzer_id = %s'''
        cursor3.execute(Geschlecht, IDValue)
        player.Geschlecht = (
            str(str(cursor3.fetchone()).replace("(", "").replace(")", "").replace(",", "")).replace("[", "").replace(
                "]", "").replace("'", ''))

        NettoEinkommen = '''SELECT Netto_Einkommen FROM Novaland WHERE nutzer_id = %s'''
        cursor3.execute(NettoEinkommen, IDValue)
        player.NettoEinkommen = (
            float(str(str(cursor3.fetchone()).replace("(", "").replace(")", "").replace(",", "")).replace("[",
                                                                                                          "").replace(
                "]", "").replace("'", '')))

        Wohnungskosten = '''SELECT Wohnungskosten FROM Novaland WHERE nutzer_id = %s'''
        cursor3.execute(Wohnungskosten, IDValue)
        player.Wohnungskosten = (
            float(str(str(cursor3.fetchone()).replace("(", "").replace(")", "").replace(",", "")).replace("[",
                                                                                                          "").replace(
                "]", "").replace("'", '')))

        Verpflegungskosten = '''SELECT Verpflegungskosten FROM Novaland WHERE nutzer_id = %s'''
        cursor3.execute(Verpflegungskosten, IDValue)
        player.Verpflegungskosten = (
            float(str(str(cursor3.fetchone()).replace("(", "").replace(")", "").replace(",", "")).replace("[",
                                                                                                          "").replace(
                "]", "").replace("'", '')))

        Mobilitaetskosten = '''SELECT Mobilitaetskosten FROM Novaland WHERE nutzer_id = %s'''
        cursor3.execute(Mobilitaetskosten, IDValue)
        player.Mobilitaetskosten = (
            float(str(str(cursor3.fetchone()).replace("(", "").replace(")", "").replace(",", "")).replace("[",
                                                                                                          "").replace(
                "]", "").replace("'", '')))

        Resteinkommen = '''SELECT Rest_Einkommen FROM Novaland WHERE nutzer_id = %s'''
        cursor3.execute(Resteinkommen, IDValue)
        player.Resteinkommen = (
            float(str(str(cursor3.fetchone()).replace("(", "").replace(")", "").replace(",", "")).replace("[",
                                                                                                          "").replace(
                "]", "").replace("'", '')))

        Spende = '''SELECT Spende FROM Novaland WHERE nutzer_id = %s'''
        cursor3.execute(Spende, IDValue)
        player.Spende = (
            float(str(str(cursor3.fetchone()).replace("(", "").replace(")", "").replace(",", "")).replace("[",
                                                                                                          "").replace(
                "]", "").replace("'", '')))

        connection3.commit()
        cursor3.close()
        connection3.close()

        player.KontoPhase5Anfang = player.Resteinkommen * 4 - player.Spende

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

    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP5S1" in data:
            player.S5P1Zeit = data["ZeitP5S1"]
            player.UnixTimeP5S1 = time.time()


class Phase_5_Page_2(Page):
    @staticmethod
    def vars_for_template(player: Player):
        connection4 = psycopg2.connect(user='aipclfonwuiort',
                                      password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                      host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                      port='5432',
                                      database='dcoubsit8jsig0')
        cursor4 = connection4.cursor()

        IDBekommen = 'SELECT DISTINCT nutzer_id FROM Novaland'
        cursor4.execute(IDBekommen)
        ID = cursor4.fetchall()
        AlleSpenden = 0.0
        for ID in ID:
            USERID = (str(str(ID).replace("(", "").replace(")", "").replace(",", "")).replace("[", "").replace("]", "").replace("'", ''))
            ScriptZahl = '''SELECT DISTINCT Spende From Novaland Where nutzer_id = %s'''
            Users = [USERID]
            cursor4.execute(ScriptZahl, Users)
            Spenden = cursor4.fetchone()
            SpendenZahl = float(str(str(Spenden).replace("(", "").replace(")", "").replace(",", "")).replace("[", "").replace("]", "").replace("'", ''))
            AlleSpenden = AlleSpenden + SpendenZahl

        player.SpendenInsgesamt = AlleSpenden
        cursor4.close()
        connection4.close()

    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP5S2" in data:
            player.S5P2Zeit = data["ZeitP5S2"]
            player.UnixTimeP5S2 = time.time()


class Phase_5_Page_3(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP5S3" in data:
            player.S5P3Zeit = data["ZeitP5S3"]
            player.UnixTimeP5S3 = time.time()


class Phase_5_Page_4(Page):
    @staticmethod
    def vars_for_template(player: Player):
        betroffene = range(1, 250, 2)
        NichtBetroffen = range(2, 250, 2)
        if player.id_in_group in betroffene:
            player.BrandBetroffen = "Ja"
            player.BrandSchadenKosten = (player.KontoPhase5Anfang / 2) + player.Resteinkommen
            player.KontoNachBrandSchaden = player.KontoPhase5Anfang - player.BrandSchadenKosten
        if player.id_in_group in NichtBetroffen:
            player.BrandBetroffen = "Nein"
            player.BrandSchadenKosten = 0
            player.KontoNachBrandSchaden = player.KontoPhase5Anfang - player.BrandSchadenKosten

    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP5S4" in data:
            player.S5P4Zeit = data["ZeitP5S4"]
            player.UnixTimeP5S4 = time.time()


class Phase_5_Page_5(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP5S5" in data:
            player.S5P5Zeit = data["ZeitP5S5"]
            player.UnixTimeP5S5 = time.time()


class Phase_5_Page_6(Page):
    form_model = 'player'
    form_fields = ["ZufriedenheitsFrage4"]

    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP5S6" in data:
            player.S5P6Zeit = data["ZeitP5S6"]
            player.UnixTimeP5S6 = time.time()


class Phase_5_Page_7(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP5S7" in data:
            player.S5P7Zeit = data["ZeitP5S7"]
            player.UnixTimeP5S7 = time.time()
        if "Spende2" in data:
            player.Spende2 = float(data["SpendenZahl2"])
            player.KontoPhase5Ende = player.KontoNachBrandSchaden - player.Spende2

    @staticmethod
    def js_vars(player: Player):
        return {
            "Kontostand": player.KontoNachBrandSchaden,
        }


class Phase_5_Page_8(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP5S8" in data:
            player.S5P8Zeit = data["ZeitP5S8"]
            player.UnixTimeP5S8 = time.time()


class Phase_5_Page_9(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP5S9" in data:
            player.S5P9Zeit = data["ZeitP5S9"]
            player.UnixTimeP5S9 = time.time()


class Phase_5_Page_10(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP5S10" in data:
            player.S5P10Zeit = data["ZeitP5S10"]
            player.UnixTimeP5S10 = time.time()


class Phase_5_Page_11(Page):
    pass


page_sequence = [Waiting_Site, Phase_5_Page_1, Phase_5_Page_2, Phase_5_Page_3, Phase_5_Page_4, Phase_5_Page_5, Phase_5_Page_6, Phase_5_Page_7, Phase_5_Page_8, Phase_5_Page_9, Phase_5_Page_10, Phase_5_Page_11]
