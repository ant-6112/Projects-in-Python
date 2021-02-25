#! /usr/bin/python -d

import pickle
import mysql.connector
import sys
#import tkinter


# import only system from os
from os import system, name
from tkinter import *
from subprocess import call



def db_set():
    db = mysql.connector.connect(host = 'localhost',user = 'root',passwd = 'mysql963258',database = 'bankv2')
    return db

class account(object):
    def __init__(s):
        s.acno      = 0
        s.name      = ""
        s.deposit   = 0
        s.type      = ""
        s.addr      = ""
        s.accontact = ""
        s.branch    = ""
        s.pan       = ""
        s.rate      = 0
        s.acbalance = 0

    def create_account(s):  #function to get data from user for account creation
        name      = input("\n\nEnter the name of the account holder(25 characters only): ")
        s.name    = name.capitalize()
        s.adr     = input("\n\n Enter the Address of the account holder(80 characters only): ")
        s.mob     = input("\n\n Enter the Contact Number of the account holder: ")
        pan       = input("\n\n Enter the PAN number of the account holder(10): ")
        s.pan     = pan.upper()
        s.brn     = input("\n\n Enter the Bank Branch where account is opening(15 characters only):")
        s.deposit = int(input("\n Enter initial amount\n(>=500 for Saving and >=1000 for Current): "))
        

    def create_savcur(s):  #function to get data from user for bank saving and current account
        s.id    = int(input("\n\n Enter the account id: "))        
        s.tran  = input("\n\n Enter the transaction details: ")
        s.dt    = input("\n\n Enter the date of transaction: ")
        s.dbt   = int(input("\n\n Enter the amount debited: "))
        s.crdt  = int(input("\n\n Enter the amount credited: "))
        
    def create_fix(s):  #function to get data from user for fixed account               
        s.dbt   = int(input("\n\n Enter the Fixed Deposit amount : "))
        s.term  = int(input("\n\n Enter the term for FD in Months :"))             
        
def clear():
    system('cls') 
    #cls = lambda: os.system('cls')
    #cls = subprocess.call('cls', shell=True)
    #_= call('clear' if os.name == 'posix' else 'cls')
    #print("\n" * 40)
 
def write_accountdb():
    db = db_set()
    cur = db.cursor()
    typ = input("\n Enter type of the account (Current/Saving/Fixed): ")
    stype = typ.upper()
    try:           
        if (stype == 'CURRENT') or (stype == 'SAVING') :
            ac  = account()
            data        = ac.create_account()            
            sname       = ac.name            
            saddr       = ac.adr
            saccontact  = ac.mob
            span        = ac.pan
            sdeposit    = ac.deposit
            sbranch     = ac.brn
            sactdt      = ac.deposit
            dbt = 0
            trans = 'Opening Balance'
            rate = 3
            inst_act = "INSERT INTO actdata(acname,actype,acaddr,accontact,branch,pan,rate,acbalance,acdt) VALUES('%s','%s','%s','%s','%s','%s','%d','%d',CURDATE());" % (sname, stype, saddr, saccontact, sbranch, span, rate, sdeposit)
            print(inst_act)
            cur.execute(inst_act)
            db.commit()                                                                     #Changes saved
        
            sactno = "SELECT actno from actdata order by actno desc limit 1"     #############           
            cur.execute(sactno)
            rec = cur.fetchall()
            for sactno in rec:
                pactno = sactno[0]             
            if stype == 'CURRENT':
                cur_act = "INSERT INTO currentact(actno,acttype,transdesc,acttrndt,debit,credit) VALUES('%d','%s','%s',CURDATE(),'%d','%d');" % (pactno, stype, trans, dbt, sactdt)
                print(cur_act)                
                cur.execute(cur_act)
                db.commit()
            elif stype == 'SAVING':
                sav_act = "INSERT INTO savingact(actno,acttype,transdesc,acttrndt,debit,credit) VALUES('%d','%s','%s',CURDATE(),'%d','%d');" % (pactno, stype, trans, dbt, sactdt)
                print(sav_act)                
                cur.execute(sav_act)                
                db.commit()                
        elif stype == 'FIXED':
            ac = account()
            data1=ac.create_account()
            data2       = ac.create_fix()
            sname       = ac.name
            #stype = ac.type
            saddr       = ac.adr
            saccontact  = ac.mob
            span        = ac.pan
            sdeposit    = ac.deposit
            sbranch     = ac.brn            
            sdbt        = ac.dbt
            sterm       = ac.term
            rate        = 7.5
            
            sbal = sdbt+sdbt*((rate*sterm)/1200)
            print(sbal)
            inst_act = "INSERT INTO actdata(acname,actype,acaddr,accontact,branch,pan,rate,acbalance,acdt) VALUES('%s','%s','%s','%s','%s','%s','%d','%d',CURDATE());" % (sname, stype, saddr, saccontact, sbranch, span, rate, sdeposit)
            print(inst_act)
            cur.execute(inst_act)
            db.commit()
            sel_act = "SELECT actno from actdata order by actno desc limit 1"
            cur.execute(sel_act)
            rec = cur.fetchall()
            for sactno in rec:
                pactno = sactno[0]  
            fix_act = "INSERT INTO fixedact(actno,aactname,acttrndt,terms,initamt,acbalance) VALUES('%d','%s',CURDATE(),'%.2f','%d','%d');" % (pactno, sname, sterm, sdbt, sbal)
            print(fix_act)            
            cur.execute(fix_act)
            db.commit()
        db.close()
        print("\n\n Account Created Successfully")
    except:
        pass
    
    input("\n\n\n Press any key to exit...")
    clear()

