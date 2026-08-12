from tkinter import *
from tkinter import messagebox
import sqlite3

win = Tk()
win.geometry("1200x1200")

username = StringVar()
password = StringVar()

t8 = StringVar()
empid=StringVar()
empname = StringVar()
empfather = StringVar()
empaddress = StringVar()
empmail = StringVar()
empdesg = StringVar()
empsal = StringVar()
empsalary=StringVar()

cusername = StringVar()
cmail = StringVar()
ccontact = StringVar()
ccomplaint = StringVar()
csuggestion = StringVar()

acno = StringVar()
acctype = StringVar()
username = StringVar()
address = StringVar()
crbalance = StringVar()
withdraw = StringVar()
balance = StringVar()
date = StringVar()
initialamt = StringVar()
currentamt=StringVar()
withdrawmoney=StringVar()
depositemoney=StringVar()

mail = StringVar()
contact = StringVar()
altcontact = StringVar()
suggestion = StringVar()

def signup():
    ins = sqlite3.connect("project3.db")
    usernames = username.get()
    passwords = password.get()

    if (usernames==""):
        messagebox.showinfo("Banking Management System", "Please enter username")
    elif (passwords==""):
        messagebox.showinfo("Banking Management System", "Please enter password")
    else:
        ins.execute("create table if not exists login(username char(20) not null, password cgar(20) not null);")
        ins.execute("insert into login(username, password) values (?,?)", (usernames, passwords,));
        messagebox.showinfo("SIGNUP COMPLETE", "You are registered user")
        ins.commit()

def login():
    usernames=username.get()
    passwords=password.get()
    ins = sqlite3.connect("project3.db")

    if (usernames==""):
        messagebox.showinfo("Banking Management", "Please enter the username")
    elif (passwords==""):
        messagebox.showinfo("Banking Management", "Please enetr the password")
    else:
        show = ins.execute("select * from login where USERNAME = ? AND PASSWORD = ?", (usernames, passwords,))
        if show.fetchone() is None:
            messagebox.showinfo("Signup Process", "Please enter the correct username and password")
        else:
            messagebox.showinfo("Signup Process", "You are administrator of the project") 
            flog.grid_forget()
            fmain.grid(row=0, padx=120, pady=100)
    
def complaint():
    fmain.grid_forget()
    fcomp.grid(row=0, padx=200, pady=200)
        
def suggestion():
    fmain.grid_forget()
    fsugg.grid(row=0, padx=200,pady=200)

def account():
    facmt.grid(row=0, padx=200, pady=200)
    fmain.grid_forget()

def previous():
    facmt.grid_forget()
    fmain.grid(row=0, padx=200, pady=200)

def save():
    acnos=acno.get()
    empnames=empname.get()
    empfathers=empfather.get()
    acctypes=acctype.get()
    empmails=empmail.get()
    empaddresses=empaddress.get()
    contacts=contact.get()
    gender=t8.get()
    altcontacts=altcontact.get()
    dates=date.get()
    initialamts=initialamt.get()
    
    ins=sqlite3.connect('project3.db')


    if (acnos==""):
        messagebox.showinfo("Banking Management", "Please enter the account number")
    elif(empnames==""):
        messagebox.showinfo("Banking Management","Please enter the employee names")
    elif(empfathers==""):
        messagebox.showinfo("Banking Management","Please enter the father name")
    elif(acctypes==""):
        messagebox.showinfo("Banking Management","Please enter the account type")
    elif(empmails==""):
        messagebox.showinfo("Banking Management","Please enter the emails")
    elif(empaddresses==""):
        messagebox.showinfo("Banking Management","Please enter the address")
    elif(contacts==""):
        messagebox.showinfo("Banking Management","Please enter the contact")
    elif(altcontact==""):
        messagebox.showinfo("Banking Management","Please enter the alternative contact")
    elif(dates==""):
        messagebox.showinfo("Banking Management","Please enter the date")
    elif(initialamts==""):
        messagebox.showinfo("Banking Management","Please enter the initial amount")
    else:
        ins=sqlite3.connect('project3.db')
        ins.execute("create table if not exists employeedata(acno char(20) not null primary key,empname char(30) not null,empfather char(20) not null,acctype char(20) not null,empmail char(20) not null,empaddress char(20) not null,contact char(20) not null,gender,altcontact char(20) not null,date char(20) not null, initialamt char(20) not null);")
        ins.execute("insert into  employeedata(acno,empname,empfather,acctype,empmail,empaddress,contact,gender,altcontact,date,initialamt) values(?,?,?,?,?,?,?,?,?,?,?)",(acnos,empnames,empfathers,acctypes,empmails,empaddresses,contacts,gender,altcontacts,dates,initialamts,));
        messagebox.showinfo('Banking Project','Employee Data Saved')
        ins.commit()

