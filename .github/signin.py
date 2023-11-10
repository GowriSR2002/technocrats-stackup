from tkinter import *
from PIL import ImageTk
import pymysql

def topics_pg():
    login_window.destroy()
    import topics

def signup_page():
    login_window.destroy()
    import signup

def hide():
    openeye.config(file='.github/closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='.github/openeyeimg.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)
        
        
def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)


login_window=Tk()
login_window.geometry('990x600+50+50')
login_window.resizable(0,0)
login_window.title('Login Page')
bgImage=ImageTk.PhotoImage(file='.github/bgg1.png')
bgLabel=Label(login_window,image=bgImage)
bgLabel.grid(row=0,column=0)
bgLabel.place(x=0,y=0)

heading=Label(login_window,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='black')
heading.place(x=394,y=50)

usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='black')
usernameEntry.place(x=394,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)
frame1=Frame(login_window,width=250,height=1,bg='black').place(x=394,y=200)
#blue line

passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='black')
passwordEntry.place(x=394,y=260)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(login_window,width=250,height=1,bg='black').place(x=394,y=260)
openeye=PhotoImage(file='.github/openeyeimg.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=600,y=258)

forgetButton=Button(login_window,text='Forgot password',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Microsoft Yahei UI Light',9,'bold'),fg='black',activeforeground='black')
forgetButton.place(x=394,y=295)

loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='black',activebackground='black',activeforeground='white',cursor='hand2',bd=0,width=19,command=topics_pg)
loginButton.place(x=394,y=350)



orLabel=Label(login_window,text='-------------OR------------',font=('Open Sans',16),fg='black',bg='white')
orLabel.place(x=394,y=400)



signupLabel=Label(login_window,text='Dont have an account??',font=('Open Sans',9,'bold'),fg='black',bg='white')
signupLabel.place(x=394,y=440)

newaccountButton=Button(login_window,text='Create new account',font=('Open Sans',9,'bold underline'),fg='black', bg='white',activeforeground='black',activebackground='white',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=550,y=440)


login_window.mainloop()