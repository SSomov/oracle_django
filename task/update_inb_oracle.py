import csv
import re
import cx_Oracle


ip='localhost'
port = 1521
SID = 'xe'
usr = 'system'
pwd = 'oracle'
dsn_tns = cx_Oracle.makedsn(ip, port, service_name=SID)
connection = cx_Oracle.connect(usr, pwd, dsn_tns, encoding="UTF-8")
cursor = connection.cursor()
print("oracle database " + connection.version)
with open('fileupdate.csv', "r", encoding='utf-8') as csvbase:
    print(csvbase)
    spamreader = csv.reader(csvbase, delimiter=';')
    for lines in spamreader:
        print(lines)
        cursor.execute("UPDATE TEST_DJANGO SET UPDATE_STATUS = :1, UPDATE_USER = :2 WHERE MSG_ID = :3", (lines[1], lines[2], lines[0]))
#        print(cursor.execute("SELECT * FROM ALL_TABLES"))
        connection.commit()
cursor.close()
connection.close()