def savewithdraw():
    acnos=acno.get()
    usernames=username.get()
    addresses=address.get()
    crbalances=crbalance.get()
    withdrawmoneys=withdrawmoney.get()
    balances=balance.get()
    dates=date.get()
    
    ins=sqlite3.connect('project3.db')
    
    if (acnos==""):
        messagebox.showinfo("Banking Management", "Please enter the account number")
    elif(usernames==""):
        messagebox.showinfo("Banking Management","Please enter the usernames")
    elif(addresses==""):
        messagebox.showinfo("Banking Management","Please enter the address")
    elif(crbalances==""):
        messagebox.showinfo("Banking Management","Please enter the current amount")
    elif(withdrawmoneys==""):
        messagebox.showinfo("Banking Management","Please enter the withdrawn money")
    elif(balances==""):
        messagebox.showinfo("Banking Management","Please enter the balance")
    elif(dates==""):
        messagebox.showinfo("Banking Management","Please enter the date")
    else:
        ins=sqlite3.connect('project3.db')
        ins.execute("create table if not exists withdrawal(acno char(20) not null primary key,username char(30) not null,address char(20) not null,crbalance char(20) not null,withdrawmoney char(20) not null,balance char(20) not null,date char(20) not null);")
        ins.execute("insert into  withdrawal(acno,username,address,crbalance,withdrawmoney,balance,date) values(?,?,?,?,?,?,?)",(acnos,usernames,addresses,crbalances,withdrawmoneys,balances,dates,));
        messagebox.showinfo('Banking Project','Withdrawal Data Saved')
        ins.commit()

def savedeposite():
    acnos=acno.get()
    usernames=username.get()
    addresses=address.get()
    crbalances=crbalance.get()
    depositemoneys=depositemoney.get()
    balances=balance.get()
    dates=date.get()
    
    ins=sqlite3.connect('project3.db')
    
    if (acnos==""):
        messagebox.showinfo("Banking Management", "Please enter the account number")
    elif(usernames==""):
        messagebox.showinfo("Banking Management","Please enter the usernames")
    elif(addresses==""):
        messagebox.showinfo("Banking Management","Please enter the address")
    elif(crbalances==""):
        messagebox.showinfo("Banking Management","Please enter the current amount")
    elif(depositemoneys==""):
        messagebox.showinfo("Banking Management","Please enter the deposite money")
    elif(balances==""):
        messagebox.showinfo("Banking Management","Please enter the balance")
    elif(dates==""):
        messagebox.showinfo("Banking Management","Please enter the date")
    else:
        ins=sqlite3.connect('project3.db')
        ins.execute("create table if not exists deposition(acno char(20) not null primary key,username char(30) not null,address char(20) not null,crbalance char(20) not null,depositemoney char(20) not null,balance char(20) not null,date char(20) not null);")
        ins.execute("insert into  deposition(acno,username,address,crbalance,depositemoney,balance,date) values(?,?,?,?,?,?,?)",(acnos,usernames,addresses,crbalances,depositemoneys,balances,dates,));
        messagebox.showinfo('Banking Project','Deposition Data Saved')
        ins.commit()
    

def update():
    ins=sqlite3.connect('project3.db')
    acnos=acno.get()
    empnames=empname.get()
    empfathers=empfather.get()
    acctypes=acctype.get()
    empmails=empmail.get()
    empaddresses=empaddress.get()
    contacts=contact.get()
    gender=t8.get()
    altcontacts=altcontact.get()
    dates=date.get()
    initialamts=initialamt.get()
    ins.execute("update employeedata set empname=?,empfather=?, acctype=?, empmail=?, empaddress=?, contact=?, gender=?, altcontact=?, date=?, initialamt=? where acno=?",(empnames, empfathers, acctypes, empmails, empaddresses, contacts, gender, altcontacts, dates, initialamts,acnos,));
    messagebox.showinfo('Employee database','Employee Record Updated')
    ins.commit()                        

def search():
    acnos=acno.get()
    empnames=empname.get()
    empfathers=empfather.get()
    acctypes=acctype.get()
    empmails=empmail.get()
    empaddresses=empaddress.get()
    contacts=contact.get()
    gender=t8.get()
    altcontacts=altcontact.get()
    dates=date.get()
    initialamts=initialamt.get()
    ins=sqlite3.connect('project3.db')
    show=ins.execute("select * from employeedata where acno=?", (acnos,))
    if show.fetchone() is None:
        messagebox.showinfo("Employee database", "Data doesnot exist")
    else:
        show=ins.execute("select * from employeedata where acno=?", (acnos,))
        for row in show:
            acno.set(row[0])
            empname.set(row[1])
            empfather.set(row[2])
            acctype.set(row[3])
            empmail.set(row[4])
            empaddress.set(row[5])
            contact.set(row[6])
            t8.set(row[7])
            altcontact.set(row[8])
            date.set(row[9])
            initialamt.set(row[10])
            print(row[0]," ",row[1]," ",row[2]," ",row[3]," ",row[4]," ",row[5]," ",row[6]," ",row[7]," ",row[8]," ",row[9]," ",row[10]) 
            messagebox.showinfo("Employee database", "Employee Record Found")
    ins.commit()
    
def allaccount():
    ins=sqlite3.connect('project3.db')
    acnos=acno.get()
    empnames=empname.get()
    empfathers=empfather.get()
    acctypes=acctype.get()
    empmails=empmail.get()
    empaddresses=empaddress.get()
    contacts=contact.get()
    gender=t8.get()
    altcontacts=altcontact.get()
    dates=date.get()
    initialamts=initialamt.get()

    show=ins.execute("select * from employeedata")
    
    for row in show:
        print(
            row[0]," ",row[1]," ",row[2]," ",row[3]," ",row[4]," ",row[5]," ",row[6]," ",row[7]," ",row[8]," ",row[9]," ",row[10])
            
        print("welcome")
        messagebox.showinfo("Employee database", "All Employee Data")


