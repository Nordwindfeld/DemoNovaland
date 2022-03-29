import psycopg2

connection4 = psycopg2.connect(user='aipclfonwuiort',
                                      password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                      host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                      port='5432',
                                      database='dcoubsit8jsig0')
cursor4 = connection4.cursor()

IDBekommen = 'SELECT DISTINCT nutzer_id FROM Novaland'
cursor4.execute(IDBekommen)
ID = cursor4.fetchall()
AlleSpenden = 0.0
for ID in ID:
    USERID = (str(str(ID).replace("(", "").replace(")", "").replace(",", "")).replace("[", "").replace("]", "").replace("'", ''))
    ScriptZahl = '''SELECT DISTINCT Spende From Novaland Where nutzer_id = %s'''
    Users = [USERID]
    cursor4.execute(ScriptZahl, Users)
    Spenden = cursor4.fetchone()
    SpendenZahl = float(str(str(Spenden).replace("(", "").replace(")", "").replace(",", "")).replace("[", "").replace("]", "").replace("'", ''))
    AlleSpenden = AlleSpenden + SpendenZahl
    print(SpendenZahl)

print(AlleSpenden)
cursor4.close()
connection4.close()