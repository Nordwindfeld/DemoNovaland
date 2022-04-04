from otree.api import *
import psycopg2
from datetime import *
from email_validator import validate_email, EmailNotValidError
import time


def connectToRound0(AppStart, UserId, Alter, Gender, EMail, Nuterinformation_erledigt, Telefonnummer):
    connection = psycopg2.connect(user='aipclfonwuiort',
                                  password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                  host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                  port='5432',
                                  database='dcoubsit8jsig0')

    cursor = connection.cursor()

    try:
        create_script = '''CREATE TABLE IF NOT EXISTS Novaland(
                                        AppStart varchar(200),
                                        Nutzer_ID varchar(12),
                                        Alter_Nutzer integer,
                                        Geschlecht varchar(10),
                                        Mail varchar(50),
                                        Telefonnummer varchar(50),
                                        ChrisGeschlecht varchar(10),
                                        Frage_1_Staatsbuerger varchar(20),
                                        Frage_2_Einfluss varchar(20),
                                        Frage_3_Sozialleistung varchar(20),
                                        Brutto_Einkommen float,
                                        Netto_Einkommen float,
                                        Frage_5_Einkommen_Zahl varchar(16),
                                        Frage_6_Einkommen_Vergleich varchar(30),
                                        Frage_7_Wohnen varchar(30),
                                        Wohnungskosten float,
                                        Frage_8_Verpflegung varchar(30),
                                        Verpflegungskosten float,
                                        Frage_9_Mobilitaet varchar(30),
                                        Mobilitaetskosten float,
                                        Frage_10_Zufriedenheit varchar(30),
                                        Rest_Einkommen float,
                                        KontoPhase3Anfang float, 
                                        Partei varchar(50),
                                        LPNStimmen float,
                                        LPNProzent float,
                                        LPNPlatz float,
                                        SPNStimmen float,
                                        SPNProzent float,
                                        SPNPlatz float,
                                        KPNStimme float,
                                        KPNProzent float,
                                        KPNPlatz float,
                                        PPNStimmen float,
                                        PPNProzent float,
                                        PPNPlatz float,
                                        LPNundKPNbund varchar (100),
                                        SPNundPPNbund varchar (100),
                                        KoalitionsBund varchar (100),
                                        Zufriedenheitsfrage2 varchar (40),
                                        Zufriedenheitsfrage3 varchar (40),
                                        Spende float,
                                        SpendeInsgesamt float,
                                        KontoPhase4Anfang float, 
                                        KontoPhase4Ende float,
                                        KontoPhase5Anfang float, 
                                        BrandBetroffen varchar (10),
                                        BrandSchadenKosten float,
                                        KontoNachBrandSchaden float,
                                        Zufriedenheitsfrage4 varchar (40),
                                        Spende2 float,
                                        Spenden2Insgesamt float,
                                        KontoPhase5Ende float,
                                        Steuerfrage1 varchar (10),
                                        Vertrauensfrage1 varchar (30),
                                        OffeneFrage varchar (1000),
                                        NuterInfo_Abgeschlossen varchar(4),
                                        Runde_1_Erledigt varchar(4),
                                        Runde_2_Erledigt varchar(4),
                                        Runde_3_Erledigt varchar(4),
                                        Runde_4_Erledigt varchar(4), 
                                        Runde_5_Erledigt varchar(4),
                                        UnixTime_P1S1 float,
                                        Zeit_P1S1 varchar (8),
                                        UnixTime_P1S2 float,
                                        Zeit_P1S2 varchar (8),
                                        UnixTime_P1S3 float,
                                        Zeit_P1S3 varchar (8),
                                        UnixTime_P1S4 float,
                                        Zeit_P1S4 varchar (8),
                                        UnixTime_P1S5 float,
                                        Zeit_P1S5 varchar (8),
                                        UnixTime_P1S6 float,
                                        Zeit_P1S6 varchar (8),
                                        UnixTime_P1S7 float,
                                        Zeit_P1S7 varchar (8),
                                        UnixTime_P2S1 float,
                                        Zeit_P2S1 varchar (10),
                                        UnixTime_P2S2 float,
                                        Zeit_P2S2 varchar (10),
                                        UnixTime_P2S3 float,
                                        Zeit_P2S3 varchar (10),
                                        UnixTime_P2S4 float,
                                        Zeit_P2S4 varchar (10),
                                        UnixTime_P2S5 float,
                                        Zeit_P2S5 varchar(10),
                                        UnixTime_P2S6 float,
                                        Zeit_P2S6 varchar(10),
                                        UnixTime_P2S7 float,
                                        Zeit_P2S7 varchar(10),
                                        UnixTime_P2S8 float,
                                        Zeit_P2S8 varchar(10),
                                        UnixTime_P2S9 float,
                                        Zeit_P2S9 varchar(10),
                                        UnixTime_P2S10 float,
                                        Zeit_P2S10 varchar(10),
                                        UnixTime_P3S1 float,
                                        Zeit_P3S1 varchar (10),
                                        UnixTime_P3S2 float,
                                        Zeit_P3S2 varchar (10),
                                        UnixTime_P3S3 float,
                                        Zeit_P3S3 varchar (10),
                                        UnixTime_P3S4 float,
                                        Zeit_P3S4 varchar (10),
                                        UnixTime_P3S5 float,
                                        Zeit_P3S5 varchar (10),
                                        UnixTime_P3S6 float,
                                        Zeit_P3S6 varchar (10),
                                        UnixTime_P3S7 float,
                                        Zeit_P3S7 varchar (10),
                                        UnixTime_P3S8 float,
                                        Zeit_P3S8 varchar (10),
                                        UnixTime_P4S1 float,
                                        Zeit_P4S1 varchar(10),
                                        UnixTime_P4S2 float,
                                        Zeit_P4S2 varchar(10),
                                        UnixTime_P4S3 float,
                                        Zeit_P4S3 varchar(10),
                                        UnixTime_P4S4 float,
                                        Zeit_P4S4 varchar(10),
                                        UnixTime_P4S5 float,
                                        Zeit_P4S5 varchar(10),
                                        UnixTime_P4S6 float,
                                        Zeit_P4S6 varchar(10),
                                        UnixTime_P4S7 float,
                                        Zeit_P4S7 varchar(10),
                                        UnixTime_P4S8 float,
                                        Zeit_P4S8 varchar(10),
                                        UnixTime_P4S9 float,
                                        Zeit_P4S9 varchar(10),
                                        UnixTime_P5S1 float,
                                        Zeit_P5S1 varchar(10),
                                        UnixTime_P5S2 float,
                                        Zeit_P5S2 varchar(10),
                                        UnixTime_P5S3 float,
                                        Zeit_P5S3 varchar(10),
                                        UnixTime_P5S4 float,
                                        Zeit_P5S4 varchar(10),
                                        UnixTime_P5S5 float,
                                        Zeit_P5S5 varchar(10),
                                        UnixTime_P5S6 float,
                                        Zeit_P5S6 varchar(10),
                                        UnixTime_P5S7 float,
                                        Zeit_P5S7 varchar(10),
                                        UnixTime_P5S8 float,
                                        Zeit_P5S8 varchar(10),
                                        UnixTime_P5S9 float,
                                        Zeit_P5S9 varchar(10),
                                        UnixTime_P5S10 float,
                                        Zeit_P5S10 varchar(10),
                                        UnixTime_P5S11 float,
                                        Zeit_P5S11 varchar(10),
                                        ZwoelfUhrMail varchar (4),
                                        ZwoelUhrMailZeit varchar (200),
                                        ZwoelfUhrMailUnixTime float,
                                        VierzehnUhrMail varchar(4),
                                        VierzehnUhrMailZeit varchar(200),
                                        VierzehnUhrMailUnixTime float, 
                                        SechzehnUhrMail varchar(4),
                                        SechzehnUhrMailZeit varchar(200),
                                        SechzehnUhrMailUnixTime float, 
                                        AchtzehnUhrMail varchar(4),
                                        AchtzehnUhrMailZeit varchar(200),
                                        AchtzehnUhrMailUnixTime float, 
                                        SMSZwoelfUhr varchar (4),
                                        SMSZwoelfUhrMailZeit varchar(200),
                                        SMSZwoelfUhrMailUnixTime float, 
                                        SMSVierzehnUhr varchar (4),
                                        SMSVierzehnUhrMailZeit varchar(200),
                                        SMSVierzehnUhrMailUnixTime float, 
                                        SMSSechzehnUhr varchar (4),
                                        SMSSechzehnUhrMailZeit varchar(200),
                                        SMSSechzehnUhrMailUnixTime float, 
                                        SMSAchtzehnUhr varchar (4),
                                        SMSAchtzehnUhrMailZeit varchar(200),
                                        SMSAchtzehnUhrMailUnixTime float
                                )'''

        cursor.execute(create_script)

        insert_script = 'INSERT INTO Novaland (AppStart, Nutzer_ID, Alter_Nutzer, Geschlecht, Mail,' \
                        'NuterInfo_Abgeschlossen, Telefonnummer) ' \
                        'VALUES(%s, %s, %s, %s, %s, %s, %s)'
        insert_value = (AppStart, UserId, Alter, Gender, EMail, Nuterinformation_erledigt, Telefonnummer)

        cursor.execute(insert_script, insert_value)

        connection.commit()
    except Exception as error:
        print(error)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