def seeall():
    ins=sqlite3.connect('project3.db')
    acnos=acno.get()
    empnames=empname.get()
    empfathers=empfather.get()
    acctypes=acctype.get()
    empmails=empmail.get()
    empaddresses=empaddress.get()
    contacts=contact.get()
    gender=t8.get()
    altcontacts=altcontact.get()
    dates=date.get()
    initialamts=initialamt.get()
    see=ins.execute("select * from employeedata")
    for row in see:
        acno.set(row[0])
        empname.set(row[1])
        empfather.set(row[2])
        acctype.set(row[3])
        empmail.set(row[4])
        empaddress.set(row[5])
        contact.set(row[6])
        t8.set(row[7])
        altcontact.set(row[8])
        date.set(row[9])
        initialamt.set(row[10])
        messagebox.showinfo("Employee database", "All Employee Data")


def allemployee():
    ins=sqlite3.connect('project3.db')
    empids=empid.get()
    empnames=empname.get()
    empfathers=empfather.get()
    empaddresses=empaddress.get()
    empmails=empmail.get()
    empdesgs=empdesg.get()
    empsals=empsal.get()
    gender=t8.get()
    all=ins.execute("select * from employees")
    for row in all:
        empid.set(row[0])
        empname.set(row[1])
        empfather.set(row[2])
        empaddress.set(row[3])
        empmail.set(row[4])
        empdesg.set(row[5])
        empsalary.set(row[6])
        t8.set(row[7])
        messagebox.showinfo("Employee database", "All Employee Data")
    ins.commit()
    
def exit():
    fwithdraw.grid_forget()
    facmt.grid_forget()
    fcomp.grid_forget()
    fadcomp.grid_forget()
    fsugg.grid_forget()
    fdeposite.grid_forget()
    fmain.grid_forget()
    fthank.grid(row=0, padx=200, pady=200)

def deposite():
    fdeposite.grid(row=0, padx=120, pady=100)
    facmt.grid_forget()

def delete():
    acnos=acno.get()
    ins=sqlite3.connect('project3.db')
    ins.execute("delete from employeedata where acno=?", (acnos,))
    ins.commit()
    messagebox.showinfo("Employee database", "Employee Record Deleted")

def deleteemployee():
    empids=empid.get()
    ins=sqlite3.connect('project3.db')
    ins.execute("delete from employees where empid=?", (empids,))
    ins.commit()
    messagebox.showinfo('Banking Management','Permanently deleted the employee data')
    
def searchemployee():
    empids=empid.get()
    empnames=empname.get()
    empfathers=empfather.get()
    empaddresses=empaddress.get()
    empmails=empmail.get()
    empdesgs=empdesg.get()
    empsals=empsal.get()
    gender=t8.get()
    
    if(empids==""):
        messagebox.showinfo("Banking Management","Please enter the employee id")
    else:
        ins=sqlite3.connect('project3.db')
        empids=empid.get()
        show=ins.execute("select * from employees where empid=?",(empids,))
        if show.fetchone() is None:
            messagebox.showinfo("Banking Management", "Data doesnot exist")
        else:
            ins=sqlite3.connect('project3.db')
            show=ins.execute("select * from employees where empid=?",(empids,))
            for row in show:
                empid.set(row[0])
                empname.set(row[1])
                empfather.set(row[2])
                empaddress.set(row[3])
                empmail.set(row[4])
                empdesg.set(row[5])
                empsalary.set(row[6])
                t8.set(row[7])
                
            messagebox.showinfo('Banking Management','Employee Data Found')
        ins.commit()
    
def savesuggestion():
    cusernames=cusername.get()
    cmails=cmail.get()
    ccontacts=ccontact.get()
    csuggestions=csuggestion.get()
    
    if(cusernames==""):
        messagebox.showinfo('banking management','please enter the username')
    elif(cmails==""):
        messagebox.showinfo('banking management','please enter the emailid')
    elif(ccontacts==""):
        messagebox.showinfo('banking management','please enter the contacts')
    elif(csuggestions==""):
        messagebox.showinfo('banking management','please enter the Suggestion')
    else:
        ins=sqlite3.connect('project3.db')
        ins.execute("create table if not exists suggestions(usernames char(20) not null,mails char(30) not null,contact char(20) not null,suggestion char(30) not null);")
        ins.execute("insert into suggestions(usernames,mails,contact,suggestion) values(?,?,?,?)",(cusernames,cmails,ccontacts,csuggestions,));
        messagebox.showinfo('banking management',cusernames+'  '+cmails+'  '+ccontacts+' '+csuggestions)
        messagebox.showinfo('Banking Project','Suggestion Save')
        ins.commit()

def suggestionclear():
    cusername.set("")
    cmail.set("")
    ccontact.set("")
    csuggestion.set("")
    
def clearemployees():
    messagebox.showinfo('Banking Management','Employee Data Cleared')
    empid.set("")
    empname.set("")
    empfather.set("")
    empaddress.set("")
    empmail.set("")
    empsalary.set("")

def depositeclear():
    acno.set("")
    username.set("")
    address.set("")
    crbalance.set("")
    depositemoney.set("")
    balance.set("")
    date.set("")

def previous1():
    facc.grid_forget()
    facmt.grid(row=0, padx=200, pady=200)
    
