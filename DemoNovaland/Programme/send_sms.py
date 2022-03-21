import psycopg2
from twilio.rest import Client

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
    NutzerID = (str(str(ID).replace("(", "").replace(")", "").replace(",", "")).replace("[", "").replace("]", "").replace("'", '')).replace(" ", "")
    ScriptSMS = '''SELECT telefonnummer FROM Novaland WHERE nutzer_id = %s'''
    SMSID = [NutzerID]
    print(SMSID)
    cursor.execute(ScriptSMS, SMSID)
    SMS = cursor.fetchone()
    print(SMS)
    To_SMS = str(SMS).replace("(", "").replace(")", "").replace(",", "").replace("'", '')
    account_sid = 'ACbaa9b853b0eac4db6a4728dd0deb738f'
    auth_token = '886c2a41182d3f41aa6bbe17b850e553'
    client = Client(account_sid, auth_token)
    code = NutzerID
    Url = "https://pilotnovaland2022.herokuapp.com/join/" + code
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
                 to=To_SMS
        )
        message
        connection.commit()
        print("SMS Gesendet")

    except:
        print("SMS konnte nicht gesendet werden")

