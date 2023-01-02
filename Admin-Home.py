from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector

#--------------------LogIn Info
u="admin"
p="admin"
#--------------------DB Connection
db = mysql.connector.connect(user="root", passwd="admin",host="localhost")
cursor = db.cursor()
#--------------------End Of DB Connection
#--------------------Functions (SQL)
def createDatabase():
    try:
        sqlCheck="DROP DATABASE IF EXISTS rivendell_pourosova;"
        sql="CREATE DATABASE rivendell_pourosova;"
        cursor.execute(sqlCheck)
        cursor.execute(sql)
        messagebox.showinfo("Confirmation","Database is created.\nThank you.")

    except:
        messagebox.showwarning("Error","Sorry.\nSomething went wrong.")
    pass
#----------------Create Table   
def createTable():
    try:
        sqlcheck="DROP TABLE if exists rivendell_pourosova.user_info;"
        sql="CREATE TABLE rivendell_pourosova.user_info(username VARCHAR(20), password VARCHAR(15), NID VARCHAR(11) PRIMARY KEY, email VARCHAR(50), contact VARCHAR(11));"
        cursor.execute(sqlcheck)
        cursor.execute(sql)

        sql="INSERT INTO rivendell_pourosova.user_info(username,password,NID,email,contact) VALUES(%s,%s,%s,%s,%s);"
        for i in range(100):
            cursor.execute(sql,("mahadi"+str(i),"pass"+str(i),"99999"+str(i),"mahadi"+str(i)+"@gmail.com","01755555"+str(i)))

        sqlcheck="DROP TABLE if exists rivendell_pourosova.complain;"
        sql="CREATE TABLE rivendell_pourosova.complain(name VARCHAR(20), contact VARCHAR(15), ward VARCHAR(3), complains VARCHAR(500));"
        cursor.execute(sqlcheck)
        cursor.execute(sql)

        sql="INSERT INTO rivendell_pourosova.complain(name,contact,ward,complains) VALUES(%s,%s,%s,%s);"
        for i in range(10):
            cursor.execute(sql,("mahadi"+str(i),"01755555"+str(i),str(i),"Loram Ipsum kkkkkkkkkkkkkkkkkkkkkkkkkkk"))

        messagebox.showinfo("Confirmation","Table is created with some demo data.")

    except:
        messagebox.showwarning("Error","Sorry.\nSomething went wrong.")
        pass
    pass
#-----------------End of create table
#-----------------Update Information
def updateInfo():
    updateInforoot=Toplevel(root)
    updateInforoot.title("Update Information")
    updateInforoot.geometry("720x480")
    updateInforoot.config(bg="#00CC66")

    NIDEntry=Entry(updateInforoot)
    NIDEntry.insert(0,"NID")
    NIDEntry.place(relx=0.25,rely=0.2,width=200,height=30)

    sql="SELECT* FROM rivendell_pourosova.user_info WHERE NID=%s;"
    cursor.execute(sql,(NIDEntry.get(),))
    check=cursor.fetchall()

    usernameEntry=Entry(updateInforoot)
    usernameEntry.insert(0,"Username")
    usernameEntry.place(relx=0.2,rely=0.3,width=200,height=30)

    def updateUsername():
        if check:
            try:
                sql="UPDATE rivendell_pourosova.user_info SET username=%s WHERE NID=%s;"
                cursor.execute(sql,(usernameEntry.get(),NIDEntry.get()))
                messagebox.showinfo("Confirmation","Updated successfully.\nThank you.")
            except:
                messagebox.showwarning("Update Error","Sorry.\nUser Information can't be updated.")
                db.rollback()
        else:
            messagebox.showwarning(" ","Sorry.\nThere is no user with this NID.")

        pass

    usernameButton=Button(updateInforoot,text="Update",font=("Fira Code Bold",20),fg="#FFF",activeforeground="#FFF",bg="#F00",activebackground="#F00",borderwidth=0,command=updateUsername)
    usernameButton.place(relx=0.5,rely=0.3,width=100,height=30)

    passwordEntry=Entry(updateInforoot)
    passwordEntry.insert(0,"Password")
    passwordEntry.place(relx=0.2,rely=0.4,width=200,height=30)
