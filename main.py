import socket, sys, mysql.connector as mc
from datetime import datetime, date
import time
from tkinter import * 
from tkinter.ttk import *
user=None
print()
print(5*"\t"," WELCOME TO CHARLES BABBAGE & SONS™ SUPPLY CHAIN MANAGEMENT PORTAL®")
print()
def mastermenu():
    global user
    global ms
    global passwd
    ch=int(input("1) Login\n2) Close the Program\n\nYOUR CHOICE? --> "))
    ms=None
    if ch==1:
        for a in range(5,0,-1):
            print()
            username=input("ENTER THE USERNAME ")
            passwd=input("ENTER THE PASSWORD ")
            if username=='nandu' and passwd=='02032003':
                user='user1'
                print()
                ms=time.time()
                print("LOGIN SUCCESSFULL!")
                print(145*'-')
                logindetails()
                break
            elif username=='chachu' and passwd=='01102003':
                user='user2'
                print()
                ms=time.time()
                print("LOGIN SUCCESSFULL!")
                print(145*'-')
                logindetails()
                break
            else:
                if a-1!=0:
                    print()
                    print("INVALID CREDENTIALS! PLEASE TRY AGAIN ("+str(a-1)+" MORE CHANCE(S) LEFT)")
                    print()
                    print(100*'-')
            if a==1:
                print()
                print("5 INVALID ATTEMPTS. PROGRAM TERMINATED")
    elif ch==2:
        print()
        che=input("DO YOU REALLY WANT TO EXIT? JUST CONFIRM AE!\n(Y/N) ")
        if che in 'yY':
            print()
            print("THANK YOU & SEE YA NEXT TIME!")
            print(2*"\n",7*"\t", 2*' ',"© CHARLES BABBAGE & SONS™")
            sys.exit()
        else:
            mastermenu()
    else:
        print("INVALID INPUT! TRY AGAIN")
        mastermenu()
def insertpart():
    print()
    c=mc.connect(host="localhost", user="root", passwd="osjohn", database="mydb")
    if c.is_connected():
        print("Successfully Connected!")
    cr=c.cursor()
    partid=input("Enter the partid ")
    if 'Z' in partid:
        partname=input("Enter the partname ")
        sql="insert into Part values('{}','{}',0);".format(partid,partname)
        print()
    else:
        print("INVLAID PART_ID STRUCTURE")
        print("OPERATION ABORTED")
        return
    try:
        cr.execute(sql)
        c.commit()
        print("RECORD INSERTION SUCCESSFUL!")
    except:
        c.rollback()
        print("RECORD INSERTION UNSUCCESSFUL!")
    cr.close()
    c.close()
def insertsupplier():
    print()
    c=mc.connect(host="localhost", user="root", passwd="osjohn", database="mydb")
    if c.is_connected():
        print("Successfully Connected!")
    cr=c.cursor()
    supplierid=input("Enter the supplier id")
    if 'G' in supplierid:
        suppliername=input("Enter the suppliername")
        adrs=input("Enter the address")
        email=input("Enter the emailid")
        phno=int(input("Enter the phone number"))
        sql="insert into supplier values('{}','{}','{}','{}',{});".format(supplierid,suppliername,adrs,email,phno)
        print()
    else:
        print("INVLAID SUPPLIER_ID STRUCTURE")
        print("OPERATION ABORTED")
        return
    try:
        cr.execute(sql)
        c.commit()
        print("RECORD INSERTION SUCCESSFUL!")
    except:
        c.rollback()
        print("RECORD INSERTION UNSUCCESSFUL!")
    cr.close()
    c.close()       
