import psycopg2
from otree.api import *
from datetime import *
from datetime import time
import time

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
    IDPlayer = models.StringField()
    # --------------------------
    # Seite 1
    # Daten runterladen
    Geschlecht = models.StringField()
    NettoEinkommen = models.FloatField()
    Wohnungskosten = models.FloatField()
    Verpflegungskosten = models.FloatField()
    Mobilitaetskosten = models.FloatField()
    Resteinkommen = models.FloatField()
    KontoPhase4Anfang = models.FloatField()  # für die Tabelle

    # ---------------------------
    # Seite 3
    # Koalitionsbündnis
    LPNundKPNbund = models.StringField()
    SPNundPPNbund = models.StringField()
    KoalitionsBund = models.StringField()

    # --------------------------
    # Seite 4
    Zufriedenheitsfrage_2 = models.StringField(
        choices=[["Sehr zufrieden", "Sehr zufrieden"], ["zufrieden", ""], ["Mitte", ""], ["Nicht zufrieden", ""],
                 ["Überhaupt nicht zufrieden", "Überhaupt nicht zufrieden"]],
        label="",
        widget=widgets.RadioSelect
    )
    # ---------------------------
    # Seite 6
    Zufriedenheitsfrage_3 = models.StringField(
        choices=[["Sehr zufrieden", "Sehr zufrieden"], ["zufrieden", ""], ["Mitte", ""], ["Nicht zufrieden", ""],
                 ["Überhaupt nicht zufrieden", "Überhaupt nicht zufrieden"]],
        label="",
        widget=widgets.RadioSelect
    )

    # Seite 8
    Spende = models.FloatField()
    KontoPhase4Ende = models.FloatField()

    # ---------------------------
    # Ergebnis
    # --------------------------
    LPNStimmen = models.FloatField()  # für die Tabelle
    LPNProzent = models.FloatField()  # für die Tabelle
    SPNStimmen = models.FloatField()  # für die Tabelle
    SPNProzent = models.FloatField()  # für die Tabelle
    KPNStimme = models.FloatField()  # für die Tabelle
    KPNProzent = models.FloatField()  # für die Tabele
    PPNStimmen = models.FloatField()  # Tabelle
    PPNProzent = models.FloatField()  # Tabelle
    PlatzEins = models.StringField()

    # Zeit
    S4P1Zeit = models.FloatField()
    S4P2Zeit = models.FloatField()
    S4P3Zeit = models.FloatField()
    S4P4Zeit = models.FloatField()
    S4P5Zeit = models.FloatField()
    S4P6Zeit = models.FloatField()
    S4P7Zeit = models.FloatField()
    S4P8Zeit = models.FloatField()
    S4P9Zeit = models.FloatField()
    UnixTimeP4S1 = models.FloatField()
    UnixTimeP4S2 = models.FloatField()
    UnixTimeP4S3 = models.FloatField()
    UnixTimeP4S4 = models.FloatField()
    UnixTimeP4S5 = models.FloatField()
    UnixTimeP4S6 = models.FloatField()
    UnixTimeP4S7 = models.FloatField()
    UnixTimeP4S8 = models.FloatField()
    UnixTimeP4S9 = models.FloatField()
    Runde_4_Erledigt = models.StringField()


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


class Phase_4_Page_1(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP4S1" in data:
            player.S4P1Zeit = data["ZeitP4S1"]
            player.UnixTimeP4S1 = time.time()

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
            float(str(str(cursor3.fetchone()).replace("(", "").replace(")", "").replace(",", "")).replace("[", "").replace(
                "]", "").replace("'", '')))

        Wohnungskosten = '''SELECT Wohnungskosten FROM Novaland WHERE nutzer_id = %s'''
        cursor3.execute(Wohnungskosten, IDValue)
        player.Wohnungskosten = (
            float(str(str(cursor3.fetchone()).replace("(", "").replace(")", "").replace(",", "")).replace("[", "").replace(
                "]", "").replace("'", '')))

        Verpflegungskosten = '''SELECT Verpflegungskosten FROM Novaland WHERE nutzer_id = %s'''
        cursor3.execute(Verpflegungskosten, IDValue)
        player.Verpflegungskosten = (
            float(str(str(cursor3.fetchone()).replace("(", "").replace(")", "").replace(",", "")).replace("[", "").replace(
                "]", "").replace("'", '')))

        Mobilitaetskosten = '''SELECT Mobilitaetskosten FROM Novaland WHERE nutzer_id = %s'''
        cursor3.execute(Mobilitaetskosten, IDValue)
        player.Mobilitaetskosten = (
            float(str(str(cursor3.fetchone()).replace("(", "").replace(")", "").replace(",", "")).replace("[", "").replace(
                "]", "").replace("'", '')))

        Resteinkommen = '''SELECT Rest_Einkommen FROM Novaland WHERE nutzer_id = %s'''
        cursor3.execute(Resteinkommen, IDValue)
        player.Resteinkommen = (
            float(str(str(cursor3.fetchone()).replace("(", "").replace(")", "").replace(",", "")).replace("[", "").replace(
                "]", "").replace("'", '')))

        connection3.commit()
        cursor3.close()
        connection3.close()

        player.KontoPhase4Anfang = player.Resteinkommen * 3

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
        if "ZeitP4S1" in data:
            player.S4P1Zeit = data["ZeitP4S1"]
            player.UnixTimeP4S1 = time.time()