# --------------------------------------------------------------------
# ALLE ID´S VON DEM SERVER RUNTERLADEN UND IN EINER VARIABEL SPEICHERN
# --------------------------------------------------------------------
connection3 = psycopg2.connect(user='aipclfonwuiort',
                               password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                               host='ec2-3-216-113-109.compute-1.amazonaws.com',
                               port='5432',
                               database='dcoubsit8jsig0')

cursor3 = connection3.cursor()
create_script = '''CREATE TABLE IF NOT EXISTS Novaland(
                                        AppStart varchar(200),
                                        Nutzer_ID varchar(12),
                                        Alter_Nutzer integer,
                                        Geschlecht varchar(10),
                                        Mail varchar(50),
                                        Telefonnummer varchar(50),
                                        ChrisGeschlecht varchar(10),
                                        Frage_1_Staatsbuerger varchar(20),
                                        Frage_2_Einfluss varchar(20),
                                        Frage_3_Sozialleistung varchar(20),
                                        Brutto_Einkommen float,
                                        Netto_Einkommen float,
                                        Frage_5_Einkommen_Zahl varchar(16),
                                        Frage_6_Einkommen_Vergleich varchar(30),
                                        Frage_7_Wohnen varchar(30),
                                        Wohnungskosten float,
                                        Frage_8_Verpflegung varchar(30),
                                        Verpflegungskosten float,
                                        Frage_9_Mobilitaet varchar(30),
                                        Mobilitaetskosten float,
                                        Frage_10_Zufriedenheit varchar(30),
                                        Rest_Einkommen float,
                                        KontoPhase3Anfang float, 
                                        Partei varchar(50),
                                        LPNStimmen float,
                                        LPNProzent float,
                                        LPNPlatz float,
                                        SPNStimmen float,
                                        SPNProzent float,
                                        SPNPlatz float,
                                        KPNStimme float,
                                        KPNProzent float,
                                        KPNPlatz float,
                                        PPNStimmen float,
                                        PPNProzent float,
                                        PPNPlatz float,
                                        LPNundKPNbund varchar (100),
                                        SPNundPPNbund varchar (100),
                                        KoalitionsBund varchar (100),
                                        Zufriedenheitsfrage2 varchar (40),
                                        Zufriedenheitsfrage3 varchar (40),
                                        Spende float,
                                        SpendeInsgesamt float,
                                        KontoPhase4Anfang float, 
                                        KontoPhase4Ende float,
                                        KontoPhase5Anfang float, 
                                        BrandBetroffen varchar (10),
                                        BrandSchadenKosten float,
                                        KontoNachBrandSchaden float,
                                        Zufriedenheitsfrage4 varchar (40),
                                        Spende2 float,
                                        Spenden2Insgesamt float,
                                        KontoPhase5Ende float,
                                        Steuerfrage1 varchar (10),
                                        Vertrauensfrage1 varchar (30),
                                        OffeneFrage varchar (1000),
                                        NuterInfo_Abgeschlossen varchar(4),
                                        Runde_1_Erledigt varchar(4),
                                        Runde_2_Erledigt varchar(4),
                                        Runde_3_Erledigt varchar(4),
                                        Runde_4_Erledigt varchar(4), 
                                        Runde_5_Erledigt varchar(4),
                                        UnixTime_P1S1 float,
                                        Zeit_P1S1 varchar (8),
                                        UnixTime_P1S2 float,
                                        Zeit_P1S2 varchar (8),
                                        UnixTime_P1S3 float,
                                        Zeit_P1S3 varchar (8),
                                        UnixTime_P1S4 float,
                                        Zeit_P1S4 varchar (8),
                                        UnixTime_P1S5 float,
                                        Zeit_P1S5 varchar (8),
                                        UnixTime_P1S6 float,
                                        Zeit_P1S6 varchar (8),
                                        UnixTime_P1S7 float,
                                        Zeit_P1S7 varchar (8),
                                        UnixTime_P2S1 float,
                                        Zeit_P2S1 varchar (10),
                                        UnixTime_P2S2 float,
                                        Zeit_P2S2 varchar (10),
                                        UnixTime_P2S3 float,
                                        Zeit_P2S3 varchar (10),
                                        UnixTime_P2S4 float,
                                        Zeit_P2S4 varchar (10),
                                        UnixTime_P2S5 float,
                                        Zeit_P2S5 varchar(10),
                                        UnixTime_P2S6 float,
                                        Zeit_P2S6 varchar(10),
                                        UnixTime_P2S7 float,
                                        Zeit_P2S7 varchar(10),
                                        UnixTime_P2S8 float,
                                        Zeit_P2S8 varchar(10),
                                        UnixTime_P2S9 float,
                                        Zeit_P2S9 varchar(10),
                                        UnixTime_P2S10 float,
                                        Zeit_P2S10 varchar(10),
                                        UnixTime_P3S1 float,
                                        Zeit_P3S1 varchar (10),
                                        UnixTime_P3S2 float,
                                        Zeit_P3S2 varchar (10),
                                        UnixTime_P3S3 float,
                                        Zeit_P3S3 varchar (10),
                                        UnixTime_P3S4 float,
                                        Zeit_P3S4 varchar (10),
                                        UnixTime_P3S5 float,
                                        Zeit_P3S5 varchar (10),
                                        UnixTime_P3S6 float,
                                        Zeit_P3S6 varchar (10),
                                        UnixTime_P3S7 float,
                                        Zeit_P3S7 varchar (10),
                                        UnixTime_P3S8 float,
                                        Zeit_P3S8 varchar (10),
                                        UnixTime_P4S1 float,
                                        Zeit_P4S1 varchar(10),
                                        UnixTime_P4S2 float,
                                        Zeit_P4S2 varchar(10),
                                        UnixTime_P4S3 float,
                                        Zeit_P4S3 varchar(10),
                                        UnixTime_P4S4 float,
                                        Zeit_P4S4 varchar(10),
                                        UnixTime_P4S5 float,
                                        Zeit_P4S5 varchar(10),
                                        UnixTime_P4S6 float,
                                        Zeit_P4S6 varchar(10),
                                        UnixTime_P4S7 float,
                                        Zeit_P4S7 varchar(10),
                                        UnixTime_P4S8 float,
                                        Zeit_P4S8 varchar(10),
                                        UnixTime_P4S9 float,
                                        Zeit_P4S9 varchar(10),
                                        UnixTime_P5S1 float,
                                        Zeit_P5S1 varchar(10),
                                        UnixTime_P5S2 float,
                                        Zeit_P5S2 varchar(10),
                                        UnixTime_P5S3 float,
                                        Zeit_P5S3 varchar(10),
                                        UnixTime_P5S4 float,
                                        Zeit_P5S4 varchar(10),
                                        UnixTime_P5S5 float,
                                        Zeit_P5S5 varchar(10),
                                        UnixTime_P5S6 float,
                                        Zeit_P5S6 varchar(10),
                                        UnixTime_P5S7 float,
                                        Zeit_P5S7 varchar(10),
                                        UnixTime_P5S8 float,
                                        Zeit_P5S8 varchar(10),
                                        UnixTime_P5S9 float,
                                        Zeit_P5S9 varchar(10),
                                        UnixTime_P5S10 float,
                                        Zeit_P5S10 varchar(10),
                                        UnixTime_P5S11 float,
                                        Zeit_P5S11 varchar(10),
                                        ZwoelfUhrMail varchar (4),
                                        ZwoelUhrMailZeit varchar (200),
                                        ZwoelfUhrMailUnixTime float,
                                        VierzehnUhrMail varchar(4),
                                        VierzehnUhrMailZeit varchar(200),
                                        VierzehnUhrMailUnixTime float, 
                                        SechzehnUhrMail varchar(4),
                                        SechzehnUhrMailZeit varchar(200),
                                        SechzehnUhrMailUnixTime float, 
                                        AchtzehnUhrMail varchar(4),
                                        AchtzehnUhrMailZeit varchar(200),
                                        AchtzehnUhrMailUnixTime float, 
                                        SMSZwoelfUhr varchar (4),
                                        SMSZwoelfUhrMailZeit varchar(200),
                                        SMSZwoelfUhrMailUnixTime float, 
                                        SMSVierzehnUhr varchar (4),
                                        SMSVierzehnUhrMailZeit varchar(200),
                                        SMSVierzehnUhrMailUnixTime float, 
                                        SMSSechzehnUhr varchar (4),
                                        SMSSechzehnUhrMailZeit varchar(200),
                                        SMSSechzehnUhrMailUnixTime float, 
                                        SMSAchtzehnUhr varchar (4),
                                        SMSAchtzehnUhrMailZeit varchar(200),
                                        SMSAchtzehnUhrMailUnixTime float )'''

