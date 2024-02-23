import mysql.connector
c1=mysql.connector.connect(host="localhost", user="root", passwd="osjohn", database="mydb")
if c1.is_connected():
    print("Successfully Connected!")
cr=c1.cursor()
sql="create table Part(Part_ID char(3) primary key, Part_Name varchar(20), Units_in_Stock int);"
cr.execute(sql)
cr.close()
c1.close()
