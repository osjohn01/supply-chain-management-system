import mysql.connector
c1=mysql.connector.connect(host="localhost", user="root", passwd="osjohn", database="mydb")
if c1.is_connected():
    print("Successfully Connected!")
cr=c1.cursor()
sql="create table SUPPLIER(Supplier_ID char(3) primary key, Supplier_Name varchar(20), Address varchar(15), EMail_ID varchar(10), Ph_NO int);"
cr.execute(sql)
cr.close()
c1.close()