def previous2():
    femp.grid_forget()
    fmain.grid(row=0, padx=200, pady=200)


def saveemployee():
    empids=empid.get()
    empnames=empname.get()
    empfathers=empfather.get()
    empaddresses=empaddress.get()
    empmails=empmail.get()
    empdesgs=empdesg.get()
    empsals=empsalary.get()
    gender=t8.get()

    if (empids==""):
        messagebox.showinfo("Banking Management", "Please enter the employee id")
    elif(empnames==""):
        messagebox.showinfo("Banking Management","Please enter the employee names")
    elif(empfathers==""):
        messagebox.showinfo("Banking Management","Please enter the father name")
    elif(empaddresses==""):
        messagebox.showinfo("Banking Management","Please enter the employee address")
    elif(empmails==""):
        messagebox.showinfo("Banking Management","Please enter the emails")
    elif(empdesgs==""):
        messagebox.showinfo("Banking Management","Please enter the designation")
    
    else:
        ins=sqlite3.connect('project3.db')
        ins.execute("create table if not exists employees(empid char(20) not null primary key,empname char(30) not null,empfather char(20) not null,empaddress  char(30) not null,empmail char(30) not null,empdesg char(200) not null, empsalary char(30)not null,gender);")
        ins.execute("insert into  employees(empid,empname,empfather,empaddress,empmail,empdesg,empsalary,gender) values(?,?,?,?,?,?,?,?)",(empids,empnames,empfathers,empaddresses,empmails,empdesgs,empsals,gender,));
        messagebox.showinfo('Banking Project','Employee Data Saved')
        ins.commit()

def updateemployee():
    empids=empid.get()
    empnames=empname.get()
    empfathers=empfather.get()
    empaddresses=empaddress.get()
    empmails=empmail.get()
    empdesgs=empdesg.get()
    empsals=empsalary.get()
    gender=t8.get()

    if (empids==""):
        messagebox.showinfo("Banking Management", "Please enter the employee id")
    elif(empnames==""):
        messagebox.showinfo("Banking Management","Please enter the employee names")
    elif(empfathers==""):
        messagebox.showinfo("Banking Management","Please enter the father name")
    elif(empaddresses==""):
        messagebox.showinfo("Banking Management","Please enter the employee address")
    elif(empmails==""):
        messagebox.showinfo("Banking Management","Please enter the emails")
    elif(empsals==""):
        messagebox.showinfo("Banking Management","Please enter the employee salary")
    else:
        ins=sqlite3.connect('project3.db')                                                                                                                                                                               
        ins.execute("update employees set empname=?,empfather=?,empaddress=?,empmail=?,empsalary=?,gender=? where empid=?",(empnames,empfathers,empaddresses,empmails,empsals,gender,empids));
        messagebox.showinfo('Banking Project','Employee Data Updated')
        ins.commit()

def previous3():
    fcomp.grid_forget()
    fmain.grid(row=0, padx=200, pady=200)

def addcomplaint():
    addcomplaint.grid(row=0, padx=200, pady=200)
    fcomp.grid_forget()

def showcomplaints():
    ins=sqlite3.connect('project3.db')
    show=ins.execute("select * from complaints")
 
    for row in show:
        print(row[0]+'   '+row[1]+'   '+row[2]+'  '+row[3])

    ins.commit()

def savecomplaint():
    cusernames=cusername.get()
    cmails=cmail.get()
    ccontacts=ccontact.get()
    complaints=ccomplaint.get()

    if (cusernames==""):
        messagebox.showinfo('Banking Management', 'Please enter the username')
    elif (cmails==""):
        messagebox.showinfo('Banking Management', 'Please enter the email')
    elif(ccontacts==""):
        messagebox.showinfo('Banking Management','Please enter the contacts')
    elif(complaints==""):
        messagebox.showinfo('Banking Management','Please enter the complaint')
    else:
        ins=sqlite3.connect('project3.db')
        ins.execute("create table if not exists complaints(usernames char(20) not null,mails char(30) not null,contact char(20) not null,ccomplaint char(30) not null);")
        ins.execute("insert into complaints(usernames,mails,contact,ccomplaint) values(?,?,?,?)",(cusernames,cmails,ccontacts,complaints,));
        messagebox.showinfo('Banking Management',cusernames+'  '+cmails+'  '+ccontacts+' '+complaints)
        messagebox.showinfo('Banking Project','Complaint Saved')
        ins.commit()   

def complaintclear():
    cusername.set("")
    cmail.set("")
    ccontact.set("")
    ccomplaint.set("")

def withdrawclear():
    acno.set("")
    username.set("")
    address.set("")
    crbalance.set("")
    withdrawmoney.set("")
    balance.set("")
    date.set("")

def reset():
    username.set("")
    password.set("")

def createaccount():
    facc.grid(row=0)
    facmt.grid_forget()

def withdraw():
    fwithdraw.grid(row=0,padx=120,pady=70)
    facmt.grid_forget()

def clears():
    username.set("")
    password.set("")

def addcomplaint():
    fadcomp.grid(row=0,padx=130,pady=100)
    fcomp.grid_forget()

def employee():
    femp.grid(row=0)
    fmain.grid_forget()

def deleteemployee():
     empids=empid.get()
     if(empids==""):
         messagebox.showinfo("Banking Management","Please enter the employee id")
     else:
         empids=empid.get()
         ins=sqlite3.connect('project3.db')
         ins.execute("delete from employees where empid=?",(empids,))
         messagebox.showinfo('Banking Management','Permanently deleted the employee data')

