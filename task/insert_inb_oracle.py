import csv
import re
import cx_Oracle


ip='localhost'
port = 1521
SID = 'xe'
usr = 'system'
pwd = 'oracle'
dsn_tns = cx_Oracle.makedsn(ip, port, SID)
connection = cx_Oracle.connect(usr, pwd, dsn_tns)
cursor = connection.cursor()
print("oracle database " + connection.version)
with open('insert.csv', "r", encoding='utf-8') as csvbase:
    print(csvbase)
    spamreader = csv.reader(csvbase, delimiter=';')
    for lines in spamreader:
        print(lines)
#        cursor.execute("INSERT INTO TEST_DJANGO (ADAPTER,DATA_LOAD,SENDER,RECEIVER,INTERFACE_NAME,TYPE_ERROR,MSG_ID,ERROR_TEXT) VALUES (:1, :2, :3, :4, :5, :6, :7, :8)", 
#                (lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6], lines[7]))
#        cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES")
        connection.commit()
connection.close()
cursor.close()
