import psycopg2
from otree.api import *
import random


class C(BaseConstants):
    NAME_IN_URL = 'phase_2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # ----------------------
    # Login
    # ----------------------
    IdAlle = models.StringField()
    IDPlayer = models.StringField()
    ID_korrekt = models.IntegerField()

    # -----------------------
    # Page 1
    # ----------------------
    Brutto_Einkommen = models.FloatField()
    Netto_Einkommen = models.FloatField()

    # -----------------------
    # Page 2
    # ----------------------
    Frage_1 = models.StringField()

    # -----------------------
    # Page 3
    # ----------------------
    Frage_2 = models.StringField()
    # -----------------------
    # Page 4
    # ----------------------
    Frage_3_Wohnen = models.StringField()

    Wohnungskosten = models.FloatField()

    # -----------------------
    # Page 5
    # ----------------------
    Frage_4_Verpflegung = models.StringField()
    Verpflegungskosten = models.FloatField()

    # -----------------------
    # Page 6
    # ----------------------
    Frage_5_Mobilitaet = models.StringField()
    Mobilitaetskosten = models.FloatField()
    # -----------------------
    # Page 9
    # ----------------------
    Rest_Einkommen = models.FloatField()

    # ----------------------
    # Zeit
    # ---------------------
    P2S2Zeit = models.FloatField()
    P2S3Zeit = models.FloatField()
    P2S4Zeit = models.FloatField()
    P2S5Zeit = models.FloatField()
    P2S6Zeit = models.FloatField()
    P2S7Zeit = models.FloatField()
    P2S8Zeit = models.FloatField()
    P2S9Zeit = models.FloatField()

    # ------------------------------------------
    # Info, ob diese Runde schon gespielt worden ist
    # ------------------------------------------
    Runde_2_erledigt = models.StringField()

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

    def vars_for_template(player: Player):
        player.ID_korrekt = 0
        connection5 = psycopg2.connect(user='aipclfonwuiort',
                                       password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                       host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                       port='5432',
                                       database='dcoubsit8jsig0')

        cursor5 = connection5.cursor()

        create_script = '''CREATE TABLE IF NOT EXISTS Novaland(
                                    AppStart varchar(200),
                                    Nutzer_ID varchar(12),
                                    Alter_Nutzer integer,
                                    Geschlecht varchar(10),
                                    Mail varchar(50),
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
                                    Zeit_Phase1_Seite1 varchar (8),
                                    Zeit_Phase1_Seite2 varchar (8),
                                    Zeit_Phase1_Seite3 varchar (8),
                                    Zeit_Phase1_Seite4 varchar (8),
                                    Zeit_Phase1_Seite5 varchar (8),
                                    Zeit_Phase1_Seite6 varchar (8),
                                    Zeit_Phase1_Seite7 varchar (8),
                                    Zeit_Phase1_Seite8 varchar (8),
                                    Zeit_P2S2 varchar (10),
                                    Zeit_P2S3 varchar (10),
                                    Zeit_P2S4 varchar (10),
                                    Zeit_P2S5 varchar(10),
                                    Zeit_P2S6 varchar(10),
                                    Zeit_P2S7 varchar(10),
                                    Zeit_P2S8 varchar(10),
                                    Zeit_P2S9 varchar(10),
                                    Zeit_P3S1 varchar (10),
                                    Zeit_P3S2 varchar (10),
                                    Zeit_P3S3 varchar (10),
                                    Zeit_P3S4 varchar (10),
                                    Zeit_P3S5 varchar (10),
                                    Zeit_P3S6 varchar (10),
                                    Zeit_P3S7 varchar (10)
                                      )'''

        cursor5.execute(create_script)

        id_script = 'SELECT Nutzer_ID from Novaland'
        cursor5.execute(id_script)
        id_value = cursor5.fetchall()
        player.IdAlle = str(id_value)
        cursor5.close()
        connection5.close()

        player.IDPlayer = ""