def showsuggestion():
    ins=sqlite3.connect('project3.db')
    show=ins.execute("select * from suggestions")
    
    for row in show:
        print(row[0]+'   '+row[1]+'   '+row[2]+'  '+row[3])
        
  
    
flog=Frame(win)

label0= Label(flog, text="BANKING MANAGEMENT SYSTEM", bg="black", fg="white", font=("mangal", 40, "bold")).grid(row=0, column=2, columnspan=4)
label1= Label(flog, text='Admin Login', font=('arial', 20, 'bold'), bg='steelblue').grid(row=3, column=3)
label2= Label(flog,text="Username",font=('arial',20,'bold'),height=2).grid(row=5, column=2)
label3= Label(flog,text="Password",font=('arial',20,'bold'),height=2).grid(row=6, column=2)

e1=Entry(flog,textvariable=username,bg="steelblue",bd=5,font=('arial',25,'bold'),border='3',fg='white').grid(row=5, column=3)
e2=Entry(flog,textvariable=password,bg="steelblue",bd=5,font=('arial',25,'bold'),border='3',fg='white').grid(row=6, column=3)
  
b1=Button(flog,text="Login",font=('arial',20,'bold'),padx=35,pady=2,bd=20,bg="cyan",border='2',command=login).grid(row=10,column=3,sticky='w')
b2=Button(flog,text="Sign Up",font=('arial',20,'bold'),padx=25,pady=2,bd=5,bg="cyan",border='4',command=signup).grid(row=10, column=3,sticky='e')
b3=Button(flog,text="Reset",font=('arial',20,'bold'),padx=35,pady=2,bd=5,bg="cyan",border='4',command=clears).grid(row=12,column=3)


fmain= Frame(win, bg='linen')

label4=Label(fmain, text='WELCOME TO BANKING MANAGEMENT SYSTEM', bg='black', fg='white', font=('arial', 30, 'bold')).grid(row=4, column=3, columnspan=5)

btmain1=Button(fmain,text="Account Management",font=('arial',20,'bold'),padx=7,pady=2,bd=7,bg="cyan",command=account).grid(row=7, column=2, columnspan=5)
btmain2=Button(fmain,text="Employee",font=('arial',20,'bold'),padx=84,pady=2,bd=7,bg="cyan",command=employee).grid(row=9, column=2, columnspan=5)
btmain3=Button(fmain,text="Complaint",font=('arial',20,'bold'),padx=82,pady=2,bd=7,bg="cyan",command=complaint).grid(row=11, column=2, columnspan=5)
btmain4=Button(fmain,text="Suggestion",font=('arial',20,'bold'),padx=75,pady=2,bd=7,bg="cyan",command=suggestion).grid(row=13, column=2, columnspan=5)
btmain5=Button(fmain,text="Exit",font=('arial',20,'bold'),padx=124,pady=2,bd=7,bg="cyan",command=exit).grid(row=15, column=2, columnspan=5)



facmt= Frame(win, bg='linen')

label4=Label(facmt,text=" ACCOUNT MANAGEMENT ",bg='black',fg='white',font=('arial',40,'bold')).grid(row=4, column=4,columnspan=5)

btmain1=Button(facmt,text="Create Account",font=('arial',20,'bold'),padx=52,pady=2,bd=7,bg="cyan",command=createaccount).grid(row=6, column=4, columnspan=5)
btmain2=Button(facmt,text="Withdraw Money",font=('arial',20,'bold'),padx=41,pady=2,bd=7,bg="cyan",command=withdraw).grid(row=8, column=4, columnspan=5)
btmain3=Button(facmt,text="Deposite Money",font=('arial',20,'bold'),padx=44,pady=2,bd=7,bg="cyan", command=deposite).grid(row=10, column=4, columnspan=5)
btmain4=Button(facmt,text="All Accounts",font=('arial',20,'bold'),padx=65,pady=2,bd=7,bg="cyan", command=allaccount).grid(row=12, column=4, columnspan=5)
btmain5=Button(facmt,text="Previous",font=('arial',20,'bold'),padx=100,pady=2,bd=7,bg="cyan",command=previous).grid(row=14, column=4, columnspan=5)


facc= Frame(win)

label0=Label(facc,text="  CUSTOMER ACCOUNT  ",bg='black',fg='white',font=('arial',40,'bold')).grid(row=4,column=3,columnspan=5,sticky='e')

label1=Label(facc,text="Account No. :",font=('arial',20,'bold')).grid(row=6,column=2)
eacc1=Entry(facc,textvariable=acno, justify="right",bg="pink",bd=3,font=('arial',20,'bold')).grid(row=6, column=4)

label2=Label(facc,text="User Name :",font=('arial',20,'bold')).grid(row=7,column=2)
eacc1=Entry(facc,textvariable=empname, justify="right",bg="pink",bd=3,font=('arial',20,'bold')).grid(row=7, column=4)

label3=Label(facc,text="Father's Name :",font=('arial',20,'bold')).grid(row=8,column=2)
eacc1=Entry(facc,textvariable=empfather, justify="right",bg="pink",bd=3,font=('arial',20,'bold')).grid(row=8, column=4)