def write_deposit():
    try:
        ac          = account()
        data        = ac.create_account()
        sname       = ac.name
        stype       = ac.type
        saddr       = ac.adr
        saccontact  = ac.mob
        span        = ac.pan
        sdeposit    = ac.deposit
        sbranch     = ac.brn
        db          = db_set()
        cur         = db.cursor()
        
        if stype == 'CURRENT':
            rate = 3
            inst_act = "INSERT INTO currentact(actno,acttype,transdesc,acttrndt,debit,credit) VALUES('%d','%s','%s',CURDATE(),'%d','%d');" % (pactno, stype, trans, dbt, sactdt)

        elif stype == 'SAVING':
            rate = 3.5
            inst_act = "INSERT INTO savingact(actno,acttype,transdesc,acttrndt,debit,credit) VALUES('%d','%s','%s',CURDATE(),'%d','%d');" % (pactno, stype, trans, dbt, sactdt)
            
        elif stype == 'FIXED':
            rate = 7.5
            inst_act = "INSERT INTO fixedact(actno,aactname,acttrndt,terms,initamt,acbalance) VALUES('%d','%s',CURDATE(),'%.2f','%d','%d');" % (pactno, sname, sterm, sdbt, sbal)
            
        print(inst_act)
        cur.execute(inst_act)
        db.commit()
        db.close()
        print("\n\n Account Created Successfully")
    except:
        pass
    
    input("\n\n\n Press any key to exit...")
    clear()

