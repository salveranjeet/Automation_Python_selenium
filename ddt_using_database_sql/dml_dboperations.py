# DML: insert, update, delete
import mysql.connector

insert_query = "insert into Student values(105,'Alia','Bhatt','Pune');"
update_query = "update Student set FirstName='Rohan' where sid=105;"
delete_query = "delete from Student where sid=105;"

#connecting to the database
try:
    con = mysql.connector.connect(host="localhost",port=3306,user="root",passwd="root",database="testdb")

    #cretae a cursor which is a temprory memory
    curs = con.cursor()

    #execute query through cursor
    curs.execute(delete_query)

    #commit transaction(for making changes in the database)
    con.commit()

    #closing the connection
    con.close()

except:
    print("Connection Unsuccessful.")







