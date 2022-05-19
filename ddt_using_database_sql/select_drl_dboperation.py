# DRL: select

import mysql.connector

select_query = "select * from Student;"

#connecting to the database
try:
    con = mysql.connector.connect(host="localhost",port=3306,user="root",passwd="root",database="testdb")

    #cretae a cursor which is a temprory memory
    curs = con.cursor()

    #execute query through cursor
    curs.execute(select_query)

    #for retreiving data from curs
    for row in curs:
        print(row[0],row[1],row[2],row[3])

    #closing the connection
    con.close()

except:
    print("Connection Unsuccessful.")