def display_sp():
    num     = int(input("\n\nEnter Account Number: "))
    db      = db_set()
    sel_act = "SELECT * from actdata where actno = '%d';" % num
    cur     = db.cursor()
    cur.execute(sel_act)
    record3 = cur.fetchall()
    
    for rcds in record3:
        act     = rcds[0]                                               #Account Number
        nm      = rcds[1]                                               #Account Name
        tpe     = rcds[2]                                               #Account Type
        adr     = rcds[3]                                               #Address 
        cont    = rcds[4]                                               #Contact
        br      = rcds[5]                                               #Account Branch
        pn      = rcds[6]                                               #PAN Number
        rt      = rcds[7]                                               #Rate
        bal     = rcds[8]                                               #Balance
    sel_sav = "SELECT * from savingact where actno = '%d';" % num
    #cur = db.cur()
    cur.execute(sel_sav)
    record4 = cur.fetchall()
    

    sel_cur = "SELECT * from currentact where actno = '%d';" % num
    #cur = db.cur()
    cur.execute(sel_cur)
    record5 = cur.fetchall()        

    sel_fix = "SELECT * from fixedact where actno = '%d';" % num
    #cur = db.cursor()
    cur.execute(sel_fix)
    record6 = cur.fetchall()

    #def actstmt(act,nm,tpe,adr,cont,br,pn):
    root = Tk()
    T = Text(root, height= 30, width = 150)
    T.pack()

    T.insert(END, "Account Statement\n")
    T.insert(END, "Account Number: %d" % act)
    T.insert(END, "\nAccount Name: %s" % nm)
    T.insert(END, "\nAccount Type: %s" % tpe)
    T.insert(END, "\nAddress : %s" % adr)
    T.insert(END, "\nAccount Branch: %s" % br)
    T.insert(END, "\nContact Number: %s" % cont)
    T.insert(END, "\nPAN Number: %s\n" % pn)
    T.insert(END, "\nCurrent Balance:%d\n" % bal)
    T.insert(END, "\nTransaction Details | Date       | Debit   | Credit  \n")

    if act==num:
        if tpe == 'CURRENT':
            for rcds2 in record5:
                cact    = rcds2[0]            
                ctpe    = rcds2[1]
                cdsc    = rcds2[2]
                ctrndt  = str(rcds2[3])
                cdbt    = rcds2[4]
                ccdt    = rcds2[5]
                #actstmt(act,nm,tpe,adr,cont,br,pn)


                r = "{:<19} | {:<10} | {:<7} | {:<7}\n"
                T.insert(END, r.format(cdsc,ctrndt,cdbt,ccdt))
            mainloop()    
                
        elif tpe == 'SAVING':
            for rcds1 in record4:
                sact    = rcds1[0]            
                stpe    = rcds1[1]
                sdsc    = rcds1[2]
                strndt  = str(rcds1[3])
                sdbt    = rcds1[4]
                scdt    = rcds1[5]
                #actstmt(act,nm,tpe,adr,cont,br,pn)
                r = "{:<19} | {:<10} | {:<7} | {:<7}"
                T.insert(END, r.format(sdsc,strndt,sdbt,scdt))
            mainloop()
                
        elif tpe == 'FIXED':
            for rcds3 in record6:
                fact    = rcds3[0]
                fnm     = rcds3[1]
                ftrndt  = str(rcds3[2])
                fterm   = rcds3[3]
                fiamt   = rcds3[4]
                fbal    = rcds3[5]
                #actstmt(act,nm,tpe,adr,cont,br,pn,rt,bal)
                #T.insert(END, "\nTransaction Date | Terms in Months | Initial Amount | Maturity Amount\n")
                r = "{:<16} | {:<15} | {:<14} | {:<15}"
                T.insert(END, r.format(strndt,fterm,fiamt,fbal))
            mainloop()
            
    input("\n\n\n Press any key to exit...")
    clear()

def mod_account():
    found=0
    try:
        db = db_set()
        num = int(input("\n\nEnter Account Number: "))
        print("\n 1. Change Name \n 2. Change Address \n 3. Change Contact number \n 4. Change Branch \n ")
        ch = int(input("Enter Your Choice(1-4): "))
        
        if ch==1:
            name=input("\n\nEnter Account Name: ")
            mod_act = "UPDATE actdata set acname = '%s' where actno = '%d';" % (name , num)
            print(mod_act)
            #input("\n\n\n Press any key to exit...")
            
        elif ch==2:
            addr = input("\n\nEnter Account Address: ")
            mod_act = "UPDATE actdata set acaddr = '%s' where actno = '%d';" % (addr , num)
            
        elif ch==3:
            contact = input("\n\nEnter Contact Number : ")
            mod_act = "UPDATE actdata set accontact = '%s' where actno = '%d';" % (contact , num)
            
        elif ch==4:
            braddr=input("\n\nEnter Branch Address: ")
            mod_act = "UPDATE actdata set branch = '%s' where actno = '%d';" % (braddr , num )
            
        else:
            print("Input correct choice...(1-5)")
            clear()
            pass

        cur = db.cursor()
        cur.execute(mod_act)
        db.commit()
        #input("\n\n\n Press any key to exit...")
        clear()
    except NameError:
        print("Input correct choice..\(1-5\)")
    db.close()
    input("\n\n\n\n\nTHANK YOU\n\nPress any key to exit...")
    clear()