#-----------------Update Password
    def updatePassword():
        if check:
            try:
                sql="UPDATE rivendell_pourosova.user_info SET password=%s WHERE NID=%s;"
                cursor.execute(sql,(passwordEntry.get(),NIDEntry.get()))
                messagebox.showinfo("Confirmation","Updated successfully.\nThank you.")
            except:
                messagebox.showwarning("Update Error","Sorry.\nUser Information can't be updated.")
                db.rollback()
        else:
            messagebox.showwarning(" ","Sorry.\nThere is no user with this NID.")
        pass

    passwordButton=Button(updateInforoot,text="Update",font=("Fira Code Bold",20),fg="#FFF",activeforeground="#FFF",bg="#F00",activebackground="#F00",borderwidth=0,command=updatePassword)
    passwordButton.place(relx=0.5,rely=0.4,width=101,height=30)

    emailEntry=Entry(updateInforoot)
    emailEntry.insert(0,"Email")
    emailEntry.place(relx=0.2,rely=0.5,width=200,height=30)

    def updateEmail():
        if check:
            try:
                sql="UPDATE rivendell_pourosova.user_info SET email=%s WHERE NID=%s;"
                cursor.execute(sql,(emailEntry.get(),NIDEntry.get()))
                messagebox.showinfo("Confirmation","Updated successfully.\nThank you.")
            except:
                messagebox.showwarning("Update Error","Sorry.\nUser Information can't be updated.")
                db.rollback()
        else:
            messagebox.showwarning(" ","Sorry.\nThere is no user with this password.")
        pass

    emailButton=Button(updateInforoot,text="Update",font=("Fira Code Bold",20),fg="#FFF",activeforeground="#FFF",bg="#F00",activebackground="#F00",borderwidth=0,command=updateEmail)
    emailButton.place(relx=0.5,rely=0.5,width=100,height=30)

    contactEntry=Entry(updateInforoot)
    contactEntry.insert(0,"Contact")
    contactEntry.place(relx=0.2,rely=0.6,width=200,height=30)

    def updateContact():
        if check:
            try:
                sql="UPDATE rivendell_pourosova.user_info SET contact=%s WHERE NID=%s;"
                cursor.execute(sql,(contactEntry.get(),NIDEntry.get()))
                messagebox.showinfo("Confirmation","Updated successfully.\nThank you.")
            except:
                messagebox.showwarning("Update Error","Sorry.\nUser Information can't be updated.")
                db.rollback()
        else:
            messagebox.showwarning(" ","Sorry.\nThere is no user with this password.")
        pass

    contactButton=Button(updateInforoot,text="Update",font=("Fira Code Bold",20),fg="#FFF",activeforeground="#FFF",bg="#F00",activebackground="#F00",borderwidth=0,command=updateContact)
    contactButton.place(relx=0.5,rely=0.6,width=100,height=30)

    pass
#-------------------End of update password
#-----------------End of update Information
#------------------Delete User
def deleteUser():
    deleteUser_root=Toplevel(root)
    deleteUser_root.title("Delete an user")
    deleteUser_root.geometry("480x200")
    deleteUser_root.config(bg="#00CC66")

    NIDEntry=Entry(deleteUser_root)
    NIDEntry.insert(0,"NID")
    NIDEntry.place(relx=0.25,rely=0.2,width=200,height=30)

    def delete():
        try:
            sql="SELECT* FROM rivendell_pourosova.user_info WHERE NID=%s;"
            cursor.execute(sql,(NIDEntry.get(),))
            check=cursor.fetchall()

            if check:
                sql="DELETE FROM rivendell_pourosova.user_info WHERE NID=%s;"
                cursor.execute(sql,(NIDEntry.get(),))
                db.commit()
                messagebox.showinfo("Confirmation","The user has been removed.")
            else:
                messagebox.showwarning(" ","Sorry.\nThere is no user with this password.")

        except:
            messagebox.showwarning("Error","Sorry.\Something went wrong.")

        pass

    deleteButton=Button(deleteUser_root,text="Delete",font=("Fira Code Bold",15),fg="#FFF",activeforeground="#FFF",bg="#F00",activebackground="#F00",borderwidth=0,command=delete)
    deleteButton.place(relx=0.35,rely=0.4,width=100,height=30)
    pass

#-----------------End of Delete User
#-----------------Delete Table
def deleteTable():
    try:
        sql1="DROP TABLE if exists rivendell_pourosova.user_info;"
        cursor.execute(sql1)
        sql2="DROP TABLE if exists rivendell_pourosova.complain;"
        cursor.execute(sql2)
        db.commit()
        # db.close()
        messagebox.showinfo("Confirmation","Deleted Successfully")
    except:
        messagebox.showwarning("Error","Sorry.\nSomething went wrong.\nThank you.")
    pass
