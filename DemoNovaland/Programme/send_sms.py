import psycopg2
from twilio.rest import Client
from datetime import *
from datetime import time
import requests


def SMSZwoelfUhr():
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
        NutzerID = (
            str(str(ID).replace("(", "").replace(")", "").replace(",", "")).replace("[", "").replace("]", "").replace(
                "'", '')).replace(" ", "")
        ScriptSMS = '''SELECT telefonnummer FROM Novaland WHERE nutzer_id = %s'''
        SMSID = [NutzerID]
        cursor.execute(ScriptSMS, SMSID)
        SMS = cursor.fetchone()
        To_SMS = str(SMS).replace("(", "").replace(")", "").replace(",", "").replace("'", '')
        account_sid = 'ACbaa9b853b0eac4db6a4728dd0deb738f'
        auth_token = '886c2a41182d3f41aa6bbe17b850e553'
        client = Client(account_sid, auth_token)
        code = NutzerID
        Url = "https://DemoNovaland.herokuapp.com/InitializeParticipant/" + code
        msg = "Sehr geehrte:r Teilnehmer:in an unserem politischen Verhaltensspiel 'Novaland', " \
              "\nDie Universität Duisburg bedankt sich bei Ihnen für ihre Teilnahme an der ersten Runde. " \
              "Damit die Teilnahme vollständig ist, würden wir Sie drum bitte, an der zweiten Runde teilzunehmen. \n" \
              "Um an der zweiten Runde teilnehmen zu können, müssen Sie auf diesen Link klicken: " + Url + " " \
                                                                                                           "\n\nDamit Sie sich einlogen können müssen Sie einfach diesen Code eingeben: " + code + \
              "\n\nWir bedanken uns bei ihnen recht herzlich!\n\n Universität Duisburg"
        try:
            message = client.messages.create(
                body=msg,
                from_='+17622487388',
                to=To_SMS)
            message
            connection.commit()
            print("SMS an " + SMSID + " mit der Nummer: " + SMS + " wurde gesendet")

        except:
            print("PROBLEM!! SMS an " + SMSID + " mit der Nummer: " + SMS + " konnte nicht gesendet werden")


def SMSVierZehnUhr():
    connection2 = psycopg2.connect(user='aipclfonwuiort',
                                   password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                   host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                   port='5432',
                                   database='dcoubsit8jsig0')
    cursor2 = connection2.cursor()

    IDBekommen = 'SELECT nutzer_id FROM Novaland'
    cursor2.execute(IDBekommen)
    ID = cursor2.fetchall()
    for ID in ID:
        NutzerID = (
            str(str(ID).replace("(", "").replace(")", "").replace(",", "")).replace("[", "").replace("]", "").replace(
                "'", '')).replace(" ", "")
        ScriptSMS = '''SELECT telefonnummer FROM Novaland WHERE nutzer_id = %s'''
        SMSID = [NutzerID]
        cursor2.execute(ScriptSMS, SMSID)
        SMS = cursor2.fetchone()
        To_SMS = str(SMS).replace("(", "").replace(")", "").replace(",", "").replace("'", '')
        account_sid = 'ACbaa9b853b0eac4db6a4728dd0deb738f'
        auth_token = '886c2a41182d3f41aa6bbe17b850e553'
        client = Client(account_sid, auth_token)
        code = NutzerID
        Url = "https://DemoNovaland.herokuapp.com/InitializeParticipant/" + code
        msg = "Sehr geehrte:r Teilnehmer:in an unserem politischen Verhaltensspiel 'Novaland', " \
              "\nDie Universität Duisburg bedankt sich bei Ihnen für ihre Teilnahme an der ersten Runde. " \
              "Damit die Teilnahme vollständig ist, würden wir Sie drum bitte, an der zweiten Runde teilzunehmen. \n" \
              "Um an der zweiten Runde teilnehmen zu können, müssen Sie auf diesen Link klicken: " + Url + " " \
                                                                                                           "\n\nDamit Sie sich einlogen können müssen Sie einfach diesen Code eingeben: " + code + \
              "\n\nWir bedanken uns bei ihnen recht herzlich!\n\n Universität Duisburg"
        try:
            message = client.messages.create(
                body=msg,
                from_='+17622487388',
                to=To_SMS)
            message
            connection2.commit()
            print("SMS an " + SMSID + " mit der Nummer: " + SMS + " wurde gesendet")
        except:
            print("PROBLEM!! SMS an " + SMSID + " mit der Nummer: " + SMS + " konnte nicht gesendet werden")


def SMSSechZehnUhr():
    connection3 = psycopg2.connect(user='aipclfonwuiort',
                                   password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                   host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                   port='5432',
                                   database='dcoubsit8jsig0')
    cursor3 = connection3.cursor()

    IDBekommen = 'SELECT nutzer_id FROM Novaland'
    cursor3.execute(IDBekommen)
    ID = cursor3.fetchall()
    for ID in ID:
        NutzerID = (
            str(str(ID).replace("(", "").replace(")", "").replace(",", "")).replace("[", "").replace("]", "").replace(
                "'", '')).replace(" ", "")
        ScriptSMS = '''SELECT telefonnummer FROM Novaland WHERE nutzer_id = %s'''
        SMSID = [NutzerID]
        cursor3.execute(ScriptSMS, SMSID)
        SMS = cursor3.fetchone()
        To_SMS = str(SMS).replace("(", "").replace(")", "").replace(",", "").replace("'", '')
        account_sid = 'ACbaa9b853b0eac4db6a4728dd0deb738f'
        auth_token = '886c2a41182d3f41aa6bbe17b850e553'
        client = Client(account_sid, auth_token)
        code = NutzerID
        Url = "https://DemoNovaland.herokuapp.com/InitializeParticipant/" + code
        msg = "Sehr geehrte:r Teilnehmer:in an unserem politischen Verhaltensspiel 'Novaland', " \
              "\nDie Universität Duisburg bedankt sich bei Ihnen für ihre Teilnahme an der ersten Runde. " \
              "Damit die Teilnahme vollständig ist, würden wir Sie drum bitte, an der zweiten Runde teilzunehmen. \n" \
              "Um an der zweiten Runde teilnehmen zu können, müssen Sie auf diesen Link klicken: " + Url + " " \
                                                                                                           "\n\nDamit Sie sich einlogen können müssen Sie einfach diesen Code eingeben: " + code + \
              "\n\nWir bedanken uns bei ihnen recht herzlich!\n\n Universität Duisburg"
        try:
            message = client.messages.create(
                body=msg,
                from_='+17622487388',
                to=To_SMS)
            message
            connection3.commit()
            print("SMS an " + SMSID + " mit der Nummer: " + SMS + " wurde gesendet")
        except:
            print("PROBLEM!! SMS an " + SMSID + " mit der Nummer: " + SMS + " konnte nicht gesendet werden")