def insertsupplychain():
    print()
    c=mc.connect(host="localhost", user="root", passwd="osjohn", database="mydb")
    if c.is_connected():
        print("Successfully Connected!")
    cr=c.cursor()
    partid=input("Enter the partid")
    supplierid=input("Enter the supplierid")
    
    sqltemp1="select * from part;"
    crtemp1=c.cursor()
    crtemp1.execute(sqltemp1)
    d1=crtemp1.fetchall()
    
    sqltemp2="select * from supplier;"
    crtemp2=c.cursor()
    crtemp2.execute(sqltemp2)
    d2=crtemp2.fetchall()
    
    for a1 in d1:
        if a1[0]==partid:
            flag1=True
            break
        else:
            flag1=False
    for a2 in d2:
        if a2[0]==supplierid:
            flag2=True
            break
        else:
            flag2=False
    if flag1==False:
        print()
        print("PART_ID NOT EXISTING. PLEASE RECORD IT IN MASTER TABLE")
        chtemp=input("DO YOU WANT TO RECORD IT? (Y/N) ")
        if chtemp in 'yY':
            if user=='user1':
                insertpart()
            elif user=='user2':
                print()
                username=input("ENTER VALID USERNAME WITH PRIVILEGES OVER MASTER TABLES ")
                passwd=input("ENTER THE PASSWORD ")
                if username=='nandu' and passwd=='02032003':
                    print("LOGIN SUCCESSFUL")
                    insertpart()
                    return
                else:
                    print("INVALID CREDENTIALS! OPERATION TERMINATED")
                    return
        else:
            print("PLEASE DO A DIFFERENT OPERATION")
            return
    if flag2==False:
        print()
        print("SUPPLIER_ID NOT EXISTING. PLEASE RECORD IT IN MASTER TABLE")
        chtemp=input("DO YOU WANT TO RECORD IT? (Y/N) ")
        if chtemp in 'yY':
            if user=='user1':
                insertsupplier()
            elif user=='user2':
                print()
                username=input("ENTER VALID USERNAME WITH PRIVILEGES OVER MASTER TABLES ")
                passwd=input("ENTER THE PASSWORD ")
                if username=='nandu' and passwd=='02032003':
                    print("LOGIN SUCCESSFUL")
                    insertsupplier()
                    return
                else:
                    print("INVALID CREDENTIALS! OPERATION TERMINATED")
                    return
        else:
            print("PLEASE DO A DIFFERENT OPERATION")
            return
    order=int(input("Enter the order"))
    totprice=int(input("Enter the total price"))
    sql="insert into supply_chain values('{}','{}',{},0,{});".format(partid,supplierid,order,totprice)
    print()
    try:
        cr.execute(sql)
        c.commit()
        print("RECORD INSERTION SUCCESSFUL!")
    except:
        c.rollback()
        print("RECORD INSERTION UNSUCCESSFUL!")
    cr.close()
    c.close()
def updatepart():
    print()
    c=mc.connect(host="localhost", user="root", passwd="osjohn", database="mydb")
    if c.is_connected():
        print("Successfully Connected!")
    partname=input("Enter the partname to be modified ")
    partid=input("Enter the partid to be modified ")
    sql="update part set part_name='{}' where part_id='{}';".format(partname,partid)
    print()
    try:
        sqltemp="select * from part;"
        crtemp=c.cursor()
        crtemp.execute(sqltemp)
        d=crtemp.fetchall()
        for a in d:
            flag=False
            if a[0]==partid:
                flag=True
                break
        if flag==True:
            cr=c.cursor()
            cr.execute(sql)
            c.commit()
            print("RECORD UPDATE SUCCESSFUL!")
        else:
            print("PART_ID NOT FOUND")
    except:
        c.rollback()
        print("RECORD UPDATE UNSUCCESSFUL!")
    cr.close()
    c.close()
def updatesupplier():
    print()
    c=mc.connect(host="localhost", user="root", passwd="osjohn", database="mydb")
    if c.is_connected():
        print("Successfully Connected!")
    supplierid=input("ENTER THE SUPPLIER_ID TO BE MODIFIED ")
    print("ENTER YOUR CHOICE")
    chupdate=int(input("1) SUPPLIER NAME\n2) ADDRESS\n3) EMAIL_ID\n4) PHONE_NUMBER"))
    if chupdate==1:
        sname=input("Enter the supplier name to be modified")
        sql="update supplier set supplier_name='{}' where supplier_id='{}';".format(sname,supplierid)
    elif chupdate==2:
        address=input("Enter the address to be modified")
        sql="update supplier set address='{}' where supplier_id='{}';".format(address,supplierid)
    elif chupdate==3:
        emailid=input("Enter the emailid to be modified")
        sql="update supplier set email_id ='{}' where supplier_id='{}';".format(emailid,supplierid)
    elif chupdate==4:
        phno=int(input("Enter the phone number to be modified"))
        sql="update supplier set ph_no='{}' where supplier_id='{}';".format(phno,supplierid)
    else:
        print("invalid selection")   
    cr=c.cursor()
    print()
    try:
        sqltemp="select * from supplier;"
        crtemp=c.cursor()
        crtemp.execute(sqltemp)
        d=crtemp.fetchall()
        for a in d:
            flag=False
            if a[0]==supplierid:
                flag=True
                break
        if flag==True:
            cr.execute(sql)
            c.commit()
            print("RECORD UPDATE SUCCESSFUL!")
        else:
            print("SUPPLIER_ID NOT FOUND")
    except:
        c.rollback()
        print("RECORD UPDATION UNSUCCESSFUL")
    cr.close()
    c.close()
