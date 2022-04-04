from email import message
import psycopg2
import pyshorteners
import smtplib
import email
import ssl

PROVIDERS = {
    "AT&T": {"sms": "txt.att.net", "mms": "mms.att.net", "mms_support": True},
    "Boost Mobile": {
        "sms": "sms.myboostmobile.com",
        "mms": "myboostmobile.com",
        "mms_support": True,
    },
    "C-Spire": {"sms": "cspire1.com", "mms_support": False},
    "Cricket Wireless" : {
        "sms": "sms.cricketwireless.net ",
        "mms": "mms.cricketwireless.net",
        "mms_support": True,
    },
    "Consumer Cellular": {"sms": "mailmymobile.net", "mms_support": False},
    "Google Project Fi": {"sms": "msg.fi.google.com", "mms_support": True},
    "Metro PCS": {"sms": "mymetropcs.com", "mms_support": True},
    "Mint Mobile": {"sms": "mailmymobile.net", "mms_support": False},
    "Page Plus": {
        "sms": "vtext.com",
        "mms": "mypixmessages.com",
        "mms_support": True,
    },
    "Republic Wireless": {
        "sms": "text.republicwireless.com",
        "mms_support": False,
    },
    "Sprint": {
        "sms": "messaging.sprintpcs.com",
        "mms": "pm.sprint.com",
        "mms_support": True,
    },
    "Straight Talk": {
        "sms": "vtext.com",
        "mms": "mypixmessages.com",
        "mms_support": True,
    },
    "T-Mobile": {"sms": "tmomail.net", "mms_support": True},
    "Ting": {"sms": "message.ting.com", "mms_support": False},
    "Tracfone": {"sms": "", "mms": "mmst5.tracfone.com", "mms_support": True},
    "U.S. Cellular": {
        "sms": "email.uscc.net",
        "mms": "mms.uscc.net",
        "mms_support": True,
    },
    "Verizon": {"sms": "vtext.com", "mms": "vzwpix.com", "mms_support": True},
    "Virgin Mobile": {
        "sms": "vmobl.com",
        "mms": "vmpix.com",
        "mms_support": True,
    },
    "Xfinity Mobile": {
        "sms": "vtext.com",
        "mms": "mypixmessages.com",
        "mms_support": True,
    },
}
carriers = {
    'att': '@mms.att.net',
    'tmobile': ' @tmomail.net',
    'verizon': '@vtext.com',
    'sprint': '@page.nextel.com'
}

connection4 = psycopg2.connect(user='aipclfonwuiort',
                                   password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                   host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                   port='5432',
                                   database='dcoubsit8jsig0')
cursor4 = connection4.cursor()

IDBekommen = 'SELECT DISTINCT nutzer_id FROM Novaland'
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
    ssl_context = ssl.create_default_context()
    msg = message.Message()
    msg.set_charset("utf-8")
    msg['Content-type'] = 'text/plain; charset=utf-8'
    msg['Content-transfer-encoding'] = '8bit'
    msg['From'] = "novaland@uni-duisburg-essen.de"
    msg['To'] = To_SMS + "@vtext.com"
    print(msg['To'])
    code = NutzerID
    url = "https://pilotnovaland2022.herokuapp.com/room/DemoNovaland?participant_label=" + code
    try:
        type_tiny = pyshorteners.Shortener()
        shortend_url = type_tiny.tinyurl.short(url)
        URL = shortend_url
        print(URL)
        msg = "Sehr geehrte:r Teilnehmer:in an unserem politischen Verhaltensspiel 'Novaland', " \
              "\nDie Universität Duisburg bedankt sich bei Ihnen für ihre Teilnahme an der ersten Runde. " \
              "Damit die Teilnahme vollständig ist, würden wir Sie drum bitte, an der zweiten Runde teilzunehmen. \n" \
              "Um an der zweiten Runde teilnehmen zu können, müssen Sie auf diesen Link klicken: " + URL + " " \
                                                                                                           "\n\nDamit Sie sich einlogen können müssen Sie einfach diesen Code eingeben: " + code + \
              "\n\nWir bedanken uns bei ihnen recht herzlich!\n\n Universität Duisburg"
        server = smtplib.SMTP("mailout.uni-duisburg-essen.de", 465, context=ssl_context)
        server.starttls()
        server.login("hq0679", "0?$W6XrieU!J+KO=,,zv")
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        connection4.commit()
        print("SMS versendet an: " + NutzerID + " mit der URL: " +URL)
    except:
        print("Fehler beim versenden der SMS an: " + NutzerID)