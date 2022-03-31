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
    IDPlayer = models.StringField()

    # Seite 1
    Geschlecht = models.StringField()
    NettoEinkommen = models.FloatField()
    Wohnungskosten = models.FloatField()
    Verpflegungskosten = models.FloatField()
    Mobilitaetskosten = models.FloatField()
    Resteinkommen = models.FloatField()
    Spende = models.FloatField()
    KontoPhase5Anfang = models.FloatField()  ###################
    KontoPhase5Ende = models.FloatField()
    KoalitionsBund = models.StringField()
    Brutto_Einkommen = models.FloatField()

    Wohnung_satz = models.StringField()
    Verpflegungssatz = models.StringField()
    Mobilitaetssatz = models.StringField()

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

    # Seite 8
    Spenden2Insgesamt = models.FloatField()

    # Seite 9
    SteuerFrage1 = models.StringField(
        choices=[["Ja", "Ja"], ["Nein", "Nein"]],
        label="",
        widget=widgets.RadioSelect
    )

    # Seite 10
    Vertrauensfrage1 = models.StringField(
        choices=[["Volles Vertrauen", "Volles Vertrauen"], ["Leichtes Vertrauen", ""], ["Mitte", ""],
                 ["Wenig Vertrauen", ""],
                 ["Überhaupt kein Vertrauen", "Überhaupt kein Vertrauen"]],
        label="",
        widget=widgets.RadioSelect
    )

    # Seite 11
    OffeneFrage = models.LongStringField()

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
    S5P10Zeit = models.FloatField()
    S5P11Zeit = models.FloatField()
    UnixTimeP5S1 = models.FloatField()
    UnixTimeP5S2 = models.FloatField()
    UnixTimeP5S3 = models.FloatField()
    UnixTimeP5S4 = models.FloatField()
    UnixTimeP5S5 = models.FloatField()
    UnixTimeP5S6 = models.FloatField()
    UnixTimeP5S7 = models.FloatField()
    UnixTimeP5S8 = models.FloatField()
    UnixTimeP5S9 = models.FloatField()
    UnixTimeP5S10 = models.FloatField()
    UnixTimeP5S11 = models.FloatField()
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
        player.IDPlayer = player.participant.label

        connection3 = psycopg2.connect(user='aipclfonwuiort',
                                       password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                       host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                       port='5432',
                                       database='dcoubsit8jsig0')

        cursor3 = connection3.cursor()
        IDValue = [player.participant.label]

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

        if player.Wohnungskosten == 1100:
            player.Wohnung_satz = "einem großen Haus zu wohnen"
        elif player.Wohnungskosten == 950:
            player.Wohnung_satz = "einem Reihenhaus zu wohnen"
        elif player.Wohnungskosten == 700:
            player.Wohnung_satz = "in einer geräumigen Wohnung zu wohnen"
        elif player.Wohnungskosten == 500:
            player.Wohnung_satz = "einer normal großen Wohnung zu wohnen"

        Verpflegungskosten = '''SELECT Verpflegungskosten FROM Novaland WHERE nutzer_id = %s'''
        cursor3.execute(Verpflegungskosten, IDValue)
        player.Verpflegungskosten = (
            float(str(str(cursor3.fetchone()).replace("(", "").replace(")", "").replace(",", "")).replace("[",
                                                                                                          "").replace(
                "]", "").replace("'", '')))

        if player.Verpflegungskosten == 400:
            player.Verpflegungssatz = "regelmäßig in Restaurants Essen zu gehen"
        elif player.Verpflegungskosten == 300:
            player.Verpflegungssatz = "häufig etwas Essen zu bestellen"
        elif player.Verpflegungskosten == 200:
            player.Verpflegungssatz = "häufig selber zu kochen"

        Mobilitaetskosten = '''SELECT Mobilitaetskosten FROM Novaland WHERE nutzer_id = %s'''
        cursor3.execute(Mobilitaetskosten, IDValue)
        player.Mobilitaetskosten = (
            float(str(str(cursor3.fetchone()).replace("(", "").replace(")", "").replace(",", "")).replace("[",
                                                                                                          "").replace(
                "]", "").replace("'", '')))

        if player.Mobilitaetskosten == 200:
            player.Mobilitaetssatz = "hauptsächlich mit dem eigenen Auto zu fahren"
        if player.Mobilitaetskosten == 150:
            player.Mobilitaetssatz = "das Sie bei Bedarf ein Auto mieten und öffentliche Verkehrsmittel nutzen"
        if player.Mobilitaetskosten == 50:
            player.Mobilitaetssatz = "das sie Fahrrad fahren und bei Bedarf öffentliche Verkehrsmittel verwenden"

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

        KoalitionsBund = '''SELECT KoalitionsBund FROM Novaland WHERE nutzer_id = %s'''
        cursor3.execute(KoalitionsBund, IDValue)
        player.KoalitionsBund = (
            str(str(cursor3.fetchone()).replace("(", "").replace(")", "").replace(",", "")).replace("[",
                                                                                                    "").replace(
                "]", "").replace("'", ''))

        Brutto_Einkommen = '''SELECT Brutto_Einkommen FROM Novaland WHERE nutzer_id = %s'''
        cursor3.execute(Brutto_Einkommen, IDValue)
        player.Brutto_Einkommen = (
            float(str(str(cursor3.fetchone()).replace("(", "").replace(")", "").replace(",", "")).replace("[",
                                                                                                          "").replace(
                "]", "").replace("'", '')))

        connection3.commit()
        cursor3.close()
        connection3.close()

        ### Die Szenarien durchgehen, wenn ein bestimmtes Bündnis entstanden ist
        if player.KoalitionsBund == "LPN und KPN":
            if player.Brutto_Einkommen == 5000:
                x = player.NettoEinkommen - player.Resteinkommen
                xReich = (player.NettoEinkommen * 0.1) + player.NettoEinkommen - x
                player.KontoPhase5Anfang = player.Resteinkommen * 3 - player.Spende + xReich
                if player.KontoPhase5Anfang < 0:
                    player.KontoPhase5Anfang = 0
                return {
                    "xReich": xReich,
                    "xArm": 0
                }

            if player.Brutto_Einkommen == 2850:
                player.KontoPhase5Anfang = player.Resteinkommen * 4 - player.Spende
                if player.KontoPhase5Anfang < 0:
                    player.KontoPhase5Anfang = 0
                return {
                    "xReich": 0,
                    "xArm": 0
                }

            if player.Brutto_Einkommen == 2000:
                x = player.NettoEinkommen - player.Resteinkommen
                xArm = player.NettoEinkommen - (player.NettoEinkommen * 0.05) - x
                player.KontoPhase5Anfang = player.Resteinkommen * 3 - player.Spende - xArm
                if player.KontoPhase5Anfang < 0:
                    player.KontoPhase5Anfang = 0
                return {
                    "xReich": 0,
                    "xArm": xArm
                }

        elif player.KoalitionsBund == "SPN und PPN":
            if player.Brutto_Einkommen == 5000:
                x = player.NettoEinkommen - player.Resteinkommen
                xReich = player.NettoEinkommen - (player.NettoEinkommen * 0.05) - x
                player.KontoPhase5Anfang = player.Resteinkommen * 3 - player.Spende - xReich
                if player.KontoPhase5Anfang < 0:
                    player.KontoPhase5Anfang = 0
                return {
                    "xReich": xReich,
                    "xArm": 0
                }

            if player.Brutto_Einkommen == 2850:
                player.KontoPhase5Anfang = player.Resteinkommen * 4 - player.Spende
                if player.KontoPhase5Anfang < 0:
                    player.KontoPhase5Anfang = 0
                return {
                    "xReich": 0,
                    "xArm": 0
                }

            if player.Brutto_Einkommen == 2000:
                x = player.NettoEinkommen - player.Resteinkommen
                xArm = (player.NettoEinkommen * 0.1) + player.NettoEinkommen - x
                player.KontoPhase5Anfang = player.Resteinkommen * 3 - player.Spende + xArm
                if player.KontoPhase5Anfang < 0:
                    player.KontoPhase5Anfang = 0
                return {
                    "xReich": 0,
                    "xArm": xArm
                }

        elif player.KoalitionsBund == "Gleichstand":
            player.KontoPhase5Anfang = player.Resteinkommen * 4 - player.Spende
            if player.KontoPhase5Anfang < 0:
                player.KontoPhase5Anfang = 0
            return {
                "xReich": 0,
                "xArm": 0
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
            USERID = str(
                str(ID).replace("(", "").replace(")", "").replace(",", "").replace("[", "").replace("]", "").replace(
                    "'", ''))
            ScriptZahl = '''SELECT Spende From Novaland Where nutzer_id = %s'''
            Users = [USERID]
            cursor4.execute(ScriptZahl, Users)
            Spenden = cursor4.fetchone()

            try:
                SpendenZahl = float(
                    str(Spenden).replace("(", "").replace(")", "").replace(",", "").replace("[", "").replace("]",
                                                                                                             "").replace(
                        "'", ''))
                AlleSpenden = AlleSpenden + SpendenZahl
            except:
                SpendenZahl = 0
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
            player.BrandSchadenKosten = (player.KontoPhase5Anfang - player.Resteinkommen) / 2
            if player.KontoPhase5Anfang >= player.BrandSchadenKosten:
                player.KontoNachBrandSchaden = player.KontoPhase5Anfang - player.BrandSchadenKosten
            if player.KontoPhase5Anfang < player.BrandSchadenKosten:
                player.BrandSchadenKosten = player.KontoPhase5Anfang
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
    def js_vars(player: Player):
        return {
            "Kontostand2": player.KontoNachBrandSchaden,
        }

    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP5S7" in data:
            player.S5P7Zeit = data["ZeitP5S7Zeit"]
            player.UnixTimeP5S7 = time.time()

        def SpendenSchicken():
            player.Runde_5_Erledigt = "Ja"
            connection6 = psycopg2.connect(user='aipclfonwuiort',
                                           password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                           host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                           port='5432',
                                           database='dcoubsit8jsig0')

            cursor6 = connection6.cursor()

            update_rows3 = '''UPDATE Novaland SET spende2 = %s WHERE nutzer_id = %s'''
            update_values3 = [player.Spende2, player.IDPlayer]
            cursor6.execute(update_rows3, update_values3)

            connection6.commit()
            cursor6.close()
            connection6.close()

        if "Spende2" in data:
            player.Spende2 = float(data["SpendenZahl2"])
            player.KontoPhase5Ende = player.KontoNachBrandSchaden - player.Spende2
            SpendenSchicken()


class Phase_5_Page_8(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP5S8" in data:
            player.S5P8Zeit = data["ZeitP5S8"]
            player.UnixTimeP5S8 = time.time()

    @staticmethod
    def vars_for_template(player: Player):
        connection5 = psycopg2.connect(user='aipclfonwuiort',
                                       password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                       host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                       port='5432',
                                       database='dcoubsit8jsig0')
        cursor5 = connection5.cursor()

        IDBekommen = 'SELECT DISTINCT nutzer_id FROM Novaland'
        cursor5.execute(IDBekommen)
        ID = cursor5.fetchall()
        AlleSpenden2 = 0.0
        for ID in ID:
            USERID = (str(str(ID).replace("(", "").replace(")", "").replace(",", "")).replace("[", "").replace("]",
                                                                                                               "").replace(
                "'", ''))
            ScriptZahl = '''SELECT Spende2 From Novaland Where nutzer_id = %s'''
            Users = [USERID]
            cursor5.execute(ScriptZahl, Users)
            Spenden2 = cursor5.fetchone()
            try:
                SpendenZahl2 = float(
                    str(str(Spenden2).replace("(", "").replace(")", "").replace(",", "")).replace("[", "").replace("]",
                                                                                                               "").replace(
                        "'", ''))
                AlleSpenden2 = AlleSpenden2 + SpendenZahl2
            except:
                SpendenZahl2 = 0
                AlleSpenden2 = AlleSpenden2 + SpendenZahl2

        player.Spenden2Insgesamt = AlleSpenden2
        cursor5.close()
        connection5.close()


class Phase_5_Page_9(Page):
    form_model = 'player'
    form_fields = ['SteuerFrage1']

    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP5S9" in data:
            player.S5P9Zeit = data["ZeitP5S9"]
            player.UnixTimeP5S9 = time.time()


class Phase_5_Page_10(Page):
    form_model = 'player'
    form_fields = ['Vertrauensfrage1']

    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP5S10" in data:
            player.S5P10Zeit = data["ZeitP5S10"]
            player.UnixTimeP5S10 = time.time()


class Phase_5_Page_11(Page):
    @staticmethod
    def vars_for_template(player: Player):
        player.Runde_5_Erledigt = "Ja"
        connection3 = psycopg2.connect(user='aipclfonwuiort',
                                       password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                       host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                       port='5432',
                                       database='dcoubsit8jsig0')

        cursor3 = connection3.cursor()

        update_rows2 = '''UPDATE Novaland SET KontoPhase5Anfang = %s, BrandBetroffen = %s, BrandSchadenKosten = %s, KontoNachBrandSchaden = %s, Zufriedenheitsfrage4 = %s, Spende2 = %s, Spenden2Insgesamt = %s, KontoPhase5Ende = %s, Steuerfrage1 = %s, Vertrauensfrage1 = %s, Runde_5_Erledigt = %s, Zeit_P5S1 = %s, Zeit_P5S2 = %s, Zeit_P5S3 = %s, Zeit_P5S4 = %s, Zeit_P5S5 = %s, Zeit_P5S6 = %s, Zeit_P5S7 = %s, Zeit_P5S8 = %s, Zeit_P5S9 = %s, Zeit_P5S10 = %s, UnixTime_P5S1 = %s, UnixTime_P5S2 = %s, UnixTime_P5S3 = %s, UnixTime_P5S4 = %s, UnixTime_P5S5 = %s, UnixTime_P5S6 = %s, UnixTime_P5S7 = %s, UnixTime_P5S8 = %s, UnixTime_P5S9 = %s, UnixTime_P5S10 = %s, spendeinsgesamt = %s WHERE nutzer_id = %s'''
        update_values2 = (
            player.KontoPhase5Anfang, player.BrandBetroffen,
            player.BrandSchadenKosten, player.KontoNachBrandSchaden, player.ZufriedenheitsFrage4, player.Spende2,
            player.Spenden2Insgesamt, player.KontoPhase5Ende, player.SteuerFrage1, player.Vertrauensfrage1,
            player.Runde_5_Erledigt, player.S5P1Zeit, player.S5P2Zeit,
            player.S5P3Zeit, player.S5P4Zeit,
            player.S5P5Zeit, player.S5P6Zeit, player.S5P7Zeit, player.S5P8Zeit, player.S5P9Zeit, player.S5P10Zeit,
            player.UnixTimeP5S1,
            player.UnixTimeP5S2, player.UnixTimeP5S3, player.UnixTimeP5S4, player.UnixTimeP5S5, player.UnixTimeP5S6,
            player.UnixTimeP5S7, player.UnixTimeP5S8, player.UnixTimeP5S9, player.UnixTimeP5S10, player.SpendenInsgesamt, player.IDPlayer)
        cursor3.execute(update_rows2, update_values2)

        connection3.commit()
        cursor3.close()
        connection3.close()

    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP5S11" in data:
            player.S5P11Zeit = data["ZeitP5S11"]
            player.UnixTimeP5S11 = time.time()
        if "OffeneFrage" in data:
            player.OffeneFrage = data["OffeneFrageAntwort"]


class Phase_5_Page_12(Page):
    @staticmethod
    def vars_for_template(player: Player):
        connection4 = psycopg2.connect(user='aipclfonwuiort',
                                       password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                       host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                       port='5432',
                                       database='dcoubsit8jsig0')

        cursor4 = connection4.cursor()

        update_rows3 = '''UPDATE Novaland SET OffeneFrage = %s, Zeit_P5S11 = %s, UnixTime_P5S11 = %s WHERE nutzer_id = %s'''
        update_values3 = (player.OffeneFrage, player.S5P11Zeit, player.UnixTimeP5S11, player.IDPlayer)
        cursor4.execute(update_rows3, update_values3)

        connection4.commit()
        cursor4.close()
        connection4.close()


page_sequence = [Waiting_Site, Phase_5_Page_1, Phase_5_Page_2, Phase_5_Page_3, Phase_5_Page_4, Phase_5_Page_5,
                 Phase_5_Page_6, Phase_5_Page_7, Phase_5_Page_8, Phase_5_Page_9, Phase_5_Page_10, Phase_5_Page_11,
                 Phase_5_Page_12]
