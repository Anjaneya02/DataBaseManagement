import tkinter 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkFont
from pymongo import MongoClient
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import filedialog
import pandas as pd
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

def admin():
    oot = Toplevel(root)
    oot.state("zoomed")
    oot.config(bg='#89CFEF')


   
    heading5=Canvas(oot,width=1700,height=60,bg='black',highlightbackground="black", highlightcolor="black")
    heading5.place(x=-1,y=1)
    heading=Label(
        oot,
        text="Stock Management System Dashboard",
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
                    
                    ct=MongoClient('localhost',27017)
                    myd=ct['sms']
                    myp=myd['store']
                    gt1=e1.get()
                    gt2=e2.get()
                    gt3=e3.get()
                    gt4=e4.get()
                    gt5=e5.get()
                    gt6=e6.get()
                    gt7=e7.get()
                    columns=['Store_ID','Store Name','Store Address','Store City','Store Phone No','Store Email ID','Store Registration No']
                    values=[gt1,gt2,gt3,gt4,gt5,gt6,gt7]
                    d=dict(zip(columns,values))
                    myp.insert_one(d)
                    messagebox.showinfo("hi","Data Saved")
                    e1.delete(0,"end")
                    e2.delete(0,"end")
                    e3.delete(0,"end")
                    e4.delete(0,"end")
                    e5.delete(0,"end")
                    e6.delete(0,"end")
                    e7.delete(0,"end")
            

            def check():
                # Connect to the MongoDB database (assuming it's running on localhost and listening on the default port)
                client = MongoClient("localhost", 27017)
                db = client["SMS"]  # Use the "SMS" database in MongoDB
                store_collection = db["store"]  # Use the "store" collection

                a1 = e1.get()

                # Check if the StoreID already exists in the MongoDB collection
                if store_collection.find_one({"Store_ID": a1}):
                    messagebox.showerror("Error", "Store with this ID already exists.")
                    return

                # Validate the Email ID
                email = e6.get()
                if len(email) >= 5 and '@' in email and '.' in email:
                    lty.config(text='Your Email ID is valid')
                else:
                    lty.config(text='Enter a Valid Email ID')

                # Validate the Phone Number
                phone_no = e5.get()
                if len(phone_no) < 10 or len(phone_no) >= 12:
                    ltx1 = Label(tk, text='Enter a valid phone number.', fg='red', bg='light grey')
                    ltx1.place(x=1050, y=350)
                else:
                    pass
                




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
            bt1=Button(tk,text='Save data', width=10, height=2, bg='blue', fg='white', font=customfont,command=savedata)
            bt1.place(x=575,y=575)
            bt2=Button(tk,text='CHECK', width=10, height=2, bg='blue', fg='white', font=customfont, command=check)
            bt2.place(x=700,y=575)
            ltx=Label(tk,text=" ",fg='red',bg='light grey',font=customfont)
            ltx.place(x=1050,y=50)
            lty=Label(tk,text=" ",fg='red',bg='light grey',font=customfont)
            lty.place(x=1050,y=425)
            tk.mainloop()
        
        def store_find():
            tk=Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="grey")
            tk.title('store screen find')
            lt=[]
            def filldata_combo():
                client = MongoClient("localhost", 27017)
                db = client["sms"]
                store_collection = db["store"]

                
                for document in store_collection.find({}, {"Store_ID": 1, "_id": 0}):
                    lt.append(document["Store_ID"])

            def find():
                ct=MongoClient('localhost',27017)
                myd=ct['sms']
                myp=myd['store']
                gt1=e1.get()
                d={'Store_ID':gt1}
                data=myp.find_one(d)
                e2.delete(0,"end")
                e3.delete(0,"end")
                e4.delete(0,"end")
                e5.delete(0,"end")
                e6.delete(0,"end")
                e7.delete(0,"end")
                e2.insert(0,data["Store Name"])
                e3.insert(0,data["Store Address"])
                e4.insert(0,data["Store City"])
                e5.insert(0,data["Store Phone No"])
                e6.insert(0,data["Store Email ID"])
                e7.insert(0,data["Store Registration No"])
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
            tk.config(bg="grey")
            tk.title('store screen insert')
            lt=[]
           


            def filldata_combo():
                client = MongoClient("localhost", 27017)
                db = client["sms"]
                store_collection = db["store"]

                
                for document in store_collection.find({}, {"Store_ID": 1, "_id": 0}):
                    lt.append(document["Store_ID"])

            
 

            
            def store_find():
                ct=MongoClient('localhost',27017)
                myd=ct['sms']
                myp=myd['store']
                gt1=e1.get()
                d={'Store_ID':gt1}
                data=myp.find_one(d)
                e2.delete(0,"end")
                e3.delete(0,"end")
                e4.delete(0,"end")
                e5.delete(0,"end")
                e6.delete(0,"end")
                e7.delete(0,"end")
                e2.insert(0,data["Store Name"])
                e3.insert(0,data["Store Address"])
                e4.insert(0,data["Store City"])
                e5.insert(0,data["Store Phone No"])
                e6.insert(0,data["Store Email ID"])
                e7.insert(0,data["Store Registration No"])

            def update():
            
                ct=MongoClient('localhost',27017)
                myd=ct['sms']
                myp=myd['store']

                store_id_to_update = e1.get()

                # Define the new values you want to set
                new_values = {
                    "Store Name": e2.get(),
                    "Store Address": e3.get(),
                    "Store City": e4.get(),
                    "Store Phone No":e5.get() ,
                    "Store Email ID": e6.get(),
                    "Store Registration No":e7.get() 
                }

                # Update the store record based on the store ID
                filter = {"Store_ID": store_id_to_update}
                update = {"$set": new_values}

                result = myp.update_one(filter, update)
                if result.modified_count > 0:
                    messagebox.showinfo("hi","Updated successfully")
                else:
                    messagebox.showerror("error","Store record not found or not updated")
            
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
            e4=Entry(tk,width=50,font=customfont, highlightbackground='black', highlightcolor='black', highlightthickness=2)
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
            bt2=Button(tk,text='find', width=10, height=1, bg='blue', fg='white', font=customfont, command=store_find)
            bt2.place(x=575,y=120)
            tk.mainloop()
        
        def store_delete():
            tk=Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="grey")
            tk.title('store screen insert')
            lt=[]
           

