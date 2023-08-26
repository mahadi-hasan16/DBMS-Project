from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector

#--------------------DB Connection
db = mysql.connector.connect(user="root", passwd="admin",host="localhost")
cursor = db.cursor()
#--------------------End Of DB Connection
#-------------Complain Box
def insertComplain():
	insertComplain_root=Toplevel(root)
	insertComplain_root.title("Complain")
	insertComplain_root.geometry("480x480")
	insertComplain_root.config(bg="#00CC66")

	Label(insertComplain_root,text="Name",font=("Fira Code Bold",12),bg="#00CC66").place(relx=0,rely=0.0)
	nameEntry=Entry(insertComplain_root)
	nameEntry.place(relx=0.2,rely=0.0,width=200,height=30)

	Label(insertComplain_root,text="Contact",font=("Fira Code Bold",12),bg="#00CC66").place(relx=0,rely=0.1)
	contactEntry=Entry(insertComplain_root)
	contactEntry.place(relx=0.2,rely=0.1,width=200,height=30)

	Label(insertComplain_root,text="Ward no.",font=("Fira Code Bold",12),bg="#00CC66").place(relx=0,rely=0.2)
	wardEntry=Entry(insertComplain_root)
	wardEntry.place(relx=0.2,rely=0.2,width=200,height=30)

	Label(insertComplain_root,text="State your complain-",font=("Fira Code Bold",12),bg="#00CC66").place(relx=0,rely=0.35)

	complain=Text(insertComplain_root,width=50,height=10)
	complain.place(relx=0.08,rely=0.45)

	def Submit():
		sql="INSERT INTO rivendell_pourosova.complain(name,contact,ward,complains) VALUES(%s,%s,%s,%s)"
		cursor.execute(sql,(nameEntry.get(),contactEntry.get(),wardEntry.get(),complain.get("1.0","end-1c")))
		db.commit()

		insertComplain_root.destroy()
		messagebox.showinfo("Submitted","Your complain has been submitted.\nThank you.")
		pass

	submitButton=Button(insertComplain_root,text="Submit",font=("Fira Code Bold",15),borderwidth=0,fg="#FFF",activeforeground="#FFF",bg="#F00",activebackground="#F00",command=Submit)
	submitButton.place(relx=0.4,rely=0.85,width=100,height=40)

	pass
#-------------End Of Complain Box
#-------------Birth Registration Widget
def birthRegistrationWidget():
	birthRegistrationWidget_root=Toplevel(root)
	birthRegistrationWidget_root.geometry('480x720')
	birthRegistrationWidget_root.title("Holding Tax")
	birthRegistrationWidget_root.config(bg="#00CC66")
	
	logo=Label(birthRegistrationWidget_root,image=pourosova,bg="#00CC66")
	logo.place(relx=0.1,rely=0)

	birthRegistration=Radiobutton(birthRegistrationWidget_root,text="Birth Registration",bg="#00CC66",activebackground="#00CC66",font=("Fira Code Bold",12),value=1)
	birthRegistration.place(relx=0.1,rely=0.4)

	birthCertificateCorrection=Radiobutton(birthRegistrationWidget_root,text="Birth Certificate Correction",bg="#00CC66",activebackground="#00CC66",font=("Fira Code Bold",12),value=2)
	birthCertificateCorrection.place(relx=0.1,rely=0.45)

	dateOfBirthLabel=Label(birthRegistrationWidget_root,text="Date of birth",bg="#00CC66",font=("Fira Code Bold",12))
	dateOfBirthLabel.place(relx=0.1,rely=0.6)

	dateOfBirthEntry=Entry(birthRegistrationWidget_root)
	dateOfBirthEntry.place(relx=0.55,rely=0.61)

	wardNoLabel=Label(birthRegistrationWidget_root,text="Ward no",bg="#00CC66",font=("Fira Code Bold",12))
	wardNoLabel.place(relx=0.1,rely=0.63)

	wardNoEntry=Entry(birthRegistrationWidget_root)
	wardNoEntry.place(relx=0.55,rely=0.64)

	birthCertificateNoLabel=Label(birthRegistrationWidget_root,text="Birth certificate no",bg="#00CC66",font=("Fira Code Bold",12))
	birthCertificateNoLabel.place(relx=0.1,rely=0.67)

	birthCertificateNoEntry=Entry(birthRegistrationWidget_root)
	birthCertificateNoEntry.place(relx=0.55,rely=0.68)

	def ok():
		birthRegistrationWidget_root.destroy()
		messagebox.showinfo("Confirmation","Your priliminary registration is completed.\nGo to your ward councellor for next procedure.\nThank you.")

	okButton=Button(birthRegistrationWidget_root,text="OK",font=("Fira Code Bold",15),borderwidth=0,fg="#FFF",activeforeground="#FFF",bg="#F00",activebackground="#F00",command=ok)
	okButton.place(relx=0.4,rely=0.9,width=90,height=40)

	pass
