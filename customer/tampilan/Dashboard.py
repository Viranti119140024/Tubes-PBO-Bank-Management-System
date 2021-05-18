from tkinter import *
from tksheet import Sheet
from functools import partial
from tkinter.font import BOLD
from PIL import ImageTk, Image
from data.Account import *
class Dashboard():
    def __init__(self, customer_id):
        self.customer_id = customer_id
        """
            DATAS
        """
        akun = Account()
        self.akun = akun.getAccountsByCustomerId(customer_id)

        self.saldoTotal = 0

        """
            Window Configuration
        """
        self.dashroot = Tk()
        self.window_height = 700                                            #Window Height
        self.window_width = 1100                                            #Window Width
        self.screen_width = self.dashroot.winfo_screenwidth()               #Screen Width
        self.screen_height = self.dashroot.winfo_screenheight()             #Screen Height
        self.x_cordinate = int((self.screen_width/2) - (self.window_width/2))
        self.y_cordinate = int((self.screen_height/2) - (self.window_height/2))
        self.dashroot.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, self.x_cordinate, 5))     #Implement and Center Window based on Device Screen
        self.dashroot.config(bg='#00bd56')                                  #Window Background
        # self.dashroot.overrideredirect(True)                                #Remove Window Status Bar
        self.dashroot.resizable(False, False)                               #Disable Resizing Window


        """
            Image Declaration
        """
        imgExit = PhotoImage(file='tampilan/images/exit-btn.png')
        #Dashboard Icon Navbar
        dashimage = Image.open('tampilan/images/dashboard.png')
        dashImage = dashimage.resize((38, 38), Image.ANTIALIAS)
        dashboardIMG = ImageTk.PhotoImage(dashImage)
        #Account Icon Navbar
        checkImg = Image.open('tampilan/images/checkingicon.png')
        chImage = checkImg.resize((35, 35), Image.ANTIALIAS)
        accountImage = ImageTk.PhotoImage(chImage)
        #Transaction Icon Navbar
        saveImg = Image.open('tampilan/images/transfer.png')
        sImage = saveImg.resize((30, 30), Image.ANTIALIAS)
        transImage = ImageTk.PhotoImage(sImage)
        #Logout Icon Navbar
        logoutImg = Image.open('tampilan/images/logout.png')
        logImage = logoutImg.resize((30, 30), Image.ANTIALIAS)
        logoutImage = ImageTk.PhotoImage(logImage)
        #Dashboard Info Background Icon Navbar
        cusInfoImg = Image.open('tampilan/images/info-bg.png')
        cInfoImg = cusInfoImg.resize((180, 180), Image.ANTIALIAS)
        cIImg = ImageTk.PhotoImage(cInfoImg)
        #Account Info
        siIMG = Image.open('tampilan/images/savingicon.png')
        ssImg = siIMG.resize((80, 80), Image.ANTIALIAS)
        savIMG = ImageTk.PhotoImage(ssImg)
        #Balance Info
        chIMG = Image.open('tampilan/images/checkingicon.png')
        chsImg = chIMG.resize((80, 80), Image.ANTIALIAS)
        cheIMG = ImageTk.PhotoImage(chsImg)


        ##############################################################################
        ############                    SIDEBAR CONTENT                     ##########
        ##############################################################################

        navbarLabel = Label(
            self.dashroot,
            bg='#e5e5e5',
            width=30,
            height=self.window_height
        )
        navbarLabel.place(x=0,y=0)
        
        #Dashboard Icon Navbar
        dashboardNavIcon = Label(
            self.dashroot,
            image=dashboardIMG,
            bg='#e5e5e5',
            cursor='hand2'
        )
        dashboardNavIcon.place(x=15,y=25)
        dashboardNavIcon.bind("<Button>",self.bindingToDashboard)
        #Dashboard Label Navbar
        dashboardNavLabel = Label(
            self.dashroot,
            text="DASHBOARD",
            font=(
                'Segoe UI',
                16,
                BOLD
            ),
            bg='#e5e5e5',
            fg='#23374d',
            cursor='hand2'
        )
        dashboardNavLabel.place(x=55, y=25)
        dashboardNavLabel.bind("<Button>",self.bindingToDashboard)

        #Account Icon Navbar
        accNavIcon = Label(
            self.dashroot,
            image=accountImage,
            bg='#e5e5e5',
            cursor='hand2'
        )
        accNavIcon.place(x=15,y=80)
        accNavIcon.bind("<Button>",self.bindingToAccount)
        #Account Label Navbar
        accNavLabel = Label(
            self.dashroot,
            text="ACCOUNT",
            font=(
                'Segoe UI',
                16,
                BOLD
            ),
            bg='#e5e5e5',
            fg='#23374d',
            cursor='hand2'
        )
        accNavLabel.place(x=55, y=80)
        accNavLabel.bind("<Button>",self.bindingToAccount)
        
        #Transaction Icon Navbar
        transNavIcon = Label(
            self.dashroot,
            image=transImage,
            bg='#e5e5e5',
            cursor='hand2'
        )
        transNavIcon.place(x=15,y=140)
        transNavIcon.bind("<Button>",self.bindingToTranscation)
        #Transaction Label Navbar
        transNavLabel = Label(
            self.dashroot,
            text="TRANSACTION",
            font=(
                'Segoe UI',
                16,
                BOLD
            ),
            bg='#e5e5e5',
            fg='#23374d',
            cursor='hand2'
        )
        transNavLabel.place(x=55, y=140)
        transNavLabel.bind("<Button>",self.bindingToTranscation)

        #Logout Icon Navbar
        logoutNavIcon = Label(
            self.dashroot,
            image=logoutImage,
            bg='#e5e5e5',
            cursor='hand2'
        )
        logoutNavIcon.place(x=10,y=650)
        logoutNavIcon.bind("<Button>",self.doLogout)
        #Logout Label Navbar
        logoutNavLabel = Label(
            self.dashroot,
            text="LOGOUT",
            font=(
                'Segoe UI',
                16,
                BOLD
            ),
            bg='#e5e5e5',
            fg='#23374d',
            cursor='hand2'
        )
        logoutNavLabel.place(x=50, y=650)
        logoutNavLabel.bind("<Button>",self.doLogout)


        ##############################################################################
        ############                    DASHBOARD CONTENT                   ##########
        ##############################################################################

        #Customer Page Title
        cusTitle = Label(
            self.dashroot,
            text="Customer Bank System Dashboard",
            font=(
                'Segoe UI',
                20,
                BOLD
            ),
            bg='#00bd56',
            fg='#e5e5e5'
        )
        cusTitle.place(x =450, y=20)

        greetLabel = Label(
            text="Welcome to Bank Customer Management System",
            font=(
                'Segoe UI',
                16,
                BOLD
            ),
            fg='#e5e5e5',
            bg='#00bd56'
        )
        greetLabel.place(x=430, y=80)

        """
            Dashboard Info Background Graphic User Interface
        """
        accountInfoLabel = Label(
            self.dashroot,
            image=cIImg,
            border=0,
            bg='#00bd56',
        )
        accountInfoLabel.place(x=570,y=150)

        """
            Dashboard Info Icon Graphic User Interface
        """
        accountInfoIcon = Label(
            self.dashroot,
            image=savIMG,
            border=0,
            bg='#e5e5e5',
        )
        accountInfoIcon.place(x=585,y=190)

        """
            Dashboard Info Bottom Label Graphic User Interface
        """
        accountInfoBottom = Label(
            self.dashroot,
            text='Account',
            font=(
                'Segoe UI',
                16,
            ),
            bg='#e5e5e5',
            fg='#23374d'
        )
        accountInfoBottom.place(x=610,y=280)
        
        """
            Dashboard Info Number Graphic User Interface
        """
        #TODO
        accountInfoNumber = Label(
            self.dashroot,
            text=len(self.akun),
            font=(
                'Segoe UI',
                40,
                BOLD
            ),
            bg='#e5e5e5',
        )
        accountInfoNumber.place(x=670,y=190)
        
        #Exit Button Property
        exitButton = Button(
            self.dashroot,
            image=imgExit,
            border=0,
            bg='#00bd56',
            activebackground='#00bd56',
            command=self.dashroot.destroy,
            cursor='hand2'
        )
        exitButton.place(x=980, y=650)

        self.dashroot.mainloop()


    """
        Function Declaration
    """
    def bindingToDashboard(self, event):
        pass

    def bindingToAccount(self, event):
        self.dashroot.destroy()
        from tampilan.Account import Account
        Account(self.customer_id)

    def bindingToTranscation(self, event):
        self.dashroot.destroy()
        from tampilan.Transaction import Transaction
        Transaction(self.customer_id)

    def doLogout(self, event):
        self.dashroot.destroy()
        from tampilan.SplashScreen import SplashScreen
        SplashScreen()