def delete_account():
    found=0
##    try:
    num=int(input("\n\nEnter Account Number: "))
    db=db_set()
    sel_act = "SELECT * from actdata where actno = '%d';" % num
    cur = db.cursor()
    cur.execute(sel_act)
    record = cur.fetchall()
    for rcds in record:
        act = rcds[0]
        tpe = rcds[2]


    if act==num:
        if tpe == 'CURRENT':
            del_act = "DELETE from current where actno = '%d';" % num

        elif tpe == 'SAVING':
            del_act = "DELETE from savingact where actno = '%d';" % num
            
        elif tpe == 'FIXED':
            del_act = "DELETE from fixedact where actno = '%d';" % num
        cur.execute(del_act)
    
        found=1
        del_act = "DELETE from actdata where actno = '%d';" % num
        cur = db.cursor()
        cur.execute(del_act)
        print("\n\n\tRecord Deleted ..")
        db.commit()


    db.close()
    input("\n\n\n Press any key to exit...")
    clear()

def display_all():

    db=db_set()
    sel_act = "SELECT * from actdata " 
    cur = db.cursor()
    cur.execute(sel_act)
    record4 = cur.fetchall()


    root = Tk()
    T = Text(root, height= 30, width = 170)
    T.pack()
    r = "{:^170}\n\n"
    T.insert(END, r.format("ACCOUNT DETAILS"))
    T.insert(END, "Account Id | Account Name         | Type       | Balance    | Address                                                 | Contact    | Branch\n")
    
    for rcds in record4:                     
        act     = rcds[0]
        nm      = rcds[1]
        tpe     = rcds[2]
        bal     = rcds[8]
        addr    = rcds[3]
        con     = rcds[4]
        br      = rcds[5]
        r = '{:<10} | {:<20} | {:<15} | {:<10} | {:<50} | {:<10} | {:<25}\n'

        T.insert(END, r.format(act, nm, tpe, bal, addr, con, br))
        T.insert(END, "\n")
        
    mainloop()    

    input("\n\n\n Press any key to exit...")
    clear()


def deposit():
    found   = 0
    bal     = 0
    total   = 0
    amt     = 0

    num     = int (input("\n\nEnter Account Number: "))
    db      = db_set()
    sel_act = "SELECT * from actdata where actno = '%d';" % num
    cur     = db.cursor()
    cur.execute(sel_act)
    record1 = cur.fetchall()
    sel_bal = "SELECT actno,actype,acbalance from actdata where actno = '%d';" % num
    cur.execute(sel_bal)
    record2 = cur.fetchall()
    for row in record2:
        act     = row[0]
        atyp    = row[1]
        bal     = row[2]

        if act==num:
            print("Your account details are: ")
            print(act, "\t",atyp,"\t", bal)
            amt     = int(input("Enter the amount to be deposited: "))
            trandt  = input("Enter the transaction description: " )
            bal = amt + bal
            updtstmt = "UPDATE actdata SET acbalance = '%d' where actno = '%d';" %(bal, num)
            cur.execute(updtstmt)
            db.commit()
            
            if (atyp == "SAVING"):
                inst_act = "INSERT INTO savingact (actno, acttype, transdesc, acttrndt, debit, credit) VALUES ('%d', '%s', '%s', CURDATE(), 0, '%d');" %(num,atyp,trandt,amt)
                cur      = db.cursor()
                cur.execute(inst_act)
                db.commit()

            elif (atyp == "CURRENT"):
                inst_act = "INSERT INTO currentact (actno, acttype, transdesc, acttrndt, debit, credit) VALUES ('%d', '%s', '%s', CURDATE(), 0, '%d');" %(num,atyp,trandt,amt)
                cur      = db.cursor()
                cur.execute(inst_act)
                db.commit()             
                         
            db.close()
            found = 1
            
            print("\n\n\tRecord Updated")
        else:
            print("\n\n\tRecord Not Updated")
      

    input("\n\n\n Press any key to exit...")
    clear()

