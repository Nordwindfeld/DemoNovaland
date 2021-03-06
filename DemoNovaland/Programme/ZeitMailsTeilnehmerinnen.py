import smtplib
from datetime import *
import time
import psycopg2
import ssl
from email import *


####################################################################################################
#                      Programm für das automatische verschicken von E-Mails:
#
# # Ich habe in dem Programm datetime Variabeln drin, die bestimmen ab wann, welche Mail abgeschickt
# # werden kann. Wenn der Code abgespielt wird, checkt er ganz unten, welche Funktion nun abgespielt
# # werden soll. Schickt, diese aber jedes mal ab, wenn der Code läuft, wenn man also möchte, dass
# # alle zwei Stunden Mail abgeschickt werden sollen, muss das manuell gemacht werden oder eine
# # get-Funktion auf dem Server schreiben, welche das Programm nur alle zwei Stunden checked
####################################################################################################

# Hier werden die Funktionen für die einzelne Uhrzeit geschrieben
#########################################################################

###################################################
#                       12 Uhr Mail:
###################################################

def zwoelfUhrMail():
    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(user='aipclfonwuiort',
                                      password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                      host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                      port='5432',
                                      database='dcoubsit8jsig0')
        cursor = connection.cursor()

        IDBekommen = 'SELECT DISTINCT nutzer_id FROM Novaland'
        cursor.execute(IDBekommen)
        ID = cursor.fetchall()
        for ID in ID:
            MailAdress = str(ID).replace("(", "").replace(")", "").replace(",", "")
            USERID = (str(MailAdress).replace("[", "").replace("]", "").replace("'", ''))
            print("Die User ID lautet: " + USERID)
            ScriptMail = '''SELECT DISTINCT Mail FROM Novaland WHERE nutzer_id = %s'''
            MailID = [USERID]
            cursor.execute(ScriptMail, MailID)
            Mail = cursor.fetchone()
            To_Mail = str(Mail).replace("(", "").replace(")", "").replace(",", "").replace("'", '')
            From_mail = "hq0679"
            Passwort = "0?$W6XrieU!J+KO=,,zv"
            ssl_context = ssl.create_default_context()
            subject = 'Ihre Teilnahme an unserem politischen Verhaltensspiel "Novaland.'
            code = USERID
            Url = "https://pilotnovaland2022.herokuapp.com/room/DemoNovaland?participant_label=" + code
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
            msg['From'] = "novaland@uni-duisburg-essen.de"
            msg['To'] = To_Mail
            msg.set_payload(Nachricht, charset="utf-8")

            try:
                server = smtplib.SMTP_SSL("mailout.uni-duisburg-essen.de", 465, context=ssl_context)
                server.login(From_mail, Passwort)
                server.sendmail(msg['From'], msg['To'], msg.as_string())
                server.quit()
                print("Die Mail an: " + code + " - " + To_Mail + " wurde versendet. \n")
                ChangeValue = '''UPDATE Novaland SET ZwoelfUhrMail = %s, ZwoelfUhrMailZeit = %s, ZwoelfUhrMailUnixTime = %s WHERE Nutzer_ID = %s'''
                Values = ["Ja", str(datetime.now()), time.time(), code]
                cursor.execute(ChangeValue, Values)
                connection.commit()
                print("Die Daten von " + code + " wurden in der Datenbank aktualisiert." + '\n' + '\n')
            except:
                server.quit()
                ChangeValue = '''UPDATE Novaland SET ZwoelfUhrMail = %s WHERE Nutzer_ID = %s'''
                Values = ["Nein", USERID]
                cursor.execute(ChangeValue, Values)
                connection.commit()
                print('PROBLEM!! - Es gab ein Problem mit: ' + To_Mail + '\n')
    except Exception as error:
        print(error)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


###################################################
#                       14 Uhr Mail:
###################################################

