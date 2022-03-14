import smtplib
from time import *
from datetime import *
from datetime import time
import psycopg2
import ssl
from email import *


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

        IDBekommen = 'SELECT nutzer_id FROM Novaland'
        cursor.execute(IDBekommen)
        ID = cursor.fetchall()
        for ID in ID:
            MailAdress = str(ID).replace("(", "").replace(")", "").replace(",", "")
            USERID = (str(MailAdress).replace("[", "").replace("]", "").replace("'", ''))
            print(USERID)
            ScriptMail = '''SELECT Mail FROM Novaland WHERE nutzer_id = %s'''
            MailID = [USERID]
            cursor.execute(ScriptMail, MailID)
            Mail = cursor.fetchone()
            To_Mail = str(Mail).replace("(", "").replace(")", "").replace(",", "").replace("'", '')
            print(str(Mail).replace("(", "").replace(")", "").replace(",", "").replace("'", ''))
            From_mail = "pilotnovaland@gmail.com"
            Passwort = "0?$W6XrieU!J+KO=,,zv"
            ssl_context = ssl.create_default_context()
            subject = 'Ihre Teilnahme an unserem politischen Verhaltensspiel "Novaland.'
            code = USERID
            Url = "https://pilotnovaland2022.herokuapp.com/demo"
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

            try:
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl_context)
                server.login(From_mail, Passwort)
                server.sendmail(msg['From'], msg['To'], msg.as_string())
                server.quit()
                cursor = connection.cursor()
                print("Email gesendet")
            except:
                print('Die Mail ist falsch')
                pass
    except Exception as error:
        print(error)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()

###################################################
#                       15 Uhr Mail:
###################################################

def vierzehnUhrMail():
    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(user='aipclfonwuiort',
                                       password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                       host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                       port='5432',
                                       database='dcoubsit8jsig0')
        cursor = connection.cursor()

        IDBekommen = 'SELECT nutzer_id FROM Novaland'
        cursor.execute(IDBekommen)
        ID = cursor.fetchall()
        for ID in ID:
            MailAdress = str(ID).replace("(", "").replace(")", "").replace(",", "")
            USERID = (str(MailAdress).replace("[", "").replace("]", "").replace("'", ''))
            print(USERID)
            ScriptMail = '''SELECT Mail FROM Novaland WHERE nutzer_id = %s'''
            MailID = [USERID]
            cursor.execute(ScriptMail, MailID)
            Mail = cursor.fetchone()
            To_Mail = str(Mail).replace("(", "").replace(")", "").replace(",", "").replace("'", '')
            print(str(Mail).replace("(", "").replace(")", "").replace(",", "").replace("'", ''))
            From_mail = "pilotnovaland@gmail.com"
            Passwort = "0?$W6XrieU!J+KO=,,zv"
            ssl_context = ssl.create_default_context()
            subject = 'Ihre Teilnahme an unserem politischen Verhaltensspiel "Novaland.'
            code = USERID
            Url = "https://pilotnovaland2022.herokuapp.com/demo"
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

            try:
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl_context)
                server.login(From_mail, Passwort)
                server.sendmail(msg['From'], msg['To'], msg.as_string())
                server.quit()
                cursor = connection.cursor()
                print("Email gesendet")
            except:
                print('Die Mail ist falsch')
                pass
    except Exception as error:
        print(error)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


###################################################
#                       16 Uhr Mail:
###################################################

def SechzehnUhrMail():
    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(user='aipclfonwuiort',
                                       password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                       host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                       port='5432',
                                       database='dcoubsit8jsig0')
        cursor = connection.cursor()

        IDBekommen = 'SELECT nutzer_id FROM Novaland'
        cursor.execute(IDBekommen)
        ID = cursor.fetchall()
        for ID in ID:
            MailAdress = str(ID).replace("(", "").replace(")", "").replace(",", "")
            USERID = (str(MailAdress).replace("[", "").replace("]", "").replace("'", ''))
            print(USERID)
            ScriptMail = '''SELECT Mail FROM Novaland WHERE nutzer_id = %s'''
            MailID = [USERID]
            cursor.execute(ScriptMail, MailID)
            Mail = cursor.fetchone()
            To_Mail = str(Mail).replace("(", "").replace(")", "").replace(",", "").replace("'", '')
            print(str(Mail).replace("(", "").replace(")", "").replace(",", "").replace("'", ''))
            From_mail = "pilotnovaland@gmail.com"
            Passwort = "0?$W6XrieU!J+KO=,,zv"
            ssl_context = ssl.create_default_context()
            subject = 'Ihre Teilnahme an unserem politischen Verhaltensspiel "Novaland.'
            code = USERID
            Url = "https://pilotnovaland2022.herokuapp.com/demo"
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

            try:
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl_context)
                server.login(From_mail, Passwort)
                server.sendmail(msg['From'], msg['To'], msg.as_string())
                server.quit()
                cursor = connection.cursor()
                print("Email gesendet")
            except:
                print('Die Mail ist falsch')
                pass
    except Exception as error:
        print(error)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


