import psycopg2

connection = psycopg2.connect(user='aipclfonwuiort',
                              password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                              host='ec2-3-216-113-109.compute-1.amazonaws.com',
                              port='5432',
                              database='dcoubsit8jsig0')

cursor = connection.cursor()

id_script2 = 'UPDATE novaland SET partei = %s WHERE nutzer_id = %s'
id_value = ["Liberale Partei Novaland", "pxn5meqx"]
cursor.execute(id_script2, id_value)
connection.commit()

id_script = 'SELECT Partei FROM Novaland'
cursor.execute(id_script)
Abstimmen = cursor.fetchall()

connection.commit()
cursor.close()
connection.close()
Hass = str(Abstimmen)
print(Hass)

Wort = Hass.count("Konservative Partei Novland")
print(Wort)

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)