#-----------------End of Delete Table
#-----------------Delete Database
def deleteDB():
    try:
        sql="DROP DATABASE IF EXISTS rivendell_pourosova;"
        cursor.execute(sql)
        db.commit()
        # db.close()
        messagebox.showinfo("Confirmation","Deleted Successfully")
    except:
        messagebox.showwarning("Error","Sorry.\nSomething went wrong.\nThank you.")
    pass
#-----------------End of Delete Database
#-------------------User Information
def UserInfo():
    userinforoot=Toplevel()
    userinforoot.geometry("1020x480")
    userinforoot.title("User Information")

    frame=Frame(userinforoot)
    frame.pack(pady=10)

    scroll=Scrollbar(frame)
    scroll.pack(side="right",fill=Y)

    tree=ttk.Treeview(frame,height=20,yscrollcommand=scroll.set)
    scroll.config(command=tree.yview)

    tree['column']=("username","password","NID","email","contact")

    tree.column("#0",width=0,stretch=NO)
    tree.column("username",width=200)
    tree.column("password",width=200)
    tree.column("NID",width=200)
    tree.column("email",width=200)
    tree.column("contact",width=200)

    tree.heading("username",text="Username")
    tree.heading("password",text="Password")
    tree.heading("NID",text="NID")
    tree.heading("email",text="Email")
    tree.heading("contact",text="Contact")

    tree.tag_configure('oddrow',background="cyan")
    tree.tag_configure('evenrow',background="lightblue")

    try:
        sql="SELECT* FROM rivendell_pourosova.user_info"
        cursor.execute(sql)
        result=cursor.fetchall()
        db.commit()

        j=0
        for i in result:
            if j%2==0:
                tree.insert(parent="",iid=i,index=END,values=(i[0],i[1],i[2],i[3],i[4]),tags=('evenrow',))
            else:
                tree.insert(parent="",iid=i,index=END,values=(i[0],i[1],i[2],i[3],i[4]),tags=('oddrow',))
            j+=1

    except:
        messagebox.showwarning("Error","Sorry.\nSomething went wrong.")

    tree.pack(pady=10)
    pass
#--------------------End of user info
#--------------------Complains
def Complains():
    complainroot=Toplevel()
    complainroot.geometry("1020x480")
    complainroot.title("User Information")

    frame=Frame(complainroot)
    frame.pack(pady=10)

    scroll=Scrollbar(frame)
    scroll.pack(side="right",fill=Y)

    tree=ttk.Treeview(frame,height=20,yscrollcommand=scroll.set)
    scroll.config(command=tree.yview)

    tree['column']=("name","contact","ward","complain")

    tree.column("#0",width=0,stretch=NO)
    tree.column("name",width=200)
    tree.column("contact",width=200)
    tree.column("ward",width=200)
    tree.column("complain",width=300)
    
    tree.heading("name",text="Name")
    tree.heading("contact",text="Contact")
    tree.heading("ward",text="Ward No.")
    tree.heading("complain",text="Complain")

    tree.tag_configure('oddrow',background="cyan")
    tree.tag_configure('evenrow',background="lightblue")

    sql="SELECT* FROM rivendell_pourosova.complain"
    cursor.execute(sql)
    result=cursor.fetchall()
    db.commit()

    j=0
    for i in result:
        if j%2==0:
            tree.insert(parent="",iid=i,index=END,values=(i[0],i[1],i[2],i[3]),tags=('evenrow',))
        else:
            tree.insert(parent="",iid=i,index=END,values=(i[0],i[1],i[2],i[3]),tags=('oddrow',))
        j+=1

    tree.pack(pady=10)
    pass
