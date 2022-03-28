import psycopg2
from otree.api import *
import random
from datetime import *
from datetime import time
import time


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
    ParticipantID = models.StringField()
    LoginCheck = models.IntegerField()

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

    # ---------------------
    # Zufriedenheitsfrage
    # --------------------
    Zufriedenheitsfrage1 = models.StringField(
        choices=[["Sehr zufrieden", "Sehr zufrieden"], ["zufrieden", ""], ["Mitte", ""], ["Nicht zufrieden", ""], ["Überhaupt nicht zufrieden", "Überhaupt nicht zufrieden"]],
        label="",
        widget=widgets.RadioSelect
    )

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
    P2S10Zeit = models.FloatField()
    UnixTimeP2S2 = models.FloatField()
    UnixTimeP2S3 = models.FloatField()
    UnixTimeP2S4 = models.FloatField()
    UnixTimeP2S5 = models.FloatField()
    UnixTimeP2S6 = models.FloatField()
    UnixTimeP2S7 = models.FloatField()
    UnixTimeP2S8 = models.FloatField()
    UnixTimeP2S9 = models.FloatField()
    UnixTimeP2S10 = models.FloatField()

    # ------------------------------------------
    # Info, ob diese Runde schon gespielt worden ist
    # ------------------------------------------
    Runde_2_erledigt = models.StringField()


class Waiting_Site(Page):
    def is_displayed(player: Player):
        Zeit = 12 * 60 * 60
        ProgrammTagZeit = (datetime.now().time().hour * 60 * 60) + (
                    datetime.now().time().minute * 60) + datetime.now().time().second
        differenz = Zeit - ProgrammTagZeit
        if differenz > 0:
            return True
        else:
            return False


class Phase_2_page_1(Page):
    @staticmethod
    def vars_for_template(player: Player):
        player.IDPlayer = player.participant.code

        niedrig = range(1, 250, 3)
        mittel = range(2, 250, 3)
        hoch = range(3, 250, 3)

        if player.id_in_group in niedrig:
            player.Brutto_Einkommen = 2000
        elif player.id_in_group in mittel:
            player.Brutto_Einkommen = 2850
        elif player.id_in_group in hoch:
            player.Brutto_Einkommen = 5000

        player.Netto_Einkommen = player.Brutto_Einkommen - ((player.Brutto_Einkommen / 100) * 30)
        if player.Netto_Einkommen == 1995:
            player.Netto_Einkommen = 2000
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
            player.UnixTimeP2S2 = time.time()


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
            player.UnixTimeP2S3 = time.time()


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
            player.UnixTimeP2S4 = time.time()


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
            player.UnixTimeP2S5 = time.time()


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
            player.UnixTimeP2S6 = time.time()


class Phase_2_Page_7(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP2S7" in data:
            player.P2S7Zeit = data["ZeitP2S7"]
            player.UnixTimeP2S7 = time.time()


class Phase_2_Page_8(Page):
    @staticmethod
    def live_method(player: Player, data):
        if "ZeitP2S8" in data:
            player.P2S8Zeit = data["ZeitP2S8"]
            player.UnixTimeP2S8 = time.time()


class Phase_2_Page_9(Page):
    def vars_for_template(player: Player):
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
            player.UnixTimeP2S9 = time.time()


class Phase_2_Page_10(Page):
    form_model = 'player'
    form_fields = ['Zufriedenheitsfrage1']

    def live_method(player: Player, data):
        if "ZeitP2S10" in data:
            player.P2S10Zeit = data["ZeitP2S10"]
            player.UnixTimeP2S10 = time.time()


class Phase_2_Page_11(Page):
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
                    'frage_9_mobilitaet = %s, mobilitaetskosten = %s, Frage_10_Zufriedenheit = %s, rest_einkommen = %s, Runde_2_Erledigt = %s WHERE nutzer_id = %s'
        id_value = (
            player.Brutto_Einkommen, player.Netto_Einkommen, player.Frage_1, player.Frage_2, player.Frage_3_Wohnen,
            player.Wohnungskosten, player.Frage_4_Verpflegung, player.Verpflegungskosten, player.Frage_5_Mobilitaet,
            player.Mobilitaetskosten, player.Zufriedenheitsfrage1, player.Rest_Einkommen, player.Runde_2_erledigt, player.IDPlayer)
        cursor3.execute(id_script, id_value)
        connection3.commit()
        InsertValues = '''UPDATE NOVALAND SET zeit_p2s2 = %s, Zeit_p2s3 = %s, Zeit_p2s4 = %s, Zeit_p2s5 = %s, Zeit_p2s6 = %s, Zeit_p2s7 = %s, Zeit_p2s8 = %s, Zeit_p2S9 = %s, Zeit_p2s10 = %s, UnixTime_P2S2 = %s, UnixTime_P2S3 = %s, UnixTime_P2S4 = %s, UnixTime_P2S5 = %s, UnixTime_P2S6 = %s, UnixTime_P2S7 = %s, UnixTime_P2S8 = %s, UnixTime_P2S9 = %s, UnixTime_P2S10 = %s WHERE nutzer_id = %s  '''
        ValueNames = (
        player.P2S2Zeit, player.P2S3Zeit, player.P2S4Zeit, player.P2S5Zeit, player.P2S6Zeit, player.P2S7Zeit,
        player.P2S8Zeit, player.P2S9Zeit, player.P2S10Zeit, player.UnixTimeP2S2, player.UnixTimeP2S3, player.UnixTimeP2S4,
        player.UnixTimeP2S5, player.UnixTimeP2S6, player.UnixTimeP2S7, player.UnixTimeP2S8, player.UnixTimeP2S9, player.UnixTimeP2S10,
        player.IDPlayer)
        cursor3.execute(InsertValues, ValueNames)
        connection3.commit()
        cursor3.close()
        connection3.close()


page_sequence = [Waiting_Site, Phase_2_page_1, Phase_2_Page_2, Phase_2_page_3, Phase_2_Page_4, Phase_2_Page_5,
                 Phase_2_Page_6,
                 Phase_2_Page_7, Phase_2_Page_8, Phase_2_Page_9, Phase_2_Page_10, Phase_2_Page_11]