def updatesupplychain():
    print()
    c=mc.connect(host="localhost", user="root", passwd="osjohn", database="mydb")
    if c.is_connected():
        print("Successfully Connected!")
    partid=input("ENTER THE PART_ID TO BE MODIFIED ")
    supplierid=input("ENTER THE SUPPLIER_ID TO BE MODIFIED ")
    sqltemp="select * from supply_chain;"
    crtemp=c.cursor()
    crtemp.execute(sqltemp)
    d=crtemp.fetchall()
    for a in d:
        flag1=flag2=False
        if a[0]==partid:
            flag1=True
        if a[1]==supplierid:
            flag2=True
        if flag1==flag2==True:
            break
    if flag1==False:
        print()
        print("PART_ID NOT EXISTING. PLEASE RECORD IT IN MASTER TABLE TO CONTINUE")
        chtemp=input("DO YOU WANT TO RECORD IT? (Y/N) ")
        if chtemp in 'yY':
            if user=='user1':
                insertpart()
            elif user=='user2':
                print()
                username=input("ENTER VALID USERNAME WITH PRIVILEGES OVER MASTER TABLES ")
                passwd=input("ENTER THE PASSWORD ")
                if username=='nandu' and passwd=='02032003':
                    print("LOGIN SUCCESSFUL")
                    insertpart()
                    return
                else:
                    print("INVALID CREDENTIALS! OPERATION TERMINATED")
                    return
        else:
            print("PLEASE DO A DIFFERENT OPERATION")
            return
    if flag2==False:
        print()
        print("SUPPLIER_ID NOT EXISTING. PLEASE RECORD IT IN MASTER TABLE TO CONTINUE")
        chtemp=input("DO YOU WANT TO RECORD IT? (Y/N) ")
        if chtemp in 'yY':
            if user=='user1':
                insertsupplier()
            elif user=='user2':
                print()
                username=input("ENTER VALID USERNAME WITH PRIVILEGES OVER MASTER TABLES ")
                passwd=input("ENTER THE PASSWORD ")
                if username=='nandu' and passwd=='02032003':
                    print("LOGIN SUCCESSFUL")
                    insertsupplier()
                    return
                else:
                    print("INVALID CREDENTIALS! OPERATION TERMINATED")
                    return
        else:
            print("PLEASE DO A DIFFERENT OPERATION")
            return       
    print("ENTER YOUR CHOICE")
    chupdate=int(input("1) ORDERED\n2) DELIVERED\n3) TOTAL PRICE"))
    if chupdate==1: 
        ordered=int(input("Enter the total ordered quantity "))
        sql="update supply_chain set ordered={} where part_id='{}' and supplier_id='{}';".format(ordered,partid,supplierid)
    if chupdate==2:
        chdel=input("DO YOU WANT TO ADD/SUBTRACT DELIVERED QUANTITIES? ENTER YOU CHOICE (+/-) ")
        if chdel=='+':
            delivered=int(input("Enter the delivered quantity to be added "))
            sql="update supply_chain set delivered=delivered+{} where part_id='{}' and supplier_id='{}';".format(delivered,partid,supplierid)
            sqlu="update part set units_in_stock=units_in_stock+{} where part_id='{}';".format(delivered, partid)
        elif chdel=='-':
            delivered=int(input("Enter the delivered quantity to be reduced "))
            sql="update supply_chain set delivered=delivered-{} where part_id='{}' and supplier_id='{}';".format(delivered,partid,supplierid)
            sqlu="update part set units_in_stock=units_in_stock-{} where part_id='{}';".format(delivered, partid)
        else:
            print("INVALID INPUT. OPERATION TERMINATED")
            return
        cru=c.cursor()
        cru.execute(sqlu)
        print("SUCCESSFULLY UPDATED IN MASTER (PARTS) TABLE!")
        cru.close()
    if chupdate==3:
        totprice=int(input("Enter the total price "))
        sql="update supply_chain set total_price={} where part_id='{}' and supplier_id='{}';".format(totprice,partid,supplierid)
    cr=c.cursor()
    print()
    try:
        cr.execute(sql)
        c.commit()
        print("SUCCESSFULLY UPDATED!")
    except:
        print("OPERATION UNSUCCESSFULL")
        c.rollback()
    cr.close()
    c.close()