#--------------------End of complains
#--------------------End of Functions(SQL)
#--------------------Admin Panel Widget
def Main():
    Main_root=Toplevel(root)
    Main_root.title("Admin Panel")
    Main_root.geometry("1080x720")
    Main_root.config(bg="#00CC66")

    logo=Label(Main_root,image=pourosova,bg="#00CC66",borderwidth=0)
    logo.place(relx=0.35,rely=0)

    createDBButton=Button(Main_root,text="Create Database",font=("Fira Code Bold",20),fg="#FFF",activeforeground="#FFF",bg="#F00",activebackground="#F00",borderwidth=0,command=createDatabase)
    createDBButton.place(relx=0.0,rely=0.4,width=500,height=40)

    createTableButton=Button(Main_root,text="Create Table",font=("Fira Code Bold",20),fg="#FFF",activeforeground="#FFF",bg="#F00",activebackground="#F00",borderwidth=0,command=createTable)
    createTableButton.place(relx=0.0,rely=0.5,width=500,height=40)

    updateInfoButton=Button(Main_root,text="Update User information",font=("Fira Code Bold",20),fg="#FFF",activeforeground="#FFF",bg="#F00",activebackground="#F00",borderwidth=0,command=updateInfo)
    updateInfoButton.place(relx=0.0,rely=0.6,width=500,height=40)

    deleteUserButton=Button(Main_root,text="Delete an user",font=("Fira Code Bold",20),fg="#FFF",activeforeground="#FFF",bg="#F00",activebackground="#F00",borderwidth=0,command=deleteUser)
    deleteUserButton.place(relx=0.0,rely=0.7,width=500,height=40)

    UserInfoButton=Button(Main_root,text="See User Information",font=("Fira Code Bold",20),fg="#FFF",activeforeground="#FFF",bg="#F00",activebackground="#F00",borderwidth=0,command=UserInfo)
    UserInfoButton.place(relx=0.6,rely=0.4,width=500,height=40)

    seeComplainButton=Button(Main_root,text="Check Complains",font=("Fira Code Bold",20),fg="#FFF",activeforeground="#FFF",bg="#F00",activebackground="#F00",borderwidth=0,command=Complains)
    seeComplainButton.place(relx=0.6,rely=0.5,width=500,height=40)

    deleteTableButton=Button(Main_root,text="Delete Tables",font=("Fira Code Bold",20),fg="#FFF",activeforeground="#FFF",bg="#F00",activebackground="#F00",borderwidth=0,command=deleteTable)
    deleteTableButton.place(relx=0.6,rely=0.6,width=500,height=40)

    deleteDBButton=Button(Main_root,text="Delete Database",font=("Fira Code Bold",20),fg="#FFF",activeforeground="#FFF",bg="#F00",activebackground="#F00",borderwidth=0,command=deleteDB)
    deleteDBButton.place(relx=0.6,rely=0.7,width=500,height=40)

    pass

#--------------------
root=Tk()
root.geometry('480x720')
root.title("Admin LogIn")
root.config(bg="#00CC66")
#--------------------Image Upload Section
username=ImageTk.PhotoImage(Image.open("D:\\Python\\DBMS Project\\Images\\username.png"))
password=ImageTk.PhotoImage(Image.open("D:\\Python\\DBMS Project\\Images\\password.png"))
login=ImageTk.PhotoImage(Image.open("D:\\Python\\DBMS Project\\Images\\login.png"))
# img1=Image.open("D:\\Python\\DBMS Project\\Images\\Rivendell Pourosova.jpg")#Pourosova Logo
pourosova=ImageTk.PhotoImage(Image.open("D:\\Python\\DBMS Project\\Images\\Rivendell Pourosova.jpg").resize((350,350)))#Pourosova Logo
#--------------------
logo=Label(root,image=pourosova,bg="#00CC66",borderwidth=0)
logo.place(relx=0.15,rely=0)

usernameLabel=Label(root,image=username,bg="#00CC66")
usernameLabel.place(relx=0.25,rely=0.5)

usernameEntry=Entry(root)
usernameEntry.place(relx=0.35,rely=0.52,width=200,height=30)

passwordLabel=Label(root,image=password,bg="#00CC66")
passwordLabel.place(relx=0.25,rely=0.6)

passwordEntry=Entry(root)
passwordEntry.place(relx=0.35,rely=0.63,width=200,height=30)

#--------------------
def logIn():
    if usernameEntry.get()==u and passwordEntry.get()==p:
        Main()
    else:
        messagebox.showwarning("Login Failed","Sorry.\nAn error has been occured.\nPlease insert the correct Username or Password.\nThank You.")
#--------------------
loginButton=Button(root,image=login,borderwidth=0.0,bg="#00CC66",activebackground="#00CC66",command=logIn)
loginButton.place(relx=0.35,rely=0.8)
#--------------------
root.mainloop()