def vierzehnUhrMail():
    connection2 = None
    cursor2 = None

    try:
        connection2 = psycopg2.connect(user='aipclfonwuiort',
                                       password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                       host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                       port='5432',
                                       database='dcoubsit8jsig0')
        cursor2 = connection2.cursor()

        IDBekommen = 'SELECT DISTINCT nutzer_id FROM Novaland'
        cursor2.execute(IDBekommen)
        ID = cursor2.fetchall()
        for ID in ID:
            MailAdress = str(ID).replace("(", "").replace(")", "").replace(",", "")
            USERID = (str(MailAdress).replace("[", "").replace("]", "").replace("'", ''))
            print("Die User ID lautet: " + USERID)
            ScriptMail = '''SELECT DISTINCT Mail FROM Novaland WHERE nutzer_id = %s'''
            MailID = [USERID]
            cursor2.execute(ScriptMail, MailID)
            Mail = cursor2.fetchone()
            To_Mail = str(Mail).replace("(", "").replace(")", "").replace(",", "").replace("'", '')
            From_mail = "hq0679"
            Passwort = "0?$W6XrieU!J+KO=,,zv"
            ssl_context = ssl.create_default_context()
            subject = 'Ihre Teilnahme an unserem politischen Verhaltensspiel "Novaland.'
            code = USERID
            Url = "https://pilotnovaland2022.herokuapp.com/room/DemoNovaland?participant_label=" + code
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
            msg['From'] = "novaland@uni-duisburg-essen.de"
            msg['To'] = To_Mail
            msg.set_payload(Nachricht, charset="utf-8")

            try:
                server = smtplib.SMTP_SSL("mailout.uni-duisburg-essen.de", 465, context=ssl_context)
                server.login(From_mail, Passwort)
                server.sendmail(msg['From'], msg['To'], msg.as_string())
                server.quit()
                print("Die Mail an: " + code + " - " + To_Mail + " wurde versendet. \n")
                ChangeValue = '''UPDATE Novaland SET VierzehnUhrMail = %s, VierzehnUhrMailZeit = %s, VierzehnUhrMailUnixTime = %s  WHERE Nutzer_ID = %s'''
                Values = ["Ja", str(datetime.now()), time.time(), code]
                cursor2.execute(ChangeValue, Values)
                connection2.commit()
                print("Die Daten von " + code + " wurden in der Datenbank aktualisiert." + '\n' + '\n')
            except:
                print('PROBLEM!! - Es gab ein Problem mit: ' + To_Mail + '\n')
                server.quit()
                ChangeValue = '''UPDATE Novaland SET VierzehnUhrMail = %s WHERE Nutzer_ID = %s'''
                Values = ["Nein", USERID]
                cursor2.execute(ChangeValue, Values)
                connection2.commit()
                pass
    except Exception as error:
        print(error)
    finally:
        if cursor2 is not None:
            cursor2.close()
        if connection2 is not None:
            connection2.close()


###################################################
#                       16 Uhr Mail:
###################################################

def SechzehnUhrMail():
    connection3 = None
    cursor3 = None

    try:
        connection3 = psycopg2.connect(user='aipclfonwuiort',
                                       password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                       host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                       port='5432',
                                       database='dcoubsit8jsig0')
        cursor3 = connection3.cursor()

        IDBekommen = 'SELECT DISTINCT nutzer_id FROM Novaland'
        cursor3.execute(IDBekommen)
        ID = cursor3.fetchall()
        for ID in ID:
            MailAdress = str(ID).replace("(", "").replace(")", "").replace(",", "")
            USERID = (str(MailAdress).replace("[", "").replace("]", "").replace("'", ''))
            print("Die User ID lautet: " + USERID)
            ScriptMail = '''SELECT DISTINCT Mail FROM Novaland WHERE nutzer_id = %s'''
            MailID = [USERID]
            cursor3.execute(ScriptMail, MailID)
            Mail = cursor3.fetchone()
            To_Mail = str(Mail).replace("(", "").replace(")", "").replace(",", "").replace("'", '')
            From_mail = "hq0679"
            Passwort = "0?$W6XrieU!J+KO=,,zv"
            ssl_context = ssl.create_default_context()
            subject = 'Ihre Teilnahme an unserem politischen Verhaltensspiel "Novaland.'
            code = USERID
            Url = "https://pilotnovaland2022.herokuapp.com/room/DemoNovaland?participant_label=" + code
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
            msg['From'] = "novaland@uni-duisburg-essen.de"
            msg['To'] = To_Mail
            msg.set_payload(Nachricht, charset="utf-8")

            try:
                server = smtplib.SMTP_SSL("mailout.uni-duisburg-essen.de", 465, context=ssl_context)
                server.login(From_mail, Passwort)
                server.sendmail(msg['From'], msg['To'], msg.as_string())
                server.quit()
                print("Die Mail an: " + code + " - " + To_Mail + " wurde versendet. \n")
                ChangeValue = '''UPDATE Novaland SET SechzehnUhrMail = %s, SechzehnUhrMailZeit = %s, SechzehnUhrMailUnixTime = %s  WHERE Nutzer_ID = %s'''
                Values = ["Ja", str(datetime.now()), time.time(), code]
                cursor3.execute(ChangeValue, Values)
                connection3.commit()
                print("Die Daten von " + code + " wurden in der Datenbank aktualisiert." + '\n' + '\n')
            except:
                print('PROBLEM!! - Es gab ein Problem mit: ' + To_Mail + '\n')
                ChangeValue = '''UPDATE Novaland SET SechzehnUhrMail = %s WHERE Nutzer_ID = %s'''
                Values = ["Nein", USERID]
                cursor3.execute(ChangeValue, Values)
                connection3.commit()
                server.quit()
                pass
    except Exception as error:
        print(error)
    finally:
        if cursor3 is not None:
            cursor3.close()
        if connection3 is not None:
            connection3.close()


###################################################
#                       18 Uhr Mail:
###################################################