def delete():
    print()
    c=mc.connect(host="localhost",user="root",passwd='osjohn',database='mydb')
    if c.is_connected():
        print("Successfully Connected!")
    cr=c.cursor()
    partid=input('ENTER THE PARTID TO BE DELETED ')
    supplier_id=input('ENTER THE SUPPLIERID TO BE DELETED ')
    sql="delete from supply_chain where part_id='{}' and supplier_id='{}';".format(partid,supplier_id)
    print()
    try:
        sqltemp="select * from supply_chain;"
        crtemp=c.cursor()
        crtemp.execute(sqltemp)
        d=crtemp.fetchall()
        for a in d:
            flag1=flag2=False
            if a[0]==partid:
                flag1=True
            if a[1]==supplier_id:
                flag2=True
            if flag1==flag2==True:
                break
        if flag1==flag2==True:
            cr.execute(sql)
            print("RECORD SUCCESSFULY DELETED!")
        else:
            print("RECORD NOT EXISTING")
        c.commit()
    except:
        c.rollback()
        print("ERROR!! PLS TRY AGAIN")
    cr.close()
    c.close()       
def update1():
    ans='y'
    while ans in 'yY':
        print("ENTER YOUR CHOICE")
        chinsert1=int(input("1) TABLE PART\n2) TABLE SUPPLIER\n3) TABLE SUPPLY_CHAIN\n"))
        if chinsert1==1:
            updatepart()
        elif chinsert1==2:
            updatesupplier()
        elif chinsert1==3:
            updatesupplychain()
        else:
            print("INVALID SELECTION!")
        ans=input("DO YOU WANNA CONTINUE UPDATING? (Y/N) ")
def update2():
    ans='y'
    while ans in 'yY':
        updatesupplychain()
        ans=input("DO YOU WANNA CONTINUE UPDATING? (Y/N) ")
def insert1():
    ans='y'
    while ans in 'yY':
        print("ENTER YOUR CHOICE")
        chinsert1=int(input("1) TABLE PART\n2) TABLE SUPPLIER\n3) TABLE SUPPLY_CHAIN\n"))
        if chinsert1==1:
            insertpart()
        elif chinsert1==2:
            insertsupplier()
        elif chinsert1==3:
            insertsupplychain()
        else:
            print("INVALID SELECTION!")
        ans=input("DO YOU WANNA CONTINUE INSERTING? (Y/N) ")
def insert2():
    ans='y'
    while ans in 'yY':
        insertsupplychain()
        ans=input("DO YOU WANNA CONTINUE INSERTING? (Y/N) ")
def displaypart():
    print()
    c=mc.connect(host="localhost", user="root", passwd="osjohn", database="mydb")
    if c.is_connected():
        print("Successfully Connected!")     
    cr=c.cursor()
    sql="select * from part;"
    start=time.time()
    print("PARTID\t\tNAME\t\tSTOCK")
    cr.execute(sql)
    d=cr.fetchall()
    for r in d:
        r=list(r)
        q=''
        for a in r:
            a=str(a)
            q+=a+'\t\t'
        print(q)
    end=time.time()
    print()
    print("NUMBER OF ROWS DISPLAYED ",cr.rowcount)
    print("TIME TAKEN ",end-start,"s")
    cr.close()
    c.close()    
def displaysupplier():
    print()
    c=mc.connect(host="localhost", user="root", passwd="osjohn", database="mydb")
    if c.is_connected():
        print("Successfully Connected!")    
    cr=c.cursor()
    sql="select * from supplier;"
    start=time.time()
    print("ID\t\t\tNAME\t\t\tAddress\t\t\tEmailid\t\t\t\t\tPh_no")
    cr.execute(sql)
    d=cr.fetchall()
    for r in d:
        r=list(r)
        q=''
        for a in r:
            a=str(a)
            q+=a+'\t\t\t'
        print(q)
    end=time.time()
    print()
    print("NUMBER OF ROWS DISPLAYED ",cr.rowcount)
    print("TIME TAKEN ",end-start,"s")
    cr.close()
    c.close()
