from tkinter import *
from tkinter import messagebox
from tkinter import Radiobutton
import mysql.connector
import pandas as pd


def main_win():
    global root

    root = Tk()

    lbltitle = Label(root , text = "WELCOME TO OUR GUI PROGRAM:)",font = "Arial,35")
    lbltitle.pack()
    lbltitle1 = Label(root, text="WHAT WOULD U LIKE TO DO?", font="Arial,30")
    lbltitle1.pack()
    btn1  =Button(root, text = "SAVE CUSTOMER",command = second_win,font = "Arial,20")
    btn1.place(x=170,y = 50)
    btn2 =Button(root,text = "UPDATE CUSTOMER",command = updatecus,font = "Arial,20")
    btn2.place(x =170, y=100)
    btn3 = Button(root,text = "DELETE CUSTOMER",command = delcus,font = "Arial,20")
    btn3.place(x=170,y = 150)
    btn4 = Button(root,text = "VIEW CUSTOMER",command = viewcus,font = "Arial,20")
    btn4.place(x=170,y= 200)
    btn5 = Button(root,text = "VIEW ALL CUSTOMERS",command = viewallcus,font = "Arial,20")
    btn5.place(x=170,y=250)
    root.geometry("600x300+320+220")
    root.mainloop()


def save():

    name = entrname.get()
    phone = entrphone.get()
    email = entremail.get()

    # 1. Write SQL Statement
    sql = "insert into customers values(null, '{}', '{}', '{}')".format(name, phone, email)

    # 2. Create Connection with DataBase
    con = mysql.connector.connect(user="root", password="", host="localhost", database="customer")

    # 3. Create cursor from connection to execute sql commands : insert/update/delete and select commands
    cursor = con.cursor()
    cursor.execute(sql)

    # 4. Commit as Transaction
    con.commit()  # Transaction

    print(name, " Saved in DataBase")

    messagebox.showinfo("SUCCESS","information saved")

def second_win():
    global window
    global entrname
    global entremail
    global entrphone
    root.destroy()
    window = Tk()

    lbltitle = Label(window,text = "DEAR USER ENTER DETAILS",font = "Arial,25",bg = "yellow")
    lbltitle.pack()
    lblname = Label(window,text ="USER NAME",font ="Arial,20")
    lblname.pack()
    entrname = Entry(window)
    entrname.pack()
    lblphone = Label(window,text = "USER PHONE NO.",font = "Arial,20")
    lblphone.pack()
    entrphone = Entry(window)
    entrphone.pack()
    lblemail =Label(window, text = "USER EMAIL", font = "Arial,20" )
    lblemail.pack()
    entremail = Entry(window,)
    entremail.pack()
    btn = Button(window,text  ="SAVE",command = save)
    btn.pack()
    btn4 = Button(window, text="GO TO MAIN", command=onclick).place(x=150, y=250)
    window.geometry("600x300+120+120")
    window.mainloop()

def call_me():
    messagebox.showinfo("success","information updated")


def finallyupdate():
    cid = entrywindowcid.get()
    radioButton = radioget.get()

    if radioButton == 1:
        customername = entrname.get()
        update1 = "update customers set name = '{}' where cid = '{}'".format(
            customername, cid)
        con = mysql.connector.connect(user="root", password="", host="localhost", database="customer")
        cursor = con.cursor()
        cursor.execute(update1)
        con.commit()
        messagebox.showinfo("Message", "Data has been Updated Successfully")
    elif radioButton == 2:
        customerphone = entrphone.get()

        update2 = "update customers set phone = '{}' where cid = '{}'".format(
            customerphone, cid)
        con = mysql.connector.connect(user="root", password="", host="localhost", database="customer")
        cursor = con.cursor()
        cursor.execute(update2)
        con.commit()
        messagebox.showinfo("Message", "Data has been Updated Successfully")
    elif radioButton == 3:
        customeremail = entremail.get()

        update3 = "update customers set email = '{}' where cid = '{}'".format(customeremail, cid)
        con = mysql.connector.connect(user="root", password="", host="localhost", database="customer")
        cursor = con.cursor()
        cursor.execute(update3)
        con.commit()
        messagebox.showinfo("Message", "Data has been Updated Successfully")
    else:
        messagebox.showerror("ERROR","PLEASE SELECT VALID OPTION")
