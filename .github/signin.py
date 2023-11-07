from tkinter import *
from PIL import ImageTk

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
bgImage=ImageTk.PhotoImage(file='.github/bg1.png')
bgLabel=Label(login_window,image=bgImage)
bgLabel.grid(row=0,column=0)
bgLabel.place(x=0,y=0)

heading=Label(login_window,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='darkblue')
heading.place(x=660,y=50)

usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='darkblue')
usernameEntry.place(x=680,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)
frame1=Frame(login_window,width=250,height=2,bg='darkblue').place(x=680,y=200)
#blue line

passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='darkblue')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(login_window,width=250,height=2,bg='darkblue').place(x=680,y=260)
openeye=PhotoImage(file='.github/openeyeimg.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=258)

forgetButton=Button(login_window,text='Forgot password',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Microsoft Yahei UI Light',9,'bold'),fg='darkblue',activeforeground='darkblue')
forgetButton.place(x=715,y=295)

loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='darkblue',activebackground='darkblue',activeforeground='white',cursor='hand2',width=19)
loginButton.place(x=578,y=350)



orLabel=Label(login_window,text='-------------OR------------',font=('Open Sans',16),fg='darkblue',bg='white')
orLabel.place(x=583,y=400)

facebook_logo=PhotoImage(file='.github/facebook.png')
fbLabel=Label(login_window,image=facebook_logo,bg='white')
fbLabel.place(x=640,y=440)

google_logo=PhotoImage(file='.github/googleimg.png')
googleLabel=Label(login_window,image=google_logo,bg='white')
googleLabel.place(x=690,y=440)

twitter_logo=PhotoImage(file='.github/twitter1.png')
twitterLabel=Label(login_window,image=google_logo,bg='white')
twitterLabel.place(x=740,y=440)

signupLabel=Label(login_window,text='Dont have an account??',font=('Open Sans',9,'bold'),fg='darkblue',bg='white')
signupLabel.place(x=590,y=500)

newaccountButton=Button(login_window,text='Create new account',font=('Open Sans',9,'bold underline'),fg='darkblue', bg='white',activeforeground='darkblue',activebackground='white',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=727,y=500)


login_window.mainloop()