#-------------End of Birth Registration Widget
#-------------Pay Holding Tax Widget
def insertHoldingTaxInfo():
	insertHoldingTaxInfo_root=Toplevel(root)
	insertHoldingTaxInfo_root.geometry('480x720')
	insertHoldingTaxInfo_root.title("Holding Tax")
	insertHoldingTaxInfo_root.config(bg="#00CC66")
	
	logo=Label(insertHoldingTaxInfo_root,image=pourosova,bg="#00CC66")
	logo.place(relx=0.1,rely=0)

	holdingNoLabel=Label(insertHoldingTaxInfo_root,text="Holding no",bg="#00CC66",font=("Fira Code Bold",12))
	holdingNoLabel.place(relx=0.1,rely=0.5)

	holdingNoEntry=Entry(insertHoldingTaxInfo_root)
	holdingNoEntry.place(relx=0.33,rely=0.51)

	wardNoLabel=Label(insertHoldingTaxInfo_root,text="Ward no",bg="#00CC66",font=("Fira Code Bold",12))
	wardNoLabel.place(relx=0.1,rely=0.55)

	wardNoEntry=Entry(insertHoldingTaxInfo_root)
	wardNoEntry.place(relx=0.33,rely=0.56)

	bkashLabel=Label(insertHoldingTaxInfo_root,text="Bkash no",bg="#00CC66",font=("Fira Code Bold",12))
	bkashLabel.place(relx=0.1,rely=0.6)

	bkashEntry=Entry(insertHoldingTaxInfo_root)
	bkashEntry.place(relx=0.33,rely=0.61)

	def pay():
		if len(holdingNoEntry.get())==0 or len(wardNoEntry.get())==0 or len(bkashEntry.get())==0:
			messagebox.showwarning("Error","Please fill-up all the boxes.\nThank you.")
		else:
			messagebox.showinfo("Confirmation","Your Tax is paid.\nThank you.")
			insertHoldingTaxInfo_root.destroy()

	payButton=Button(insertHoldingTaxInfo_root,text="Pay",font=("Fira Code Bold",15),borderwidth=0,fg="#FFF",activeforeground="#FFF",bg="#F00",activebackground="#F00",command=pay)
	payButton.place(relx=0.4,rely=0.9,width=90,height=40)

	pass