label4=Label(facc,text="Account Type :",font=('arial',20,'bold')).grid(row=9,column=2)
eacc1=Entry(facc,textvariable=acctype,justify="right",bg="pink",bd=3,font=('arial',20,'bold')).grid(row=9, column=4)

label5=Label(facc,text="Email Id:",font=('arial',20,'bold')).grid(row=10,column=2)
eacc1=Entry(facc,textvariable=empmail,justify="right",bg="pink",bd=3,font=('arial',20,'bold')).grid(row=10, column=4)

label6=Label(facc,text="Address :",font=('arial',20,'bold')).grid(row=11,column=2)
eacc1=Entry(facc,textvariable=empaddress,justify="right",bg="pink",bd=3,font=('arial',20,'bold')).grid(row=11, column=4)

label7=Label(facc,text="Contact No. :",font=('arial',20,'bold')).grid(row=12,column=2)
eacc1=Entry(facc,textvariable=contact,justify="right",bg="pink",bd=3,font=('arial',20,'bold')).grid(row=12, column=4)

label8=Label(facc,text="Gender :",font=('arial',20,'bold')).grid(row=13,column=2)
radiobutton=Radiobutton(facc,text="Male",variable=t8, font=('arial',20,'bold'),value=1).grid(row=13,column=3,columnspan=2,sticky='e')
radiobutton=Radiobutton(facc,text="Female",variable=t8, font=('arial',20,'bold'),value=0).grid(row=13,column=3,columnspan=2,sticky='w')

label9=Label(facc,text="Alternative Contact No. :",font=('arial',20,'bold')).grid(row=14,column=2)
eacc1=Entry(facc,textvariable=altcontact, justify="right",bg="pink",bd=3,font=('arial',20,'bold')).grid(row=14, column=4)

label10=Label(facc,text="Date :",font=('arial',20,'bold')).grid(row=15,column=2)
eacc1=Entry(facc, textvariable=date, justify="right",bg="pink",bd=3,font=('arial',20,'bold')).grid(row=15, column=4)

label11=Label(facc,text="Initial Amount :",font=('arial',20,'bold')).grid(row=16,column=2)
eacc1=Entry(facc, textvariable=initialamt, justify="right",bg="pink",bd=3,font=('arial',20,'bold')).grid(row=16, column=4)

bfacc1=Button(facc,text="Save",font=('arial',20,'bold'),padx=84,pady=2,bd=4,bg="grey",command=save).grid(row=18, column=2,columnspan=3)
bfacc2=Button(facc,text="Update",font=('arial',20,'bold'),padx=69,pady=2,bd=4,bg="grey",command=update).grid(row=18, column=3,columnspan=3,sticky='e')
bfacc3=Button(facc,text="Delete",font=('arial',20,'bold'),padx=74,pady=2,bd=4,bg="grey",command=delete).grid(row=20, column=2,columnspan=3)
bfacc4=Button(facc,text="Search",font=('arial',20,'bold'),padx=70,pady=2,bd=4,bg="grey",command=search).grid(row=20, column=3,columnspan=3,sticky='e')
bfacc5=Button(facc,text="See All Accounts",font=('arial',20,'bold'),padx=3,pady=2,bd=4,bg="grey", command=seeall).grid(row=22, column=2,columnspan=3)
bfacc6=Button(facc,text="Previous Page",font=('arial',20,'bold'),padx=20,pady=2,bd=4,bg="grey",command=previous1).grid(row=22, column=3,columnspan=3,sticky='e')


fwithdraw = Frame(win)

label0= Label(fwithdraw, text="WITHDRAW MONEY", bg='black', fg='white', font=('arial', 40, 'bold')).grid(row=3, column=3, columnspan=5, sticky='e')

label1= Label(fwithdraw, text="Account No.:", font=('arial', 20, 'bold'), justify='left').grid(row=6, column=2)
e1=Entry(fwithdraw,textvariable=acno,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=6,column=3)

label2=Label(fwithdraw,text="Username :",justify='left',font=('arial',20,'bold')).grid(row=7,column=2)
e2=Entry(fwithdraw,textvariable=username,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=7,column=3)

labe3=Label(fwithdraw,text="Address :",font=('arial',20,'bold')).grid(row=8,column=2)
e3=Entry(fwithdraw,textvariable=address,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=8,column=3)

label4=Label(fwithdraw,text="Current Amount :",font=('arial',20,'bold')).grid(row=9,column=2)
e4=Entry(fwithdraw,textvariable=crbalance,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=9,column=3)

label5=Label(fwithdraw,text="Withdraw Money :",font=('arial',20,'bold')).grid(row=10,column=2)
e5=Entry(fwithdraw,textvariable=withdrawmoney,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=10,column=3)

label6=Label(fwithdraw,text="Balance :",font=('arial',20,'bold')).grid(row=11,column=2)
e6=Entry(fwithdraw,textvariable=balance,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=11,column=3)

label7=Label(fwithdraw,text="Date :",font=('arial',20,'bold')).grid(row=12,column=2)
e7=Entry(fwithdraw,textvariable=date,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=12,column=3)