def achzehnUhrMail():
    connection4 = psycopg2.connect(user='aipclfonwuiort',
                                   password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                   host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                   port='5432',
                                   database='dcoubsit8jsig0')
    cursor4 = connection4.cursor()

    try:
        IDBekommen = '''SELECT DISTINCT nutzer_id FROM Novaland'''
        cursor4.execute(IDBekommen)
        ID = cursor4.fetchall()
        for ID in ID:
            MailAdress = str(ID).replace("(", "").replace(")", "").replace(",", "")
            USERID = (str(MailAdress).replace("[", "").replace("]", "").replace("'", ''))
            print("Die User ID lautet: " + USERID)
            ScriptMail = '''SELECT Mail FROM Novaland WHERE nutzer_id = %s'''
            MailID = [USERID]
            cursor4.execute(ScriptMail, MailID)
            Mail = cursor4.fetchone()
            To_Mail = str(Mail).replace("(", "").replace(")", "").replace(",", "").replace("'", '')
            From_mail = "hq0679"
            Passwort = "0?$W6XrieU!J+KO=,,zv"
            ssl_context = ssl.create_default_context()
            subject = 'Ihre Teilnahme an unserem politischen Verhaltensspiel "Novaland.'
            code = USERID
            Url = "https://pilotnovaland2022.herokuapp.com/room/DemoNovaland?participant_label=" + code
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
            msg['From'] = "novaland@uni-duisburg-essen.de"
            msg['To'] = To_Mail
            msg.set_payload(Nachricht, charset="utf-8")

            try:
                server = smtplib.SMTP_SSL("mailout.uni-duisburg-essen.de", 465, context=ssl_context)
                server.login(From_mail, Passwort)
                server.sendmail(msg['From'], msg['To'], msg.as_string())
                server.quit()
                print("Die Mail an: " + code + " - " + To_Mail + " wurde versendet. \n")
                connection4 = psycopg2.connect(user='aipclfonwuiort',
                                               password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                               host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                               port='5432',
                                               database='dcoubsit8jsig0')
                cursor4 = connection4.cursor()
                ChangeValue = '''UPDATE Novaland SET achtzehnuhrmail = %s, achtzehnuhrmailzeit = %s, achtzehnuhrmailunixtime = %s WHERE Nutzer_ID = %s'''
                Values = ["Ja", str(datetime.now()), time.time(), code]
                cursor4.execute(ChangeValue, Values)
                connection4.commit()
                print("Die Daten von " + code + " wurden in der Datenbank aktualisiert." + '\n' + '\n')

            except:
                print('PROBLEM!! - Es gab ein Problem mit: ' + code + " - " + To_Mail + '\n')
                ChangeValue = '''UPDATE Novaland SET AchtzehnUhrMail = %s WHERE Nutzer_ID = %s'''
                Values = ["Nein", code]
                cursor4.execute(ChangeValue, Values)
                connection4.commit()
                server.quit()
    except Exception as error:
        print(error)
    finally:
        if cursor4 is not None:
            cursor4.close()
        if connection4 is not None:
            connection4.close()


############################################----------------------------####################################
############################################----------------------------####################################
############################################----------------------------####################################

# ----------------------------------------
# Hier wird bestimmt, wann was ausgeführt wird
# ---------------------------------------
# Ersmal wird hier gechecked, ob das Datum des Programms mit dem Datum der Studie übereinstimmt
# Wenn das der Fall ist, wird danach gechecked, welche Uhrzeit es gerade ist und ob diese Uhrzeit in den von uns vorgegebenen Zeitraum reinpasst.
# Heißt es wird gechecked, ob das Programm sich eine Stunde vor um 12 befindet, bevor die nächste Mail verschickt wird

# Programm Uhrzeit
Datum_Programm = date.today()
Zeit_Programm = datetime.now().time()
ProgrammTagZeit = (datetime.now().time().hour * 60 * 60) + (
        datetime.now().time().minute * 60) + datetime.now().time().second

# Studie Uhrzeit
Datum_Studie = date(2022, 4,
                    4)  ########## Diese Variabel muss geändert werden, um das Datum für die Studie anzupassen ########
ZeitZwoelf = 12 * 60 * 60
ZeitVierzehnUhr = 14 * 60 * 60
ZeitSechzehnUhr = 20 * 60 * 60
ZeitAchtZehnUhr = 18 * 60 * 60

differenzZwoelf = ZeitZwoelf - ProgrammTagZeit
differenzVierzehn = ZeitVierzehnUhr - ProgrammTagZeit
differentSechzehn = ZeitSechzehnUhr - ProgrammTagZeit
differenzAchtzehn = ZeitAchtZehnUhr - ProgrammTagZeit

Test = Datum_Studie - Datum_Programm
if str(Datum_Programm - Datum_Studie) == "0:00:00":
    if 1800 >= differenzZwoelf > 0:
        zwoelfUhrMail()
        print(differenzZwoelf)
    if 1800 >= differenzVierzehn > 0:
        vierzehnUhrMail()
        print(differenzVierzehn)
    if 1800 >= differentSechzehn > 0:
        SechzehnUhrMail()
        print(differentSechzehn)
    if 1800 >= differenzAchtzehn > 0:
        achzehnUhrMail()
        print(differenzAchtzehn)