#-------------End of Pay Holding Tax Widget
#-------------Welcome Widget
def Welcome():
	welcome_root=Toplevel(root)
	welcome_root.geometry("1080x720")
	welcome_root.config(bg="#00CC66")

	logo=Label(welcome_root,image=pourosova,bg="#00CC66",borderwidth=0)
	logo.place(relx=0.4,rely=0.1)

	def Menu():
		frame=Frame(welcome_root,width=300,height=720,bg="#CC0099")
		frame.place(x=0,y=0)

		def Complain():
			welcome_root.destroy()
			insertComplain()
			pass

		complainButton=Button(frame,text="Complain",font=("Courier New",20,"bold"),fg="#FFF",activeforeground="#FFF",bg="#F00",activebackground="#F00",borderwidth=0,command=Complain)
		complainButton.place(relx=0.0,rely=0.2,width=300,height=40)

		def complainStatus():
			messagebox.showinfo("Complain Status","We are reviewing your complain and going to take proper steps.\nThank You.")
			pass

		complain_statusButton=Button(frame,text="Complain Status",font=("Courier New",20,"bold"),fg="#FFF",activeforeground="#FFF",bg="#F00",activebackground="#F00",borderwidth=0,command=complainStatus)
		complain_statusButton.place(relx=0.0,rely=0.27,width=300,height=40)

		def birthRegistration():
			welcome_root.destroy()
			birthRegistrationWidget()
			pass

		birthRegistrationButton=Button(frame,text="Birth Registration\n/Correction",font=("Courier New",15,"bold"),fg="#FFF",activeforeground="#FFF",bg="#F00",activebackground="#F00",borderwidth=0,command=birthRegistration)
		birthRegistrationButton.place(relx=0.0,rely=0.34,width=315,height=40)

		def holdingTax():
			insertHoldingTaxInfo()
			pass

		holdingTaxButton=Button(frame,text="Pay Holding Tax",font=("Courier New",20,"bold"),fg="#FFF",activeforeground="#FFF",bg="#F00",activebackground="#F00",borderwidth=0,command=holdingTax)
		holdingTaxButton.place(relx=0.0,rely=0.41,width=300,height=40)

		def deleteAccount():
			deleteUser_root=Toplevel(root)
			deleteUser_root.title("Delete an user")
			deleteUser_root.geometry("480x200")
			deleteUser_root.config(bg="#00CC66")

			NIDEntry=Entry(deleteUser_root)
			NIDEntry.insert(0,"NID")
			NIDEntry.place(relx=0.25,rely=0.2,width=200,height=30)

			def delete():
				sql="SELECT* FROM rivendell_pourosova.user_info WHERE NID=%s;"
				cursor.execute(sql,(NIDEntry.get(),))
				check=cursor.fetchall()

				if check:
					sql="DELETE FROM rivendell_pourosova.user_info WHERE NID=%s;"
					cursor.execute(sql,(NIDEntry.get(),))
					db.commit()
					messagebox.showinfo("Confirmation","Your account has been deleted.")
				else:
					messagebox.showwarning(" ","Sorry.\nInvalid password.")
					pass

			deleteButton=Button(deleteUser_root,text="Delete",font=("Fira Code Bold",15),fg="#FFF",activeforeground="#FFF",bg="#F00",activebackground="#F00",borderwidth=0,command=delete)
			deleteButton.place(relx=0.35,rely=0.4,width=100,height=30)
			pass


		delete_accountButton=Button(frame,text="Delete Account",font=("Courier New",20,"bold"),fg="#FFF",activeforeground="#FFF",bg="#F00",activebackground="#F00",borderwidth=0,command=deleteAccount)
		delete_accountButton.place(relx=0.0,rely=0.48,width=300,height=40)

		def Close():
			frame.destroy()
		closeButton=Button(frame,image=close,bg="#CC0099",activebackground="#CC0099",borderwidth=0,command=Close)
		closeButton.place(x=0,y=0)
	#-------------Menu Button
	menuButton=Button(welcome_root,image=menu,bg="#00CC66",activebackground="#00CC66",borderwidth=0,command=Menu)
	menuButton.place(x=0,y=0)