# Assuming you have already established a MongoDB connection
# You can create the connection earlier in your code or use a function like `connect_to_mongodb()` to establish the connection.

            def filldata_combo():
                # Connect to MongoDB (assuming it's running on localhost and listening on the default port)
                client = MongoClient("localhost", 27017)
                db = client["sms"]
                store_collection = db["store"]
                for document in store_collection.find({}, {"Store_ID": 1, "_id": 0}):
                    lt.append(document["Store_ID"])

                
            def delete_store():
                store_id = e1.get()

                if not store_id:
                    messagebox.showerror("Error", "Please enter a Store ID for deletion")
                else:
                    ct = MongoClient('localhost', 27017)
                    myd = ct['sms']
                    myp = myd['store']

                    # Find the document with the specified Store_ID and delete it
                    result = myp.delete_one({"Store_ID": store_id})

                    if result.deleted_count > 0:
                        messagebox.showinfo("Success", "Store data with ID {} deleted successfully".format(store_id))
                    else:
                         messagebox.showerror("Error", "Store data with ID {} not found".format(store_id))
                    e1.delete(0, "end")
            customfont = tkFont.Font(family="Helvetica", size=15, weight="bold")
            l1=Label(tk,text='Store ID', font=customfont)
            l1.place(x=100,y=100)
            e1 = ttk.Combobox(tk, width=80)        
            filldata_combo()
            e1['values']=lt
            e1.place(x=400,y=100)


            bt1=Button(tk,text='delete', width=10, height=1, bg='blue', fg='white', font=customfont,command=delete_store)
            bt1.place(x=450,y=200)
            tk.mainloop()
        
        def viewalldata():
            tk = tkinter.Tk() #change to Toplevel
            tk.state('zoomed')  # Fix the typo here
            tk.config(bg="grey")
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
                ct=MongoClient('localhost',27017)
                myd=ct['sms']
                myp=myd['store']
                data=list(myp.find({})) # converts from object to list

                for row in data:
                    a1.append(row['Store_ID'])
                    a2.append(row["Store Name"])
                    a3.append(row["Store Address"])
                    a4.append(row["Store City"])
                    a5.append(row["Store Phone No"])
                    a6.append(row["Store Email ID"])
                    a7.append(row["Store Registration No"])
           
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
                # Create a Tkinter window
                tk_window = tkinter.Tk()
                tk_window.title("Store Data")

                # Connect to the MongoDB database (assuming it's running on localhost and listening on the default port)
                client = MongoClient("localhost", 27017)
                db = client["sms"]  # Use the "SMS" database in MongoDB
                store_collection = db["store"]  # Use the "store" collection

                # Create a Treeview widget
                table = ttk.Treeview(tk_window, columns=("StoreID", "Name", "Address", "City", "PhoneNO", "EmailID", "RegistrationNo"), show="headings")

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

                # Insert data from MongoDB into the table
                for document in store_collection.find():
                    store_id = document.get("Store_ID")
                    name = document.get("Store Name")
                    address = document.get("Store Address")
                    city = document.get("Store City")
                    phone_no = document.get("Store Phone No")
                    email_id = document.get("Store Email ID")
                    registration_no = document.get("Store Registration No")

                    table.insert("", "end", values=(store_id, name, address, city, phone_no, email_id, registration_no))

                table.pack()
                tk_window.mainloop()



        class ExcelToMongoDBGUI:
            def __init__(self, ot):
                self.root = ot
                self.root.title("Excel to MongoDB")
                self.file_path = ""

                # Create and set up the GUI components
                self.label = tkinter.Label(ot, text="Select Excel File:")
                self.label.pack(pady=10)

                self.browse_button = tkinter.Button(ot, text="Browse", command=self.browse_excel)
                self.browse_button.pack(pady=10)

                self.import_button = tkinter.Button(ot, text="Import to MongoDB", command=self.import_to_mongo)
                self.import_button.pack(pady=10)

            def browse_excel(self):
                self.file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])

            def import_to_mongo(self):
                if not self.file_path:
                    messagebox.showerror("error","Please select an Excel file.")
                    return

                # Read Excel file into a DataFrame
                df = pd.read_excel(self.file_path)

                # Connect to MongoDB
                client = MongoClient('mongodb://localhost:27017/')
                db = client['sms']
                collection = db['store']

                # Convert DataFrame to dictionary and insert into MongoDB
                data = df.to_dict(orient='records')
                collection.insert_many(data)

                messagebox.showinfo("success","Data imported to MongoDB successfully.")

        def on_button_click():
            # Create the main application window
            ot = tkinter.Tk()

            # Create an instance of ExcelToMongoDBGUI
            app = ExcelToMongoDBGUI(ot)

            # Start the application's main event loop
            ot.mainloop()

        
            
        Button(t,text='Insert',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=store_insert).place(x=600,y=100)
        Button(t,text='Find',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=store_find).place(x=600,y=175)
        Button(t,text='Update',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=store_update).place(x=600,y=250)
        Button(t,text='Delete',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=store_delete).place(x=600,y=325)
        Button(t,text='View all data',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=viewalldata).place(x=600,y=400)
        Button(t,text='Tabular form',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=create_table).place(x=600,y=600)
        Button(t,text='import data',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=on_button_click).place(x=600,y=700)

        t.mainloop()
        
    st=Button(oot,text='Store',bg='green',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black",command=store).place(x=300,y=150)
    pc=Button(oot,text='ProductCategory',bg='pink',width=15,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black").place(x=250,y=240)
    pr=Button(oot,text='Product',bg='red',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black").place(x=300,y=330)
    Sup=Button(oot,text='Suppliers',bg='yellow',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black").place(x=300,y=420)
    stkin=Button(oot,text='StockIn',bg='magenta',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black").place(x=850,y=150)
    Cust=Button(oot,text='Customers',bg='orange',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black").place(x=850,y=240)
    Ord=Button(oot,text='Orders',bg='maroon',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black").place(x=850,y=330)
    Bil=Button(oot,text='Bill',bg='#B87333',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black").place(x=850,y=420)
    oot.mainloop()
def user():
    oot = Toplevel(root)
    oot.state("zoomed")
    oot.config(bg='#89CFEF')


   
    heading5=Canvas(oot,width=1700,height=60,bg='black',highlightbackground="black", highlightcolor="black")
    heading5.place(x=-1,y=1)
    heading=Label(
        oot,
        text="Stock Management System Dashboard",
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
        t=Toplevel(oot)
        t.state("zoomed")
        t.config(bg="grey")
        l1=Label(t,text="Action to Perform",font=("Rockwell Extra Bold",35),bg='white',fg='black' )
        l1.place(x=430,y=10)
        
        
        def store_find():
            tk=Toplevel(t)
            tk.state('zoomed')
            tk.config(bg="grey")
            tk.title('store screen find')
            
            def find():
                ct=MongoClient('localhost',27017)
                myd=ct['sms']
                myp=myd['store']
                gt1=e1.get()
                d={'Store_ID':gt1}
                data=myp.find_one(d)
                e2.delete(0,"end")
                e3.delete(0,"end")
                e4.delete(0,"end")
                e5.delete(0,"end")
                e6.delete(0,"end")
                e7.delete(0,"end")
                e2.insert(0,data["Store Name"])
                e3.insert(0,data["Store Address"])
                e4.insert(0,data["Store City"])
                e5.insert(0,data["Store Phone No"])
                e6.insert(0,data["Store Email ID"])
                e7.insert(0,data["Store Registration No"])
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
            bt1=Button(tk,text='Find', width=10, height=2, bg='blue', fg='white', font=customfont,command=find)
            bt1.place(x=575,y=575)
            tk.mainloop()
        
        
        
        def viewalldata():
            tk = tkinter.Tk() #change to Toplevel
            tk.state('zoomed')  # Fix the typo here
            tk.config(bg="grey")
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
                ct=MongoClient('localhost',27017)
                myd=ct['sms']
                myp=myd['store']
                data=list(myp.find({})) # converts from object to list

                for row in data:
                    a1.append(row['Store_ID'])
                    a2.append(row["Store Name"])
                    a3.append(row["Store Address"])
                    a4.append(row["Store City"])
                    a5.append(row["Store Phone No"])
                    a6.append(row["Store Email ID"])
                    a7.append(row["Store Registration No"])
           
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
                # Create a Tkinter window
                tk_window = tkinter.Tk()
                tk_window.title("Store Data")

                # Connect to the MongoDB database (assuming it's running on localhost and listening on the default port)
                client = MongoClient("localhost", 27017)
                db = client["sms"]  # Use the "SMS" database in MongoDB
                store_collection = db["store"]  # Use the "store" collection

                # Create a Treeview widget
                table = ttk.Treeview(tk_window, columns=("StoreID", "Name", "Address", "City", "PhoneNO", "EmailID", "RegistrationNo"), show="headings")

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

                # Insert data from MongoDB into the table
                for document in store_collection.find():
                    store_id = document.get("Store_ID")
                    name = document.get("Store Name")
                    address = document.get("Store Address")
                    city = document.get("Store City")
                    phone_no = document.get("Store Phone No")
                    email_id = document.get("Store Email ID")
                    registration_no = document.get("Store Registration No")

                    table.insert("", "end", values=(store_id, name, address, city, phone_no, email_id, registration_no))

                table.pack()
                tk_window.mainloop()




        
            
        Button(t,text='Find',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=store_find).place(x=600,y=175)
        Button(t,text='View all data',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=viewalldata).place(x=600,y=400)
        Button(t,text='Tabular form',bg='blue',relief="solid",width=10,font=("Helvetica",24),fg='white',highlightbackground='black', highlightcolor='black', highlightthickness=2,borderwidth=5,command=create_table).place(x=600,y=600)

        t.mainloop()

    
    st=Button(oot,text='Store',bg='green',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black",command=store).place(x=300,y=150)
    pc=Button(oot,text='ProductCategory',bg='pink',width=15,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black").place(x=250,y=240)
    pr=Button(oot,text='Product',bg='red',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black").place(x=300,y=330)
    Sup=Button(oot,text='Suppliers',bg='yellow',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black").place(x=300,y=420)
    stkin=Button(oot,text='StockIn',bg='magenta',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black").place(x=850,y=150)
    Cust=Button(oot,text='Customers',bg='orange',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black").place(x=850,y=240)
    Ord=Button(oot,text='Orders',bg='maroon',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black").place(x=850,y=330)
    Bil=Button(oot,text='Bill',bg='#B87333',width=10,font=("Cooper Black", 24),fg='black',relief="solid",borderwidth=8,highlightbackground="black", highlightcolor="black").place(x=850,y=420)
    oot.mainloop()
def check():

    usr = e1.get()
    pssw = e2.get()

    # Connect to MongoDB (assuming it's running on localhost and listening on the default port)
    client = MongoClient("localhost", 27017)
    db = client["sms"]
    users_collection = db["users"]

    user_data = users_collection.find_one({"username": usr})
    
    if user_data:
        if user_data["password"] == pssw:
            if user_data["user_type"] == "Admin":
                admin()
                
            else:
                user()
        else:
            messagebox.showerror("error", "Username and password do not match")
    else:
        messagebox.showerror("error", "User not found")

def forgot():
    win2 = Toplevel(root, bg='#89CFEF')
    win2.state('zoomed')

    l1 = Label(win2, text='Username', font=customfont, bg='#89CFEF')
    l1.place(x=350, y=200)
    e1 = Entry(win2, width=100, highlightbackground='black', highlightcolor='black', highlightthickness=2)
    e1.place(x=600, y=215)

    l2 = Label(win2, text='email_id', font=customfont, bg='#89CFEF')
    l2.place(x=350, y=375)
    e2 = Entry(win2, width=100, highlightbackground='black', highlightcolor='black', highlightthickness=2)
    e2.place(x=600, y=388)

    def mail():
        usr = e1.get()
        mailid = e2.get()

        # Connect to MongoDB
        client = MongoClient("mongodb://localhost:27017/")
        db = client["sms"]
        users_collection = db["users"]

        user_data = users_collection.find_one({"username": usr})

        if user_data:
            password = user_data["password"]
        else:
            messagebox.showerror('Error', 'Enter correct username')
            win2.destroy()

        from_address = "anjnaymahajan@gmail.com"
        to_address = mailid

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Test email"
        msg['From'] = from_address
        msg['To'] = to_address

        # Create the message (HTML).
        html = f" USERNAME = '{usr}' \n PASSWORD = '{password}'"

        # Record the MIME type - text/html.
        part1 = MIMEText(html, 'html')

        # Attach parts into the message container
        msg.attach(part1)

        # Credentials
        username = 'anjnaymahajan@gmail.com'
        password = 'jxraqsrukjcittsr'

        # Sending the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
    bt2=Button(win2,text="send mail", width=17, height=0, bg='black', fg='orange',font=('Rockwell Extra Bold',12),command=mail)
    bt2.place(x=1300,y=388)

    

bt2=Button(root,text="forgot password", width=17, height=0, bg='black', fg='orange',font=('Rockwell Extra Bold',12),command=forgot)
bt2.place(x=1300,y=388)


def save():
    win = Toplevel(root)
    win.state("zoomed")
    win.config(bg='#89CFEF')

    customfont = ('Rockwell Extra Bold', 48)

    heading = Label(win, text='SIGN UP', font=customfont, bg='#89CFEF')
    heading.place(x=550, y=30)

    l1 = Label(win, text='Username', font=('Rockwell Extra Bold', 28), bg='#89CFEF')
    l1.place(x=350, y=200)
    e1 = Entry(win, width=100, highlightbackground='black', highlightcolor='black', highlightthickness=2)
    e1.place(x=600, y=215)

    l2 = Label(win, text='Password', font=('Rockwell Extra Bold', 28), bg='#89CFEF')
    l2.place(x=350, y=375)
    e2 = Entry(win, width=100, highlightbackground='black', highlightcolor='black', highlightthickness=2)
    e2.place(x=600, y=388)

    def sn_admin():
        u = e1.get()
        p = e2.get()

        # Connect to MongoDB (assuming it's running on localhost and listening on the default port)
        client = MongoClient("localhost", 27017)
        db = client["sms"]
        users_collection = db["users"]

        user_data = {
            "username": u,
            "password": p,
            "user_type": "Admin"
        }

        users_collection.insert_one(user_data)

        messagebox.showinfo("insert", "New admin added")
        win.destroy()

    bt1 = Button(win, text="sign in as admin", width=15, height=0, bg='black', fg='orange',
                 font=('Rockwell Extra Bold', 12), command=sn_admin)
    bt1.place(x=550, y=500)

    def sn_regular():
        u = e1.get()
        p = e2.get()

        # Connect to MongoDB (assuming it's running on localhost and listening on the default port)
        client = MongoClient("localhost", 27017)
        db = client["sms"]
        users_collection = db["users"]

        user_data = {
            "username": u,
            "password": p,
            "user_type": "Regular"
        }

        users_collection.insert_one(user_data)

        messagebox.showinfo("insert", "New user added")
        win.destroy()

    bt2 = Button(win, text="sign in as user", width=15, height=0, bg='black', fg='orange',
                 font=('Rockwell Extra Bold', 12), command=sn_regular)
    bt2.place(x=800, y=500)

    win.mainloop()

bt1=Button(root,text="sign in", width=10, height=0, bg='black', fg='orange',font=('Rockwell Extra Bold',12),command=save)
bt1.place(x=650,y=500)

bt=Button(root,text="Login", width=10, height=0, bg='black', fg='orange',font=('Rockwell Extra Bold',12),command=check)
bt.place(x=500,y=500)
root.mainloop()