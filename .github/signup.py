from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import pymysql


def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0,END)
    confirmpasswordEntry.delete(0,END)
    check.set(0)


def connect_database():
    if emailEntry.get()==''or usernameEntry.get()==''or passwordEntry.get()==''or confirmpasswordEntry.get()=='':
        messagebox.showerror('Error','All Feilds Are Required')
    elif passwordEntry.get()!=confirmpasswordEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get()==0:
         messagebox.showerror('Error','Please accept terms & conditions')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='root')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue,Please Try Again')
            return
        try:
            query='create database userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query) 
        except:
            mycursor.execute('use userdata')
        query='select * from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))
        row=mycursor.fetchone()
        if row !=None:
             messagebox.showerror('Error','Username Already Exists')
        else:   
            query='insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is successful')
            clear()
            signup_window.destroy()
            import signin      
            

              
         
        
   
def login_page():
    signup_window.destroy()
    import signin


signup_window=Tk()
signup_window.title('Sign Up')
signup_window.resizable(False,False)
background=ImageTk.PhotoImage(file='.github/bgg1.png')

bgLabel=Label(signup_window,image=background)
bgLabel.grid()

frame=Frame(signup_window)
frame.place(x=394,y=100)
heading=Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light',18,'bold'),bg='white',fg='black')
heading.grid(row=0,column=0,padx=10,pady=10)



emailLabel=Label(frame,text='Email',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='black')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))
emailEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='black')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)


usernameLabel=Label(frame,text='Username',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='black')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
usernameEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='black')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='black')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))
passwordEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='black')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmpasswordLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='black')
confirmpasswordLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))
confirmpasswordEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='black')
confirmpasswordEntry.grid(row=8,column=0,sticky='w',padx=25)
check=IntVar()

termsandcondition=Checkbutton(frame,text='I agree to the Terma & Conditions',font=('Microsoft Yahei UI Light',10,'bold'),fg='black',bg='white',activebackground='white',activeforeground='black',cursor='hand2',variable=check)
termsandcondition.grid(row=9,column=0,pady=10,padx=15)

signupButton=Button(frame,text='SignUp',font=('Open Sans',16,'bold'),bd=0,fg='white',bg='black',activebackground='black',activeforeground='black',width=17,command=connect_database)
signupButton.grid(row=10,column=0,pady=10)

alreadyaccount=Button(frame,text="Don't have an account?",font=('Open Sans','9','bold'),bg='white',fg='black')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginButton=Button(frame,text='Log in',font=('Open Sans','9','bold underline'),bg='white',fg='black',bd=0,cursor='hand2',activebackground='white',activeforeground='black',command=login_page)
loginButton.place(x=170,y=404)

signup_window.mainloop()