#-------------End Of Welcome Widget
#-------------Log In Widget
def Login():
	login_root=Toplevel(root)
	login_root.geometry('480x720')
	login_root.title("LogIn")
	login_root.config(bg="#00CC66")
	
	logo=Label(login_root,image=pourosova,bg="#00CC66")
	logo.place(relx=0.1,rely=0)

	usernameLabel=Label(login_root,image=username,bg="#00CC66")
	usernameLabel.place(relx=0.15,rely=0.5)

	passwordLabel=Label(login_root,image=password,bg="#00CC66")
	passwordLabel.place(relx=0.15,rely=0.6)

	usernameEntry=Entry(login_root)
	usernameEntry.insert(0,"Username")
	usernameEntry.place(relx=0.26,rely=0.52,width=200,height=30)

	passwordEntry=Entry(login_root)
	passwordEntry.insert(0,"Password")
	passwordEntry.place(relx=0.26,rely=0.63,width=200,height=30)

	def LogIn():
		sql="SELECT* FROM rivendell_pourosova.user_info WHERE username=%s and password=%s;"
		cursor.execute(sql,(usernameEntry.get(),passwordEntry.get()))
		check=cursor.fetchall()

		if check:
			login_root.destroy()
			messagebox.showinfo(" ","Login Successful")
			Welcome()
		else:
			messagebox.showwarning(" ","Sorry.\nIncorrect username or password.")

	loginButton=Button(login_root,text="LogIn",font=("Fira Code Bold",20),borderwidth=0,fg="#FFF",activeforeground="#FFF",bg="#F00",activebackground="#F00",command=LogIn)
	loginButton.place(relx=0.4,rely=0.85,width=100,height=40)

#-------------Create Account Widget
def createAccount():
	createAccount_root=Toplevel(root)
	createAccount_root.geometry("480x750")
	createAccount_root.title("Create Your Account")
	createAccount_root.config(bg="#00CC66")

	logo=Label(createAccount_root,image=pourosova,borderwidth=0)
	logo.place(relx=0.1,rely=0.0)

	usernameLabel=Label(createAccount_root,image=username,borderwidth=0,bg="#00CC66")
	usernameLabel.place(relx=0.1,rely=0.4)

	usernameEntry=Entry(createAccount_root)
	usernameEntry.insert(0,"Username")
	usernameEntry.place(relx=0.2,rely=0.412,width=200,height=30)

	passwordLabel=Label(createAccount_root,image=password,borderwidth=0,bg="#00CC66")
	passwordLabel.place(relx=0.1,rely=0.48)

	passwordEntry=Entry(createAccount_root)
	passwordEntry.insert(0,"Password")
	passwordEntry.place(relx=0.2,rely=0.51,width=200,height=30)

	rePasswordLabel=Label(createAccount_root,image=password,borderwidth=0,bg="#00CC66")
	rePasswordLabel.place(relx=0.1,rely=0.56) #Re Enter Password

	repasswordEntry=Entry(createAccount_root)
	repasswordEntry.insert(0,"Re enter password")
	repasswordEntry.place(relx=0.2,rely=0.58,width=200,height=30)

	nidLabel=Label(createAccount_root,image=nid,borderwidth=0,bg="#00CC66")
	nidLabel.place(relx=0.1,rely=0.64)

	nidEntry=Entry(createAccount_root)
	nidEntry.insert(0,"NID")
	nidEntry.place(relx=0.2,rely=0.66,width=200,height=30)

	emailLabel=Label(createAccount_root,image=email,borderwidth=0,bg="#00CC66")
	emailLabel.place(relx=0.1,rely=0.72)

	emailEntry=Entry(createAccount_root)
	emailEntry.insert(0,"Email")
	emailEntry.place(relx=0.2,rely=0.74,width=200,height=30)

	contactLabel=Label(createAccount_root,image=contact,borderwidth=0,bg="#00CC66")
	contactLabel.place(relx=0.1,rely=0.8)

	contactEntry=Entry(createAccount_root)
	contactEntry.insert(0,"Contact")
	contactEntry.place(relx=0.2,rely=0.81,width=200,height=30)
#---------------------------------
	def Next():
		try:
			if passwordEntry.get()==repasswordEntry.get():
				sql="INSERT INTO rivendell_pourosova.user_info(username,password,NID,email,contact) VALUES(%s,%s,%s,%s,%s)"
				cursor.execute(sql,(usernameEntry.get(),passwordEntry.get(),nidEntry.get(),emailEntry.get(),contactEntry.get()))
				db.commit()
				createAccount_root.destroy()
				messagebox.showinfo("Succesful!","Your Account is created")
				Welcome()
			else:
				messagebox.showwarning("Error","Sorry\nDoesn't match the password.")
		except:
			messagebox.showwarning("Failed","Sorry.\nAn account has been created using this NID.\nThank You")