class Phase_4_Page_2(Page):
    @staticmethod
    def vars_for_template(player: Player):
        player.IDPlayer = player.participant.code
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
        player.KPNProzent = (player.KPNStimme / AlleStimmenZahl) * 100
        player.SPNProzent = (player.SPNStimmen / AlleStimmenZahl) * 100
        player.LPNProzent = (player.LPNStimmen / AlleStimmenZahl) * 100
        player.PPNProzent = (player.PPNStimmen / AlleStimmenZahl) * 100
        ListeWahl = sorted([player.KPNProzent, player.SPNProzent, player.LPNProzent, player.PPNProzent])
        if ListeWahl[3] == player.KPNProzent:
            Platzeins = "Konservative Partei Novaland"
            player.PlatzEins = "Konservative Partei Novaland"
        elif ListeWahl[3] == player.SPNProzent:
            Platzeins = "Soziale Partei Novaland"
            player.PlatzEins = "Soziale Partei Novaland"
        elif ListeWahl[3] == player.LPNProzent:
            Platzeins = "Liberale Partei Novaland"
            player.PlatzEins = "Liberale Partei Novaland"
        elif ListeWahl[3] == player.PPNProzent:
            Platzeins = "Partei Progressives Novaland"
            player.PlatzEins = "Partei Progressives Novaland"

        if ListeWahl[2] == player.KPNProzent:
            PlatzZwei = "Konservative Partei Novaland"
        if ListeWahl[2] == player.SPNProzent:
            PlatzZwei = "Soziale Partei Novaland"
        if ListeWahl[2] == player.LPNProzent:
            PlatzZwei = "Liberale Partei Novaland"
        if ListeWahl[2] == player.PPNProzent:
            PlatzZwei = "Partei Progressives Novaland"

        if ListeWahl[1] == player.KPNProzent:
            PlatzDrei = "Konservative Partei Novaland"
        if ListeWahl[1] == player.SPNProzent:
            PlatzDrei = "Soziale Partei Novaland"
        if ListeWahl[1] == player.LPNProzent:
            PlatzDrei = "Liberale Partei Novaland"
        if ListeWahl[1] == player.PPNProzent:
            PlatzDrei = "Partei Progressives Novaland"

        if ListeWahl[0] == player.KPNProzent:
            PlatzVier = "Konservative Partei Novaland"
        if ListeWahl[0] == player.SPNProzent:
            PlatzVier = "Soziale Partei Novaland"
        if ListeWahl[0] == player.LPNProzent:
            PlatzVier = "Liberale Partei Novaland"
        if ListeWahl[0] == player.PPNProzent:
            PlatzVier = "Partei Progressives Novaland"

        return {
            "LPNProzent": int(player.LPNProzent),
            "SPNProzent": int(player.SPNProzent),
            "KPNProzent": int(player.KPNProzent),
            "PPNProzent": int(player.PPNProzent),
            "Platzeins": Platzeins,
            "PlatzZwei": PlatzZwei,
            "PlatzDrei": PlatzDrei,
            "PlatzVier": PlatzVier

        }

        cursor.close()
        connection.close()
        connection.close()

    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP4S2" in data:
            player.S4P2Zeit = data["ZeitP4S2"]
            player.UnixTimeP4S2 = time.time()


class Phase_4_Page_3(Page):
    @staticmethod
    def vars_for_template(player: Player):
        if player.KPNStimme + player.LPNStimmen > player.SPNStimmen + player.PPNStimmen:
            player.LPNundKPNbund = "Ja"
            player.SPNundPPNbund = "Nein"
            player.KoalitionsBund = "LPN und KPN"

        if player.KPNStimme + player.LPNStimmen < player.SPNStimmen + player.PPNStimmen:
            player.SPNundPPNbund = "Ja"
            player.LPNundKPNbund = "Nein"
            player.KoalitionsBund = "SPN und PPN"

    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP4S3" in data:
            player.S4P3Zeit = data["ZeitP4S3"]
            player.UnixTimeP4S3 = time.time()


