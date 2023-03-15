from tkinter import *
from tkinter.ttk import Combobox
from tkinter.messagebox import *
import pymysql


def login_window():
    root.destroy()
    import login


def clear():
    entryemail.delete(0, END)
    entrycontact.delete(0, END)
    entrypassword.delete(0, END)
    entryconfirmpassword.delete(0, END)
    entryfirstname.delete(0, END)
    entrylastname.delete(0, END)
    entryanswer.delete(0, END)
    comboquestion.current(0)
    check.set(0)



def register():
    if entryfirstname.get() == '' or entrylastname.get() == '' or entryemail.get() == '' or entrycontact.get() == '' or \
            entrypassword.get() == '' or entryconfirmpassword.get() == '' or comboquestion.get() == 'Select' or entryanswer.get() == '':
        showerror('Error', "All Fields Are Required", parent=root)

    elif len(entrypassword.get())!=8:
        showerror('Error',"Atleast 8 Characters Required!",parent=root)

    elif entrypassword.get() != entryconfirmpassword.get():
        showerror('Error', "Password Mismatch", parent=root)

    elif check.get() == 0:
        showerror('Error', "Please Agree To Our Terms & Conditions", parent=root)
    else:
            try:
                con = pymysql.connect(host='localhost', user='faizan', password='1234', database='employee2')
                cur = con.cursor()
                cur.execute('select * from employee where email=%s', entryemail.get())
                row = cur.fetchone()
                if row != None:
                    showerror('Error', "User Already Exists", parent=root)
                else:

                    cur.execute(
                        'insert into employee (f_name,l_name,contact,email,password,question,answer) values(%s,%s,%s,%s,%s,%s,%s)',
                        (entryfirstname.get(), entrylastname.get(),entrycontact.get(), entryemail.get(),
                         entrypassword.get(),comboquestion.get(),
                         entryanswer.get()))
                    con.commit()
                    con.close()
                    showinfo('Success', "Registration Successful", parent=root)
                    clear()
                    root.destroy()
                    import login
            except Exception as e:
                showerror('Error', f"Error due to: {e}", parent=root)


root = Tk() #for generating window
root.geometry('1350x710+10+10') #for width and height
root.title('Registration Portal')
bgimage=PhotoImage(file="Registerbg.png")
bglabel=Label(root,image=bgimage) #to see the image on the window
bglabel.place(x=0,y=0)

regframe=Frame(root,width =650,height=650,bg='white') #for frame container to add button
regframe.place(x=350,y=30)

titlelabel=Label(regframe,text='REGISTER',font=('Arial',22,'bold'),fg='black')
titlelabel.place(x=20,y=20)

firstnameLabel = Label(regframe, text='First Name', font=('times new roman', 18, 'bold'), bg='white',
                       fg='black', )
firstnameLabel.place(x=20, y=80)
entryfirstname = Entry(regframe, font=('times new roman', 18), bg='lightgray')
entryfirstname.place(x=20, y=115, width=250)

lastnameLabel = Label(regframe, text='Last Name', font=('times new roman', 18, 'bold'), bg='white',
                      fg='black', )
lastnameLabel.place(x=370, y=80)
entrylastname = Entry(regframe, font=('times new roman', 18), bg='lightgray')
entrylastname.place(x=370, y=115, width=250)

contactLabel = Label(regframe, text='Contact Number', font=('times new roman', 18, 'bold'), bg='white',
                     fg='black', )
contactLabel.place(x=20, y=200)
entrycontact = Entry(regframe, font=('times new roman', 18), bg='lightgray')
entrycontact.place(x=20, y=235, width=250)

emailLabel = Label(regframe, text='Email-id', font=('times new roman', 18, 'bold'), bg='white', fg='black', )
emailLabel.place(x=370, y=200)
entryemail = Entry(regframe, font=('times new roman', 18), bg='lightgray')
entryemail.place(x=370, y=235, width=250)

passwordLabel = Label(regframe, text='Password', font=('times new roman', 18, 'bold'), bg='white',
                      fg='black', )
passwordLabel.place(x=20, y=315)
entrypassword = Entry(regframe, font=('times new roman', 18), bg='lightgray',show='*')
entrypassword.place(x=20, y=350, width=250)

confirmpasswordLabel = Label(regframe, text='Confirm Password', font=('times new roman', 18, 'bold'),
                             bg='white',
                             fg='black', )
confirmpasswordLabel.place(x=370, y=315)

entryconfirmpassword = Entry(regframe, font=('times new roman', 18), bg='lightgray',show='*')
entryconfirmpassword.place(x=370, y=350, width=250)

questionLabel = Label(regframe, text='Security Question', font=('times new roman', 18, 'bold'), bg='white',
                      fg='black', )
questionLabel.place(x=20, y=430)
comboquestion = Combobox(regframe, font=('times new roman', 16), state='readonly', justify=CENTER)
comboquestion['values'] = ('Select', 'Your First Pet Name?', 'Your Birth Place Name?', 'Your Best Friend Name?',
                           'Your Favourite Teacher?', 'Your Favourite Hobby?')
comboquestion.place(x=20, y=465, width=250)
comboquestion.current(0)  #default

answerLabel = Label(regframe, text='Answer', font=('times new roman', 18, 'bold'), bg='white',
                    fg='black', )
answerLabel.place(x=370, y=430)
entryanswer = Entry(regframe, font=('times new roman', 18), bg='lightgray')
entryanswer.place(x=370, y=465, width=250)

check = IntVar()
checkButton = Checkbutton(regframe, text='I Agree All The Terms & Conditions', variable=check, onvalue=1,
                          offvalue=0, font=('times new roman', 14, 'bold'), bg='white')
checkButton.place(x=20, y=550)

button = PhotoImage(file='buttonn.png')
registerbutton = Button(regframe, image=button, border=0, cursor='hand2', bg='white', activebackground='white'
                        , activeforeground='white', command=register)
registerbutton.place(x=350, y=590)

loginimage = PhotoImage(file='LOG.png')
loginbutton1 = Button(regframe, image=loginimage, bd=0, cursor='hand2', bg='white', activebackground='white',
                      activeforeground='white', command=login_window)
loginbutton1.place(x=490, y=590)



root.mainloop()  #for holding the window on the screen