cursor3.execute(create_script)
id_script = 'SELECT Nutzer_ID FROM Novaland'
cursor3.execute(id_script)
id_value = cursor3.fetchall()
ID_Alle = str(id_value)
cursor3.close()
connection3.close()


class C(BaseConstants):
    NAME_IN_URL = 'Novaland'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # ------------------------------------------
    # NutzerInfo
    # -----------------------------------------
    # -----------------------------
    # Nutzer Informationen sammeln
    # -----------------------------
    # ----------------------------
    # Nutzer ID
    NutzerID = models.StringField()
    NutzerInformationsSeiteAbgeschlossen = models.StringField()
    ErsteRundeErledigt = models.IntegerField()
    URL = models.StringField()

    # ------------------------------
    # Seite 2
    # -----------------------------
    Nutzer_Email = models.StringField(
        label="Geben Sie bitte eine E-Mail Adresse ein, unter welcher wir Sie erreichen können, für die weitere Teilnahme an der Studie")
    Nutzer_Alter = models.IntegerField(label="Geben Sie bitte ihr Alter ein")
    Nutzer_Gender = models.StringField(
        choices=[["Männlich", "Männlich"],
                 ["Weiblich", "Weiblich"],
                 ["Divers", "Divers"],
                 ["Keine Angabe", "Keine Angabe"]],
        label="Wählen Sie bitte das Geschlecht aus, welches Sie sich zugehörig fühlen",
        widget=widgets.RadioSelect
    )
    Telefonnummer = models.StringField(
        label="Wenn Sie eine Benachrichtung per SMS bekommen wollen, können Sie hier ihre Telefonnummer eingeben. Bitte geben Sie zusätzlich noch ihre Landesvorwahl mit an. Beispiel: +491763456784  -   Wenn Sie das nicht wollen, geben Sie bitte ein Minus - ein.")

    # ------------------------------
    # Zeitabfrage
    # -----------------------------
    # Wann die App geöffnet worden ist
    ZeitStartapp = models.StringField()

    # Zeit: Erste Seite - Nutzerinfo
    ZeitErsteSeite = models.FloatField()

    # Zeit: Zweite Seite - Nutzerinfo
    ZeitZweiteSeite = models.FloatField()

    # --------------------------------------------------
    # Phase Eins Zeit
    # -------------------------------------------------

    # Zeit: Phase 1 Seite 1
    PhaseEinsSeiteEins = models.FloatField()
    UnixTimeP1S1 = models.FloatField()
    # Zeit: Phase 1 Seite 2
    PhaseEinsSeiteZwei = models.FloatField()
    UnixTimeP1S2 = models.FloatField()
    # Zeit: Phase 1 Seite 3
    PhaseEinsSeiteDrei = models.FloatField()
    UnixTimeP1S3 = models.FloatField()
    # Zeit: Phase 1 Seite 4
    PhaseEinsSeiteVier = models.FloatField()
    UnixTimeP1S4 = models.FloatField()
    # Zeit: Phase 1 Seite 5
    PhaseEinsSeiteFuenf = models.FloatField()
    UnixTimeP1S5 = models.FloatField()
    # Zeit: Phase 1 Seite 6
    PhaseEinsSeiteSechs = models.FloatField()
    UnixTimeP1S6 = models.FloatField()
    # Zeit: Phase 1 Seite 7
    PhaseEinsSeiteSieben = models.FloatField()
    UnixTimeP1S7 = models.FloatField()

    test = models.StringField()

    # Group ID für Phase 1
    GroupID = models.StringField()

    # -------------------------------------------
    # Page_1
    # ------------------------------------------
    # Auswahl welches Geschlecht Chris haben soll
    ChrisGender = models.StringField(choices=[["Männlich", "Männlich"], ["Weiblich", "Weiblich"], ["Divers", "Divers"]],
                                     label="",
                                     widget=widgets.RadioSelect)

    # -------------------------------------------
    # Page_5
    # ------------------------------------------
    Frage_1 = models.StringField(choices=[["Ja", "Ja"], ["Nein", "Nein"]],
                                 label="",
                                 widget=widgets.RadioSelect)
    # -------------------------------------------
    # Page_6
    # ------------------------------------------
    Frage_2 = models.StringField(choices=[["Ja", "Ja"], ["Nein", "Nein"]],
                                 label="",
                                 widget=widgets.RadioSelect)
    # -------------------------------------------
    # Page_7
    # ------------------------------------------
    Frage_3 = models.StringField()


    # ------------------------------------------
    # Info, ob diese Runde schon gespielt worden ist
    # ------------------------------------------
    Runde_1_erledigt = models.StringField()

    Loop = models.IntegerField()