def SMSAchtZehnUhr():
    connection4 = psycopg2.connect(user='aipclfonwuiort',
                                   password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                   host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                   port='5432',
                                   database='dcoubsit8jsig0')
    cursor4 = connection4.cursor()

    IDBekommen = 'SELECT nutzer_id FROM Novaland'
    cursor4.execute(IDBekommen)
    ID = cursor4.fetchall()
    for ID in ID:
        NutzerID = (
            str(str(ID).replace("(", "").replace(")", "").replace(",", "")).replace("[", "").replace("]", "").replace(
                "'", '')).replace(" ", "")
        ScriptSMS = '''SELECT telefonnummer FROM Novaland WHERE nutzer_id = %s'''
        SMSID = [NutzerID]
        cursor4.execute(ScriptSMS, SMSID)
        SMS = cursor4.fetchone()
        To_SMS = str(SMS).replace("(", "").replace(")", "").replace(",", "").replace("'", '')
        account_sid = 'ACbaa9b853b0eac4db6a4728dd0deb738f'
        auth_token = '97ec70c4436040e9a14a0316e27bcf78'
        client = Client(account_sid, auth_token)
        code = NutzerID
        api_key = "1aca2f603ca8b4d9d78c01412837f3fe7e582"
        url = "https://DemoNovaland.herokuapp.com/InitializeParticipant/" + code
        api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
        data = requests.get(api_url).json()["url"]
        if data["status"] == 7:
            shortened_url = data["shortLink"]
            URL = str(shortened_url).replace("(", "").replace(")", "").replace(",", "").replace("[", "").replace("]", "").replace("'", '').replace(" ", "")
        else:
            print("[!] Error Shortening URL:", data)
        msg = "Sehr geehrte:r Teilnehmer:in an unserem politischen Verhaltensspiel 'Novaland', " \
              "\nDie Universität Duisburg bedankt sich bei Ihnen für ihre Teilnahme an der ersten Runde. " \
              "Damit die Teilnahme vollständig ist, würden wir Sie drum bitte, an der zweiten Runde teilzunehmen. \n" \
              "Um an der zweiten Runde teilnehmen zu können, müssen Sie auf diesen Link klicken: " + URL + " " \
                                                                                                                     "\n\nDamit Sie sich einlogen können müssen Sie einfach diesen Code eingeben: " + code + \
              "\n\nWir bedanken uns bei ihnen recht herzlich!\n\n Universität Duisburg"
        try:
            message = client.messages.create(
                body=msg,
                from_='+17622487388',
                to=To_SMS)
            message
            connection4.commit()
            print("SMS an " + SMSID + " mit der Nummer: " + SMS + " wurde gesendet")
        except:
            print("PROBLEM!! SMS an " + SMSID + " mit der Nummer: " + SMS + " konnte nicht gesendet werden")


Datum_Programm = date.today()
Zeit_Programm = datetime.now().time()
ProgrammTagZeit = (datetime.now().time().hour * 60 * 60) + (
        datetime.now().time().minute * 60) + datetime.now().time().second

Datum_Studie = date(2022, 4, 2)  ########## Diese Variabel muss geändert werden, um das Datum für die Studie anzupassen ########
zwoelfUhrZeit = time(12, 0, 0)
ZeitZwoelf = 12 * 60 * 60
vierzehnUhrZeit = time(14, 0, 0)
ZeitVierzehnUhr = 14 * 60 * 60
SechZehnUhrZeit = time(16, 0, 0)
ZeitSechzehnUhr = 16 * 60 * 60
achtzehnUhrzeit = time(18, 0, 0)
ZeitAchtZehnUhr = 12 * 3600

differenzZwoelf = ZeitZwoelf - ProgrammTagZeit
differenzVierzehn = ZeitVierzehnUhr - ProgrammTagZeit
differentSechzehn = ZeitSechzehnUhr - ProgrammTagZeit
differenzAchtzehn = ZeitAchtZehnUhr - ProgrammTagZeit

if str(Datum_Programm - Datum_Studie) == "0:00:00":
    if 3600 >= differenzZwoelf > 0:
        print("12 Uhr SMS wird versendet:")
        SMSZwoelfUhr()
    if 3600 >= differenzVierzehn > 0:
        print("14 Uhr SMS wird versendet:")
        SMSVierZehnUhr()
    if 3600 >= differentSechzehn > 0:
        print("16 Uhr SMS wird versendet:")
        SMSSechZehnUhr()
    if 3600 >= differenzAchtzehn > 0:
        print("18 Uhr SMS wird versendet:")
        SMSAchtZehnUhr()