bc1=Button(fwithdraw,text="Save",font=('arial',20,'bold'),padx=74,pady=2,bd=4,bg="grey",command=savewithdraw).grid(row=18, column=3,columnspan=3,sticky='w')
bc2=Button(fwithdraw,text="Reset",font=('arial',20,'bold'),padx=70,pady=2,bd=4,bg="grey", command=withdrawclear).grid(row=18, column=3,columnspan=3,sticky='e')
bc3=Button(fwithdraw,text="Exit",font=('arial',20,'bold'),padx=30,pady=2,bd=4,bg="grey",command=exit).grid(row=20, column=3,columnspan=5)



fdeposite = Frame(win)

label0=Label(fdeposite,text="DEPOSITE MONEY",bg='black',fg='white',font=('arial',40,'bold')).grid(row=1,column=3,columnspan=3,sticky='e')

l1=Label(fdeposite,text="Account No. :",font=('arial',20,'bold'),justify='left').grid(row=3,column=2)
e1=Entry(fdeposite,textvariable=acno,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=3,column=3)

l2=Label(fdeposite,text="Username :",justify='left',font=('arial',20,'bold')).grid(row=4,column=2)
e2=Entry(fdeposite,textvariable=username,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=4,column=3)

l3=Label(fdeposite,text="Address :",font=('arial',20,'bold')).grid(row=5,column=2)
e3=Entry(fdeposite,textvariable=address,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=5,column=3)

l4=Label(fdeposite,text="Current Amount :",font=('arial',20,'bold')).grid(row=6,column=2)
e4=Entry(fdeposite,textvariable=crbalance,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=6,column=3)

l5=Label(fdeposite,text="Deposite Money :",font=('arial',20,'bold')).grid(row=7,column=2)
e5=Entry(fdeposite,textvariable=depositemoney,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=7,column=3)

l6=Label(fdeposite,text="Balance :",font=('arial',20,'bold')).grid(row=8,column=2)
e6=Entry(fdeposite,textvariable=balance,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=8,column=3)

l7=Label(fdeposite,text="Date :",font=('arial',20,'bold')).grid(row=9,column=2)
e7=Entry(fdeposite,textvariable=date,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=9,column=3)

bc1=Button(fdeposite,text="Deposite",font=('arial',20,'bold'),padx=74,pady=2,bd=4,bg="grey", command=savedeposite).grid(row=14, column=3,columnspan=3,sticky='w')
bc2=Button(fdeposite,text="Reset",font=('arial',20,'bold'),padx=70,pady=2,bd=4,bg="grey", command=depositeclear).grid(row=14, column=3,columnspan=3,sticky='e')
bc3=Button(fdeposite,text="Exit",font=('arial',20,'bold'),padx=3,pady=2,bd=4,bg="grey",command=exit).grid(row=16, column=3,columnspan=5)

                                                                        

femp=Frame(win)
                                                                                                          
label0=Label(femp,text="EMPLOYEE DETAILS",bg='black',fg='white',font=('arial',40,'bold')).grid(row=4,column=3,columnspan=5,sticky='e')

l1=Label(femp,text="Employee Id :",font=('arial',20,'bold'),justify='left').grid(row=6,column=2)
e1=Entry(femp,textvariable=empid,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=6,column=3)

l2=Label(femp,text="Employee Name :",justify='left',font=('arial',20,'bold')).grid(row=7,column=2)
e2=Entry(femp,textvariable=empname,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=7,column=3)

l3=Label(femp,text="Father's Name :",font=('arial',20,'bold')).grid(row=8,column=2)
e3=Entry(femp,textvariable=empfather,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=8,column=3)

l4=Label(femp,text="Employee Address :",font=('arial',20,'bold')).grid(row=9,column=2)
e4=Entry(femp,textvariable=empaddress,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=9,column=3)

l5=Label(femp,text="Email Id :",font=('arial',20,'bold')).grid(row=10,column=2)
e5=Entry(femp,textvariable=empmail,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=10,column=3)

l6=Label(femp,text="Designation :",font=('arial',20,'bold')).grid(row=11,column=2)
e6=Entry(femp,textvariable=empdesg,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=11,column=3)

l7=Label(femp,text="Salary :",font=('arial',20,'bold')).grid(row=12,column=2)
e7=Entry(femp,textvariable=empsalary, justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=12,column=3)

l8=Label(femp,text="Gender :",font=('arial',20,'bold')).grid(row=13,column=2)
radiobutton=Radiobutton(femp,text="Male",variable=t8,font=('arial',20,'bold'),value=1).grid(row=13,column=3,columnspan=2,sticky='e')
radiobutton=Radiobutton(femp,text="Female",variable=t8,font=('arial',20,'bold'),value=0).grid(row=13,column=3,columnspan=2,sticky='w')

bfacc1=Button(femp,text="Save",font=('arial',20,'bold'),padx=84,pady=2,bd=4,bg="grey",command=saveemployee).grid(row=16, column=2,columnspan=3)
bfacc2=Button(femp,text="Update",font=('arial',20,'bold'),padx=69,pady=2,bd=4,bg="grey",command=updateemployee).grid(row=16, column=3,columnspan=3,sticky='e')
bfacc3=Button(femp,text="Delete",font=('arial',20,'bold'),padx=74,pady=2,bd=4,bg="grey",command=deleteemployee).grid(row=18, column=2,columnspan=3)
bfacc4=Button(femp,text="Search",font=('arial',20,'bold'),padx=70,pady=2,bd=4,bg="grey",command=searchemployee).grid(row=18, column=3,columnspan=3,sticky='e')
bfacc5=Button(femp,text="All Employees ",font=('arial',20,'bold'),padx=16,pady=2,bd=4,bg="grey", command= allemployee).grid(row=20, column=2,columnspan=3)
bfacc6=Button(femp,text="Previous Page",font=('arial',20,'bold'),padx=21,pady=2,bd=4,bg="grey",command=previous2).grid(row=20, column=3,columnspan=3,sticky='e')