class Phase_4_Page_4(Page):
    form_model = 'player'
    form_fields = ['Zufriedenheitsfrage_2']

    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP4S4" in data:
            player.S4P4Zeit = data["ZeitP4S4"]
            player.UnixTimeP4S4 = time.time()


class Phase_4_Page_5(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP4S5" in data:
            player.S4P5Zeit = data["ZeitP4S5"]
            player.UnixTimeP4S5 = time.time()


class Phase_4_Page_6(Page):
    form_model = 'player'
    form_fields = ['Zufriedenheitsfrage_3']

    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP4S6" in data:
            player.S4P6Zeit = data["ZeitP4S6"]
            player.UnixTimeP4S6 = time.time()


class Phase_4_Page_7(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP4S7" in data:
            player.S4P7Zeit = data["ZeitP4S7"]
            player.UnixTimeP4S7 = time.time()


class Phase_4_Page_8(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP4S8" in data:
            player.S4P8Zeit = data["ZeitP4S8"]
            player.UnixTimeP4S8 = time.time()


class Phase_4_Page_9(Page):
    @staticmethod
    def vars_for_template(player: Player):
        player.Runde_4_Erledigt = "Ja"

    @staticmethod
    def js_vars(player: Player):
        return {
            "Kontostand": player.KontoPhase4Anfang,
        }

    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP4S9" in data:
            player.S4P9Zeit = data["ZeitP4S9"]
            player.UnixTimeP4S9 = time.time()
        if "Spende" in data:
            player.Spende = float(data["SpendenZahl"])
            player.KontoPhase4Ende = player.KontoPhase4Anfang - player.Spende


class Phase_4_Page_10(Page):
    @staticmethod
    def vars_for_template(player: Player):

        connection3 = psycopg2.connect(user='aipclfonwuiort',
                                       password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                       host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                       port='5432',
                                       database='dcoubsit8jsig0')

        cursor3 = connection3.cursor()

        update_rows2 = '''UPDATE Novaland SET LPNundKPNbund = %s, SPNundPPNbund = %s, KoalitionsBund = %s, KontoPhase4Anfang = %s, KontoPhase4Ende = %s, Zufriedenheitsfrage2 = %s, Zufriedenheitsfrage3 = %s, Spende = %s, Runde_4_Erledigt = %s, Zeit_P4S1 = %s, Zeit_P4S2 = %s, Zeit_P4S3 = %s, Zeit_P4S4 = %s, Zeit_P4S5 = %s, Zeit_P4S6 = %s, Zeit_P4S7 = %s, Zeit_P4S8 = %s, Zeit_P4S9 = %s, UnixTime_P4S1 = %s, UnixTime_P4S2 = %s, UnixTime_P4S3 = %s, UnixTime_P4S4 = %s, UnixTime_P4S5 = %s, UnixTime_P4S6 = %s, UnixTime_P4S7 = %s, UnixTime_P4S8 = %s, UnixTime_P4S9 = %s WHERE nutzer_id = %s'''
        update_values2 = (
            player.LPNundKPNbund, player.SPNundPPNbund, player.KoalitionsBund, player.KontoPhase4Anfang, player.KontoPhase4Ende, player.Zufriedenheitsfrage_2, player.Zufriedenheitsfrage_3, player.Spende, player.Runde_4_Erledigt, player.S4P1Zeit, player.S4P2Zeit,
            player.S4P3Zeit, player.S4P4Zeit,
            player.S4P5Zeit, player.S4P6Zeit, player.S4P7Zeit, player.S4P8Zeit, player.S4P9Zeit, player.UnixTimeP4S1,
            player.UnixTimeP4S2, player.UnixTimeP4S3, player.UnixTimeP4S4, player.UnixTimeP4S5, player.UnixTimeP4S6,
            player.UnixTimeP4S7, player.UnixTimeP4S8, player.UnixTimeP4S9, player.IDPlayer)
        cursor3.execute(update_rows2, update_values2)

        connection3.commit()
        cursor3.close()
        connection3.close()


page_sequence = [Waiting_Site, Phase_4_Page_1, Phase_4_Page_2, Phase_4_Page_3, Phase_4_Page_4, Phase_4_Page_5,
                 Phase_4_Page_6, Phase_4_Page_7, Phase_4_Page_8, Phase_4_Page_9, Phase_4_Page_10]