def displaysupplychain():
    print()
    c=mc.connect(host="localhost", user="root", passwd="osjohn", database="mydb")
    if c.is_connected():
        print("Successfully Connected!")    
    cr=c.cursor()
    sql="select * from supply_chain;"
    start=time.time()
    print("PARTId\t\t\tsupplierid\t\torder\t\t\t\tdeliver\t\t\ttotprice")
    cr.execute(sql)
    d=cr.fetchall()
    for r in d:
        r=list(r)
        q=''
        for a in r:
            a=str(a)
            q+=a+'\t\t\t'
        print(q)
    end=time.time()
    print()
    print("NUMBER OF ROWS DISPLAYED ",cr.rowcount)
    print("TIME TAKEN ",end-start,"s")
    cr.close()
    c.close()
def displayrecordscondition():
    print()
    c=mc.connect(host="localhost", user="root", passwd="osjohn", database="mydb")
    if c.is_connected():
        print("Successfully Connected!")
    print("ENTER YOUR CHOICE")
    print("OPERATION VALID ONLY IN SUPPLY_CHAIN TABLE!")
    chdiscond=int(input("1) RECORD BY SUPPLIER_ID INPUT\n2) RECORD BY PART_ID INPUT\n3) PARTICULAR RECORD IN SUPPLY_CHAIN TABLE\n"))
    if chdiscond==1:
        supplierid=input("Enter the supplier id ")
        sqltemp="select * from supply_chain;"
        crtemp=c.cursor()
        crtemp.execute(sqltemp)
        d=crtemp.fetchall()
        flag1=True
        for a in d:
            flag2=False
            if a[1]==supplierid:
                flag2=True
                break
        sql="select * from supply_chain where supplier_id='{}';".format(supplierid)   
    elif chdiscond==2:
        partid=input("Enter the partid ")
        sqltemp="select * from supply_chain;"
        crtemp=c.cursor()
        crtemp.execute(sqltemp)
        d=crtemp.fetchall()
        flag2=True
        for a in d:
            flag1=False
            if a[0]==partid:
                flag1=True
                break
        sql="select * from supply_chain where part_id='{}';".format(partid)
    elif chdiscond==3:
        partid=input("ENTER PARTID ")
        supplierid=input("ENTER SUPPLIERID ")
        sqltemp="select * from supply_chain;"
        crtemp=c.cursor()
        crtemp.execute(sqltemp)
        d=crtemp.fetchall()
        for a in d:
            flag1=flag2=False
            if a[0]==partid:
                flag1=True
            if a[1]==supplierid:
                flag2=True
            if flag1==flag2==True:
                break
        sql="select * from supply_chain where part_id='{}' and supplier_id='{}';".format(partid, supplierid)
    cr=c.cursor()
    try:
        if flag1==flag2==True:
            cr.execute(sql)
            d=cr.fetchall()
            start=time.time()
            print("PARTId\t\t\tsupplierid\t\torder\t\t\t\tdeliver\t\t\ttotprice")
            for r in d:
                r=list(r)
                q=''
                for a in r:
                    a=str(a)
                    q+=a+'\t\t\t'
                print(q)
            end=time.time()
            print()
            print("NUMBER OF ROWS DISPLAYED ",cr.rowcount)
            print("TIME TAKEN ",end-start,"s")
        else:
            print("RECORD NOT EXISTING")
    except:
        print("OPERATION UNSUCCESSFUL!")
    cr.close()
    c.close()          
def displayequijoin():
    print()
    c=mc.connect(host="localhost", user="root", passwd="osjohn", database="mydb")
    if c.is_connected():
        print("Successfully Connected!")
    print("ENTER YOUR CHOICE")
    ch=int(input("1) SUPPLY_CHAIN & SUPPLIER TABLES\n2) SUPPLY_CHAIN & PART TABLES\n"))
    if ch==1:
        sql="select part_id, supplier.supplier_id, ordered, delivered, total_price, supplier_name, address, email_id, ph_no from supply_chain equi join supplier;"
    elif ch==2:
        sql="select part.part_id, supplier_id, ordered, delivered, total_price, part_name, units_in_stock from supply_chain equi join part;"
    cr=c.cursor()
    cr.execute(sql)
    d=cr.fetchall()
    start=time.time()
    for r in d:
        r=list(r)
        q=''
        for a in r:
            a=str(a)
            q+=a+'\t\t\t'
        print(q)
    end=time.time()
    print()
    print("NUMBER OF ROWS DISPLAYED ",cr.rowcount)
    print("TIME TAKEN ",end-start,"s")
    cr.close()
    c.close()