# PAGES

class NutzerInfo_Page_1(Page):
    form_model = 'player'

    # -----------------------------
    # Prüft ob das heutige Datum in der Vorraussetzung definiert ist
    # -----------------------------

    # def is_displayed(player: Player):
    # HeutigeDatum = str(datetime.now().strftime("%H:%M:%S %d.%m.%Y)"))
    # DatumDerStudie = str(datetime(2022, 3, 14).strftime("%d.%m.%Y"))
    # if DatumDerStudie in HeutigeDatum:
    #     return True

    @staticmethod
    def vars_for_template(player: Player):
        DatumHeute = datetime.now()
        player.ZeitStartapp = str(DatumHeute)
        player.NutzerID = player.participant.label


    @staticmethod
    def live_method(player: Player, data):
        if "ZeitErsteRunde" in data:
            player.ZeitErsteSeite = data['Zeit1']
            P0S1Zeit = dict(type='P0S1Weiter')
            return {0: P0S1Zeit}


class NutzerInfo_Page_2(Page):
    form_model = 'player'
    form_fields = ["Nutzer_Email", "Nutzer_Alter", "Nutzer_Gender", "Telefonnummer"]

    @staticmethod
    def error_message(player, value):
        try:
            valid = validate_email(value["Nutzer_Email"].strip())
        except EmailNotValidError as e:
            return 'Die eingegebene E-Mail-Adresse ist ungültig. Bitte geben Sie Ihre E-Mail-Adresse erneut ein.'

    @staticmethod
    def live_method(player: Player, data):
        if "ZeitZweiteRunde" in data:
            player.ZeitZweiteSeite = data['Zeit2']
            P0S2Zeit = dict(type='P0S2Weiter')
            return {0: P0S2Zeit}

        if "Savedata" in data:
            player.NutzerInformationsSeiteAbgeschlossen = "Ja"

        if 'Telefonnummer' in data:
            player.Telefonnummer = data['Telefonnummer']