def updatecus():
    global roote
    global entrywindowcid
    global radio1,radio2,radio3
    global radioget
    global entrphone,entremail,entrname
    roote = Toplevel()
    radioget = IntVar()
    lbltitle = Label(roote,text ="Enter Customer ID You Want To Update :)",font = "Arial,30")
    lbltitle.pack()
    entrywindowcid = Entry(roote)
    entrywindowcid.pack()
    lblname = Label(roote, text = "NEW NAME",font ="Arial,10").place(x=50,y=120)
    entrname = Entry(roote ,state = DISABLED)
    entrname.place(x= 300, y=120)
    lblphone = Label(roote , text ="NEW PHONE NO.",font = "Arial,10").place(x = 50,y=160)
    entrphone = Entry(roote,state = DISABLED)
    entrphone.place(x = 300, y=160)
    lblemail = Label(roote , text ="NEW EMAIL",font = "Arial,10").place(x = 50,y=200)
    entremail = Entry(roote,state = DISABLED)
    entremail.place(x = 300, y=200)

    radio1 = Radiobutton(roote, text = "Name",variable =radioget,value =1,command = rbtn1)
    radio1.pack()
    radio2 = Radiobutton(roote, text = "Phone",variable = radioget,value = 2 ,command = rbtn2)
    radio2.pack()
    radio3 = Radiobutton(roote, text = "Email" ,variable = radioget,value = 3,command =rbtn3)
    radio3.pack()
    btn = Button(roote,text = "Update Info",command = finallyupdate)
    btn.place(x = 300, y=250)
    btn11 = Button(roote,text = "GO TO MAIN").place(x = 150, y=250)

    roote.geometry("600x300+120+120")
    roote.mainloop()

def delcus():
    global win2
    global entrycid
    win2 = Tk()
    lbltitle3 = Label(win2,text = "ENTER ID OF CUSTOMER YOU WANT TO DELETE:)",font = "Arial,30").pack()
    entrycid = Entry(win2)
    entrycid.place(x=200,y=20)
    btn0 = Button(win2, text="DELETE",command = finallydel)
    btn0.place(x=200,y= 80)
    btn12 = Button(win2, text="GO TO MAIN", command=main_win).place(x=100, y=80)
    win2.geometry("600x300+120+120")
    win2.mainloop()


def finallydel():
    cus_id = entrycid.get()
    sql_statement = "delete from customers where cid ='{}'".format(
        cus_id)
    con = mysql.connector.connect(user="root", password="", host="localhost", database="customer")
    cursor = con.cursor()
    cursor.execute(sql_statement)
    con.commit()
    messagebox.showinfo("success","DATA DELETED")


def viewcus():
    global win3
    global entrycid
    win3 = Tk()
    lbltitle = Label(win3,text = "ENTER CUSTOMER ID WHOSE DETAILS YOU WANT TO SEE",font = "Arial,20")
    lbltitle.pack()
    entrycid = Entry(win3)
    entrycid.pack()
    btn = Button(win3,text = "VIEW",command = gotoview)
    btn.pack()
    win3.mainloop()

def gotoview():
    global win4
    win4 = Tk()

    lbltitle = Label(win4, text="DETAILS:", font="Arial,20")
    lbltitle.pack()
    view = entrycid.get()
    sql = "select * from customers where cid ='{}'".format(view)
    con = mysql.connector.connect(user="root", password="", host="localhost", database="customer")
    cursor = con.cursor()
    cursor.execute(sql)
    cusdetail = cursor.fetchall()
    cusdetails = pd.DataFrame(cusdetail)

    lbldetail = Label(win4,text = cusdetails,font="Arial,30").pack()
    win4.geometry("600x300+120+120")
    win4.mainloop()

def viewallcus():
    win5 = Tk()
    sql = "select * from customers"
    con = mysql.connector.connect(user="root", password="", host="localhost", database="customer")
    cursor = con.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        row = pd.DataFrame(rows)

    lbltable = Label(win5,text = row,font ="Arial,20").pack()
    print("deatails of all customers are printed below")

def onclick():
    window.destroy()
    main_win()

def rbtn1():
    entrname.configure(state = "normal")
    entrphone.configure(state = "disabled")
    entremail.configure(state ="disabled")

def rbtn2():
    entrphone.configure(state = "normal")
    entremail.configure(state = "disabled")
    entrname.configure(state ="disabled")
def rbtn3():
    entrname.configure(state="disabled")
    entrphone.configure(state="disabled")
    entremail.configure(state ="normal")


main_win()