def customdisplay():
    print()
    ans1=input("WARNING! ATTEMPT CUSTOM QUERIES ONLY IF YOU HAVE GOOD KNOWLEDGE ON SQL! DO YOU WAN'T TO CONTINUE ANYWAYS? (Y/N)")
    if ans1 in 'yY':
        c=mc.connect(host="localhost", user="root", passwd="osjohn", database="mydb")
        cr=c.cursor()
        print()
        sql=input("ENTER YOUR CUSTOM SQL QUERY HERE \n")
        if "select" in sql and 'supply_chain' in sql or 'part' in sql or 'supplier' in sql:
            try:
                cr.execute(sql)
                d=cr.fetchall()
                start=time.time()
                for r in d:
                    r=list(r)
                    q=''
                    for a in r:
                        a=str(a)
                        q+=a+'\t\t\t'
                    print(q)
                print()
                end=time.time()
                print("NUMBER OF ROWS DISPLAYED ",cr.rowcount)
                print("TIME TAKEN ",end-start,"s")
            except:
                print("OPERATION UNSUCCESSFUL!\nCHECK THE QUERY")
            cr.close()
            c.close()
        else:
            print("INVALID SELECT QUERY or INVALID TABLE NAME")
def displaygroupby():
    c=mc.connect(host="localhost",user='root',passwd='osjohn',database='mydb')
    if c.is_connected():
        print("successfully connected")
    cr=c.cursor()
    print("ENTER YOUR CHOICE. THIS OPERATION VALID ONLY FOR SUPPLY_CHAIN TABLE & WILL DISPLAY ALONG WITH SUM OF ORDERED QUANTITIES")
    chgroup=int(input('1) PartID\n2) SupplierID\n'))
    if chgroup==1:
        sql="select part_id, sum(ordered) from supply_chain group by PART_ID;"
        print("PARTID\t\t\tSUM")
    elif chgroup==2:
        sql="select supplier_id, sum(ordered) from supply_chain group by SUPPLIER_ID;"
        print("SUPPLIERID\t\tSUM")
    try:
        cr.execute(sql)
        d=cr.fetchall()
        start=time.time()
        for r in d:
            r=list(r)
            q=''
            for a in r:
                a=str(a)
                q+=a+'\t\t\t'
            print(q)
        end=time.time()
        print()
        print("NUMBER OF ROWS DISPLAYED ",cr.rowcount)
        print("TIME TAKEN ",end-start,"s")
    except:
        print("OPERATION UNSUCCESFUL!")
def display():
    ans='y'
    while ans in 'yY':
        print("ENTER YOUR CHOICE")
        chdisplay=int(input("1) ALL THE TABLES\n2) TABLE PART\n3) TABLE SUPPLIER\n4) TABLE SUPPLY_CHAIN\n5) EQUI-JOIN TABLES\n6) GROUP-BY SUM OF ORDERED\n7) RECORDS BASED ON CONDITION\n8) CUSTOM DISPLAY QUERY\n"))
        if chdisplay==1:
            print()
            print("TABLE PART")
            displaypart()
            print()
            print("TABLE SUPPLIER")
            displaysupplier()
            print()
            print("TABLE SUPPLY_CHAIN")
            displaysupplychain()
        elif chdisplay==2:
            print()
            displaypart()
        elif chdisplay==3:
            print()
            displaysupplier()
        elif chdisplay==4:
            print()
            displaysupplychain()
        elif chdisplay==5:
            print()
            displayequijoin()
        elif chdisplay==6:
            print()
            displaygroupby()
        elif chdisplay==7:
            print()
            displayrecordscondition()
        elif chdisplay==8:
            print()
            customdisplay()
        else:
            print("INVALID SELECTION!")
        print()
        ans=input("DO YOU WANNA CONTINUE DISPLAYING RECORDS/TABLES? (Y/N) ")