class NutzerInfo_Page_3(Page):
    @staticmethod
    def vars_for_template(player: Player):
        player.NutzerInformationsSeiteAbgeschlossen = "Ja"
        player.Loop = 0
        if player.Loop == 0:
            connectToRound0(player.ZeitStartapp, player.NutzerID, player.Nutzer_Alter,
                            player.Nutzer_Gender, player.Nutzer_Email, player.NutzerInformationsSeiteAbgeschlossen,
                            player.Telefonnummer)
            player.Loop = 1
        player.Loop = 1


# ----------------------------------------------------------------------------------------
#
# PHASE 1 SEITEN
#
# ---------------------------------------------------------------------------------------

class Page_1(Page):
    form_model = 'player'
    form_fields = ['ChrisGender']

    @staticmethod
    def live_method(player: Player, data):
        if "ZeitPhaseEinsErsteSeite" in data:
            player.PhaseEinsSeiteEins = data['Phase1Seite1Zeit']
            player.UnixTimeP1S1 = time.time()
            P1S1Zeit = dict(type='P1S1Weiter')
            return {0: P1S1Zeit}


class Page_2(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitPhaseEinsZweiteSeite" in data:
            player.PhaseEinsSeiteZwei = data['Phase1Seite2Zeit']
            player.UnixTimeP1S2 = time.time()
            P1S2Weiter = dict(type='P1S2Weiter')
            return {0: P1S2Weiter}


class Page_3(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitPhaseEinsDritteSeite" in data:
            player.PhaseEinsSeiteDrei = data['Phase1Seite3Zeit']
            player.UnixTimeP1S3 = time.time()
            P1S3Weiter = dict(type='P1S3Weiter')
            return {0: P1S3Weiter}


class Page_4(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitPhaseEinsVierteSeite" in data:
            player.PhaseEinsSeiteVier = data['Phase1Seite4Zeit']
            player.UnixTimeP1S4 = time.time()
            P1S4Weiter = dict(type='P1S4Weiter')
            return {0: P1S4Weiter}


class Page_5(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitPhaseEinsFuenfeSeite" in data:
            player.PhaseEinsSeiteFuenf = data['Phase1Seite5Zeit']
            player.UnixTimeP1S5 = time.time()
            P1S5Weiter = dict(type='P1S5Weiter')
            return {0: P1S5Weiter}
        if "Frage1" in data:
            player.Frage_1 = data["Frage1Antwort"]


class Page_6(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitPhaseEinsSechsteSeite" in data:
            player.PhaseEinsSeiteSechs = data['Phase1Seite6Zeit']
            player.UnixTimeP1S6 = time.time()
            P1S6Weiter = dict(type='P1S6Weiter')
            return {0: P1S6Weiter}
        if "Frage2" in data:
            player.Frage_2 = data["Frage2Antwort"]


class Page_7(Page):
    form_model = 'player'

    @staticmethod
    def live_method(player: Player, data):
        if "ZeitPhaseEinsSiebteSeite" in data:
            player.PhaseEinsSeiteSieben = data['Phase1Seite7Zeit']
            player.UnixTimeP1S7 = time.time()
            P1S7Weiter = dict(type='P1S7Weiter')
            return {0: P1S7Weiter}

        if "Frage3" in data:
            player.Frage_3 = data["Frage3Antwort"]
            player.Runde_1_erledigt = "Ja"


class Page_8(Page):
    @staticmethod
    def vars_for_template(player: Player):
        player.URL = "https://DemoNovaland.herokuapp.com/InitializeParticipant/" + player.participant.label

        connection4 = psycopg2.connect(user='aipclfonwuiort',
                                       password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                       host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                       port='5432',
                                       database='dcoubsit8jsig0')

        cursor4 = connection4.cursor()

        id_script2 = 'UPDATE Novaland SET chrisgeschlecht = %s, frage_1_staatsbuerger = %s, frage_2_einfluss = %s,' \
                     'Frage_3_Sozialleistung = %s, Zeit_P1S1 = %s, Zeit_P1S2 = %s, Zeit_P1S3 = %s,' \
                     'Zeit_P1S4 = %s, Zeit_P1S5 = %s, Zeit_P1S6 = %s, Zeit_P1S7 = %s, Runde_1_Erledigt = %s, UnixTime_P1S1 =%s, UnixTime_P1S2 = %s, UnixTime_P1S3 = %s, UnixTime_P1S4 = %s, UnixTime_P1S5 = %s, UnixTime_P1S6 = %s, UnixTime_P1S7 = %s WHERE nutzer_id = %s'
        id_value2 = (player.ChrisGender, player.Frage_1, player.Frage_2, player.Frage_3,
                     player.PhaseEinsSeiteEins, player.PhaseEinsSeiteZwei, player.PhaseEinsSeiteDrei,
                     player.PhaseEinsSeiteVier,
                     player.PhaseEinsSeiteFuenf, player.PhaseEinsSeiteSechs, player.PhaseEinsSeiteSieben,
                     player.Runde_1_erledigt, player.UnixTimeP1S1, player.UnixTimeP1S2, player.UnixTimeP1S3,
                     player.UnixTimeP1S4, player.UnixTimeP1S5, player.UnixTimeP1S6, player.UnixTimeP1S7, player.NutzerID)
        cursor4.execute(id_script2, id_value2)
        connection4.commit()
        cursor4.close()
        connection4.close()


page_sequence = [NutzerInfo_Page_1, NutzerInfo_Page_2, NutzerInfo_Page_3, Page_1, Page_2, Page_3, Page_4, Page_5,
                 Page_6, Page_7, Page_8]
