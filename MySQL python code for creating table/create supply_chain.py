import mysql.connector
c1=mysql.connector.connect(host="localhost", user="root", passwd="osjohn", database="mydb")
if c1.is_connected():
    print("Successfully Connected!")
cr=c1.cursor()
sql="create table SUPPLY_CHAIN(Part_ID char(3), Supplier_ID char(3), Ordered int, Delivered int, Total_Price int, primary key(Part_ID, Supplier_ID), foreign key (Part_ID) references part(Part_ID), foreign key (Supplier_ID) references supplier(Supplier_ID));"
cr.execute(sql)
cr.close()
c1.close()