def login_history():
                c=c=mc.connect(host="localhost",user='root',passwd='osjohn',database='mydb')
                cr=c.cursor()
                master=Tk()
                master.geometry("900x900")
                def opennewwindow():
                    newWindow = Toplevel(master)
                    newWindow.title("New Window")
                    newWindow.geometry("900x900")
                    Label(newWindow,text ="This is a new window").pack()
                sql="select * from login_history;"
                cr.execute(sql)
                d=cr.fetchall()
                q=("UserID\t\tPassWord\t\tLogin Time\t\tLogin Day & Date\t\tIP Address")
                start=time.time()
                for r in d:
                    r=list(r)
                    q=''
                    for a in r:
                        a=str(a)
                        q+=a+'\t\t'
                    qwer='\n'+q
                Label(master,text =qwer)
                Label.pack(master,pady = 10)
                print()
                end=time.time()
                print("NUMBER OF ROWS DISPLAYED ",cr.rowcount)
                print("TIME TAKEN ",end-start,"s")
                print()
                cr.close()
                c.close()
def userlogin(user):
    if user=='user1':
        print("LOGGED IN AS admin nandu")
        print()
        print("YOU HAVE FULL PRIVILEDGE OVER THE DATABASE SYSTEM")
        print()
        while True:
            print("1) INSERT\n2) UPDATE\n3) DELETE\n4) DISPLAY\n5) VIEW LOGIN HISTORY\n6) SAVE & LOGOUT") 
            ch1=int(input("ENTER YOUR CHOICE "))
            if ch1==1:
                print(145*'-')
                print("INSERT OPERATION INITIATED!")
                print()
                insert1()
            elif ch1==2:
                print(145*'-')
                print("UPDATE OPERATION INITIATED!")
                print()
                update1()
            elif ch1==3:
                print(145*'-')
                print("DELETE OPERATION INITIATED!")
                print()
                delete()
            elif ch1==4:
                print(145*'-')
                print("DISPLAY OPERATION INITIATED!")
                print()
                display()
            elif ch1==5:
                print(145*'-')
                print()
                login_history()
            elif ch1==6:
                print()
                me=time.time()
                print("USER nandu LOGGED OUT")
                print("TIME ONLINE ",time.strftime("%H:%M:%S", time.gmtime(me-ms)))
                print(145*'-')
                mastermenu()
            else:
                print("INVALID INPUT")
    elif user=='user2':
        print("LOGGED IN AS user chachu")
        print()
        print("YOU HAVE LIMITED PRIVILEDGE OVER THE DATABASE SYSTEM")
        print()
        while True:
            print("1) INSERT\n2) UPDATE\n3) DISPLAY\n4) SAVE & LOGOUT") 
            ch1=int(input("ENTER YOUR CHOICE "))
            if ch1==1:
                print(145*'-')
                print("INSERT OPERATION INITIATED!")
                print()
                insert2()
            elif ch1==2:
                print(145*'-')
                print("UPDATE OPERATION INITIATED!")
                print()
                update2()
            elif ch1==3:
                print(145*'-')
                print("DISPLAY OPERATION INITIATED!")
                print()
                displaysupplychain()
            elif ch1==4:
                print()
                me=time.time()
                print("USER chachu LOGGED OUT")
                print("TIME ONLINE ",time.strftime("%H:%M:%S", time.gmtime(me-ms)))
                print(145*'-')
                mastermenu()
            else:
                print("INVALID INPUT")
def logindetails():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print("Your Computer Name is: CHARLES BABBAGE 2.0 ULTRA PRO MAX Z FOLD")
    print("Your Computer IP Address is:", IPAddr)
    print()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S %p")
    today=date.today()
    current_date=today.strftime("%a %B %d %Y")
    c=c=mc.connect(host="localhost",user='root',passwd='osjohn',database='mydb')
    cr=c.cursor()
    if user=="user1":
        userd='nandu'
    elif user=="user2":
        userd='chachu'
    sql="insert into login_history values('{}','{}', '{}', '{}', '{}');".format(userd, passwd, current_time, current_date, IPAddr)
    try:
        cr.execute(sql)
        c.commit()
    except:
        c.rollback()
    cr.close()
    c.close()
    print("Login Time (24H) =", current_time)
    print("Date =",current_date)
    print(145*'-')
    userlogin(user)
mastermenu()
