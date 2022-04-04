import smtplib
from datetime import *
import psycopg2
import time
import ssl
from email import *

connection4 = psycopg2.connect(user='aipclfonwuiort',
                               password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                               host='ec2-3-216-113-109.compute-1.amazonaws.com',
                               port='5432',
                               database='dcoubsit8jsig0')
cursor4 = connection4.cursor()
ChangeValue = '''UPDATE Novaland SET achtzehnuhrmail = %s, achtzehnuhrmailzeit = %s, achtzehnuhrmailunixtime = %s WHERE Nutzer_ID = %s'''
Values = ["Ja", str(datetime.now()), time.time(), "qga901f8"]
cursor4.execute(ChangeValue, Values)
connection4.commit()