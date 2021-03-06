import psycopg2

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

    connection3 = psycopg2.connect(user='aipclfonwuiort',
                                   password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                   host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                   port='5432',
                                   database='dcoubsit8jsig0')

    cursor3 = connection3.cursor()

    Geschlecht = '''SELECT Nutzer_ID FROM Novaland'''
    cursor3.execute(Geschlecht)
    ID = (
        str(str(cursor3.fetchall())))

    if "Test" in ID:
        print("Yeah")
    else:
        insert_script = 'INSERT INTO Novaland (Nutzer_ID) ' \
                        'VALUES(%s) '
        insert_value = ["Test"]

        cursor.execute(insert_script, insert_value)

    connection.commit()
except Exception as error:
    print(error)
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
