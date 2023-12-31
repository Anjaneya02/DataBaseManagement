import tkinter 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkFont
import pymysql
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

root=tkinter.Tk()
root.state('zoomed')
root.config(bg="#89CFEF")

customfont = tkFont.Font(family="Rockwell Extra Bold", size=24, weight="bold")

heading=Label(root,text='LOGIN',font=('Rockwell Extra Bold',48),bg='#89CFEF')
heading.place(x=550,y=30)

l1=Label(root,text='Username',font=customfont,bg='#89CFEF')
l1.place(x=350,y=200)
e1=Entry(root,width=100, highlightbackground='black', highlightcolor='black', highlightthickness=2)
e1.place(x=600,y=215)

l2=Label(root,text='Password',font=customfont,bg='#89CFEF')
l2.place(x=350,y=375)
e2=Entry(root,width=100, highlightbackground='black', highlightcolor='black', highlightthickness=2)
e2.place(x=600,y=388)

def main():
    root = tkinter.Tk()
    root.state("zoomed")
    root.config(bg='#89CFEF')


    heading2=Canvas(root,width=52,height=1000,bg='black',highlightbackground="black", highlightcolor="black")
    heading2.place(x=-1,y=0)
    heading3=Canvas(root,width=53,height=1000,bg='black',highlightbackground="black", highlightcolor="black")
    heading3.place(x=1309,y=0)
    heading4=Canvas(root,width=1500,height=60,bg='black',highlightbackground="black", highlightcolor="black")
    heading4.place(x=-1,y=655)
    heading5=Canvas(root,width=1500,height=60,bg='black',highlightbackground="black", highlightcolor="black")
    heading5.place(x=-1,y=1)
    heading=Label(
        root,
        text="Stock Management System Dashboard For Admin",
        font=("Rockwell Extra Bold", 24,"bold"),  # Change the font and size
        fg="yellow",  # Change the text color
        bg="black",
        padx=20,  # Add horizontal padding
        pady=10,  # Add vertical padding
        relief="flat",  # Add a border around the label
        borderwidth=2,  # Set border width
        width=0,  # Set a fixed width for the label
        highlightbackground="yellow", 
        highlightcolor="yellow"
    )
    heading.place(x=300,y=0)

    def store():
        t=Toplevel(root)
        t.state("zoomed")
        t.config(bg="grey")
        l1=Label(t,text="Action to Perform",font=("Rockwell Extra Bold",35),bg='white',fg='black' )
        l1.place(x=430,y=10)

        def store_insert():
            tk=Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('store screen insert')
            def savedata():
                if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e5.get())==0 or len(e6.get())==0 or len(e7.get())==0:
                    messagebox.showerror("Hello","Pls fill all data")
                else:
                    db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                    cur=db.cursor()
                    a=e1.get()
                    b=e2.get()
                    c=e3.get()
                    d=e4.get()
                    e=e5.get()
                    f=e6.get()
                    g=e7.get()
                    sq="insert into store values('%s','%s','%s','%s','%s','%s','%s')"%(a,b,c,d,e,f,g)
                    cur.execute(sq)
                    messagebox.showinfo("hi","Data Saved")
                    e1.delete(0,"end")
                    e2.delete(0,"end")
                    e3.delete(0,"end")
                    e4.delete(0,"end")
                    e5.delete(0,"end")
                    e6.delete(0,"end")
                    e7.delete(0,"end")
                    db.commit()
                    db.close()
            def check():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                
                a1=e1.get()
                sql="select StoreID from store"
                cur.execute(sql)
                data=cur.fetchall()
                name=['']
                for x in data:
                    name.append(x[0])
                if a1 in name:
                    ltx.config(text='Store ID already exist')
                else:
                    ltx.config(text='You can go ahead')

                if len(e6.get())>=5 and '@' in e6.get() and '.' in e6.get():
                    lty.config(text='Your Email id is valid ')
                else:
                    lty.config(text='Enter a Valid Email id')

                if len(e5.get())<10 or len(e5.get())>=12:
                    ltx1=Label(tk,text='Enter valid phone number',fg='red',bg='light grey',font=('Helvetica',15,'bold'))
                    ltx1.place(x=1050,y=350)
                else:
                    ltx1=Label(tk,text='you can go ahead',fg='red',bg='light grey',font=('Helvetica',15,'bold'))
                    ltx1.place(x=1050,y=350)


            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")
            l1=Label(tk,text='Store ID', font=customfont)
            l1.place(x=75,y=50)
            e1=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e1.place(x=450,y=50)
            l2=Label(tk,text='Store Name', font=customfont)
            l2.place(x=75,y=125)
            e2=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e2.place(x=450,y=125)
            l3=Label(tk,text='Store Address', font=customfont)
            l3.place(x=75,y=200)
            e3=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e3.place(x=450,y=200)

            l4=Label(tk,text='Store City', font=customfont)
            l4.place(x=75,y=275)
            e4=ttk.Combobox(tk, width=60)
            e4['values'] = ['Agra', 'Delhi', 'Noida', 'Gwalior', 'Mathura', 'Gurgaon', 'Greater Noida', 'Bhopal', 'Indore', 'Nagpur', 'Raipur','Jabalpur', 'Aurangabad', 'Ujjain', 'Amravati']
            e4.place(x=450,y=275)

            l5=Label(tk,text='Store Phone No', font=customfont)
            l5.place(x=75,y=350)
            e5=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e5.place(x=450,y=350)

            l6=Label(tk,text='Store Email ID', font=customfont)
            l6.place(x=75,y=425)
            e6=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e6.place(x=450,y=425)

            l7=Label(tk,text='Store Registration No', font=customfont)
            l7.place(x=75,y=500)
            e7=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e7.place(x=450,y=500)
            bt1=Button(tk,text='Save data', width=10, height=2, bg='blue', fg='white', font=customfont,command=savedata)
            bt1.place(x=575,y=575)
            bt2=Button(tk,text='CHECK', width=10, height=2, bg='blue', fg='white', font=customfont, command=check)
            bt2.place(x=700,y=575)

            ltx=Label(tk,text=" ",fg='red',bg='light grey',font=('Helvetica',15,'bold'))
            ltx.place(x=1050,y=50)
            lty=Label(tk,text=" ",fg='red',bg='light grey',font=('Helvetica',15,'bold'))
            lty.place(x=1050,y=425)
            tk.mainloop()
        
        def store_find():
            tk=Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('store screen find')
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select StoreID from store"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=e1.get()
                try:
                    sq="select * from store where storeid='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    e2.delete(0,100)
                    e3.delete(0,100)
                    e4.delete(0,100)
                    e5.delete(0,100)
                    e6.delete(0,100)
                    e7.delete(0,100)

                    e2.insert(0,data[1])
                    e3.insert(0,data[2])
                    e4.insert(0,data[3])
                    e5.insert(0,data[4])
                    e6.insert(0,data[5])
                    e7.insert(0,data[6])
                except:
                    messagebox.showinfo("info","data not found")
                db.close()
            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")
            l1=Label(tk,text='Store ID', font=customfont)
            l1.place(x=75,y=50)
            e1=ttk.Combobox(tk,width=80)
            filldata_combo()
            e1['values']=lt
            e1.place(x=450,y=50)



            l2=Label(tk,text='Store Name', font=customfont)
            l2.place(x=75,y=125)
            e2=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e2.place(x=450,y=125)
            l3=Label(tk,text='Store Address', font=customfont)
            l3.place(x=75,y=200)
            e3=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e3.place(x=450,y=200)
            
            l4=Label(tk,text='Store City', font=customfont)
            l4.place(x=75,y=275)
            e4=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e4.place(x=450,y=275)
            l5=Label(tk,text='Store Phone No', font=customfont)
            l5.place(x=75,y=350)
            e5=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e5.place(x=450,y=350)
            l6=Label(tk,text='Store Email ID', font=customfont)
            l6.place(x=75,y=425)
            e6=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e6.place(x=450,y=425)
            l7=Label(tk,text='Store Registration No', font=customfont)
            l7.place(x=75,y=500)
            e7=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e7.place(x=450,y=500)
            bt1=Button(tk,text='Find', width=10, height=2, bg='blue', fg='white', font=customfont,command=find)
            bt1.place(x=575,y=575)
            tk.mainloop()
        
        def store_update():
            tk=Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('store screen insert')
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select StoreID from store"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close() 


            def find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=e1.get()
                try:
                    sq="select * from store where storeid='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    e2.delete(0,100)
                    e3.delete(0,100)
                    e4.delete(0,100)
                    e5.delete(0,100)
                    e6.delete(0,100)
                    e7.delete(0,100)
                    e2.insert(0,data[1])
                    e3.insert(0,data[2])
                    e4.insert(0,data[3])
                    e5.insert(0,data[4])
                    e6.insert(0,data[5])
                    e7.insert(0,data[6])
                except:
                    messagebox.showinfo("info","data not found")
                db.close()
            
            def update():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=e1.get()
                s2=e2.get()
                s3=e3.get()
                s4=e4.get()
                s5=e5.get()
                s6=e6.get()
                s7=e7.get()
                sq="update store set Name='%s', Address='%s', City='%s', PhoneNo='%s', EmailId='%s', RegistrationNo='%s' where StoreID='%s'"%(s2,s3,s4,s5,s6,s7,s)
                cur.execute(sq)
                db.commit()
                messagebox.showinfo('Hi','Data updated')
                e2.delete(0,100)
                e3.delete(0,100)
                e4.delete(0,100)
                e5.delete(0,100)
                e6.delete(0,100)
                e7.delete(0,100)
                db.close()
            
            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")
            l1=Label(tk,text='Store ID', font=customfont)
            l1.place(x=75,y=50)
            e1=ttk.Combobox(tk,width=80)
            filldata_combo()
            e1['values']=lt
            e1.place(x=450,y=50)


            l2=Label(tk,text='Store Name', font=customfont)
            l2.place(x=75,y=200)
            e2=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e2.place(x=450,y=200)

            l3=Label(tk,text='Store Address', font=customfont)
            l3.place(x=75,y=275)
            e3=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e3.place(x=450,y=275)

            l4=Label(tk,text='Store City', font=customfont)
            l4.place(x=75,y=350)
            e4=ttk.Combobox(tk, width=60)
            e4['values'] = ['Agra', 'Delhi', 'Noida', 'Gwalior', 'Mathura', 'Gurgaon', 'Greater Noida', 'Bhopal', 'Indore', 'Nagpur', 'Raipur','Jabalpur', 'Aurangabad', 'Ujjain', 'Amravati']
            e4.place(x=450,y=350)

            l5=Label(tk,text='Store Phone No', font=customfont)
            l5.place(x=75,y=425)
            e5=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e5.place(x=450,y=425)
            l6=Label(tk,text='Store Email ID', font=customfont)
            l6.place(x=75,y=500)
            e6=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e6.place(x=450,y=500)
            l7=Label(tk,text='Store Registration No', font=customfont)
            l7.place(x=75,y=575)
            e7=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e7.place(x=450,y=575)
            bt1=Button(tk,text='Update', width=10, height=1, bg='blue', fg='white', font=customfont,command=update)
            bt1.place(x=572,y=625)
            bt2=Button(tk,text='find', width=10, height=1, bg='blue', fg='white', font=customfont, command=find)
            bt2.place(x=575,y=120)
            tk.mainloop()
        
        def store_delete():
            tk=Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('store screen insert')
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select StoreID from store"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def delete():
                try:
                    a1 = e1.get()
                    if len(a1) == 0:
                        messagebox.showerror("Wrong", "Please enter data")
                    else:
                        db = pymysql.connect(host='localhost', user='root', password='root', db='SMS')
                        cur = db.cursor()
                        sql = "select count(*) from store where StoreID='%s'" % (a1)
                        cur.execute(sql)
                        data = cur.fetchone()
                        if data[0] == 0:
                            messagebox.showerror("Wrong", "Data does not exist")
                        else:
                            sq = "delete from store where StoreID='%s'" % (a1)
                            cur.execute(sq)
                            messagebox.showinfo("Success", "Deleted")
                            db.commit()
                        db.close()
                except Exception as e:
                    messagebox.showerror("Error", str(e))
            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")
            l1=Label(tk,text='Store ID', font=customfont)
            l1.place(x=100,y=100)
            e1 = ttk.Combobox(tk, width=80)        
            filldata_combo()
            e1['values']=lt
            e1.place(x=400,y=100)


            bt1=Button(tk,text='delete', width=10, height=1, bg='red', fg='black', font=customfont,command=delete)
            bt1.place(x=450,y=200)
            tk.mainloop()
        
        def viewalldata():
            tk = Toplevel(t)
            tk.state('zoomed')  # Fix the typo here
            tk.config(bg="light grey")
            tk.title('store view all data')  # Fix the typo here
            a1=[]
            a2=[]
            a3=[]
            a4=[]
            a5=[]
            a6=[]
            a7=[]
            global i 
            i=0
            def getdata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='sms')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                sql="select * from store"
                cur.execute(sql) #It inserts the data into the 'employee' table in the database
                data=cur.fetchall()
                for res in data:
                    a1.append(res[0])
                    a2.append(res[1])
                    a3.append(res[2])
                    a4.append(res[3])
                    a5.append(res[4])
                    a6.append(res[5])
                    a7.append(res[6])
            def showfirst():
                global i
                i=0
                e1.delete(0,100)
                e2.delete(0,100)
                e3.delete(0,100)
                e4.delete(0,100)
                e5.delete(0,100)
                e6.delete(0,100)
                e7.delete(0,100)
                e1.insert(0,a1[i])
                e2.insert(0,a2[i])
                e3.insert(0,a3[i])
                e4.insert(0,a4[i])
                e5.insert(0,a5[i])
                e6.insert(0,a6[i])
                e7.insert(0,a7[i])
            def shownext():
                global i
                i=i+1
                e1.delete(0,100)
                e2.delete(0,100)
                e3.delete(0,100)
                e4.delete(0,100)
                e5.delete(0,100)
                e6.delete(0,100)
                e7.delete(0,100)
                e1.insert(0,a1[i])
                e2.insert(0,a2[i])
                e3.insert(0,a3[i])
                e4.insert(0,a4[i])
                e5.insert(0,a5[i])
                e6.insert(0,a6[i])
                e7.insert(0,a7[i])
                
            def showprev():
                global i
                i=i-1
                e1.delete(0,100)
                e2.delete(0,100)
                e3.delete(0,100)
                e4.delete(0,100)
                e5.delete(0,100)
                e6.delete(0,100)
                e7.delete(0,100)
                e1.insert(0,a1[i])
                e2.insert(0,a2[i])
                e3.insert(0,a3[i])
                e4.insert(0,a4[i])
                e5.insert(0,a5[i])
                e6.insert(0,a6[i])
                e7.insert(0,a7[i])
            def showlast():
                global i
                i=len(a1)-1
                e1.delete(0,100)
                e2.delete(0,100)
                e3.delete(0,100)
                e4.delete(0,100)
                e5.delete(0,100)
                e6.delete(0,100)
                e7.delete(0,100)
                e1.insert(0,a1[i])
                e2.insert(0,a2[i])
                e3.insert(0,a3[i])
                e4.insert(0,a4[i])
                e5.insert(0,a5[i])
                e6.insert(0,a6[i])
                e7.insert(0,a7[i])
        
            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")
            l1=Label(tk,text='Store ID', font=customfont)
            l1.place(x=75,y=50)
            e1=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e1.place(x=450,y=50)
            l2=Label(tk,text='Store Name', font=customfont)
            l2.place(x=75,y=125)
            e2=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e2.place(x=450,y=125)
            l3=Label(tk,text='Store Address', font=customfont)
            l3.place(x=75,y=200)
            e3=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e3.place(x=450,y=200)
            l4=Label(tk,text='Store City', font=customfont)
            l4.place(x=75,y=275)
            e4=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e4.place(x=450,y=275)
            l5=Label(tk,text='Store Phone No', font=customfont)
            l5.place(x=75,y=350)
            e5=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e5.place(x=450,y=350)
            l6=Label(tk,text='Store Email ID', font=customfont)
            l6.place(x=75,y=425)
            e6=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e6.place(x=450,y=425)
            l7=Label(tk,text='Store Registration No', font=customfont)
            l7.place(x=75,y=500)
            e7=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e7.place(x=450,y=500)
            bt=Button(tk,text='Preview ',font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2, bg='blue', fg='white',command=showfirst)
            bt.place(x=250,y=600)
            bt1=Button(tk,text='Next ',font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2, bg='blue', fg='white',command=shownext)
            bt1.place(x=450,y=600)
            bt2=Button(tk,text='Previous ',font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2, bg='blue', fg='white',command=showprev)
            bt2.place(x=600,y=600)
            bt3=Button(tk,text='Last',font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2, bg='blue', fg='white',command=showlast)
            bt3.place(x=800,y=600)
            getdata()
            showfirst()
            tk.mainloop()
        
        def create_table():
            tk= tkinter.Tk()
            tk.title("Store Data")
            # Connect to the MySQL database
            db = pymysql.connect(host='localhost', user='root', password='root', db='SMS')
            cur = db.cursor()
            sql = "SELECT * FROM store;"
            cur.execute(sql)
            data = cur.fetchall()
            

            # Create a Treeview widget
            table = ttk.Treeview(tk, columns=("StoreID", "Name", "Address", "City", "PhoneNO", "EmailID", "RegistrationNo"), show="headings")

            # Define column headings
            table.heading("StoreID", text="StoreID")
            table.heading("Name", text="Name")
            table.heading("Address", text="Address")
            table.heading("City", text="City")
            table.heading("PhoneNO", text="PhoneNO")
            table.heading("EmailID", text="EmailID")
            table.heading("RegistrationNo", text="RegistrationNo")

            # Define column widths
            table.column("StoreID", width=100)
            table.column("Name", width=100)
            table.column("Address", width=200)
            table.column("City", width=100)
            table.column("PhoneNO", width=100)
            table.column("EmailID", width=150)
            table.column("RegistrationNo", width=150)

            # Insert data into the table
            for row in data:
                table.insert("", "end", values=row)

            table.pack()
            tk.mainloop()
        
            
        Button(t,text='Insert',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=store_insert).place(x=600,y=100)
        Button(t,text='Find',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=store_find).place(x=600,y=175)
        Button(t,text='Update',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=store_update).place(x=600,y=250)
        Button(t,text='Delete',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=store_delete).place(x=600,y=325)
        Button(t,text='View all data',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=viewalldata).place(x=600,y=400)
        Button(t,text='Tabular form',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=create_table).place(x=600,y=475)

        t.mainloop()

   
    def Prodcat():
        t=Toplevel(root)
        t.state('zoomed')
        t.config(bg="grey")
        l1=Label(t,text="Action  to Perform",font=("Rockwell Extra Bold",35) )
        l1.place(x=390,y=10)
        
        def prodcat_insert():
            tk=Toplevel(t)
            tk.config(bg="light grey")
            tk.state('zoomed')
            tk.title('Product category save')

            def insert():
                if len(a1.get())==0 or len(b1.get())==0 or len(c1.get())==0 :
                    messagebox.showerror("Hello","Pls fill all data")
                else:
                    db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                    cur=db.cursor()
                    a=a1.get()
                    b=b1.get()
                    c=c1.get()
                    sq="insert into productcategory values('%s','%s','%s')"%(a,b,c)
                    cur.execute(sq)
                    messagebox.showinfo("hi","Data Saved")
                    a1.delete(0,"end")
                    b1.delete(0,"end")
                    c1.delete(0,"end")
                    db.commit()
                    db.close()
            def check():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                
                a2=a1.get()
                sql="select count(*) from productcategory where CategoryID='%s'"%(a2)
                cur.execute(sql)
                data=cur.fetchone()
                if data[0]==0:
                    ltx.config(text='No data found you can proceed')
                else:
                    ltx.config(text='Data already present change the id')

                
            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")
            a=Label(tk,text='Product Catagory ID', font=customfont)
            a.place(x=75,y=150)
            a1=Entry(tk,width=60, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            a1.place(x=500,y=155)
            b=Label(tk,text='Product Catagory Name', font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=60, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            b1.place(x=500,y=205)
            c=Label(tk,text='Product Catagory Description', font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=60, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            c1.place(x=500,y=255)
            bt=Button(tk,text='SAVE',command=insert,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2,width=10, height=2, bg='blue', fg='white')
            bt.place(x=400,y=350)
            bt2=Button(tk,text='CHECK', width=10, height=2, bg='blue', fg='white', font=customfont, command=check)
            bt2.place(x=600,y=350)

            ltx=Label(tk,text=" ",fg='red',bg='light grey',font=('Helvetica',12,'bold'))
            ltx.place(x=1100,y=150)
            tk.mainloop()
    
        def prodcat_delete():
            tk=Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('ProdcatDELETE')
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select CategoryID from productcategory"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def delete():
                try:
                    t1 = e1.get()
                    if len(t1) == 0:
                        messagebox.showerror("Wrong", "Please enter data")
                    else:
                        db = pymysql.connect(host='localhost', user='root', password='root', db='SMS')
                        cur = db.cursor()
                        sql = "select count(*) from productcategory where CategoryID='%s'" % (t1)
                        cur.execute(sql)
                        data = cur.fetchone()
                        if data[0] == 0:
                            messagebox.showerror("Wrong", "Data does not exist")
                        else:
                            sq = "delete from productcategory where CategoryID='%s'" % (t1)
                            cur.execute(sq)
                            messagebox.showinfo("Success", "Deleted")
                            db.commit()
                        db.close()
                except Exception as e:
                    messagebox.showerror("Error", str(e))
            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")
            a=Label(tk,text='Product Catagory ID', font=customfont)
            a.place(x=75,y=150)
            e1 = ttk.Combobox(tk, width=80)        
            filldata_combo()
            e1['values']=lt
            e1.place(x=400,y=150)
            bt=Button(tk,text='delete',font=customfont, command=delete,highlightbackground='black', highlightcolor='black', highlightthickness=2, bg='red', fg='black')
            bt.place(x=515,y=225)
            tk.mainloop()
        
        def prodcat_find():
            tk=Toplevel(t)
            tk.config(bg="light grey")
            tk.state("zoomed")
            tk.title('prodcatFIND')
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select CategoryID from productcategory"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                try:
                    sq="select * from productcategory where CategoryID='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    b1.delete(0,100)
                    c1.delete(0,100)
                    b1.insert(0,data[1])
                    c1.insert(0,data[2])
                except:    
                
                    messagebox.showinfo("info","data not found")
                db.close()

            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")
            a=Label(tk,text='Product Catagory ID', font=customfont)
            a.place(x=75,y=150)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=400,y=150)

            b=Label(tk,text='Product Catagory Name', font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=60, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            b1.place(x=400,y=200)

            c=Label(tk,text='Product Catagory Description', font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=60, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            c1.place(x=400,y=250)

            bt=Button(tk,text='FIND',font=customfont, command=find,highlightbackground='black', highlightcolor='black', highlightthickness=2,bg='blue',fg="white")
            bt.place(x=400,y=400)
            tk.mainloop()
        
        def prodcat_update():
            tk=Toplevel(t)
            tk.config(bg="light grey")
            tk.state("zoomed")
            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select CategoryID from productcategory"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                try:
                    sq="select * from productcategory where categoryId='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    b1.delete(0,100)
                    c1.delete(0,100)
                    
                    b1.insert(0,data[1])
                    c1.insert(0,data[2])
                    
                except:
                    messagebox.showinfo("info","data not found")
                db.close()
            
            def update():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                s2=b1.get()
                s3=c1.get()
                
                sq="update productcategory set  Categoryname ='%s', Description ='%s' where CategoryID ='%s'"%(s2,s3,s)
                cur.execute(sq)
                db.commit()
                messagebox.showinfo('Hi','Data updated')
                b1.delete(0,100)
                c1.delete(0,100)
                
                db.close()
            a=Label(tk,text='Product Catagory ID', font=customfont)
            a.place(x=75,y=150)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=500,y=150)

            b=Label(tk,text='Product Catagory Name', font=customfont)
            b.place(x=75,y=300)
            b1=Entry(tk,width=60, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            b1.place(x=500,y=300)

            c=Label(tk,text='Product Catagory Description', font=customfont)
            c.place(x=75,y=400)
            c1=Entry(tk,width=60, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            c1.place(x=500,y=400)

            bt=Button(tk,text='find',font=customfont,command=find, highlightbackground='black', highlightcolor='black', highlightthickness=2, bg='blue', fg='white')
            bt.place(x=515,y=225)
            bt=Button(tk,text='update',font=customfont,command=update, highlightbackground='black', highlightcolor='black', highlightthickness=2, bg='blue', fg='white')
            bt.place(x=500,y=500)

            tk.mainloop()

        def prodcat_viewalldata():
            tk=Toplevel(t)
            tk.state("zoomed")
            tk.title("View all data")
            tk.config(bg='light grey')
            
            a0=[]
            a2=[]
            a3=[]
            
            global i 
            i=0
            def getdata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='sms')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                sql="select * from productcategory"
                cur.execute(sql) #It inserts the data into the 'employee' table in the database
                data=cur.fetchall()
                print(data)
                for res in data:
                    a0.append(res[0])
                    a2.append(res[1])
                    a3.append(res[2])
            print(a0)
            def showfirst():
                global i
                i=0
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                print(i)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
            def shownext():
                global i
                i=i+1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
            def showprev():
                global i
                i=i-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
            def showlast():
                global i
                i=len(a0)-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")

            a=Label(tk,text='Product Catagory ID', font=customfont)
            a.place(x=75,y=150)
            a1=Entry(tk,width=60, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            a1.place(x=500,y=155)

            b=Label(tk,text='Product Catagory Name', font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=60, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            b1.place(x=500,y=205)

            c=Label(tk,text='Product Catagory Description', font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=60, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            c1.place(x=500,y=255)

            bt=Button(tk,text='first ',command=showfirst,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2, bg='blue', fg='white')
            bt.place(x=300,y=350)
            bt1=Button(tk,text='Next ',font=customfont,command=shownext ,highlightbackground='black', highlightcolor='black', highlightthickness=2, bg='blue', fg='white')
            bt1.place(x=500,y=350)
            bt2=Button(tk,text='Previous ',font=customfont, command=showprev,highlightbackground='black', highlightcolor='black', highlightthickness=2, bg='blue', fg='white')
            bt2.place(x=650,y=350)
            bt3=Button(tk,text='Last',font=customfont,command=showlast,highlightbackground='black', highlightcolor='black', highlightthickness=2, bg='blue', fg='white')
            bt3.place(x=850,y=350)
            getdata()
            showfirst()

            tk.mainloop()

        def create_table():
            tk= tkinter.Tk()
            tk.title("Product Category Data")
            # Connect to the MySQL database
            db = pymysql.connect(host='localhost', user='root', password='root', db='SMS')
            cur = db.cursor()
            sql = "SELECT * FROM productcategory;"
            cur.execute(sql)
            data = cur.fetchall()
            

            # Create a Treeview widget
            table = ttk.Treeview(tk, columns=("CategoryID", "Categoryname", "Description"), show="headings")

            # Define column headings
            table.heading("CategoryID", text="CategoryID")
            table.heading("Categoryname", text="Categoryname")
            table.heading("Description", text="Description")
            
            # Define column widths
            table.column("CategoryID", width=100)
            table.column("Categoryname", width=100)
            table.column("Description", width=200)
            
            # Insert data into the table
            for row in data:
                table.insert("", "end", values=row)

            table.pack()
            tk.mainloop()
       
        Button(t,text='Insert',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=prodcat_insert).place(x=550,y=100)
        Button(t,text='Find',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=prodcat_find).place(x=550,y=175)
        Button(t,text='Update',bg='blue',relief="solid",width=10,font=("Helvetica",24), fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=prodcat_update).place(x=550,y=250)
        Button(t,text='Delete',bg='blue',relief="solid",width=10,font=("Helvetica",24), fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=prodcat_delete).place(x=550,y=325)
        Button(t,text='View all data',bg='blue',relief="solid",width=10,font=("Helvetica",24), fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=prodcat_viewalldata).place(x=550,y=400)
        Button(t,text='Tabular form',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=create_table).place(x=550,y=475)

        t.mainloop()


    def Prod():
        t=Toplevel(root)
        t.state('zoomed')
        t.config(bg="grey")
        l1=Label(t,text="Action to Perform",font=("Rockwell Extra Bold",35),bg='white',fg='black' )
        l1.place(x=390,y=10)

        def productinsert():

            tk = Toplevel(t)
            tk.state('zoomed') 
            tk.config(bg="light grey") 
            tk.title('Product insert')
            
            def prod_insert():
                if len(a1.get())==0 or len(b1.get())==0 or len(c1.get())==0 or len(d1.get())==0 or len(e1.get())==0 or len(f1.get())==0 or len(g1.get())==0:
                    messagebox.showerror("Hello","Pls fill all data")
                else:
                    db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                    cur=db.cursor()
                    a=a1.get()
                    b=b1.get()
                    c=c1.get()
                    d=d1.get()
                    e=e1.get()
                    f=f1.get()
                    g=g1.get()
                    sq="insert into product values('%s','%s','%s','%s','%s','%s','%s')"%(a,b,c,d,e,f,g)
                    cur.execute(sq)
                    messagebox.showinfo("hi","Data Saved")
                    a1.delete(0,"end")
                    b1.delete(0,"end")
                    c1.delete(0,"end")
                    d1.delete(0,"end")
                    e1.delete(0,"end")
                    f1.delete(0,"end")
                    g1.delete(0,"end")
                    db.commit()
                    db.close()
            def check():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                
                a2=a1.get()
                sql="select count(*) from product where ProductID='%s'"%(a2)
                cur.execute(sql)
                data=cur.fetchone()
                if data[0]==0:
                    ltx.config(text='No data found you can proceed')
                else:
                    ltx.config(text='Data already present change the id')


            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")

            a=Label(tk,text='Product ID', font=customfont)
            a.place(x=75,y=150)
            a1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            a1.place(x=300,y=155)

            b=Label(tk,text='Catagory ID', font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Product Name', font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Unit of Sale', font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Price Per Unit', font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e1.place(x=300,y=355)

            f=Label(tk,text='Open Quantity', font=customfont)
            f.place(x=75,y=400)
            f1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            f1.place(x=300,y=405)

            g=Label(tk,text='Current Quantity', font=customfont)
            g.place(x=75,y=450)
            g1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            g1.place(x=300,y=455)

            bt=Button(tk,text='INSERT',width=10, height=2, bg='blue', fg='white', font=customfont,command=prod_insert )
            bt.place(x=400,y=525)
            bt2=Button(tk,text='CHECK', width=10, height=2, bg='blue', fg='white', font=customfont,command=check)
            bt2.place(x=550,y=525)

            ltx=Label(tk,text=" ",fg='red',bg='light grey',font=('Helvetica',12,'bold'))
            ltx.place(x=1050,y=155)

            tk.mainloop()

        def productfind():
            tk = Toplevel(t)
            tk.state('zoomed') 
            tk.config(bg="light grey")
            tk.title('Product insert')

            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")

            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select ProductID from product"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()

            def prod_find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                try:
                    sq="select * from product where ProductID='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    b1.delete(0,100)
                    c1.delete(0,100)
                    d1.delete(0,100)
                    e1.delete(0,100)
                    f1.delete(0,100)
                    g1.delete(0,100)
                    b1.insert(0,data[1])
                    c1.insert(0,data[2])
                    d1.insert(0,data[3])
                    e1.insert(0,data[4])
                    f1.insert(0,data[5])
                    g1.insert(0,data[6])
                except:
                    messagebox.showinfo("info","data not found")
                db.close()

            a=Label(tk,text='Product ID', font=customfont)
            a.place(x=75,y=150)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=300,y=150)

            b=Label(tk,text='Catagory ID', font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Product Name', font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Unit of Sale', font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Price Per Unit', font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e1.place(x=300,y=355)

            f=Label(tk,text='Open Quantity', font=customfont)
            f.place(x=75,y=400)
            f1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            f1.place(x=300,y=405)

            g=Label(tk,text='Current Quantity', font=customfont)
            g.place(x=75,y=450)
            g1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            g1.place(x=300,y=455)

            bt=Button(tk,text='FIND',bg="blue",fg="white",font=customfont,command=prod_find, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt.place(x=75,y=600)

            tk.mainloop()

        def productupdate():
            tk = Toplevel(t)
            tk.state('zoomed') 
            tk.config(bg="light grey")
            tk.title('Product insert')
            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")

            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select ProductID from product"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()

            def find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                try:
                    sq="select * from product where ProductID='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    b1.delete(0,100)
                    c1.delete(0,100)
                    d1.delete(0,100)
                    e1.delete(0,100)
                    f1.delete(0,100)
                    g1.delete(0,100)
                    b1.insert(0,data[1])
                    c1.insert(0,data[2])
                    d1.insert(0,data[3])
                    e1.insert(0,data[4])
                    f1.insert(0,data[5])
                    g1.insert(0,data[6])
                except:
                    messagebox.showinfo("info","data not found")
                db.close()
            
            def update():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                s2=b1.get()
                s3=c1.get()
                s4=d1.get()
                s5=e1.get()
                s6=f1.get()
                s7=g1.get()
                sq="update product set CategoryID='%s', Productname='%s', Unit_of_sale='%s', Price_per_unit='%s', Open_qty='%s', Current_qty='%s' where ProductID='%s'"%(s2,s3,s4,s5,s6,s7,s)
                cur.execute(sq)
                db.commit()
                messagebox.showinfo('Hi','Data updated')
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                g1.delete(0,100)
                db.close()
            a=Label(tk,text='Product ID', font=customfont)
            a.place(x=75,y=150)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=300,y=150)

            b=Label(tk,text='Catagory ID', font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Product Name', font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Unit of Sale', font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Price Per Unit', font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e1.place(x=300,y=355)

            f=Label(tk,text='Open Quantity', font=customfont)
            f.place(x=75,y=400)
            f1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            f1.place(x=300,y=405)

            g=Label(tk,text='Current Quantity', font=customfont)
            g.place(x=75,y=450)
            g1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            g1.place(x=300,y=455)

            bt=Button(tk,text='UPDATE',bg="blue", fg="white",font=customfont,command=update, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt.place(x=75,y=600)

            bt1=Button(tk,text='Find',bg="blue", fg="white",font=customfont,command=find, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt1.place(x=200,y=600)
            tk.mainloop()
        
        def productdelete():
            tk = Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('Product insert')
            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select ProductID from product"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()

            def delete():
                try:
                    t1 = a1.get()
                    if len(t1) == 0:
                        messagebox.showerror("Wrong", "Please enter data")
                    else:
                        db = pymysql.connect(host='localhost', user='root', password='root', db='SMS')
                        cur = db.cursor()
                        sql = "select count(*) from productcategory where CategoryID='%s'" % (t1)
                        cur.execute(sql)
                        data = cur.fetchone()
                        if data[0] == 0:
                            messagebox.showerror("Wrong", "Data does not exist")
                        else:
                            sq = "delete from productcategory where CategoryID='%s'" % (t1)
                            cur.execute(sq)
                            messagebox.showinfo("Success", "Deleted")
                            db.commit()
                        db.close()
                except Exception as e:
                    messagebox.showerror("Error", str(e))


            a=Label(tk,text='Product ID', font=customfont)
            a.place(x=75,y=150)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=300,y=150)


            bt=Button(tk,text='DELETE', bg="red", fg="blacks",font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2, command=delete)
            bt.place(x=300,y=250)
            tk.mainloop()

        def productviewdata():
            tk = Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('Product view data')

            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")
            a0=[]
            a2=[]
            a3=[]
            a4=[]
            a5=[]
            a6=[]
            a7=[]
            global i 
            i=0
            def getdata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='sms')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                sql="select * from product"
                cur.execute(sql) #It inserts the data into the 'employee' table in the database
                data=cur.fetchall()
                for res in data:
                    a0.append(res[0])
                    a2.append(res[1])
                    a3.append(res[2])
                    a4.append(res[3])
                    a5.append(res[4])
                    a6.append(res[5])
                    a7.append(res[6])
            def showfirst():
                global i
                i=0
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                g1.delete(0,100)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                g1.insert(0,a7[i])
            def shownext():
                global i
                i=i+1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                g1.delete(0,100)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                g1.insert(0,a7[i])
                
            def showprev():
                global i
                i=i-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                g1.delete(0,100)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                g1.insert(0,a7[i])
            def showlast():
                global i
                i=len(a0)-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                g1.delete(0,100)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                g1.insert(0,a7[i])
        

            a=Label(tk,text='Product ID', font=customfont)
            a.place(x=75,y=150)
            a1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            a1.place(x=300,y=155)

            b=Label(tk,text='Catagory ID', font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Product Name', font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Unit of Sale', font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Price Per Unit', font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e1.place(x=300,y=355)

            f=Label(tk,text='Open Quantity', font=customfont)
            f.place(x=75,y=400)
            f1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            f1.place(x=300,y=405)

            g=Label(tk,text='Current Quantity', font=customfont)
            g.place(x=75,y=450)
            g1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            g1.place(x=300,y=455)

            bt1=Button(tk,text='PREVIEW',bg="blue", fg="white",command=showfirst,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt1.place(x=100,y=550)

            bt2=Button(tk,text='NEXT',bg="blue", fg="white",font=customfont,command=shownext, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt2.place(x=350,y=550)

            bt3=Button(tk,text='PREVIOUS',bg="blue", fg="white",font=customfont,command=showprev, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt3.place(x=650,y=550)

            bt4=Button(tk,text='LAST',bg="blue", fg="white",font=customfont,command=showlast, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt4.place(x=950,y=550)

            getdata()
            showfirst()
            tk.mainloop()

        def create_table():
            tk= tkinter.Tk()
            tk.title("Store Data")
            # Connect to the MySQL database
            db = pymysql.connect(host='localhost', user='root', password='root', db='SMS')
            cur = db.cursor()
            sql = "SELECT * FROM product;"
            cur.execute(sql)
            data = cur.fetchall()
            

            # Create a Treeview widget
            table = ttk.Treeview(tk, columns=("ProductID", "CategoryID", "Productname", "Unit_of_sale", "Price_per_unit", "Open_qty", "Current_qty"), show="headings")

            # Define column headings
            table.heading("ProductID", text="ProductID")
            table.heading("CategoryID", text="CategoryID")
            table.heading("Productname", text="Productname")
            table.heading("Unit_of_sale", text="Unit_of_sale")
            table.heading("Price_per_unit", text="Price_per_unit")
            table.heading("Open_qty", text="Open_qty")
            table.heading("Current_qty", text="Current_qty")

            # Define column widths
            table.column("ProductID", width=100)
            table.column("CategoryID", width=100)
            table.column("Productname", width=200)
            table.column("Unit_of_sale", width=100)
            table.column("Price_per_unit", width=100)
            table.column("Open_qty", width=150)
            table.column("Current_qty", width=150)

            # Insert data into the table
            for row in data:
                table.insert("", "end", values=row)

            table.pack()
            tk.mainloop()
               

        Button(t,text='Insert',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=productinsert).place(x=550,y=100)
        Button(t,text='Find',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=productfind).place(x=550,y=175)
        Button(t,text='Update',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=productupdate).place(x=550,y=250)
        Button(t,text='Delete',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=productdelete).place(x=550,y=325)
        Button(t,text='View all data',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=productviewdata).place(x=550,y=400)
        Button(t,text='Tabular form',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=create_table).place(x=550,y=475)

        t.mainloop()


    def supplier():
        t=Toplevel(root)
        t.state('zoomed')
        t.config(bg="grey")
        l1=Label(t,text="Action to Perform",font=("Rockwell Extra Bold",35),bg='white',fg='black' )
        l1.place(x=390,y=10)
        
        def supplierinsert():
            tk=Toplevel(t)
            tk.config(bg="light grey")
            tk.state('zoomed')
            tk.title('supplierINSERT')

            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")

            def supp_insert():
                if len(a1.get())==0 or len(b1.get())==0 or len(c1.get())==0 or len(d1.get())==0 or len(e1.get())==0 or len(f1.get())==0 or len(g1.get())==0:
                    messagebox.showerror("Hello","Pls fill all data")
                else:
                    db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                    cur=db.cursor()
                    a=a1.get()
                    b=b1.get()
                    c=c1.get()
                    d=d1.get()
                    e=e1.get()
                    f=f1.get()
                    g=g1.get()
                    sq="insert into suppliers values('%s','%s','%s','%s','%s','%s','%s')"%(a,b,c,d,e,f,g)
                    cur.execute(sq)
                    messagebox.showinfo("hi","Data Saved")
                    a1.delete(0,"end")
                    b1.delete(0,"end")
                    c1.delete(0,"end")
                    d1.delete(0,"end")
                    e1.delete(0,"end")
                    f1.delete(0,"end")
                    g1.delete(0,"end")
                    db.commit()
                    db.close()
            def check():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                
                a2=a1.get()
                sql="select SupplierID from suppliers"
                cur.execute(sql)
                data=cur.fetchall()
                name=['']
                for x in data:
                    name.append(x[0])

                if a2 in name:
                    ltx.config(text='Enter Unique Id')
                else:
                    ltx.config(text='you can proceed')

                if len(e1.get())>=5 and '@' in e1.get() and '.' in e1.get():
                    lty.config(text='your Email id is valid ')
                else:
                    lty.config(text='Enter a Valid Email id')

                if len(f1.get())<10 or len(f1.get())>=12:
                    ltx1=Label(tk,text='enter valid phone no.',fg='red',bg='light grey',font=("Helvetica",15))
                    ltx1.place(x=1050,y=405)
                else:
                    ltx1=Label(tk,text='your phone number is valid',fg='red',bg='light grey',font=("Helvetica",15))
                    ltx1.place(x=1050,y=405)


            ltx=Label(tk,text=" ",fg='red',bg='light grey',font=("Helvetica",15))
            ltx.place(x=1050,y=150)
            lty=Label(tk,text=" ",fg='red',bg='light grey',font=("Helvetica",15))
            lty.place(x=1050,y=350)

            a=Label(tk,text='Supplier ID', font=customfont)
            a.place(x=75,y=150)
            a1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            a1.place(x=300,y=150)

            b=Label(tk,text='Supplier Name', font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Supplier Address', font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Store City', font=customfont)
            d.place(x=75,y=300)
            d1=ttk.Combobox(tk, width=60)
            d1['values'] = ['Agra', 'Delhi', 'Noida', 'Gwalior', 'Mathura', 'Gurgaon', 'Greater Noida', 'Bhopal', 'Indore', 'Nagpur', 'Raipur','Jabalpur', 'Aurangabad', 'Ujjain', 'Amravati']
            d1.place(x=300,y=300)

            e=Label(tk,text='Supplier Email ID', font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e1.place(x=300,y=355)

            f=Label(tk,text='Supplier phone No.', font=customfont)
            f.place(x=75,y=400)
            f1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            f1.place(x=300,y=405)

            g=Label(tk,text='Catagory ID', font=customfont)
            g.place(x=75,y=450)
            g1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            g1.place(x=300,y=455)

            bt=Button(tk,text='INSERT', bg="blue", fg="white",font=customfont, command=supp_insert,highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt.place(x=300,y=600)
            bt2=Button(tk,text='CHECK', width=10, height=2, bg='blue', fg='white', font=customfont,command=check)
            bt2.place(x=500,y=600)

            Button(t,text='Tabular form',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=create_table).place(x=550,y=475)


            tk.mainloop()

        def supplierfind():
            tk=Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('supplier find')
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select SupplierID from suppliers"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def supp_find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                try:
                    sq="select * from suppliers where SupplierID='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    b1.delete(0,100)
                    c1.delete(0,100)
                    d1.delete(0,100)
                    e1.delete(0,100)
                    f1.delete(0,100)
                    g1.delete(0,100)
                    b1.insert(0,data[1])
                    c1.insert(0,data[2])
                    d1.insert(0,data[3])
                    e1.insert(0,data[4])
                    f1.insert(0,data[5])
                    g1.insert(0,data[6])
                except:
                    messagebox.showinfo("info","data not found")
                db.close()

            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")
            

            a=Label(tk,text='Supplier ID', font=customfont)
            a.place(x=75,y=150)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=300,y=150)

            b=Label(tk,text='Supplier Name', font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Supplier Address', font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Supplier City', font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Supplier Email ID', font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e1.place(x=300,y=355)

            f=Label(tk,text='Supplier phone No.', font=customfont)
            f.place(x=75,y=400)
            f1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            f1.place(x=300,y=405)

            g=Label(tk,text='Catagory ID', font=customfont)
            g.place(x=75,y=450)
            g1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            g1.place(x=300,y=455)

            bt=Button(tk,text='FIND',font=customfont,bg="blue", fg="white",command=supp_find,highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt.place(x=75,y=600)

            tk.mainloop()
        
        def supplierupdate():
            tk=Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('supplier update')
            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select SupplierID from suppliers"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                try:
                    sq="select * from suppliers where SupplierID='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    b1.delete(0,100)
                    c1.delete(0,100)
                    d1.delete(0,100)
                    e1.delete(0,100)
                    f1.delete(0,100)
                    g1.delete(0,100)
                    b1.insert(0,data[1])
                    c1.insert(0,data[2])
                    d1.insert(0,data[3])
                    e1.insert(0,data[4])
                    f1.insert(0,data[5])
                    g1.insert(0,data[6])
                except:
                    messagebox.showinfo("info","data not found")
                db.close()
            
            def update():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                s2=b1.get()
                s3=c1.get()
                s4=d1.get()
                s5=e1.get()
                s6=f1.get()
                s7=g1.get()
                sq="update suppliers set Suppliername='%s', Address='%s', City='%s', Email='%s', PhoneNo='%s', categoryID='%s' where SupplierID='%s'"%(s2,s3,s4,s5,s6,s7,s)
                cur.execute(sq)
                db.commit()
                messagebox.showinfo('Hi','Data updated')
                b1.delete(0,100) 
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                g1.delete(0,100)


            a=Label(tk,text='Supplier ID', font=customfont)
            a.place(x=75,y=150)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=300,y=150)

            b=Label(tk,text='Supplier Name', font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Supplier Address', font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Store City', font=customfont)
            d.place(x=75,y=300)
            d1=ttk.Combobox(tk, width=60)
            d1['values'] = ['Agra', 'Delhi', 'Noida', 'Gwalior', 'Mathura', 'Gurgaon', 'Greater Noida', 'Bhopal', 'Indore', 'Nagpur', 'Raipur','Jabalpur', 'Aurangabad', 'Ujjain', 'Amravati']
            d1.place(x=300,y=300)

            e=Label(tk,text='Supplier Email ID', font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e1.place(x=300,y=355)

            f=Label(tk,text='Supplier phone No.', font=customfont)
            f.place(x=75,y=400)
            f1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            f1.place(x=300,y=405)

            g=Label(tk,text='Catagory ID', font=customfont)
            g.place(x=75,y=450)
            g1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            g1.place(x=300,y=455)

            bt=Button(tk,text='UPDATE',bg="blue", fg="white",font=customfont,command=update, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt.place(x=75,y=600)

            bt1=Button(tk,text='Find',bg="blue", fg="white",font=customfont, command=find,highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt1.place(x=200,y=600)

            tk.mainloop()

        def supplierdelete():
            tk=Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('supplier delete')

            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select SupplierID from suppliers"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def delete():
                try:
                    t1 = e1.get()
                    if len(t1) == 0:
                        messagebox.showerror("Wrong", "Please enter data")
                    else:
                        db = pymysql.connect(host='localhost', user='root', password='root', db='SMS')
                        cur = db.cursor()
                        sql = "select count(*) from suppliers where SupplierID='%s'" % (t1)
                        cur.execute(sql)
                        data = cur.fetchone()
                        if data[0] == 0:
                            messagebox.showerror("Wrong", "Data does not exist")
                        else:
                            sq = "delete from suppliers where SupplierID='%s'" % (t1)
                            cur.execute(sq)
                            messagebox.showinfo("Success", "Deleted")
                            db.commit()
                        db.close()
                except Exception as e:
                    messagebox.showerror("Error", str(e))


            a=Label(tk,text='Supplier ID', font=customfont)
            a.place(x=75,y=150)
            e1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            e1['values']=lt
            e1.place(x=300,y=150)

            bt=Button(tk,text='DELETE',bg="red", fg="black",font=customfont,command=delete, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt.place(x=75,y=250)

            tk.mainloop()

        def supplierviewalldata():
            tk=Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('supplier delete')

            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")
            a0=[]
            a2=[]
            a3=[]
            a4=[]
            a5=[]
            a6=[]
            a7=[]
            global i 
            i=0
            def getdata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='sms')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                sql="select * from suppliers"
                cur.execute(sql) #It inserts the data into the 'employee' table in the database
                data=cur.fetchall()
                for res in data:
                    a0.append(res[0])
                    a2.append(res[1])
                    a3.append(res[2])
                    a4.append(res[3])
                    a5.append(res[4])
                    a6.append(res[5])
                    a7.append(res[6])
            def showfirst():
                global i
                i=0
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                g1.delete(0,100)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                g1.insert(0,a7[i])
            def shownext():
                global i
                i=i+1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                g1.delete(0,100)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                g1.insert(0,a7[i])
                
            def showprev():
                global i
                i=i-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                g1.delete(0,100)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                g1.insert(0,a7[i])
            def showlast():
                global i
                i=len(a0)-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                g1.delete(0,100)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                g1.insert(0,a7[i])
            a=Label(tk,text='Supplier ID', font=customfont)
            a.place(x=75,y=150)
            a1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            a1.place(x=300,y=155)

            b=Label(tk,text='Supplier Name', font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Supplier Address', font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Supplier City', font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Supplier Email ID', font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e1.place(x=300,y=355)

            f=Label(tk,text='Supplier phone No.', font=customfont)
            f.place(x=75,y=400)
            f1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            f1.place(x=300,y=405)

            g=Label(tk,text='Catagory ID', font=customfont)
            g.place(x=75,y=450)
            g1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            g1.place(x=300,y=455)

            bt1=Button(tk,text='PREVIEW',bg="blue", fg="white",font=customfont,command=showfirst, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt1.place(x=100,y=550)

            bt2=Button(tk,text='NEXT',bg="blue", fg="white",font=customfont, command=shownext,highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt2.place(x=350,y=550)

            bt3=Button(tk,text='PREVIOUS',bg="blue", fg="white",font=customfont, command=showprev,highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt3.place(x=650,y=550)

            bt4=Button(tk,text='LAST',bg="blue", fg="white",font=customfont, command=showlast,highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt4.place(x=950,y=550)
            getdata()
            showfirst()
            tk.mainloop()

        def create_table():
            tk= tkinter.Tk()
            tk.title("Suppliers Data")
            # Connect to the MySQL database
            db = pymysql.connect(host='localhost', user='root', password='root', db='SMS')
            cur = db.cursor()
            sql = "SELECT * FROM suppliers;"
            cur.execute(sql)
            data = cur.fetchall()
            

            # Create a Treeview widget
            table = ttk.Treeview(tk, columns=("Supplier ID", "Supplier name", "Address", "City", "Email", "Phone No", "Category ID"), show="headings")

            # Define column headings
            table.heading("Supplier ID", text="Supplier ID")
            table.heading("Supplier name", text="Supplier name")
            table.heading("Address", text="Address")
            table.heading("City", text="City")
            table.heading("Email", text="Email")
            table.heading("Phone No", text="Phone No")
            table.heading("Category ID", text="Category ID")

            # Define column widths
            table.column("Supplier ID", width=100)
            table.column("Supplier name", width=100)
            table.column("Address", width=200)
            table.column("City", width=100)
            table.column("Email", width=100)
            table.column("Phone No", width=150)
            table.column("Category ID", width=150)

            # Insert data into the table
            for row in data:
                table.insert("", "end", values=row)

            table.pack()
            tk.mainloop()
               

        Button(t,text='Insert',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=supplierinsert).place(x=550,y=100)
        Button(t,text='Find',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=supplierfind).place(x=550,y=175)
        Button(t,text='Update',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=supplierupdate).place(x=550,y=250)
        Button(t,text='Delete',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=supplierdelete).place(x=550,y=325)
        Button(t,text='View all data',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=supplierviewalldata).place(x=550,y=400)
        Button(t,text='Tabular form',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=create_table).place(x=550,y=475)

        t.mainloop()


    def StockIn():
        t=Toplevel(root)
        t.state('zoomed')
        t.config(bg="grey")

        def stockininsert():
            tk=Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('stockin insert')

            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")

            def insert():
                if len(a1.get())==0 or len(b1.get())==0 or len(c1.get())==0 or len(d1.get())==0 or len(e1.get())==0 :
                    messagebox.showerror("Hello","Pls fill all data")
                else:
                    db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                    cur=db.cursor()
                    a=a1.get()
                    b=b1.get()
                    c=c1.get()
                    d=d1.get()
                    e=e1.get()
                    sq="insert into stockin values('%s','%s','%s','%s','%s')"%(a,b,c,d,e)
                    cur.execute(sq)
                    messagebox.showinfo("hi","Data Saved")
                    a1.delete(0,"end")
                    b1.delete(0,"end")
                    c1.delete(0,"end")
                    d1.delete(0,"end")
                    e1.delete(0,"end")
                    db.commit()
                    db.close()

            def check():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                
                a2=a1.get()
                sql="select count(*) from stockin where Stock_in_ID='%s'"%(a2)
                cur.execute(sql)
                data=cur.fetchone()
                if data[0]==0:
                    ltx.config(text='No data found you can proceed')
                else:
                    ltx.config(text='Data already present change the id')

            a=Label(tk,text='Stockin ID',font=customfont)
            a.place(x=75,y=150)
            a1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            a1.place(x=300,y=155)

            b=Label(tk,text='Supplier ID',font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Catagory ID',font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Quantity',font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Date In',font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            e1.place(x=300,y=355)


            bt=Button(tk,text='INSERT',bg='blue', fg='white',font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2,command=insert)
            bt.place(x=75,y=600)
            bt2=Button(tk,text='CHECK', width=10, height=2, bg='blue', fg='white', font=customfont,command=check)
            bt2.place(x=150,y=600)
            ltx=Label(tk,text=".",fg='red',bg='light grey',font=("Helvetica",15))
            ltx.place(x=1050,y=150)

            tk.mainloop()

        def stockinfind():
            tk=Toplevel(t)
            tk.state('zoomed')
            tk.title('stockin find')
            tk.config(bg="light grey")

            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select Stock_in_ID from stockin"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                try:
                    sq="select * from stockin where Stock_in_ID='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    b1.delete(0,100)
                    c1.delete(0,100)
                    d1.delete(0,100)
                    e1.delete(0,100)
                    
                    b1.insert(0,data[1])
                    c1.insert(0,data[2])
                    d1.insert(0,data[3])
                    e1.insert(0,data[4])
                    
                except:
                    messagebox.showinfo("info","data not found")
                db.close()

            a=Label(tk,text='Stockin ID',font=customfont)
            a.place(x=75,y=150)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=300,y=150)

            b=Label(tk,text='Supplier ID',font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Catagory ID',font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Quantity',font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Date In',font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            e1.place(x=300,y=355)

            bt=Button(tk,text='FIND',bg="blue", fg="white",font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2,command=find)
            bt.place(x=75,y=600)

            tk.mainloop()

        def stockinupdate():
            tk=Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('stockin update')
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select Stock_in_ID from stockin"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                try:
                    sq="select * from stockin where Stock_in_ID='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    b1.delete(0,100)
                    c1.delete(0,100)
                    d1.delete(0,100)
                    e1.delete(0,100)
                    
                    b1.insert(0,data[1])
                    c1.insert(0,data[2])
                    d1.insert(0,data[3])
                    e1.insert(0,data[4])
                    
                except:
                    messagebox.showinfo("info","data not found")
                db.close()

            def update():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                s2=b1.get()
                s3=c1.get()
                s4=d1.get()
                s5=e1.get()
                sq="update stockin set SupplierID='%s', CategoryID='%s', Qty_in='%s', Date_in='%s' where Stock_in_ID='%s'" % (s2,s3,s4,s5,s)
                cur.execute(sq)
                db.commit()
                messagebox.showinfo('Hi','Data updated')
                b1.delete(0,100) 
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                db.close()

            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")

            a=Label(tk,text='Stockin ID',font=customfont)
            a.place(x=75,y=130)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=300,y=130)

            b=Label(tk,text='Supplier ID',font=customfont)
            b.place(x=75,y=280)
            b1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            b1.place(x=300,y=280)

            c=Label(tk,text='Catagory ID',font=customfont)
            c.place(x=75,y=350)
            c1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            c1.place(x=300,y=350)

            d=Label(tk,text='Quantity ID',font=customfont)
            d.place(x=75,y=430)
            d1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            d1.place(x=300,y=430)

            e=Label(tk,text='Date In',font=customfont)
            e.place(x=75,y=500)
            e1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            e1.place(x=300,y=500)



            bt=Button(tk,text='UPDATE',bg="blue", fg="white",font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2, command=update)
            bt.place(x=75,y=600)


            bt=Button(tk,text='FIND',bg="blue", fg="white",font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2,command=find)
            bt.place(x=75,y=200)

            tk.mainloop()

        def stockindelete():
            tk=Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('stockin delete')
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select Stock_in_ID from stockin"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def delete():
                try:
                    t1 = a1.get()
                    if len(t1) == 0:
                        messagebox.showerror("Wrong", "Please enter data")
                    else:
                        db = pymysql.connect(host='localhost', user='root', password='root', db='SMS')
                        cur = db.cursor()
                        sql = "select count(*) from stockin where Stock_in_ID='%s'" % (t1)
                        cur.execute(sql)
                        data = cur.fetchone()
                        if data[0] == 0:
                            messagebox.showerror("Wrong", "Data does not exist")
                        else:
                            sq = "delete from stockin where Stock_in_ID='%s'" % (t1)
                            cur.execute(sq)
                            messagebox.showinfo("Success", "Deleted")
                            db.commit()
                        db.close()
                except Exception as e:
                    messagebox.showerror("Error", str(e))
                
            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")

            a=Label(tk,text='Stockin ID',font=customfont)
            a.place(x=75,y=150)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=300,y=150)

            bt=Button(tk,text='DELETE',bg="red", fg="black",font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2, command=delete)
            bt.place(x=75,y=300)


            tk.mainloop()
        
        def stockinviewalldata():
            tk=Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('stockin delete')


            a0=[]
            a2=[]
            a3=[]
            a4=[]
            a5=[]
            global i 
            i=0
            def getdata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='sms')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                sql="select * from stockin"
                cur.execute(sql) #It inserts the data into the 'employee' table in the database
                data=cur.fetchall()
                for res in data:
                    a0.append(res[0])
                    a2.append(res[1])
                    a3.append(res[2])
                    a4.append(res[3])
                    a5.append(res[4])
                    
            def showfirst():
                global i
                i=0
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                
            def shownext():
                global i
                i=i+1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                
                
            def showprev():
                global i
                i=i-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                
            def showlast():
                global i
                i=len(a0)-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                
            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")

            a=Label(tk,text='Stockin ID',font=customfont)
            a.place(x=75,y=150)
            a1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            a1.place(x=300,y=155)

            b=Label(tk,text='Supplier ID',font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Catagory ID',font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Quantity',font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Date In',font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            e1.place(x=300,y=355)


            bt1=Button(tk,text='PREVIEW',bg="blue", fg="white",font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2, command=showfirst)
            bt1.place(x=200,y=600)

            bt2=Button(tk,text='NEXT',bg="blue", fg="white",font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2, command=shownext)
            bt2.place(x=400,y=600)

            bt3=Button(tk,text='PREVIOUS',bg="blue", fg="white",font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2, command=showprev)
            bt3.place(x=600,y=600)

            bt4=Button(tk,text='LAST',bg="blue", fg="white",font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2, command=showlast)
            bt4.place(x=800,y=600)
            getdata()
            showfirst()     

            tk.mainloop()

        def create_table():
            tk= tkinter.Tk()
            tk.title("Stock In Data")
            # Connect to the MySQL database
            db = pymysql.connect(host='localhost', user='root', password='root', db='SMS')
            cur = db.cursor()
            sql = "SELECT * FROM stockin;"
            cur.execute(sql)
            data = cur.fetchall()
            

            # Create a Treeview widget
            table = ttk.Treeview(tk, columns=("Stock_in_ID", "Supplier ID", "Category ID", "Qty_in", "Date_in"), show="headings")

            # Define column headings
            table.heading("Stock_in_ID", text="Stock_in_ID")
            table.heading("Supplier ID", text="Supplier ID")
            table.heading("Category ID", text="Category ID")
            table.heading("Qty_in", text="Qty_in")
            table.heading("Date_in", text="Date_in")
            

            # Define column widths
            table.column("Stock_in_ID", width=100)
            table.column("Supplier ID", width=100)
            table.column("Category ID", width=200)
            table.column("Qty_in", width=100)
            table.column("Date_in", width=100)
            

            # Insert data into the table
            for row in data:
                table.insert("", "end", values=row)

            table.pack()
            tk.mainloop()

        l1=Label(t,text="Action to Perform",font=("Rockwell Extra Bold",35),bg='white',fg='black' )
        l1.place(x=390,y=10)
        Button(t,text='Insert',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=stockininsert).place(x=550,y=100)
        Button(t,text='Find',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=stockinfind).place(x=550,y=175)
        Button(t,text='Update',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=stockinupdate).place(x=550,y=250)
        Button(t,text='Delete',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5, command=stockindelete).place(x=550,y=325)
        Button(t,text='View all data',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=stockinviewalldata).place(x=550,y=400)
        Button(t,text='Tabular form',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=create_table).place(x=550,y=475)

        t.mainloop()


    def Customer():
        t=Toplevel(root)
        t.state('zoomed')
        t.config(bg="grey")
        l1=Label(t,text="Action to Perform",font=("Rockwell Extra Bold",35),bg='white',fg='black' )
        l1.place(x=390,y=10)

        def customerinsert():
            tk=Toplevel(t)
            tk.title('customerINSERT')
            tk.config(bg="light grey")
            tk.state('zoomed')
            def cust_insert():
                if len(a1.get())==0 or len(b1.get())==0 or len(c1.get())==0 or len(d1.get())==0 or len(e1.get())==0 :
                    messagebox.showerror("Hello","Pls fill all data")
                else:
                    db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                    cur=db.cursor()
                    a=a1.get()
                    b=b1.get()
                    c=c1.get()
                    d=d1.get()
                    e=e1.get()
                    sq="insert into customers values('%s','%s','%s','%s','%s')"%(a,b,c,d,e)
                    cur.execute(sq)
                    messagebox.showinfo("hi","Data Saved")
                    a1.delete(0,"end")
                    b1.delete(0,"end")
                    c1.delete(0,"end")
                    d1.delete(0,"end")
                    e1.delete(0,"end")
                    db.commit()
                    db.close()

            def check():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                
                a2=a1.get()
                sql="select CustomerID from customers"
                cur.execute(sql)
                data=cur.fetchall()
                name=['']
                for x in data:
                    name.append(x[0])

                if a2 in name:
                    ltx.config(text='Enter Unique Id')
                else:
                    ltx.config(text='you can proceed')

                if len(d1.get())>=5 and '@' in d1.get() and '.' in d1.get():
                    lty.config(text='your Email id is valid ')
                else:
                    lty.config(text='Enter a Valid Email id')

                if len(e1.get())<10 or len(e1.get())>=12:
                    ltx1=Label(tk,text='enter valid phone no.',fg='red',bg='light grey',font=("Helvetica",15))
                    ltx1.place(x=1050,y=355)
                else:
                    ltx1=Label(tk,text='your phone number is valid',fg='red',bg='light grey',font=("Helvetica",15))
                    ltx1.place(x=1050,y=355)

            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")

            ltx=Label(tk,text=" ",fg='red',bg='light grey',font=("Helvetica",15))
            ltx.place(x=1050,y=155)
            lty=Label(tk,text=" ",fg='red',bg='light grey',font=("Helvetica",15))
            lty.place(x=1050,y=305)
            
            a=Label(tk,text='Customer ID', font=customfont)
            a.place(x=75,y=150)
            a1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            a1.place(x=300,y=155)

            b=Label(tk,text='Customer Name', font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Customer Address', font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Customer Email ID', font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Customer Phone No.', font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e1.place(x=300,y=355)

            bt=Button(tk,text='INSERT',bg="blue", fg="white",command=cust_insert,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt.place(x=300,y=500)
            bt2=Button(tk,text='CHECK', width=10, height=2, bg='blue', fg='white', font=customfont, command=check)
            bt2.place(x=500,y=500)

            
            tk.mainloop()

        def customerfind():
            tk=Toplevel(t)
            tk.title('customer find')
            tk.config(bg="grey")
            tk.state('zoomed')
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select CustomerID from customers"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def cust_find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                try:
                    sq="select * from customers where CustomerID='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    b1.delete(0,100)
                    c1.delete(0,100)
                    d1.delete(0,100)
                    e1.delete(0,100)
                    
                    b1.insert(0,data[1])
                    c1.insert(0,data[2])
                    d1.insert(0,data[3])
                    e1.insert(0,data[4])
                except:
                    messagebox.showinfo("info","data not found")
                db.close()


            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")

            a=Label(tk,text='Customer ID',font=customfont)
            a.place(x=75,y=150)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=300,y=150)

            b=Label(tk,text='Customer Name',font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Customer Address',font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Email ID',font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Phone No.',font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            e1.place(x=300,y=355)



            bt=Button(tk,text='FIND',bg="blue", fg="white",command=cust_find,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=75,y=600)


            tk.mainloop()

        def customerupdate():
            tk=Toplevel(t)
            tk.title('customerINSERT')
            tk.config(bg="grey")
            tk.state('zoomed')
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select CustomerID from customers"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def cust_find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                try:
                    sq="select * from customers where CustomerID='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    b1.delete(0,100)
                    c1.delete(0,100)
                    d1.delete(0,100)
                    e1.delete(0,100)
                    b1.insert(0,data[1])
                    c1.insert(0,data[2])
                    d1.insert(0,data[3])
                    e1.insert(0,data[4])
                except:
                    messagebox.showinfo("info","data not found")
                db.close()
            def cust_update():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                s2=b1.get()
                s3=c1.get()
                s4=d1.get()
                s5=e1.get()
                
                sq="update customers set Customername='%s', Address ='%s',  EmailID='%s',PhoneNO ='%s' where CustomerID='%s'"%(s2,s3,s4,s5,s)
                cur.execute(sq)
                db.commit()
                messagebox.showinfo('Hi','Data updated')
                b1.delete(0,100) 
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                db.close()



            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")
            
            a=Label(tk,text='Customer ID',font=customfont)
            a.place(x=75,y=130)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=300,y=150)
            
            b=Label(tk,text='Customer Name',font=customfont)
            b.place(x=75,y=280)
            b1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            b1.place(x=300,y=280)
            
            c=Label(tk,text='Customer Address',font=customfont)
            c.place(x=75,y=350)
            c1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            c1.place(x=300,y=350)
            
            d=Label(tk,text='Email ID',font=customfont)
            d.place(x=75,y=430)
            d1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            d1.place(x=300,y=430)
            
            e=Label(tk,text='Phone No.',font=customfont)
            e.place(x=75,y=500)
            e1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            e1.place(x=300,y=500)
            
            
            
            bt=Button(tk,text='UPDATE',bg="blue", fg="white",command=cust_update,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=75,y=600)
            
            
            bt=Button(tk,text='FIND',bg="blue", fg="white",command=cust_find,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=75,y=200)
            
            tk.mainloop()

        def customerdelete():
            tk=Toplevel(t)
            tk.title('customerINSERT')
            tk.config(bg="grey")
            tk.state('zoomed')

            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")

            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select CustomerID from customers"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def delete():
                try:
                    t1 = a1.get()
                    if len(t1) == 0:
                        messagebox.showerror("Wrong", "Please enter data")
                    else:
                        db = pymysql.connect(host='localhost', user='root', password='root', db='SMS')
                        cur = db.cursor()
                        sql = "select count(*) from customers where CustomerID='%s'" % (t1)
                        cur.execute(sql)
                        data = cur.fetchone()
                        if data[0] == 0:
                            messagebox.showerror("Wrong", "Data does not exist")
                        else:
                            sq = "delete from customers where CustomerID='%s'" % (t1)
                            cur.execute(sq)
                            messagebox.showinfo("Success", "Deleted")
                            db.commit()
                        db.close()
                except Exception as e:
                    messagebox.showerror("Error", str(e))

            a=Label(tk,text='Customer ID',font=customfont)
            a.place(x=75,y=150)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=300,y=150)

            bt=Button(tk,text='DELETE',bg="red", fg="black",command=delete,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=75,y=300)


            tk.mainloop()

        def customerviewalldata():
            tk=Toplevel(t)
            tk.title('customerINSERT')
            tk.config(bg="grey")
            tk.state('zoomed')

            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")
            a0=[]
            a2=[]
            a3=[]
            a4=[]
            a5=[]
            
            
            global i 
            i=0
            def getdata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='sms')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                sql="select * from customers"
                cur.execute(sql) #It inserts the data into the 'employee' table in the database
                data=cur.fetchall()
                for res in data:
                    a0.append(res[0])
                    a2.append(res[1])
                    a3.append(res[2])
                    a4.append(res[3])
                    a5.append(res[4])
                    
                
            def showfirst():
                global i
                i=0
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                
                
            def shownext():
                global i
                i=i+1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                
            
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                
                
                
            def showprev():
                global i
                i=i-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                
                
            def showlast():
                global i
                i=len(a0)-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                
                

            a=Label(tk,text='Customer ID',font=customfont)
            a.place(x=75,y=150)
            a1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            a1.place(x=300,y=155)

            b=Label(tk,text='Customer Name',font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Customer Address',font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Email ID',font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Phone No.',font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            e1.place(x=300,y=355)


            bt=Button(tk,text='PREVIEW',bg="blue", fg="white",command=showfirst,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=200,y=600)

            bt=Button(tk,text='NEXT',bg="blue", fg="white",command=shownext,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=400,y=600)

            bt=Button(tk,text='PREVIOUS',bg="blue", fg="white",command=showprev,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=600,y=600)

            bt=Button(tk,text='LAST',bg="blue", fg="white",command=showlast,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=800,y=600)

            getdata()
            showfirst()
            tk.mainloop()

        def create_table():
            tk= tkinter.Tk()
            tk.title("Customers Data")
            # Connect to the MySQL database
            db = pymysql.connect(host='localhost', user='root', password='root', db='SMS')
            cur = db.cursor()
            sql = "SELECT * FROM customers;"
            cur.execute(sql)
            data = cur.fetchall()
            

            # Create a Treeview widget
            table = ttk.Treeview(tk, columns=("Customer ID", "Customer Name", "Address", "Email", "Phone No"), show="headings")

            # Define column headings
            table.heading("Customer ID", text="Customer ID")
            table.heading("Customer Name", text="Customer Name")
            table.heading("Address", text="Address")
            table.heading("Email", text="Email")
            table.heading("Phone No", text="Phone No")

            # Define column widths
            table.column("Customer ID", width=100)
            table.column("Customer Name", width=100)
            table.column("Address", width=200)
            table.column("Email", width=100)
            table.column("Phone No", width=150)

            # Insert data into the table
            for row in data:
                table.insert("", "end", values=row)

            table.pack()
            tk.mainloop()



        Button(t,text='Insert',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=customerinsert).place(x=550,y=100)
        Button(t,text='Find',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=customerfind).place(x=550,y=175)
        Button(t,text='Update',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=customerupdate).place(x=550,y=250)
        Button(t,text='Delete',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=customerdelete).place(x=550,y=325)
        Button(t,text='View all data',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=customerviewalldata).place(x=550,y=400)
        Button(t,text='Tabular form',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=create_table).place(x=550,y=475)
        
        t.mainloop()


    def Order():
        t=Toplevel(root)
        t.state('zoomed')
        t.config(bg="grey")
        
        def orderinsert():
            tk=Toplevel(t)
            tk.config(bg="light grey")
            tk.title('Order Insert')
            tk.state('zoomed')

            def ord_insert():
                if len(a1.get())==0 or len(b1.get())==0 or len(c1.get())==0 or len(d1.get())==0 or len(e1.get())==0 or len(f1.get())==0:
                    messagebox.showerror("Hello","Pls fill all data")
                else:
                    db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                    cur=db.cursor()
                    a=a1.get()
                    b=b1.get()
                    c=c1.get()
                    d=d1.get()
                    e=e1.get()
                    f=f1.get()
                    sq="insert into orders values('%s','%s','%s','%s','%s','%s')"%(a,b,c,d,e,f)
                    cur.execute(sq)
                    messagebox.showinfo("hi","Data Saved")
                    a1.delete(0,"end")
                    b1.delete(0,"end")
                    c1.delete(0,"end")
                    d1.delete(0,"end")
                    e1.delete(0,"end")
                    f1.delete(0,"end")
                    db.commit()
                    db.close()
            def check():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                
                a2=a1.get()
                sql="select count(*) from orders where OrderID='%s'"%(a2)
                cur.execute(sql)
                data=cur.fetchone()
                if data[0]==0:
                    ltx.config(text='No data found you can proceed')
                else:
                    ltx.config(text='Data already present change the id')

            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")
            a=Label(tk,text='Order ID',font=customfont)
            a.place(x=75,y=150)
            a1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            a1.place(x=300,y=155)

            b=Label(tk,text='Customer ID',font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Catagory ID',font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Product ID',font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Date Of Order',font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            e1.place(x=300,y=355)

            f=Label(tk,text='Quantity',font=customfont)
            f.place(x=75,y=400)
            f1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            f1.place(x=300,y=405)

            bt=Button(tk,text='INSERT',bg='blue', fg='white',font=customfont,command=ord_insert,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=75,y=600)
            bt2=Button(tk,text='CHECK', width=10, height=2, bg='blue', fg='white', font=customfont,command=check)
            bt2.place(x=150,y=600)

            ltx=Label(tk,text=".",fg='red',bg='grey',font=("Helvetica",15))
            ltx.place(x=1050,y=150)


            tk.mainloop()

        def orderfind():
            tk=Toplevel(t)
            tk.config(bg="light grey")
            tk.title('Order Find')
            tk.state('zoomed')
            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select OrderID from orders"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()

            def ord_find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                try:
                    sq="select * from orders where OrderID='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    b1.delete(0,100)
                    c1.delete(0,100)
                    d1.delete(0,100)
                    e1.delete(0,100)
                    f1.delete(0,100)
                    
                    b1.insert(0,data[1])
                    c1.insert(0,data[2])
                    d1.insert(0,data[3])
                    e1.insert(0,data[4])
                    f1.insert(0,data[5])
                except:
                    messagebox.showinfo("info","data not found")
                db.close()

            a=Label(tk,text='Order ID',font=customfont)
            a.place(x=75,y=150)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=300,y=150)

            b=Label(tk,text='Customer ID',font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Catagory ID',font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Product ID',font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Date Of Order',font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            e1.place(x=300,y=355)

            f=Label(tk,text='Quantity',font=customfont)
            f.place(x=75,y=400)
            f1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            f1.place(x=300,y=405)

            bt=Button(tk,text='FIND',bg='blue', fg='white',font=customfont,command=ord_find,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=75,y=600)


            tk.mainloop()

        def orderupdate():
            tk=Toplevel(t)
            tk.config(bg="light grey")
            tk.title('Order update')
            tk.state('zoomed')
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select OrderID from orders"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def update():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                s2=b1.get()
                s3=c1.get()
                s4=d1.get()
                s5=e1.get()
                s6=f1.get()
                sq="update orders set CustomerID='%s',CategoryID='%s',ProductID='%s', Date_of_order ='%s', Qty='%s' where orderID='%s'"%(s2,s3,s4,s5,s6,s)
                cur.execute(sq)
                db.commit()
                messagebox.showinfo('Hi','Data updated')
                b1.delete(0,100) 
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                db.close()      
                
            def ord_find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                try:
                    sq="select * from orders where OrderID='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    b1.delete(0,100)
                    c1.delete(0,100)
                    d1.delete(0,100)
                    e1.delete(0,100)
                    f1.delete(0,100)
                    b1.insert(0,data[1])
                    c1.insert(0,data[2])
                    d1.insert(0,data[3])
                    e1.insert(0,data[4])
                    f1.insert(0,data[5])
                except:
                    messagebox.showinfo("info","data not found")
                db.close()
            
            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")
            a=Label(tk,text='Order ID',font=customfont)
            a.place(x=75,y=130)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=300,y=150)

            b=Label(tk,text='Customer ID',font=customfont)
            b.place(x=75,y=280)
            b1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            b1.place(x=300,y=280)

            c=Label(tk,text='Catagory ID',font=customfont)
            c.place(x=75,y=350)
            c1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            c1.place(x=300,y=350)

            d=Label(tk,text='Product ID',font=customfont)
            d.place(x=75,y=430)
            d1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            d1.place(x=300,y=430)

            e=Label(tk,text='Date Of Order',font=customfont)
            e.place(x=75,y=500)
            e1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            e1.place(x=300,y=500)

            f=Label(tk,text='Quantity',font=customfont)
            f.place(x=75,y=570)
            f1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            f1.place(x=300,y=570)

            bt=Button(tk,text='UPDATE',bg='blue', fg='white',command=update,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=75,y=650)


            bt=Button(tk,text='FIND',bg='blue', fg='white',font=customfont,command=ord_find,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=75,y=200)

            tk.mainloop()

        def orderdelete():
            tk=Toplevel(t)
            tk.config(bg="light grey")
            tk.title('Order delete')
            tk.state('zoomed')
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select OrderID from orders"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def delete():
                try:
                    t1 = a1.get()
                    if len(t1) == 0:
                        messagebox.showerror("Wrong", "Please enter data")
                    else:
                        db = pymysql.connect(host='localhost', user='root', password='root', db='SMS')
                        cur = db.cursor()
                        sql = "select count(*) from orders where OrderID='%s'" % (t1)
                        cur.execute(sql)
                        data = cur.fetchone()
                        if data[0] == 0:
                            messagebox.showerror("Wrong", "Data does not exist")
                        else:
                            sq = "delete from orders where OrderID='%s'" % (t1)
                            cur.execute(sq)
                            messagebox.showinfo("Success", "Deleted")
                            db.commit()
                        db.close()
                except Exception as e:
                    messagebox.showerror("Error", str(e))

            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")

            a=Label(tk,text='Order ID',font=customfont)
            a.place(x=75,y=150)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=300,y=150)

            bt=Button(tk,text='DELETE',bg='red', fg='black',command=delete,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=75,y=300)


            tk.mainloop()

        def orderviewalldata():
            tk=Toplevel(t)
            tk.config(bg="light grey")
            tk.title('Order view all data')
            tk.state('zoomed')

            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")
            a0=[]
            a2=[]
            a3=[]
            a4=[]
            a5=[]
            a6=[]
            
            global i 
            i=0
            def getdata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='sms')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                sql="select * from orders"
                cur.execute(sql) #It inserts the data into the 'employee' table in the database
                data=cur.fetchall()
                for res in data:
                    a0.append(res[0])
                    a2.append(res[1])
                    a3.append(res[2])
                    a4.append(res[3])
                    a5.append(res[4])
                    a6.append(res[5])
                
            def showfirst():
                global i
                i=0
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                
            def shownext():
                global i
                i=i+1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
            
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                
                
            def showprev():
                global i
                i=i-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                
            def showlast():
                global i
                i=len(a0)-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                
        

            a=Label(tk,text='Order ID',font=customfont)
            a.place(x=75,y=150)
            a1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            a1.place(x=300,y=155)

            b=Label(tk,text='Customer ID',font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Catagory ID',font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Product ID',font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Date Of Order',font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            e1.place(x=300,y=355)

            f=Label(tk,text='Quantity',font=customfont)
            f.place(x=75,y=400)
            f1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            f1.place(x=300,y=405)

            bt=Button(tk,text='PREVIEW',bg='blue', fg='white',command=showfirst,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=200,y=600)

            bt=Button(tk,text='NEXT',bg='blue', fg='white',command=shownext,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=400,y=600)

            bt=Button(tk,text='PREVIOUS',bg='blue', fg='white',command=showprev,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=650,y=600)

            bt=Button(tk,text='LAST',bg='blue', fg='white',command=showlast,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=900,y=600)

            getdata()
            showfirst()
            tk.mainloop()

        def create_table():
            tk= tkinter.Tk()
            tk.title("Orders Data")
            # Connect to the MySQL database
            db = pymysql.connect(host='localhost', user='root', password='root', db='SMS')
            cur = db.cursor()
            sql = "SELECT * FROM orders;"
            cur.execute(sql)
            data = cur.fetchall()
            

            # Create a Treeview widget
            table = ttk.Treeview(tk, columns=("Order ID", "Customer ID", "Category ID", "Product ID", "Date_of_order", "Qty"), show="headings")

            # Define column headings
            table.heading("Order ID", text="Order ID")
            table.heading("Customer ID", text="Customer ID")
            table.heading("Category ID", text="Category ID")
            table.heading("Product ID", text="Product ID")
            table.heading("Date_of_order", text="Date_of_order")
            table.heading("Qty", text="Qty")

            # Define column widths
            table.column("Order ID", width=100)
            table.column("Customer ID", width=100)
            table.column("Category ID", width=200)
            table.column("Product ID", width=100)
            table.column("Date_of_order", width=150)
            table.column("Qty", width=150)

            # Insert data into the table
            for row in data:
                table.insert("", "end", values=row)

            table.pack()
            tk.mainloop()

        

        l1=Label(t,text="Action to Perform",font=("Rockwell Extra Bold",35),bg='white',fg='black' )
        l1.place(x=390,y=10)
        Button(t,text='Insert',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=orderinsert).place(x=550,y=100)
        Button(t,text='Find',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=orderfind).place(x=550,y=175)
        Button(t,text='Update',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=orderupdate).place(x=550,y=250)
        Button(t,text='Delete',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=orderdelete).place(x=550,y=325)
        Button(t,text='View all data',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=orderviewalldata).place(x=550,y=400)
        Button(t,text='Tabular form',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=create_table).place(x=550,y=475)

        t.mainloop()

    def Bill():
        t=Toplevel(root)
        t.state('zoomed')
        t.config(bg="grey")
        l1=Label(t,text="Action to Perform",font=("Rockwell Extra Bold",35),bg='white',fg='black' )
        l1.place(x=400,y=10)
        
        def billinsert():
            tk= Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('Bill Insert')
            
            def insert():
                if len(a1.get())==0 or len(b1.get())==0 or len(c1.get())==0 or len(d1.get())==0:
                    messagebox.showerror("Hello","Pls fill all data")
                else:
                    db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                    cur=db.cursor()
                    a=a1.get()
                    b=b1.get()
                    c=c1.get()
                    d=d1.get()
                    sq="insert into bill values('%s','%s','%s','%s')"%(a,b,c,d)
                    cur.execute(sq)
                    messagebox.showinfo("hi","Data Saved")
                    a1.delete(0,"end")
                    b1.delete(0,"end")
                    c1.delete(0,"end")
                    d1.delete(0,"end")
                    db.commit()
                    db.close()
            def check():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                
                a2=a1.get()
                sql="select count(*) from bill where CustomerID='%s'"%(a2)
                cur.execute(sql)
                data=cur.fetchone()
                if data[0]==0:
                    ltx.config(text='No data found you can proceed')
                else:
                    ltx.config(text='Data already present change the id')
            

            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")

            a=Label(tk,text='Customer ID',font=customfont)
            a.place(x=75,y=150)
            a1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            a1.place(x=300,y=155)

            b=Label(tk,text='Order ID',font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Catagory ID',font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Amount',font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            d1.place(x=300,y=305)

            bt=Button(tk,text='INSERT',bg='blue', fg='white',font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2, command=insert)
            bt.place(x=75,y=600)
            bt2=Button(tk,text='CHECK', width=10, height=2, bg='blue', fg='white', font=customfont,command=check)
            bt2.place(x=150,y=600)

            ltx=Label(tk,text=".",fg='red',bg='grey',font=("Helvetica",15))
            ltx.place(x=1050,y=150)

            tk.mainloop()
        
        def billfind():
            tk= Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('Bill find')
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select CustomerID from bill"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                try:
                    sq="select * from bill where CustomerID='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    b1.delete(0,100)
                    c1.delete(0,100)
                    d1.delete(0,100)
                    
                    b1.insert(0,data[1])
                    c1.insert(0,data[2])
                    d1.insert(0,data[3])
                
                except:
                    messagebox.showinfo("info","data not found")
                db.close()

            
            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")

            a=Label(tk,text='Customer ID',font=customfont)
            a.place(x=75,y=150)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=300,y=150)

            b=Label(tk,text='Order ID',font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Catagory ID',font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Amount',font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            d1.place(x=300,y=305)

            bt=Button(tk,text='FIND',bg='blue', fg='white',font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2, command=find)
            bt.place(x=75,y=600)


            tk.mainloop()

        def billupdate():
            tk= Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('Bill update')
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select CustomerID from bill"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                try:
                    sq="select * from bill where CustomerID='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    a1.delete(0,100)
                    b1.delete(0,100)
                    c1.delete(0,100)
                    d1.delete(0,100)
                    a1.insert(0,data[0])
                    b1.insert(0,data[1])
                    c1.insert(0,data[2])
                    d1.insert(0,data[3])
                
                except:
                    messagebox.showinfo("info","data not found")
                db.close()

            def updatedata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                s2=b1.get()
                s3=c1.get()
                s4=d1.get()
                sq="update bill set OrderID='%s',CategoryID='%s', Amount ='%s'where CustomerID='%s'"%(s2,s3,s4,s)
                cur.execute(sq)
                db.commit()
                messagebox.showinfo('Hi','Data updated')
                a1.delete(0,100)
                b1.delete(0,100) 
                c1.delete(0,100)
                d1.delete(0,100)
                db.close()


            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")

            a=Label(tk,text='Customer ID',font=customfont)
            a.place(x=75,y=150)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=300,y=150)

            b=Label(tk,text='Order ID',font=customfont)
            b.place(x=75,y=355)
            b1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            b1.place(x=300,y=355)

            c=Label(tk,text='Catagory ID',font=customfont)
            c.place(x=75,y=455)
            c1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            c1.place(x=300,y=455)

            d=Label(tk,text='Amount',font=customfont)
            d.place(x=75,y=555)
            d1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            d1.place(x=300,y=555)

            bt=Button(tk,text='UPDATE',bg='blue', fg='white',font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2,command=updatedata)
            bt.place(x=300,y=650)

            bt1=Button(tk,text='FIND',bg='blue', fg='white',font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2, command=find)
            bt1.place(x=300,y=250)

            tk.mainloop()

        def billdelete():
            tk= Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('Bill delete')
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select CustomerID from bill"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def delete():
                try:
                    t1 = a1.get()
                    if len(t1) == 0:
                        messagebox.showerror("Wrong", "Please enter data")
                    else:
                        db = pymysql.connect(host='localhost', user='root', password='root', db='SMS')
                        cur = db.cursor()
                        sql = "select count(*) from bill where CustomerID='%s'" % (t1)
                        cur.execute(sql)
                        data = cur.fetchone()
                        if data[0] == 0:
                            messagebox.showerror("Wrong", "Data does not exist")
                        else:
                            sq = "delete from bill where CustomerID='%s'" % (t1)
                            cur.execute(sq)
                            messagebox.showinfo("Success", "Deleted")
                            db.commit()
                        db.close()
                except Exception as e:
                    messagebox.showerror("Error", str(e))
            
            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")

            a=Label(tk,text='Customer ID',font=customfont)
            a.place(x=75,y=150)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=300,y=150)

            bt=Button(tk,text='DELETE',bg='red', fg='black',font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2, command=delete)
            bt.place(x=300,y=300)


            tk.mainloop()

        def billviewalldata():
            tk= Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('Bill view all data')


            a0=[]
            a2=[]
            a3=[]
            a4=[]
            a5=[]
            a6=[]
            
            global i 
            i=0
            def getdata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                sql="select * from bill"
                cur.execute(sql) #It inserts the data into the 'employee' table in the database
                data=cur.fetchall()
                for res in data:
                    a0.append(res[0])
                    a2.append(res[1])
                    a3.append(res[2])
                    a4.append(res[3])
                    
                
            def showfirst():
                global i
                i=0
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                
                
            def shownext():
                global i
                i=i+1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                
            
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                
                
                
            def showprev():
                global i
                i=i-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                
                
            def showlast():
                global i
                i=len(a0)-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
        
            
            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")

            a=Label(tk,text='Customer ID',font=customfont)
            a.place(x=75,y=150)
            a1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            a1.place(x=300,y=155)

            b=Label(tk,text='Order ID',font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Catagory ID',font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Amount',font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            d1.place(x=300,y=305)

            bt=Button(tk,text='PREVIEW',bg='blue', fg='white',font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2, command=showfirst)
            bt.place(x=200,y=550)

            bt=Button(tk,text='NEXT',bg='blue', fg='white',font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2, command=shownext)
            bt.place(x=400,y=550)

            bt=Button(tk,text='PREVIOUS',bg='blue', fg='white',font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2, command=showprev)
            bt.place(x=600,y=550)

            bt=Button(tk,text='LAST',bg='blue', fg='white',font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2, command=showlast)
            bt.place(x=800,y=550)

            getdata()
            showfirst()

            tk.mainloop()
            
        def create_table():
            tk= tkinter.Tk()
            tk.title("Bill Data")
            # Connect to the MySQL database
            db = pymysql.connect(host='localhost', user='root', password='root', db='SMS')
            cur = db.cursor()
            sql = "SELECT * FROM bill;"
            cur.execute(sql)
            data = cur.fetchall()
            

            # Create a Treeview widget
            table = ttk.Treeview(tk, columns=("Customer ID", "Order ID", "Category ID", "Amount"), show="headings")

            # Define column headings
            table.heading("Customer ID", text="Supplier ID")
            table.heading("Order ID", text="Supplier name")
            table.heading("Category ID", text="Address")
            table.heading("Amount", text="City")
            

            # Define column widths
            table.column("Customer ID", width=100)
            table.column("Order ID", width=100)
            table.column("Category ID", width=200)
            table.column("Amount", width=100)
            
            # Insert data into the table
            for row in data:
                table.insert("", "end", values=row)

            table.pack()
            tk.mainloop()

        Button(t,text='Insert',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5, command=billinsert).place(x=550,y=100)
        Button(t,text='Find',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=billfind).place(x=550,y=175)
        Button(t,text='Update',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5, command=billupdate).place(x=550,y=250)
        Button(t,text='Delete',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=billdelete).place(x=550,y=325)
        Button(t,text='View all data',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=billviewalldata).place(x=550,y=400)
        Button(t,text='Tabular form',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=create_table).place(x=550,y=475)

        t.mainloop()



    st=Button(root,text='Store',bg='green',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black",command=store).place(x=300,y=150)
    pc=Button(root,text='ProductCategory',bg='pink',width=15,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black",command=Prodcat).place(x=250,y=240)
    pr=Button(root,text='Product',bg='red',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black",command=Prod).place(x=300,y=330)
    Sup=Button(root,text='Suppliers',bg='yellow',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black",command=supplier).place(x=300,y=420)
    stkin=Button(root,text='StockIn',bg='magenta',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black",command=StockIn).place(x=850,y=150)
    Cust=Button(root,text='Customers',bg='orange',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black",command=Customer).place(x=850,y=240)
    Ord=Button(root,text='Orders',bg='maroon',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black",command=Order).place(x=850,y=330)
    Bil=Button(root,text='Bill',bg='#B87333',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black",command=Bill).place(x=850,y=420)


    root.mainloop()

def main_user():
    root = tkinter.Tk()
    root.state("zoomed")
    root.config(bg='#89CFEF')


    heading2=Canvas(root,width=52,height=1000,bg='black',highlightbackground="black", highlightcolor="black")
    heading2.place(x=-1,y=0)
    heading3=Canvas(root,width=53,height=1000,bg='black',highlightbackground="black", highlightcolor="black")
    heading3.place(x=1309,y=0)
    heading4=Canvas(root,width=1500,height=60,bg='black',highlightbackground="black", highlightcolor="black")
    heading4.place(x=-1,y=655)
    heading5=Canvas(root,width=1500,height=60,bg='black',highlightbackground="black", highlightcolor="black")
    heading5.place(x=-1,y=1)
    heading=Label(
        root,
        text="Stock Management System Dashboard For User",
        font=("Rockwell Extra Bold", 24,"bold"),  # Change the font and size
        fg="yellow",  # Change the text color
        bg="black",
        padx=0,  # Add horizontal padding
        pady=10,  # Add vertical padding
        relief="flat",  # Add a border around the label
        borderwidth=2,  # Set border width
        width=0,  # Set a fixed width for the label
        highlightbackground="yellow", 
        highlightcolor="yellow"
    )
    heading.place(x=300,y=0)

    def store():
        t=Toplevel(root)
        t.state("zoomed")
        t.config(bg="grey")
        l1=Label(t,text="Action to Perform",font=("Rockwell Extra Bold",35),bg='white',fg='black' )
        l1.place(x=430,y=10)
        
        
        def store_find():
            tk=Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('store screen find')
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select StoreID from store"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=e1.get()
                try:
                    sq="select * from store where storeid='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    e2.delete(0,100)
                    e3.delete(0,100)
                    e4.delete(0,100)
                    e5.delete(0,100)
                    e6.delete(0,100)
                    e7.delete(0,100)

                    e2.insert(0,data[1])
                    e3.insert(0,data[2])
                    e4.insert(0,data[3])
                    e5.insert(0,data[4])
                    e6.insert(0,data[5])
                    e7.insert(0,data[6])
                except:
                    messagebox.showinfo("info","data not found")
                db.close()
            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")
            l1=Label(tk,text='Store ID', font=customfont)
            l1.place(x=75,y=50)
            e1=ttk.Combobox(tk,width=80)
            filldata_combo()
            e1['values']=lt
            e1.place(x=450,y=50)



            l2=Label(tk,text='Store Name', font=customfont)
            l2.place(x=75,y=125)
            e2=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e2.place(x=450,y=125)
            l3=Label(tk,text='Store Address', font=customfont)
            l3.place(x=75,y=200)
            e3=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e3.place(x=450,y=200)
            l4=Label(tk,text='Store City', font=customfont)
            l4.place(x=75,y=275)
            e4=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e4.place(x=450,y=275)
            l5=Label(tk,text='Store Phone No', font=customfont)
            l5.place(x=75,y=350)
            e5=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e5.place(x=450,y=350)
            l6=Label(tk,text='Store Email ID', font=customfont)
            l6.place(x=75,y=425)
            e6=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e6.place(x=450,y=425)
            l7=Label(tk,text='Store Registration No', font=customfont)
            l7.place(x=75,y=500)
            e7=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e7.place(x=450,y=500)
            bt1=Button(tk,text='Find', width=10, height=2, bg='blue', fg='white', font=customfont,command=find)
            bt1.place(x=575,y=575)
            t.mainloop()
        
        def viewalldata():
            tk = Toplevel(t)
            tk.state('zoomed')  # Fix the typo here
            tk.config(bg="light grey")
            tk.title('store view all data')  # Fix the typo here
            a1=[]
            a2=[]
            a3=[]
            a4=[]
            a5=[]
            a6=[]
            a7=[]
            global i 
            i=0
            def getdata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='sms')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                sql="select * from store"
                cur.execute(sql) #It inserts the data into the 'employee' table in the database
                data=cur.fetchall()
                for res in data:
                    a1.append(res[0])
                    a2.append(res[1])
                    a3.append(res[2])
                    a4.append(res[3])
                    a5.append(res[4])
                    a6.append(res[5])
                    a7.append(res[6])
            def showfirst():
                global i
                i=0
                e1.delete(0,100)
                e2.delete(0,100)
                e3.delete(0,100)
                e4.delete(0,100)
                e5.delete(0,100)
                e6.delete(0,100)
                e7.delete(0,100)
                e1.insert(0,a1[i])
                e2.insert(0,a2[i])
                e3.insert(0,a3[i])
                e4.insert(0,a4[i])
                e5.insert(0,a5[i])
                e6.insert(0,a6[i])
                e7.insert(0,a7[i])
            def shownext():
                global i
                i=i+1
                e1.delete(0,100)
                e2.delete(0,100)
                e3.delete(0,100)
                e4.delete(0,100)
                e5.delete(0,100)
                e6.delete(0,100)
                e7.delete(0,100)
                e1.insert(0,a1[i])
                e2.insert(0,a2[i])
                e3.insert(0,a3[i])
                e4.insert(0,a4[i])
                e5.insert(0,a5[i])
                e6.insert(0,a6[i])
                e7.insert(0,a7[i])
                
            def showprev():
                global i
                i=i-1
                e1.delete(0,100)
                e2.delete(0,100)
                e3.delete(0,100)
                e4.delete(0,100)
                e5.delete(0,100)
                e6.delete(0,100)
                e7.delete(0,100)
                e1.insert(0,a1[i])
                e2.insert(0,a2[i])
                e3.insert(0,a3[i])
                e4.insert(0,a4[i])
                e5.insert(0,a5[i])
                e6.insert(0,a6[i])
                e7.insert(0,a7[i])
            def showlast():
                global i
                i=len(a1)-1
                e1.delete(0,100)
                e2.delete(0,100)
                e3.delete(0,100)
                e4.delete(0,100)
                e5.delete(0,100)
                e6.delete(0,100)
                e7.delete(0,100)
                e1.insert(0,a1[i])
                e2.insert(0,a2[i])
                e3.insert(0,a3[i])
                e4.insert(0,a4[i])
                e5.insert(0,a5[i])
                e6.insert(0,a6[i])
                e7.insert(0,a7[i])
        
            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")
            l1=Label(tk,text='Store ID', font=customfont)
            l1.place(x=75,y=50)
            e1=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e1.place(x=450,y=50)
            l2=Label(tk,text='Store Name', font=customfont)
            l2.place(x=75,y=125)
            e2=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e2.place(x=450,y=125)
            l3=Label(tk,text='Store Address', font=customfont)
            l3.place(x=75,y=200)
            e3=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e3.place(x=450,y=200)
            l4=Label(tk,text='Store City', font=customfont)
            l4.place(x=75,y=275)
            e4=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e4.place(x=450,y=275)
            l5=Label(tk,text='Store Phone No', font=customfont)
            l5.place(x=75,y=350)
            e5=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e5.place(x=450,y=350)
            l6=Label(tk,text='Store Email ID', font=customfont)
            l6.place(x=75,y=425)
            e6=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e6.place(x=450,y=425)
            l7=Label(tk,text='Store Registration No', font=customfont)
            l7.place(x=75,y=500)
            e7=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e7.place(x=450,y=500)
            bt=Button(tk,text='Preview ',font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2, bg='blue', fg='white',command=showfirst)
            bt.place(x=250,y=600)
            bt1=Button(tk,text='Next ',font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2, bg='blue', fg='white',command=shownext)
            bt1.place(x=450,y=600)
            bt2=Button(tk,text='Previous ',font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2, bg='blue', fg='white',command=showprev)
            bt2.place(x=600,y=600)
            bt3=Button(tk,text='Last',font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2, bg='blue', fg='white',command=showlast)
            bt3.place(x=800,y=600)
            getdata()
            showfirst()
            tk.mainloop()
        
        Button(t,text='Find',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=store_find).place(x=600,y=175)
        Button(t,text='View all data',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=viewalldata).place(x=600,y=250)


    def Prodcat():
        t=Toplevel(root)
        t.state('zoomed')
        t.config(bg="grey")
        l1=Label(t,text="Action  to Perform",font=("Rockwell Extra Bold",35) )
        l1.place(x=390,y=10)
        
        
        def prodcat_find():
            tk=Toplevel(t)
            tk.config(bg="light grey")
            tk.state("zoomed")
            tk.title('prodcatFIND')
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select CategoryID from productcategory"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                try:
                    sq="select * from productcategory where CategoryID='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    b1.delete(0,100)
                    c1.delete(0,100)
                    b1.insert(0,data[1])
                    c1.insert(0,data[2])
                except:    
                
                    messagebox.showinfo("info","data not found")
                db.close()

            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")
            a=Label(tk,text='Product Catagory ID', font=customfont)
            a.place(x=75,y=150)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=400,y=150)

            b=Label(tk,text='Product Catagory Name', font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=60, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            b1.place(x=400,y=200)

            c=Label(tk,text='Product Catagory Description', font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=60, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            c1.place(x=400,y=250)

            bt=Button(tk,text='FIND',font=customfont, command=find,highlightbackground='black', highlightcolor='black', highlightthickness=2,bg='blue',fg="white")
            bt.place(x=400,y=400)
            tk.mainloop()
        
        
        def prodcat_viewalldata():
            tk=Toplevel(t)
            tk.state("zoomed")
            tk.title("View all data")
            tk.config(bg='light grey')
            
            a0=[]
            a2=[]
            a3=[]
            
            global i 
            i=0
            def getdata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='sms')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                sql="select * from productcategory"
                cur.execute(sql) #It inserts the data into the 'employee' table in the database
                data=cur.fetchall()
                print(data)
                for res in data:
                    a0.append(res[0])
                    a2.append(res[1])
                    a3.append(res[2])
            print(a0)
            def showfirst():
                global i
                i=0
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                print(i)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
            def shownext():
                global i
                i=i+1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
            def showprev():
                global i
                i=i-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
            def showlast():
                global i
                i=len(a0)-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")

            a=Label(tk,text='Product Catagory ID', font=customfont)
            a.place(x=75,y=150)
            a1=Entry(tk,width=60, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            a1.place(x=500,y=155)

            b=Label(tk,text='Product Catagory Name', font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=60, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            b1.place(x=500,y=205)

            c=Label(tk,text='Product Catagory Description', font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=60, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            c1.place(x=500,y=255)

            bt=Button(tk,text='first ',command=showfirst,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2, bg='blue', fg='white')
            bt.place(x=300,y=350)
            bt1=Button(tk,text='Next ',font=customfont,command=shownext ,highlightbackground='black', highlightcolor='black', highlightthickness=2, bg='blue', fg='white')
            bt1.place(x=500,y=350)
            bt2=Button(tk,text='Previous ',font=customfont, command=showprev,highlightbackground='black', highlightcolor='black', highlightthickness=2, bg='blue', fg='white')
            bt2.place(x=650,y=350)
            bt3=Button(tk,text='Last',font=customfont,command=showlast,highlightbackground='black', highlightcolor='black', highlightthickness=2, bg='blue', fg='white')
            bt3.place(x=850,y=350)
            getdata()
            showfirst()

            tk.mainloop()

        Button(t,text='Find',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=prodcat_find).place(x=550,y=175)
        Button(t,text='View all data',bg='blue',relief="solid",width=10,font=("Helvetica",24), fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=prodcat_viewalldata).place(x=550,y=250)

        t.mainloop()


    def Prod():
        t=Toplevel(root)
        t.state('zoomed')
        t.config(bg="grey")
        l1=Label(t,text="Action to Perform",font=("Rockwell Extra Bold",35),bg='white',fg='black' )
        l1.place(x=390,y=10)

        def productfind():
            tk = Toplevel(t)
            tk.state('zoomed') 
            tk.config(bg="light grey")
            tk.title('Product insert')

            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")

            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select ProductID from product"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()

            def prod_find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                try:
                    sq="select * from product where ProductID='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    b1.delete(0,100)
                    c1.delete(0,100)
                    d1.delete(0,100)
                    e1.delete(0,100)
                    f1.delete(0,100)
                    g1.delete(0,100)
                    b1.insert(0,data[1])
                    c1.insert(0,data[2])
                    d1.insert(0,data[3])
                    e1.insert(0,data[4])
                    f1.insert(0,data[5])
                    g1.insert(0,data[6])
                except:
                    messagebox.showinfo("info","data not found")
                db.close()

            a=Label(tk,text='Product ID', font=customfont)
            a.place(x=75,y=150)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=300,y=150)

            b=Label(tk,text='Catagory ID', font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Product Name', font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Unit of Sale', font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Price Per Unit', font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e1.place(x=300,y=355)

            f=Label(tk,text='Open Quantity', font=customfont)
            f.place(x=75,y=400)
            f1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            f1.place(x=300,y=405)

            g=Label(tk,text='Current Quantity', font=customfont)
            g.place(x=75,y=450)
            g1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            g1.place(x=300,y=455)

            bt=Button(tk,text='FIND',bg="blue",fg="white",font=customfont,command=prod_find, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt.place(x=75,y=600)

            tk.mainloop()

        def productviewdata():
            tk = Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('Product view data')

            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")
            a0=[]
            a2=[]
            a3=[]
            a4=[]
            a5=[]
            a6=[]
            a7=[]
            global i 
            i=0
            def getdata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='sms')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                sql="select * from product"
                cur.execute(sql) #It inserts the data into the 'employee' table in the database
                data=cur.fetchall()
                for res in data:
                    a0.append(res[0])
                    a2.append(res[1])
                    a3.append(res[2])
                    a4.append(res[3])
                    a5.append(res[4])
                    a6.append(res[5])
                    a7.append(res[6])
            def showfirst():
                global i
                i=0
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                g1.delete(0,100)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                g1.insert(0,a7[i])
            def shownext():
                global i
                i=i+1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                g1.delete(0,100)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                g1.insert(0,a7[i])
                
            def showprev():
                global i
                i=i-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                g1.delete(0,100)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                g1.insert(0,a7[i])
            def showlast():
                global i
                i=len(a0)-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                g1.delete(0,100)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                g1.insert(0,a7[i])
        

            a=Label(tk,text='Product ID', font=customfont)
            a.place(x=75,y=150)
            a1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            a1.place(x=300,y=155)

            b=Label(tk,text='Catagory ID', font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Product Name', font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Unit of Sale', font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Price Per Unit', font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e1.place(x=300,y=355)

            f=Label(tk,text='Open Quantity', font=customfont)
            f.place(x=75,y=400)
            f1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            f1.place(x=300,y=405)

            g=Label(tk,text='Current Quantity', font=customfont)
            g.place(x=75,y=450)
            g1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            g1.place(x=300,y=455)

            bt1=Button(tk,text='PREVIEW',bg="blue", fg="white",command=showfirst,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt1.place(x=100,y=550)

            bt2=Button(tk,text='NEXT',bg="blue", fg="white",font=customfont,command=shownext, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt2.place(x=350,y=550)

            bt3=Button(tk,text='PREVIOUS',bg="blue", fg="white",font=customfont,command=showprev, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt3.place(x=650,y=550)

            bt4=Button(tk,text='LAST',bg="blue", fg="white",font=customfont,command=showlast, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt4.place(x=950,y=550)

            getdata()
            showfirst()
            tk.mainloop()



        Button(t,text='Find',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=productfind).place(x=550,y=175)
        Button(t,text='View all data',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=productviewdata).place(x=550,y=250)

        t.mainloop()


    def supplier():
        t=Toplevel(root)
        t.state('zoomed')
        t.config(bg="grey")
        l1=Label(t,text="Action to Perform",font=("Rockwell Extra Bold",35),bg='white',fg='black' )
        l1.place(x=390,y=10)
        

        def supplierfind():
            tk=Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('supplier find')
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select SupplierID from suppliers"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def supp_find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                try:
                    sq="select * from suppliers where SupplierID='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    b1.delete(0,100)
                    c1.delete(0,100)
                    d1.delete(0,100)
                    e1.delete(0,100)
                    f1.delete(0,100)
                    g1.delete(0,100)
                    b1.insert(0,data[1])
                    c1.insert(0,data[2])
                    d1.insert(0,data[3])
                    e1.insert(0,data[4])
                    f1.insert(0,data[5])
                    g1.insert(0,data[6])
                except:
                    messagebox.showinfo("info","data not found")
                db.close()

            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")
            

            a=Label(tk,text='Supplier ID', font=customfont)
            a.place(x=75,y=150)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=300,y=150)

            b=Label(tk,text='Supplier Name', font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Supplier Address', font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Supplier City', font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Supplier Email ID', font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e1.place(x=300,y=355)

            f=Label(tk,text='Supplier phone No.', font=customfont)
            f.place(x=75,y=400)
            f1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            f1.place(x=300,y=405)

            g=Label(tk,text='Catagory ID', font=customfont)
            g.place(x=75,y=450)
            g1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            g1.place(x=300,y=455)

            bt=Button(tk,text='FIND',font=customfont,bg="blue", fg="white",command=supp_find,highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt.place(x=75,y=600)

            tk.mainloop()
        
    

        def supplierviewalldata():
            tk=Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('supplier delete')

            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")
            a0=[]
            a2=[]
            a3=[]
            a4=[]
            a5=[]
            a6=[]
            a7=[]
            global i 
            i=0
            def getdata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='sms')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                sql="select * from suppliers"
                cur.execute(sql) #It inserts the data into the 'employee' table in the database
                data=cur.fetchall()
                for res in data:
                    a0.append(res[0])
                    a2.append(res[1])
                    a3.append(res[2])
                    a4.append(res[3])
                    a5.append(res[4])
                    a6.append(res[5])
                    a7.append(res[6])
            def showfirst():
                global i
                i=0
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                g1.delete(0,100)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                g1.insert(0,a7[i])
            def shownext():
                global i
                i=i+1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                g1.delete(0,100)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                g1.insert(0,a7[i])
                
            def showprev():
                global i
                i=i-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                g1.delete(0,100)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                g1.insert(0,a7[i])
            def showlast():
                global i
                i=len(a0)-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                g1.delete(0,100)
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                g1.insert(0,a7[i])
            a=Label(tk,text='Supplier ID', font=customfont)
            a.place(x=75,y=150)
            a1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            a1.place(x=300,y=155)

            b=Label(tk,text='Supplier Name', font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Supplier Address', font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Supplier City', font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Supplier Email ID', font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            e1.place(x=300,y=355)

            f=Label(tk,text='Supplier phone No.', font=customfont)
            f.place(x=75,y=400)
            f1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            f1.place(x=300,y=405)

            g=Label(tk,text='Catagory ID', font=customfont)
            g.place(x=75,y=450)
            g1=Entry(tk,width=56, font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            g1.place(x=300,y=455)

            bt1=Button(tk,text='PREVIEW',bg="blue", fg="white",font=customfont,command=showfirst, highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt1.place(x=100,y=550)

            bt2=Button(tk,text='NEXT',bg="blue", fg="white",font=customfont, command=shownext,highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt2.place(x=350,y=550)

            bt3=Button(tk,text='PREVIOUS',bg="blue", fg="white",font=customfont, command=showprev,highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt3.place(x=650,y=550)

            bt4=Button(tk,text='LAST',bg="blue", fg="white",font=customfont, command=showlast,highlightbackground='black', highlightcolor='black', highlightthickness=2)
            bt4.place(x=950,y=550)
            getdata()
            showfirst()
            tk.mainloop()


        Button(t,text='Find',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=supplierfind).place(x=550,y=175)
        Button(t,text='View all data',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=supplierviewalldata).place(x=550,y=250)

        t.mainloop()


    def StockIn():
        t=Toplevel(root)
        t.state('zoomed')
        t.config(bg="grey")

        

        def stockinfind():
            tk=Toplevel(t)
            tk.state('zoomed')
            tk.title('stockin find')
            tk.config(bg="light grey")

            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select Stock_in_ID from stockin"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                try:
                    sq="select * from stockin where Stock_in_ID='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    b1.delete(0,100)
                    c1.delete(0,100)
                    d1.delete(0,100)
                    e1.delete(0,100)
                    
                    b1.insert(0,data[1])
                    c1.insert(0,data[2])
                    d1.insert(0,data[3])
                    e1.insert(0,data[4])
                    
                except:
                    messagebox.showinfo("info","data not found")
                db.close()

            a=Label(tk,text='Stockin ID',font=customfont)
            a.place(x=75,y=150)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=300,y=150)

            b=Label(tk,text='Supplier ID',font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Catagory ID',font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Quantity',font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Date In',font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            e1.place(x=300,y=355)

            bt=Button(tk,text='FIND',bg="blue", fg="white",font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2,command=find)
            bt.place(x=75,y=600)

            tk.mainloop()

        def stockinviewalldata():
            tk=Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('stockin delete')


            a0=[]
            a2=[]
            a3=[]
            a4=[]
            a5=[]
            global i 
            i=0
            def getdata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='sms')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                sql="select * from stockin"
                cur.execute(sql) #It inserts the data into the 'employee' table in the database
                data=cur.fetchall()
                for res in data:
                    a0.append(res[0])
                    a2.append(res[1])
                    a3.append(res[2])
                    a4.append(res[3])
                    a5.append(res[4])
                    
            def showfirst():
                global i
                i=0
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                
            def shownext():
                global i
                i=i+1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                
                
            def showprev():
                global i
                i=i-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                
            def showlast():
                global i
                i=len(a0)-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                
            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")

            a=Label(tk,text='Stockin ID',font=customfont)
            a.place(x=75,y=150)
            a1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            a1.place(x=300,y=155)

            b=Label(tk,text='Supplier ID',font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Catagory ID',font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Quantity',font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Date In',font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            e1.place(x=300,y=355)


            bt1=Button(tk,text='PREVIEW',bg="blue", fg="white",font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2, command=showfirst)
            bt1.place(x=200,y=600)

            bt2=Button(tk,text='NEXT',bg="blue", fg="white",font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2, command=shownext)
            bt2.place(x=400,y=600)

            bt3=Button(tk,text='PREVIOUS',bg="blue", fg="white",font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2, command=showprev)
            bt3.place(x=600,y=600)

            bt4=Button(tk,text='LAST',bg="blue", fg="white",font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2, command=showlast)
            bt4.place(x=800,y=600)
            getdata()
            showfirst()     

            tk.mainloop()

        l1=Label(t,text="Action to Perform",font=("Rockwell Extra Bold",35),bg='white',fg='black' )
        l1.place(x=390,y=10)
        Button(t,text='Find',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=stockinfind).place(x=550,y=175)
        Button(t,text='View all data',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=stockinviewalldata).place(x=550,y=250)

        t.mainloop()


    def Customer():
        t=Toplevel(root)
        t.state('zoomed')
        t.config(bg="grey")
        l1=Label(t,text="Action to Perform",font=("Rockwell Extra Bold",35),bg='white',fg='black' )
        l1.place(x=390,y=10)
        
        def customerfind():
            tk=Toplevel(t)
            tk.title('customer find')
            tk.config(bg="light grey")
            tk.state('zoomed')
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select CustomerID from customers"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def cust_find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                try:
                    sq="select * from customers where CustomerID='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    b1.delete(0,100)
                    c1.delete(0,100)
                    d1.delete(0,100)
                    e1.delete(0,100)
                    
                    b1.insert(0,data[1])
                    c1.insert(0,data[2])
                    d1.insert(0,data[3])
                    e1.insert(0,data[4])
                except:
                    messagebox.showinfo("info","data not found")
                db.close()


            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")

            a=Label(tk,text='Customer ID',font=customfont)
            a.place(x=75,y=150)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=300,y=150)

            b=Label(tk,text='Customer Name',font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Customer Address',font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Email ID',font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Phone No.',font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            e1.place(x=300,y=355)



            bt=Button(tk,text='FIND',bg="blue", fg="white",command=cust_find,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=75,y=600)


            tk.mainloop()

       
        def customerviewalldata():
            tk=Toplevel(t)
            tk.title('customerINSERT')
            tk.config(bg="light grey")
            tk.state('zoomed')

            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")
            a0=[]
            a2=[]
            a3=[]
            a4=[]
            a5=[]
            
            
            global i 
            i=0
            def getdata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='sms')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                sql="select * from customers"
                cur.execute(sql) #It inserts the data into the 'employee' table in the database
                data=cur.fetchall()
                for res in data:
                    a0.append(res[0])
                    a2.append(res[1])
                    a3.append(res[2])
                    a4.append(res[3])
                    a5.append(res[4])
                    
                
            def showfirst():
                global i
                i=0
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                
                
            def shownext():
                global i
                i=i+1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                
            
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                
                
                
            def showprev():
                global i
                i=i-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                
                
            def showlast():
                global i
                i=len(a0)-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                
                

            a=Label(tk,text='Customer ID',font=customfont)
            a.place(x=75,y=150)
            a1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            a1.place(x=300,y=155)

            b=Label(tk,text='Customer Name',font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Customer Address',font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Email ID',font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Phone No.',font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            e1.place(x=300,y=355)


            bt=Button(tk,text='PREVIEW',bg="blue", fg="white",command=showfirst,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=200,y=600)

            bt=Button(tk,text='NEXT',bg="blue", fg="white",command=shownext,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=400,y=600)

            bt=Button(tk,text='PREVIOUS',bg="blue", fg="white",command=showprev,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=600,y=600)

            bt=Button(tk,text='LAST',bg="blue", fg="white",command=showlast,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=800,y=600)

            getdata()
            showfirst()
            tk.mainloop()




        Button(t,text='Find',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=customerfind).place(x=550,y=175)
        Button(t,text='View all data',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=customerviewalldata).place(x=550,y=250)

        t.mainloop()


    def Order():
        t=Toplevel(root)
        t.state('zoomed')
        t.config(bg="grey")
        
       
        def orderfind():
            tk=Toplevel(t)
            tk.config(bg="light grey")
            tk.title('Order Find')
            tk.state('zoomed')
            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select OrderID from orders"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()

            def ord_find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                try:
                    sq="select * from orders where OrderID='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    b1.delete(0,100)
                    c1.delete(0,100)
                    d1.delete(0,100)
                    e1.delete(0,100)
                    f1.delete(0,100)
                    
                    b1.insert(0,data[1])
                    c1.insert(0,data[2])
                    d1.insert(0,data[3])
                    e1.insert(0,data[4])
                    f1.insert(0,data[5])
                except:
                    messagebox.showinfo("info","data not found")
                db.close()

            a=Label(tk,text='Order ID',font=customfont)
            a.place(x=75,y=150)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=300,y=150)

            b=Label(tk,text='Customer ID',font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Catagory ID',font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Product ID',font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Date Of Order',font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            e1.place(x=300,y=355)

            f=Label(tk,text='Quantity',font=customfont)
            f.place(x=75,y=400)
            f1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            f1.place(x=300,y=405)

            bt=Button(tk,text='FIND',bg='blue', fg='white',font=customfont,command=ord_find,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=75,y=600)


            tk.mainloop()

        def orderviewalldata():
            tk=Toplevel(t)
            tk.config(bg="light grey")
            tk.title('Order view all data')
            tk.state('zoomed')

            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")
            a0=[]
            a2=[]
            a3=[]
            a4=[]
            a5=[]
            a6=[]
            
            global i 
            i=0
            def getdata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='sms')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                sql="select * from orders"
                cur.execute(sql) #It inserts the data into the 'employee' table in the database
                data=cur.fetchall()
                for res in data:
                    a0.append(res[0])
                    a2.append(res[1])
                    a3.append(res[2])
                    a4.append(res[3])
                    a5.append(res[4])
                    a6.append(res[5])
                
            def showfirst():
                global i
                i=0
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                
            def shownext():
                global i
                i=i+1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
            
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                
                
            def showprev():
                global i
                i=i-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                
            def showlast():
                global i
                i=len(a0)-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                e1.delete(0,100)
                f1.delete(0,100)
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                e1.insert(0,a5[i])
                f1.insert(0,a6[i])
                
        

            a=Label(tk,text='Order ID',font=customfont)
            a.place(x=75,y=150)
            a1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            a1.place(x=300,y=155)

            b=Label(tk,text='Customer ID',font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Catagory ID',font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Product ID',font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            d1.place(x=300,y=305)

            e=Label(tk,text='Date Of Order',font=customfont)
            e.place(x=75,y=350)
            e1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            e1.place(x=300,y=355)

            f=Label(tk,text='Quantity',font=customfont)
            f.place(x=75,y=400)
            f1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            f1.place(x=300,y=405)

            bt=Button(tk,text='PREVIEW',bg='blue', fg='white',command=showfirst,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=200,y=600)

            bt=Button(tk,text='NEXT',bg='blue', fg='white',command=shownext,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=400,y=600)

            bt=Button(tk,text='PREVIOUS',bg='blue', fg='white',command=showprev,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=650,y=600)

            bt=Button(tk,text='LAST',bg='blue', fg='white',command=showlast,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            bt.place(x=900,y=600)

            getdata()
            showfirst()
            tk.mainloop()

        l1=Label(t,text="Action to Perform",font=("Rockwell Extra Bold",35),bg='white',fg='black' )
        l1.place(x=390,y=10)
        Button(t,text='Find',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=orderfind).place(x=550,y=175)
        Button(t,text='View all data',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=orderviewalldata).place(x=550,y=250)

        t.mainloop()

    def Bill():
        t=Toplevel(root)
        t.state('zoomed')
        t.config(bg="grey")
        l1=Label(t,text="Action to Perform",font=("Rockwell Extra Bold",35),bg='white',fg='black' )
        l1.place(x=400,y=10)
        
        
        
        def billfind():
            tk= Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('Bill find')
            lt=[]
            def filldata_combo():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                sql="select CustomerID from bill"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    lt.append(res[0])
                db.close()
            def find():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()
                s=a1.get()
                try:
                    sq="select * from bill where CustomerID='%s'"%(s)
                    cur.execute(sq)
                    data=cur.fetchone()
                    b1.delete(0,100)
                    c1.delete(0,100)
                    d1.delete(0,100)
                    
                    b1.insert(0,data[1])
                    c1.insert(0,data[2])
                    d1.insert(0,data[3])
                
                except:
                    messagebox.showinfo("info","data not found")
                db.close()

            
            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")

            a=Label(tk,text='Customer ID',font=customfont)
            a.place(x=75,y=150)
            a1= ttk.Combobox(tk, width=80)        
            filldata_combo()
            a1['values']=lt
            a1.place(x=300,y=150)

            b=Label(tk,text='Order ID',font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Catagory ID',font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Amount',font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            d1.place(x=300,y=305)

            bt=Button(tk,text='FIND',bg='blue', fg='white',font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2, command=find)
            bt.place(x=75,y=600)


            tk.mainloop()

        
        def billviewalldata():
            tk= Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="light grey")
            tk.title('Bill view all data')


            a0=[]
            a2=[]
            a3=[]
            a4=[]
            a5=[]
            a6=[]
            
            global i 
            i=0
            def getdata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
                cur=db.cursor()  #This line creates a cursor object, which is used to execute SQL commands 
                                #and retrieve data from the database. The cursor is stored in the variable "cur."
                sql="select * from bill"
                cur.execute(sql) #It inserts the data into the 'employee' table in the database
                data=cur.fetchall()
                for res in data:
                    a0.append(res[0])
                    a2.append(res[1])
                    a3.append(res[2])
                    a4.append(res[3])
                    
                
            def showfirst():
                global i
                i=0
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                
                
            def shownext():
                global i
                i=i+1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                
            
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                
                
                
            def showprev():
                global i
                i=i-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
                
                
            def showlast():
                global i
                i=len(a0)-1
                a1.delete(0,100)
                b1.delete(0,100)
                c1.delete(0,100)
                d1.delete(0,100)
                
                
                a1.insert(0,a0[i])
                b1.insert(0,a2[i])
                c1.insert(0,a3[i])
                d1.insert(0,a4[i])
        
            
            customfont=tkFont.Font(family="Helvetica",size=15, weight="bold")

            a=Label(tk,text='Customer ID',font=customfont)
            a.place(x=75,y=150)
            a1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            a1.place(x=300,y=155)

            b=Label(tk,text='Order ID',font=customfont)
            b.place(x=75,y=200)
            b1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            b1.place(x=300,y=205)

            c=Label(tk,text='Catagory ID',font=customfont)
            c.place(x=75,y=250)
            c1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            c1.place(x=300,y=255)

            d=Label(tk,text='Amount',font=customfont)
            d.place(x=75,y=300)
            d1=Entry(tk,width=56,font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2)
            d1.place(x=300,y=305)

            bt=Button(tk,text='PREVIEW',bg='blue', fg='white',font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2, command=showfirst)
            bt.place(x=200,y=550)

            bt=Button(tk,text='NEXT',bg='blue', fg='white',font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2, command=shownext)
            bt.place(x=400,y=550)

            bt=Button(tk,text='PREVIOUS',bg='blue', fg='white',font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2, command=showprev)
            bt.place(x=600,y=550)

            bt=Button(tk,text='LAST',bg='blue', fg='white',font=customfont,highlightbackground='black',highlightcolor='black',highlightthickness=2, command=showlast)
            bt.place(x=800,y=550)

            getdata()
            showfirst()

            tk.mainloop()
            

        Button(t,text='Find',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=billfind).place(x=550,y=175)
        Button(t,text='View all data',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=billviewalldata).place(x=550,y=250)

        t.mainloop()



    st=Button(root,text='Store',bg='green',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black",command=store).place(x=300,y=150)
    pc=Button(root,text='ProductCategory',bg='pink',width=15,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black",command=Prodcat).place(x=250,y=240)
    pr=Button(root,text='Product',bg='red',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black",command=Prod).place(x=300,y=330)
    Sup=Button(root,text='Suppliers',bg='yellow',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black",command=supplier).place(x=300,y=420)
    stkin=Button(root,text='StockIn',bg='magenta',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black",command=StockIn).place(x=850,y=150)
    Cust=Button(root,text='Customers',bg='orange',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black",command=Customer).place(x=850,y=240)
    Ord=Button(root,text='Orders',bg='maroon',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black",command=Order).place(x=850,y=330)
    Bil=Button(root,text='Bill',bg='#B87333',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black",command=Bill).place(x=850,y=420)


    root.mainloop()

def save():
    win=Toplevel(root)
    win.state("zoomed")
    win.config(bg='#89CFEF')

    heading=Label(win,text='SIGN UP',font=('Rockwell Extra Bold',48),bg='#89CFEF')
    heading.place(x=550,y=30)

    l1=Label(win,text='Username',font=customfont,bg='#89CFEF')
    l1.place(x=350,y=200)
    e1=Entry(win,width=100, highlightbackground='black', highlightcolor='black', highlightthickness=2)
    e1.place(x=600,y=215)

    l2=Label(win,text='Password',font=customfont,bg='#89CFEF')
    l2.place(x=350,y=375)
    e2=Entry(win,width=100, highlightbackground='black', highlightcolor='black', highlightthickness=2)
    e2.place(x=600,y=388)

    def sn_admin():
        u=e1.get()
        p=e2.get()
        db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
        cur=db.cursor()
        sql="insert into users values('%s','%s','Admin')"%(u,p)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo("insert","new admin added")
        win.destroy()

    bt1=Button(win,text="sign in as admin", width=15, height=0, bg='black', fg='orange',font=('Rockwell Extra Bold',12),command=sn_admin)
    bt1.place(x=550,y=500)

    def sn_regular():
        u=e1.get()
        p=e2.get()
        db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
        cur=db.cursor()
        sql="insert into users values('%s','%s','Regular')"%(u,p)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo("insert","new user added")
        win.destroy()
    bt2=Button(win,text="sign in as user", width=15, height=0, bg='black', fg='orange',font=('Rockwell Extra Bold',12),command=sn_regular)
    bt2.place(x=800,y=500)
    win.mainloop()

def check():
    usr=e1.get()
    pssw=e2.get()
    db=pymysql.connect(host="pom.db.elephantsql.com",port=5432, user="xfkhquzu", password="TESt2ulBncAxx1RcfT48ScykB_hbfLXH", database="xfkhquzu")
    cur=db.cursor()
    sql="select username from users"
    cur.execute(sql)
    data=cur.fetchall()
    name=[]
    for x in data:
        name.append(x[0])

    if usr in name:
        sq="select password,user_type from users where username='%s'"%(usr)
        cur.execute(sq)
        d=cur.fetchone()
        if pssw==d[0]:
            if d[1]=="Admin":
                main()
            else:
                main_user()
        else:
            messagebox.showerror("error","username and password doesnt match")
    else:
        messagebox.showerror('error',"user not found")

def forgot():
    win2=Toplevel(root,bg='#89CFEF')
    win2.state('zoomed')
    win2.title('Forgotten Password')
    l=Label(win2,text='Forgotten Password',font=customfont,bg='#89CFEF')
    l.place(x=450,y=50)
    l1=Label(win2,text='Username',font=customfont,bg='#89CFEF')
    l1.place(x=350,y=200)
    e1=Entry(win2,width=100, highlightbackground='black', highlightcolor='black', highlightthickness=2)
    e1.place(x=600,y=215)

    l2=Label(win2,text='email_id',font=customfont,bg='#89CFEF')
    l2.place(x=350,y=375)
    e2=Entry(win2,width=100, highlightbackground='black', highlightcolor='black', highlightthickness=2)
    e2.place(x=600,y=388)
    def mail():
        usr=e1.get()
        mailid=e2.get()
        
        db=pymysql.connect(host='localhost',user='root',password='root',db='SMS')
        cur=db.cursor()
        sql="select username from users"
        cur.execute(sql)
        data=cur.fetchall()
        name=[]
        for x in data:
            name.append(x[0])
        print(type(mailid))
        
        if usr in name:
            sq="select password from users where username='%s'"%(usr)
            cur.execute(sq)
            d=cur.fetchone()
            print(d)
            print(type(d[0]))
        else:
            messagebox.showerror('error','enter correct user name')
        
               

        def send_email():
            from_address = "youremail"
            to_address = mailid

            # Create message container - the correct MIME type is multipart/alternative.
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Test email"
            msg['From'] = from_address
            msg['To'] = to_address

            # Create the message (HTML).
            html = "password for your stock management system account is '%s' for username  is '%s'"%(d[0],usr)

            # Record the MIME type - text/html.
            part1 = MIMEText(html, 'html')

            # Attach parts into message container
            msg.attach(part1)

            # Credentials
            username = 'youremail'  
            password = 'your gmail password'

            # Sending the email
            ## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
            server = smtplib.SMTP('smtp.gmail.com', 587) 
            server.ehlo()
            server.starttls()
            server.login(username,password)
            
            try:
                # Send the email and update the progress bar
                for i in range(101):
                    progress_bar["value"] = i
                    win2.update()
                    time.sleep(0.05)  # Simulate the sending process  
                server.sendmail(from_address, to_address, msg.as_string())  
                server.quit()
                messagebox.showinfo('Hi','Mail Send')
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                win2.destroy()

        # Start the progress bar
        progress_bar = ttk.Progressbar(win2, length=300, mode="determinate")
        progress_bar.pack(pady=20)
        progress_bar["maximum"] = 100
        progress_bar["value"] = 0

        # Use the after method to call send_email()
        win2.after(100, send_email)
            
    bt1=Button(win2,text="send mail", width=17, height=0, bg='black', fg='orange',font=('Rockwell Extra Bold',12),command=mail)
    bt1.place(x=500,y=500)

bt2=Button(root,text="forgot password", width=17, height=0, bg='black', fg='orange',font=('Rockwell Extra Bold',12),command=forgot)
bt2.place(x=800,y=500)

bt=Button(root,text="Login", width=10, height=0, bg='black', fg='orange',font=('Rockwell Extra Bold',12),command=check)
bt.place(x=500,y=500)

bt1=Button(root,text="sign in", width=10, height=0, bg='black', fg='orange',font=('Rockwell Extra Bold',12),command=save)
bt1.place(x=650,y=500)

root.mainloop()