fcomp=Frame(win)

label1=Label(fcomp, text="COMPLAINT BOX", bg='black', fg='white', font=('arial', 40, 'bold')).grid(row=6, column=3, columnspan=3)

btmain1=Button(fcomp,text="Add Complaint",font=('arial',20,'bold'),padx=40,pady=2,bd=7,bg="cyan",command=addcomplaint).grid(row=8, column=3,columnspan=5)
btmain2=Button(fcomp,text="See All Complaints",font=('arial',20,'bold'),padx=13,pady=2,bd=7,bg="cyan", command=showcomplaints).grid(row=10, column=3,columnspan=5)
btmain2=Button(fcomp,text="Previous Page",font=('arial',20,'bold'),padx=44,pady=2,bd=7,bg="cyan",command=previous3).grid(row=12, column=3,columnspan=5)



fadcomp=Frame(win)

label0=Label(fadcomp,text=" ADD COMPLAINT",bg='black',fg='white',font=('arial',40,'bold')).grid(row=3,column=3,columnspan=5,sticky='e')

l1=Label(fadcomp,text="Username :",font=('arial',20,'bold'),justify='left').grid(row=6,column=2)
e1=Entry(fadcomp,textvariable=cusername,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=6,column=3)

l2=Label(fadcomp,text="Email Id :",justify='left',font=('arial',20,'bold')).grid(row=7,column=2)
e2=Entry(fadcomp,textvariable=cmail,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=7,column=3)

l3=Label(fadcomp,text="Contact No :",font=('arial',20,'bold')).grid(row=8,column=2)
e3=Entry(fadcomp,textvariable=ccontact,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=8,column=3)

l4=Label(fadcomp,text="Complaint :",font=('arial',20,'bold')).grid(row=9,column=2)
e4=Entry(fadcomp,textvariable=ccomplaint,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=9,column=3)

bc1=Button(fadcomp,text="Save",font=('arial',20,'bold'),padx=74,pady=2,bd=4,bg="grey",command=savecomplaint).grid(row=19, column=3,columnspan=3,sticky='w')
bc2=Button(fadcomp,text="Reset",font=('arial',20,'bold'),padx=70,pady=2,bd=4,bg="grey",command=complaintclear).grid(row=19, column=3,columnspan=3,sticky='e')
bc3=Button(fadcomp,text="All Complaints",font=('arial',20,'bold'),padx=3,pady=2,bd=4,bg="grey",command=showcomplaints).grid(row=21, column=3,columnspan=5)
bc4=Button(fadcomp,text="Exit",font=('arial',20,'bold'),padx=75,pady=2,bd=4,bg="grey",command=exit).grid(row=23, column=3,columnspan=5)



fsugg=Frame(win)

label0=Label(fsugg,text="SUGGESTION BOX",bg='black',fg='white',font=('arial',40,'bold')).grid(row=3,column=3,columnspan=5,sticky='e')

l1=Label(fsugg,text="Username :",font=('arial',20,'bold'),justify='left').grid(row=6,column=2)
e1=Entry(fsugg,textvariable=cusername,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=6,column=3)

l2=Label(fsugg,text="Email Id :",justify='left',font=('arial',20,'bold')).grid(row=7,column=2)
e2=Entry(fsugg,textvariable=cmail,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=7,column=3)

l3=Label(fsugg,text="Contact No :",font=('arial',20,'bold')).grid(row=8,column=2)
e3=Entry(fsugg,textvariable=ccontact,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=8,column=3)

l4=Label(fsugg,text="Suggestions :",font=('arial',20,'bold')).grid(row=9,column=2)
e4=Entry(fsugg,textvariable=csuggestion,justify="right",bg="pink",bd=5,font=('arial',30,'bold')).grid(row=9,column=3)

bc1=Button(fsugg,text="Save",font=('arial',20,'bold'),padx=74,pady=2,bd=7,bg="grey",command=savesuggestion).grid(row=18, column=3,columnspan=3,sticky='w')
bc2=Button(fsugg,text="Reset",font=('arial',20,'bold'),padx=70,pady=2,bd=7,bg="grey",command=suggestionclear).grid(row=18, column=3,columnspan=3,sticky='e')
bc3=Button(fsugg,text="All Suggestions",font=('arial',20,'bold'),padx=2,pady=2,bd=7,bg="grey",command=showsuggestion).grid(row=20, column=3,columnspan=3,sticky='w')
bc4=Button(fsugg,text="Exit",font=('arial',20,'bold'),padx=75,pady=2,bd=7,bg="grey",command=exit).grid(row=20, column=3,columnspan=3,sticky='e')



fthank=Frame(win)
l=Label(fthank, text="THANK FOR USING", font=('arial', 30, 'bold')).grid(row=5, column=4)
l1=Label(fthank, text="BANKING MANAGEMENT SYSTEM SOFTWARE", font=('arial', 30, 'bold'), height=1).grid(row=7, column=4)
                                                                                                      

flog.grid(row=0, padx=200,pady=200)
win.mainloop()
    