def withdraw():
    found   = 0
    bal     = 0
    total   = 0
    amt     = 0
##    try:
    num     = int(input("\n\nEnter Account Number: "))
    db      = db_set()
    sel_act = "SELECT * from actdata where actno = '%d';" % num
    cur     = db.cursor()
    cur.execute(sel_act)
    record1 = cur.fetchall()
    sel_bal = "SELECT actno,actype,acbalance from actdata where actno = '%d';" % num
    #cur = db.cursor()
    cur.execute(sel_bal)
    record2 = cur.fetchall()
    for row in record2:
        act     = row[0]
        atyp    = row[1]
        bal     = row[2]

        if act==num:
            print("Your account details are :")
            print(record1)
            print("\n\n\tTO WITHDRAW AMOUNT")
            amt = int(input("Enter amount to be withdraw: "))
            trandt = input("Enter the transaction description:")
            
            if (bal<500 and atyp=="SAVING") or (bal<1000 and atyp=="CURRENT"):
                print("Insufficient balance")
            else:
                bal = bal - amt                              
                updt_act = "UPDATE actdata SET acbalance = '%d' where actno = '%d';" %(bal, num)
                cur      = db.cursor()
                cur.execute(updt_act)
                
            
            if (atyp == "SAVING"):
                inst_act = "INSERT INTO savingact (actno, acttype, transdesc, acttrndt, debit, credit) VALUES ('%d', '%s', '%s', CURDATE(), '%d', 0);" %(num,atyp,trandt,amt)
            elif (atyp == "CURRENT"):
                inst_act = "INSERT INTO currentact (actno, acttype, transdesc, acttrndt, debit, credit) VALUES ('%d', '%s', '%s', CURDATE(), '%d', 0);" %(num,atyp,trandt,amt)
            
            cur      = db.cursor()
            cur.execute(inst_act)
            db.commit()                   
            db.close()
            found=1
            print("\n\n\tRecord Updated")
        else:
            print("\n\n\tRecord Not Updated")

##    except EOFError:
##        if found==0:
##            print("\n\nRecord Not Found")
    input("\n\n\n Press any key to exit...")
    clear()

def intro():
    print("{:^170}".format("BANK MANAGEMENT"))
    print("\n\n\nMADE BY : Aniruddha Upreti, Antrang Agrawal, Sreevatsa Murthy, Stitipragyan Patra")
    print("CLASS   : 12 - B","\nSCHOOL  : Delhi Public School, Bangalore East ")


clear()
intro()

root = Tk()
root.title("Banking software ")

Label(text="Bank Management System \n BY : Aniruddha Upreti, Antrang Agrawal, Sreevatsa Murthy, Stitipragyan Patra\nCLASS   : 12 - B\nSCHOOL  : Delhi Public School, Bangalore East ").pack()

separator = Frame(height = 200, width = 700, bd = 2, relief = SUNKEN)
separator.pack(fill=X, padx=5, pady=5)


menu = Menu(root)
root.config(menu=menu)
accountmenu = Menu(menu)
menu.add_cascade(label = "Manage Accounts", menu = accountmenu)
accountmenu.add_command(label = "Add New Account", command = write_accountdb)
accountmenu.add_command(label = "Modify Account", command = mod_account)
accountmenu.add_command(label = "Remove Account", command = delete_account)
accountmenu.add_command(label = "Show Specific Account", command = display_sp)
accountmenu.add_command(label = "Show All Accounts", command = display_all)
accountmenu.add_separator()
accountmenu.add_command(label="Exit", command = root.destroy)

depositmenu = Menu(menu)
menu.add_cascade(label = "Transactions", menu = depositmenu)
depositmenu.add_command(label = "Deposit Money", command = deposit)
depositmenu.add_command(label = "Withdraw Money", command = withdraw)

mainloop()

