from otree.api import *
import smtplib
import psycopg2
import ssl
from email import *
from datetime import *
from email_validator import validate_email, EmailNotValidError


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
                                        Seitenzahl integer,
                                        ChrisGeschlecht varchar(10),
                                        Frage_1_Staatsbuerger varchar(20),
                                        Frage_2_Einfluss varchar(20),
                                        Frage_3 varchar(20),
                                        Frage_4 varchar(20),
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
                                        Rest_Einkommen float,
                                        Partei varchar(50),
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
                                        UnixTime_P1S8 float,
                                        Zeit_P1S8 varchar (8),
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
                                        Zeit_P3S7 varchar (10)
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
                                        Seitenzahl integer,
                                        ChrisGeschlecht varchar(10),
                                        Frage_1_Staatsbuerger varchar(20),
                                        Frage_2_Einfluss varchar(20),
                                        Frage_3 varchar(20),
                                        Frage_4 varchar(20),
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
                                        Rest_Einkommen float,
                                        Partei varchar(50),
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
                                        UnixTime_P1S8 float,
                                        Zeit_P1S8 varchar (8),
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
                                        Zeit_P3S7 varchar (10)
                                )'''

cursor3.execute(create_script)
id_script = 'SELECT Nutzer_ID FROM Novaland'
cursor3.execute(id_script)
id_value = cursor3.fetchall()
ID_Alle = str(id_value)
cursor3.close()
connection3.close()

ID_URL = ""


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
    Telefonnummer = models.StringField(label="Wenn Sie eine Benachrichtung per SMS bekommen wollen, können Sie hier ihre Telefonnummer eingeben wollen. Bitte gebe Sie ihre Landesvorwahl mit ein. Beispiel: +491763456784  -   Wenn Sie das nicht wollen, geben Sie bitte ein Minus ein.")

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
    # Zeit: Phase 1 Seite 8
    PhaseEinsSeiteAcht = models.FloatField()
    UnixTimeP1S8 = models.FloatField()

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
    Frage_3 = models.StringField(choices=[["Ja", "Ja"], ["Nein", "Nein"]],
                                 label="",
                                 widget=widgets.RadioSelect)

    # -------------------------------------------
    # Page_8
    # ------------------------------------------
    Frage_4 = models.StringField(choices=[["Ja", "Ja"], ["Nein", "Nein"]],
                                 label="",
                                 widget=widgets.RadioSelect)

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

    def vars_for_template(player: Player):
        DatumHeute = datetime.now()
        player.ZeitStartapp = str(DatumHeute)
        player.NutzerID = player.participant.code
        player.test = ID_URL

    @staticmethod
    def live_method(player: Player, data):
        if "ZeitErsteRunde" in data:
            player.ZeitErsteSeite = data['Zeit1']


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

        if "Savedata" in data:
            player.NutzerInformationsSeiteAbgeschlossen = "Ja"

        if 'Telefonnummer' in data:
            player.Telefonnummer = data['Telefonnummer']


class NutzerInfo_Page_3(Page):
    @staticmethod
    def vars_for_template(player: Player):
        player.Loop = 0
        if player.Loop == 0:
            player.Loop = 1
            connectToRound0(player.ZeitStartapp, player.NutzerID, player.Nutzer_Alter,
                            player.Nutzer_Gender, player.Nutzer_Email, player.NutzerInformationsSeiteAbgeschlossen,
                            player.Telefonnummer)


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


class Page_2(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitPhaseEinsZweiteSeite" in data:
            player.PhaseEinsSeiteZwei = data['Phase1Seite2Zeit']
            player.UnixTimeP1S2 = time.time()


class Page_3(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitPhaseEinsDritteSeite" in data:
            player.PhaseEinsSeiteDrei = data['Phase1Seite3Zeit']
            player.UnixTimeP1S3 = time.time()


class Page_4(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitPhaseEinsVierteSeite" in data:
            player.PhaseEinsSeiteVier = data['Phase1Seite4Zeit']
            player.UnixTimeP1S4 = time.time()


class Page_5(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitPhaseEinsFuenfeSeite" in data:
            player.PhaseEinsSeiteFuenf = data['Phase1Seite5Zeit']
            player.UnixTimeP1S5 = time.time()
        if "Frage1" in data:
            player.Frage_1 = data["Frage1Antwort"]


class Page_6(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitPhaseEinsSechsteSeite" in data:
            player.PhaseEinsSeiteSechs = data['Phase1Seite6Zeit']
            player.UnixTimeP1S6 = time.time()
        if "Frage2" in data:
            player.Frage_2 = data["Frage2Antwort"]


class Page_7(Page):
    form_model = 'player'
    form_fields = ['Frage_3']

    @staticmethod
    def live_method(player: Player, data):
        if "ZeitPhaseEinsSiebteSeite" in data:
            player.PhaseEinsSeiteSieben = data['Phase1Seite7Zeit']
            player.UnixTimeP1S7 = time.time()


class Page_8(Page):
    form_model = 'player'
    form_fields = ['Frage_4']

    @staticmethod
    def vars_for_template(player: Player):
        player.URL = "https://pilotnovaland2022.herokuapp.com/join/" + str(player.NutzerID)

    @staticmethod
    def live_method(player: Player, data):
        if "ZeitPhaseEinsAchteSeite" in data:
            player.PhaseEinsSeiteAcht = data['Phase1Seite8Zeit']
            player.UnixTimeP1S8 = time.time()
        if "RundeEinsErledigt" in data:
            player.Runde_1_erledigt = "Ja"


class Page_9(Page):
    @staticmethod
    def vars_for_template(player: Player):
        connection4 = psycopg2.connect(user='aipclfonwuiort',
                                       password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                       host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                       port='5432',
                                       database='dcoubsit8jsig0')

        cursor4 = connection4.cursor()

        id_script2 = 'UPDATE Novaland SET chrisgeschlecht = %s, frage_1_staatsbuerger = %s, frage_2_einfluss = %s,' \
                     'frage_3 = %s, frage_4 = %s, Zeit_P1S1 = %s, Zeit_P1S2 = %s, Zeit_P1S3 = %s,' \
                     'Zeit_P1S4 = %s, Zeit_P1S5 = %s, Zeit_P1S6 = %s, Zeit_P1S7 = %s,' \
                     'Zeit_P1S8 = %s, Runde_1_Erledigt = %s, UnixTime_P1S1 =%s, UnixTime_P1S2 = %s, UnixTime_P1S3 = %s, UnixTime_P1S4 = %s, UnixTime_P1S5 = %s, UnixTime_P1S6 = %s, UnixTime_P1S7 = %s, UnixTime_P1S8 = %s WHERE nutzer_id = %s'
        id_value2 = (player.ChrisGender, player.Frage_1, player.Frage_2, player.Frage_3, player.Frage_4,
                     player.PhaseEinsSeiteEins, player.PhaseEinsSeiteZwei, player.PhaseEinsSeiteDrei,
                     player.PhaseEinsSeiteVier,
                     player.PhaseEinsSeiteFuenf, player.PhaseEinsSeiteSechs, player.PhaseEinsSeiteSieben,
                     player.PhaseEinsSeiteAcht,
                     player.Runde_1_erledigt, player.UnixTimeP1S1, player.UnixTimeP1S2, player.UnixTimeP1S3, player.UnixTimeP1S4, player.UnixTimeP1S5, player.UnixTimeP1S6, player.UnixTimeP1S7, player.UnixTimeP1S8, player.NutzerID)
        cursor4.execute(id_script2, id_value2)
        connection4.commit()
        cursor4.close()
        connection4.close()
        # --------------------------------------------------------------------
        # --------------------- E-Mails versenden-----------------------------
        From_mail = "pilotnovaland@gmail.com"
        Passwort = "0?$W6XrieU!J+KO=,,zv"
        To_Mail = player.Nutzer_Email
        ssl_context = ssl.create_default_context()
        subject = 'Ihre Teilnahme an unserem politischen Verhaltensspiel "Novaland.'
        code = player.NutzerID
        Url = " https://pilotnovaland2022.herokuapp.com/join/" + player.participant.code
        Nachricht = "Sehr geehrte:r Teilnehmer:in an unserem politischen Verhaltensspiel 'Novaland', " \
                    "\nDie Universität Duisburg bedankt sich bei Ihnen für ihre Teilnahme an der ersten Runde. " \
                    "Damit die Teilnahme vollständig ist, würden wir Sie drum bitte, an der zweiten Runde teilzunehmen. \n" \
                    "Um an der zweiten Runde teilnehmen zu können, müssen Sie auf diesen Link klicken: " + Url + " " \
                                                                                                                 "\n\nDamit Sie sich einlogen können müssen Sie einfach diesen Code eingeben: " + code + \
                    "\n\nWir bedanken uns bei ihnen recht herzlich!\n\n Universität Duisburg"
        msg = message.Message()
        msg.set_charset("utf-8")
        msg['Content-type'] = 'text/plain; charset=utf-8'
        msg['Content-transfer-encoding'] = '8bit'
        msg['Subject'] = subject
        msg['From'] = From_mail
        msg['To'] = To_Mail
        msg.set_payload(Nachricht, charset="utf-8")

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl_context)
        server.login(From_mail, Passwort)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()


page_sequence = [NutzerInfo_Page_1, NutzerInfo_Page_2, NutzerInfo_Page_3, Page_1, Page_2, Page_3, Page_4, Page_5,
                 Page_6, Page_7, Page_8, Page_9]