class Phase_2_page_1(Page):
    @staticmethod
    def vars_for_template(player: Player):
        niedrig = range(1, 250, 3)
        mittel = range(2, 250, 3)
        hoch = range(3, 250, 3)

        if player.id_in_group in niedrig:
            player.Brutto_Einkommen = 1250
        elif player.id_in_group in mittel:
            player.Brutto_Einkommen = 3500
        elif player.id_in_group in hoch:
            player.Brutto_Einkommen = 5000

        player.Netto_Einkommen = player.Brutto_Einkommen - ((player.Brutto_Einkommen / 100) * 30)
        return {
            "Brutto_Einkommen": player.Brutto_Einkommen,
            "Netto_Einkommen": player.Netto_Einkommen
        }


class Phase_2_Page_2(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        Netto_Einkommen = player.Netto_Einkommen
        return {
            "Netto_Einkommen": Netto_Einkommen,
        }

    @staticmethod
    def js_vars(player: Player):
        return {
            "NettoEinkommen": player.Netto_Einkommen,
        }

    @staticmethod
    def live_method(player: Player, data):
        if "P2S2FrageEinkommen" in data:
            player.Frage_1 = data["P2S2AntwortEinkommen"]
        if "ZeitP2S2" in data:
            player.P2S2Zeit = data["ZeitP2S2Time"]


class Phase_2_page_3(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        Netto_Einkommen = player.Netto_Einkommen
        return {
            "Netto_Einkommen": Netto_Einkommen,
        }

    @staticmethod
    def js_vars(player: Player):
        return {
            "NettoEinkommen": player.Netto_Einkommen,
        }

    @staticmethod
    def live_method(player: Player, data):
        if "P2S3FrageRelation" in data:
            player.Frage_2 = data['P2S3AntwortRelation']
        if "P2S3Zeit" in data:
            player.P2S3Zeit = data['P2S3Zeit']


class Phase_2_Page_4(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        return {"Geld": player.Netto_Einkommen}

    @staticmethod
    def js_vars(player: Player):
        return {
            "Geld2": player.Netto_Einkommen,
        }

    @staticmethod
    def live_method(player: Player, data):
        if "Haus" in data:
            player.Frage_3_Wohnen = data["HausArt"]
            player.Wohnungskosten = data["HausKosten"]
        if "ZeitP2S4" in data:
            player.P2S4Zeit = data["ZeitP2S4"]


class Phase_2_Page_5(Page):
    form_model = 'player'

    @staticmethod
    def js_vars(player: Player):
        NeuerWert = player.Netto_Einkommen - player.Wohnungskosten
        return {
            "NeuerWert": NeuerWert
        }

    @staticmethod
    def vars_for_template(player: Player):
        NeuerWert2 = player.Netto_Einkommen - player.Wohnungskosten
        return {
            "NeuerWert2": NeuerWert2
        }

    @staticmethod
    def live_method(player: Player, data):
        if 'Verpflegung' in data:
            player.Frage_4_Verpflegung = data['VerpflegungsArt']
            player.Verpflegungskosten = data['VerpflegungskostenKosten']
        if "ZeitP2S5" in data:
            player.P2S5Zeit = data["ZeitP2S5"]


class Phase_2_Page_6(Page):
    form_model = 'player'

    @staticmethod
    def js_vars(player: Player):
        LetzterWert = player.Netto_Einkommen - player.Wohnungskosten - player.Verpflegungskosten
        return {
            "LetzterWert": LetzterWert
        }

    @staticmethod
    def vars_for_template(player: Player):
        LetzterWert2 = player.Netto_Einkommen - player.Wohnungskosten - player.Verpflegungskosten
        return {
            "LetzterWert2": LetzterWert2
        }

    @staticmethod
    def live_method(player: Player, data):
        if 'Mobilitaet' in data:
            player.Frage_5_Mobilitaet = data['MobilitaetArt']
            player.Mobilitaetskosten = data['MobilitaetKosten']
        if "ZeitP2S6" in data:
            player.P2S6Zeit = data["ZeitP2S6"]


class Phase_2_Page_7(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP2S7" in data:
            player.P2S7Zeit = data["ZeitP2S7"]


class Phase_2_Page_8(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP2S8" in data:
            player.P2S8Zeit = data["ZeitP2S8"]


class Phase_2_Page_9(Page):
    def vars_for_template(player: Player):
        if player.Wohnungskosten == 700:
            Wohnung_satz = "einem großen Haus zu wohnen"
        elif player.Wohnungskosten == 500:
            Wohnung_satz = "einem Reihenhaus zu wohnen"
        elif player.Wohnungskosten == 350:
            Wohnung_satz = "in einer geräumigen Wohnung zu wohnen"
        elif player.Wohnungskosten == 200:
            Wohnung_satz = "einer normal großen Wohnung zu wohnen"

        if player.Verpflegungskosten == 700:
            Verpflegungssatz = "regelmäßig in Restaurants Essen zu gehen"
        elif player.Verpflegungskosten == 500:
            Verpflegungssatz = "häufig etwas Essen zu bestellen"
        elif player.Verpflegungskosten == 200:
            Verpflegungssatz = "häufig selber zu kochen"

        if player.Mobilitaetskosten == 700:
            Mobilitaetssatz = "hauptsächlich mit dem eigenen Auto zu fahren"
        if player.Mobilitaetskosten == 450:
                Mobilitaetssatz = "das Sie bei Bedarf ein Auto mieten und öffentliche Verkehrsmittel nutzen"
        if player.Mobilitaetskosten == 200:
            Mobilitaetssatz = "das sie Fahrrad fahren und bei Bedarf öffentliche Verkehrsmittel verwenden"

        player.Rest_Einkommen = player.Netto_Einkommen - player.Wohnungskosten - player.Verpflegungskosten - player.Mobilitaetskosten

        player.Runde_2_erledigt = "Ja"

        return {
            "Wohnung": Wohnung_satz,
            "Verpflegung": Verpflegungssatz,
            "Mobilitaet": Mobilitaetssatz
        }

    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP2S9" in data:
            player.P2S9Zeit = data["ZeitP2S9"]

class Phase_2_Page_10(Page):
    @staticmethod
    def vars_for_template(player: Player):
        connection3 = psycopg2.connect(user='aipclfonwuiort',
                                       password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                       host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                       port='5432',
                                       database='dcoubsit8jsig0')

        cursor3 = connection3.cursor()

        id_script = 'UPDATE Novaland SET brutto_einkommen = %s, netto_einkommen = %s, frage_5_einkommen_zahl = %s, ' \
                    'frage_6_einkommen_vergleich = %s, frage_7_wohnen = %s, wohnungskosten = %s, frage_8_Verpflegung = %s, verpflegungskosten = %s,' \
                    'frage_9_mobilitaet = %s, mobilitaetskosten = %s, rest_einkommen = %s, Runde_2_Erledigt = %s WHERE nutzer_id = %s'
        id_value = (
            player.Brutto_Einkommen, player.Netto_Einkommen, player.Frage_1, player.Frage_2, player.Frage_3_Wohnen,
            player.Wohnungskosten, player.Frage_4_Verpflegung, player.Verpflegungskosten, player.Frage_5_Mobilitaet,
            player.Mobilitaetskosten, player.Rest_Einkommen, player.Runde_2_erledigt, player.IDPlayer)
        cursor3.execute(id_script, id_value)
        connection3.commit()
        InsertValues = '''UPDATE NOVALAND SET zeit_p2s2 = %s, Zeit_p2s3 = %s, Zeit_p2s4 = %s, Zeit_p2s5 = %s, Zeit_p2s6 = %s, Zeit_p2s7 = %s, Zeit_p2s8 = %s, Zeit_p2S9 = %s WHERE nutzer_id = %s  '''
        ValueNames = (player.P2S2Zeit, player.P2S3Zeit, player.P2S4Zeit, player.P2S5Zeit, player.P2S6Zeit, player.P2S7Zeit,
        player.P2S8Zeit, player.P2S9Zeit, player.IDPlayer)
        cursor3.execute(InsertValues, ValueNames)
        connection3.commit()
        cursor3.close()
        connection3.close()


page_sequence = [Login, Phase_2_page_1, Phase_2_Page_2, Phase_2_page_3, Phase_2_Page_4, Phase_2_Page_5, Phase_2_Page_6,
                 Phase_2_Page_7, Phase_2_Page_8, Phase_2_Page_9, Phase_2_Page_10]
