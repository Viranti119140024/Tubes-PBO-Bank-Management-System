from tkinter import *
from functools import partial
from tkinter.font import BOLD
from PIL import ImageTk, Image
from data.User import *
from tampilan.Dashboard import *

class Login:
    def __init__(self):
        #Window Property
        self.loginroot = Tk()
        loginroot = self.loginroot
        window_height = 650
        window_width = 750

        global screen_width
        global screen_height
        screen_width = loginroot.winfo_screenwidth()
        screen_height = loginroot.winfo_screenheight()

        #Centering Window when show
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        loginroot.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        loginroot.config(bg='#23374d')
        loginroot.overrideredirect(True)
        loginroot.resizable(False, False)

        # Variable Declaration
        self.userName = StringVar()
        self.userPass = StringVar()

        # Image Declaration
        imgButton = PhotoImage(file='tampilan/images/login-btn.png')
        imgExit = PhotoImage(file='tampilan/images/exit-btn.png')
        sideIMG = Image.open('tampilan/images/login-bg.png')
        sideimage = sideIMG.resize((300, 300), Image.ANTIALIAS)
        my_sideimg = ImageTk.PhotoImage(sideimage)

        # Function Declaration
        # Login Processing 

        topTitle = Label(
            text='L O G I N  P A G E',
            font=(
                'Segoe UI',
                20,
                BOLD
            ),
            bg='#23374d',
            fg='#e5e5e5'
        )
        topTitle.place(x=430, y=80)

        sideLabel = Label(
            image=my_sideimg,
            bg='#23374d',
        )
        sideLabel.place(x=50, y=250)

        #Username Label Property
        usernameLabel = Label(
            loginroot,
            text="USERNAME",
            font=('Segoe UI', 18),
            bg='#23374d',
            fg='#e5e5e5'
        )
        usernameLabel.place(x=360,y=200)

        #Username Entry Property
        usernameEntry = Entry(
            loginroot,
            width=20,
            font=(
                'normal',
                15
            ),
            textvariable=self.userName,
            bd=3
        )
        usernameEntry.place(x=500, y=200)

        #Password Label Property
        passwordLabel = Label(
            loginroot,
            text="PASSWORD",
            font=('Segoe UI', 18),
            bg='#23374d',
            fg='#e5e5e5'
        )
        passwordLabel.place(x=360,y=250)

        #Password Entry Property
        passwordEntry = Entry(
            loginroot,
            width=20,
            textvariable=self.userPass,
            font=(
                'normal',
                15
            ),
            show=u'\u2022',
            bd=3
        )
        passwordEntry.place(x=500, y=250)

        #Login Button Property
        button = Button(
            loginroot,
            image=imgButton,
            border=0,
            bg='#23374d',
            activebackground='#23374d',
            command=self.someLoginProcess,
            cursor='hand2'
        )
        button.place(x=500, y=330)

        #Exit Button Property
        exitButton = Button(
            loginroot,
            image=imgExit,
            border=0,
            bg='#23374d',
            activebackground='#23374d',
            command=loginroot.destroy,
            cursor='hand2'
        )
        exitButton.place(x=20, y=590)
        self.loginroot.mainloop()
        

    def someLoginProcess(self):
        bank_admin = BankAdmin()

        if bank_admin.login(self.userName.get(), self.userPass.get())== True:
            #goto dashboard
            self.loginroot.destroy()
            dashboard = Dashboard()