#---------------------------------
	nextButton=Button(createAccount_root,text="Next",font=("Fira Code Bold",20),borderwidth=0,bg="#F00",activebackground="#F00",command=Next)
	nextButton.place(relx=0.75,rely=0.9,width=100,height=40)
	pass
#-------------Main Window
root=Tk()
root.title("Home")
root.geometry("1080x720")
root.config(bg="#00CC66")
#--------------Image Upload Section
menu=ImageTk.PhotoImage(Image.open("D:\\Python\\DBMS Project\\Images\\menu.png"))#Menu Button
close=ImageTk.PhotoImage(Image.open("D:\\Python\\DBMS Project\\Images\\close.png"))#Close Button
pourosova=ImageTk.PhotoImage(Image.open("D:\\Python\\DBMS Project\\Images\\Rivendell Pourosova.jpg").resize((350,350)))#Pourosova Logo
img2=Image.open("D:\\Python\\DBMS Project\\Images\\Mayor.jpg")#Mayor Image
Mayor=ImageTk.PhotoImage(img2.resize((250,300)))#Mayor Image Resize
login=ImageTk.PhotoImage(Image.open("D:\\Python\\DBMS Project\\Images\\login.png"))#LogIn Button
createaccount=ImageTk.PhotoImage(Image.open("D:\\Python\\DBMS Project\\Images\\create_account.png"))#Create Account Button
contact=ImageTk.PhotoImage(Image.open("D:\\Python\\DBMS Project\\Images\\contact.png"))#Contact Label
email=ImageTk.PhotoImage(Image.open("D:\\Python\\DBMS Project\\Images\\email.png"))#Email Label
password=ImageTk.PhotoImage(Image.open("D:\\Python\\DBMS Project\\Images\\password.png"))#Password Label
username=ImageTk.PhotoImage(Image.open("D:\\Python\\DBMS Project\\Images\\username.png"))#Username Label
nxt=ImageTk.PhotoImage(Image.open("D:\\Python\\DBMS Project\\Images\\next.png"))#Next Button
nid=ImageTk.PhotoImage(Image.open("D:\\Python\\DBMS Project\\Images\\nid.png"))#NID Label
otp=ImageTk.PhotoImage(Image.open("D:\\Python\\DBMS Project\\Images\\otp.png"))#OTP Label
#--------------Home Page Logo 
background_image=Label(root,image=pourosova,borderwidth=0)
background_image.place(relx=0.6,rely=0.0)
#-------------Mayor Section
history="Rivendell Pourosova was established on\n29 November 2011. Prior to the establishment of the pourosova,\n this urban area was governed by the\nUNO of the Rivendell. The first Rivendell Pourosova election\nwere held on 28 April 2014, which saw the\nvictory of Bilbo Beggins."

aboutMayor="Md. Mahadi Hasan(2020-  )"

mayor=Frame(root,width=500,height=720,bg="#9900FF")
mayor.pack(side="left")

l=Label(mayor,text="Mayor of Rivendell:",bg="#9900FF",fg="#000",font=("Fira Code Bold",15))
l.place(relx=0.0,rely=0.0)

mayorImage=Label(mayor,image=Mayor,borderwidth=2)#Mayor Image Label
mayorImage.place(relx=0.2,rely=0.07)

mayorIntroduction=Label(mayor,text=aboutMayor,bg="#9900FF",fg="#000",font=("Fira Code Bold",15))
mayorIntroduction.place(relx=0.15,rely=0.5)

rivendellHistory=Label(mayor,text=history,font=("Fira Code Bold", 10),bg="#9900FF",fg="#FFF")
rivendellHistory.place(relx=0,rely=0.7)
#-------------Log In Button
loginButton=Button(root,image=login,bg="#00CC66",activebackground="#00CC66",borderwidth=0,command=Login)
loginButton.place(relx=0.69,rely=0.4)
#-------------Create Account Button
createaccountButton=Button(root,image=createaccount,bg="#00CC66",activebackground="#00CC66",borderwidth=0,command=createAccount)
createaccountButton.place(relx=0.65,rely=0.5)
#-------------
root.mainloop()