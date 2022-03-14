import csv
import psycopg2
from datetime import *
from datetime import time
import pandas as pd
import pyodbc

connection = None
cursor = None

try:
    connection = psycopg2.connect(user='aipclfonwuiort',
                                  password='b124aca3006fd58f483bfb154045ce201c4578231285d94b782244a044986e49',
                                  host='ec2-3-216-113-109.compute-1.amazonaws.com',
                                  port='5432',
                                  database='dcoubsit8jsig0')
    cursor = connection.cursor()

    sql_query = pd.read_sql_query('''select * from Novaland''', connection)

    df = pd.DataFrame(sql_query)
    datum = str(datetime.now().strftime("-%d-%m-%Y--%H-%M-%S"))
    df.to_csv(r'H:\Novaland Stuff\CSV\Novaland' + datum + '.csv', index=False)
except Exception as error:
    print(error)
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