###################################################
#                       15 Uhr Mail:
###################################################

def achzehnUhrMail():
    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(user='aipclfonwuiort',
                                       password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                       host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                       port='5432',
                                       database='dcoubsit8jsig0')
        cursor = connection.cursor()

        IDBekommen = 'SELECT nutzer_id FROM Novaland'
        cursor.execute(IDBekommen)
        ID = cursor.fetchall()
        for ID in ID:
            MailAdress = str(ID).replace("(", "").replace(")", "").replace(",", "")
            USERID = (str(MailAdress).replace("[", "").replace("]", "").replace("'", ''))
            print(USERID)
            ScriptMail = '''SELECT Mail FROM Novaland WHERE nutzer_id = %s'''
            MailID = [USERID]
            cursor.execute(ScriptMail, MailID)
            Mail = cursor.fetchone()
            To_Mail = str(Mail).replace("(", "").replace(")", "").replace(",", "").replace("'", '')
            print(str(Mail).replace("(", "").replace(")", "").replace(",", "").replace("'", ''))
            From_mail = "pilotnovaland@gmail.com"
            Passwort = "0?$W6XrieU!J+KO=,,zv"
            ssl_context = ssl.create_default_context()
            subject = 'Ihre Teilnahme an unserem politischen Verhaltensspiel "Novaland.'
            code = USERID
            Url = "https://pilotnovaland2022.herokuapp.com/demo"
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

            try:
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl_context)
                server.login(From_mail, Passwort)
                server.sendmail(msg['From'], msg['To'], msg.as_string())
                server.quit()
                cursor = connection.cursor()
                print("Email gesendet")
            except:
                print('Die Mail ist falsch')
                pass
    except Exception as error:
        print(error)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()



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
ProgrammTagZeit = (datetime.now().time().hour * 60 * 60) + (datetime.now().time().minute * 60) + datetime.now().time().second
print(ProgrammTagZeit)

#Studie Uhrzeit
Datum_Studie = date(2022, 3, 14) ########## Diese Variabel muss geändert werden, um das Datum für die Studie anzupassen ########
zwoelfUhrZeit = time(12, 0, 0)
ZeitZwoelf = 12 * 60 * 60
print(ZeitZwoelf)
vierzehnUhrZeit = time(14, 0, 0)
ZeitVierzehnUhr = 14 * 60 * 60
print(ZeitVierzehnUhr)
SechZehnUhrZeit = time(16, 0, 0)
ZeitSechzehnUhr = 16 * 60 * 60
print(ZeitSechzehnUhr)
achtzehnUhrzeit = time(18, 0, 0)
ZeitAchtZehnUhr = 18 * 3600
print(ZeitAchtZehnUhr)

print(zwoelfUhrZeit)

differenzZwoelf = ZeitZwoelf - ProgrammTagZeit
differenzVierzehn = ZeitVierzehnUhr - ProgrammTagZeit
differentSechzehn = ZeitSechzehnUhr - ProgrammTagZeit
differenzAchtzehn = ZeitAchtZehnUhr - ProgrammTagZeit
print(differenzZwoelf)

Test = Datum_Studie - Datum_Programm
if str(Datum_Programm - Datum_Studie) == "0:00:00":
    if 3600 >= differenzZwoelf > 0:
        zwoelfUhrMail()
        print(differenzZwoelf)
    if 3600 >= differenzVierzehn > 0:
        vierzehnUhrMail()
        print(differenzVierzehn)
    if 3600 >= differentSechzehn > 0:
        SechzehnUhrMail()
        print(differentSechzehn)
    if 3600 >= differenzAchtzehn > 0:
        achzehnUhrMail()
        print(differenzAchtzehn)








# 14 Uhr mail

