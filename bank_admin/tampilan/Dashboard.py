from tkinter import *
from tksheet import Sheet
from functools import partial
from tkinter.font import BOLD
from PIL import ImageTk, Image
from data.User import *
from data.Account import *

class Dashboard():
    def __init__(self):
        # datas
        customer = Customer()
        self._customers = customer.getAllCustomer()
        
        checkingAccount = AccountChecking()
        self._checkings = checkingAccount.getAllCheckings()

        savingAccount = AccountSaving()
        self._savingAccounts = savingAccount.getAllSavings()

        loanAccount = AccountLoan()
        self._loanAccounts = loanAccount.getAllLoans()
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
        self.dashroot.config(bg='#23374d')                                  #Window Background
        self.dashroot.overrideredirect(True)                                #Remove Window Status Bar
        self.dashroot.resizable(False, False)                               #Disable Resizing Window


        """
            Image Declaration
        """
        imgExit = PhotoImage(file='tampilan/images/exit-btn.png')
        #Dashboard Icon Navbar
        dashimage = Image.open('tampilan/images/dashboard.png')
        dashImage = dashimage.resize((38, 38), Image.ANTIALIAS)
        dashboardIMG = ImageTk.PhotoImage(dashImage)
        #Customer Icon Navbar
        cImage = Image.open('tampilan/images/customersicon.png')
        cuImage = cImage.resize((50, 50), Image.ANTIALIAS)
        cusImage = ImageTk.PhotoImage(cuImage)
        #Saving Icon Navbar
        saveImg = Image.open('tampilan/images/savingicon.png')
        sImage = saveImg.resize((30, 30), Image.ANTIALIAS)
        savingImage = ImageTk.PhotoImage(sImage)
        #Checking Icon Navbar
        checkImg = Image.open('tampilan/images/checkingicon.png')
        chImage = checkImg.resize((30, 30), Image.ANTIALIAS)
        checkImage = ImageTk.PhotoImage(chImage)
        #Loan Icon Navbar
        loanImg = Image.open('tampilan/images/loanicon.png')
        lImage = loanImg.resize((30, 30), Image.ANTIALIAS)
        loanImage = ImageTk.PhotoImage(lImage)
        #Logout Icon Navbar
        logoutImg = Image.open('tampilan/images/logout.png')
        logImage = logoutImg.resize((30, 30), Image.ANTIALIAS)
        logoutImage = ImageTk.PhotoImage(logImage)
        #Dashboard Info Background Icon Navbar
        cusInfoImg = Image.open('tampilan/images/info-bg.png')
        cInfoImg = cusInfoImg.resize((180, 180), Image.ANTIALIAS)
        cIImg = ImageTk.PhotoImage(cInfoImg)
        #Customer Icon Info
        ciIMG = Image.open('tampilan/images/customersicon.png')
        csImg = ciIMG.resize((80, 80), Image.ANTIALIAS)
        cusIMG = ImageTk.PhotoImage(csImg)
        #Saving Icon Info
        siIMG = Image.open('tampilan/images/savingicon.png')
        ssImg = siIMG.resize((80, 80), Image.ANTIALIAS)
        savIMG = ImageTk.PhotoImage(ssImg)
        #Checking Icon Info
        chIMG = Image.open('tampilan/images/checkingicon.png')
        chsImg = chIMG.resize((80, 80), Image.ANTIALIAS)
        cheIMG = ImageTk.PhotoImage(chsImg)
        #Loan Icon Info
        lsIMG = Image.open('tampilan/images/loanicon.png')
        losImg = lsIMG.resize((80, 80), Image.ANTIALIAS)
        loaIMG = ImageTk.PhotoImage(losImg)

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
        dashboardNavIcon.place(x=15,y=23)
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
        dashboardNavLabel.place(x=65, y=25)
        dashboardNavLabel.bind("<Button>",self.bindingToDashboard)

        #Customer Icon Navbar
        allcusicon = Label(
            self.dashroot,
            image=cusImage,
            bg='#e5e5e5',
            cursor='hand2'
        )
        allcusicon.place(x=10,y=73)
        allcusicon.bind("<Button>",self.bindingToCustomer)
        #Customer Label Navbar
        cusNavLabel = Label(
            self.dashroot,
            text="CUSTOMER",
            font=(
                'Segoe UI',
                16,
                BOLD
            ),
            bg='#e5e5e5',
            fg='#23374d',
            cursor='hand2'
        )
        cusNavLabel.place(x=65, y=80)
        cusNavLabel.bind("<Button>",self.bindingToCustomer)
        
        #Saving Account Icon Navbar
        savingNavIcon = Label(
            self.dashroot,
            image=savingImage,
            bg='#e5e5e5',
            cursor='hand2'
        )
        savingNavIcon.place(x=15,y=155)
        savingNavIcon.bind("<Button>",self.bindingToSavingAccount)
        #Saving Account Label Navbar
        savingNavLabel = Label(
            self.dashroot,
            text="SAVING \n ACCOUNT",
            font=(
                'Segoe UI',
                16,
                BOLD
            ),
            bg='#e5e5e5',
            fg='#23374d',
            cursor='hand2'
        )
        savingNavLabel.place(x=55, y=140)
        savingNavLabel.bind("<Button>",self.bindingToSavingAccount)

        #Checking Account Icon Navbar
        checkNavIcon = Label(
            self.dashroot,
            image=checkImage,
            bg='#e5e5e5',
            cursor='hand2'
        )
        checkNavIcon.place(x=15,y=245)
        checkNavIcon.bind("<Button>",self.bindingToCheckingAccount)
        #Checking Account Label Navbar
        checkNavLabel = Label(
            self.dashroot,
            text="CHECKING \n ACCOUNT",
            font=(
                'Segoe UI',
                16,
                BOLD
            ),
            bg='#e5e5e5',
            fg='#23374d',
            cursor='hand2'
        )
        checkNavLabel.place(x=55, y=230)
        checkNavLabel.bind("<Button>",self.bindingToCheckingAccount)

        #Loan Account Icon Navbar
        loanNavIcon = Label(
            self.dashroot,
            image=loanImage,
            bg='#e5e5e5',
            cursor='hand2'
        )
        loanNavIcon.place(x=15,y=335)
        loanNavIcon.bind("<Button>",self.bindingToLoanAccount)
        #Loan Account Label Navbar
        loanNavLabel = Label(
            self.dashroot,
            text="LOAN \n ACCOUNT",
            font=(
                'Segoe UI',
                16,
                BOLD
            ),
            bg='#e5e5e5',
            fg='#23374d',
            cursor='hand2'
        )
        loanNavLabel.place(x=55, y=320)
        loanNavLabel.bind("<Button>",self.bindingToLoanAccount)

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
            text="Admin Bank System Dashboard",
            font=(
                'Segoe UI',
                20,
                BOLD
            ),
            bg='#23374d',
            fg='#e5e5e5'
        )
        cusTitle.place(x =455, y=20)

        greetLabel = Label(
            text="Welcome to Bank Admin Management System",
            font=(
                'Segoe UI',
                16,
                BOLD
            ),
            fg='#e5e5e5',
            bg='#23374d'
        )
        greetLabel.place(x=430, y=80)

        """
            Dashboard Info Background Graphic User Interface
        """
        cusInfoLabel = Label(
            self.dashroot,
            image=cIImg,
            border=0,
            bg='#23374d',
        )
        cusInfoLabel.place(x=270,y=150)
        savingInfoLabel = Label(
            self.dashroot,
            image=cIImg,
            border=0,
            bg='#23374d',
        )
        savingInfoLabel.place(x=470,y=150)
        checkingInfoLabel = Label(
            self.dashroot,
            image=cIImg,
            border=0,
            bg='#23374d',
        )
        checkingInfoLabel.place(x=670,y=150)
        loanInfoLabel = Label(
            self.dashroot,
            image=cIImg,
            border=0,
            bg='#23374d',
        )
        loanInfoLabel.place(x=870,y=150)

        """
            Dashboard Info Icon Graphic User Interface
        """
        cusInfoIcon = Label(
            self.dashroot,
            image=cusIMG,
            border=0,
            bg='#e5e5e5',
        )
        cusInfoIcon.place(x=280,y=190)
        savingInfoIcon = Label(
            self.dashroot,
            image=savIMG,
            border=0,
            bg='#e5e5e5',
        )
        savingInfoIcon.place(x=480,y=190)
        checkingInfoIcon = Label(
            self.dashroot,
            image=cheIMG,
            border=0,
            bg='#e5e5e5',
        )
        checkingInfoIcon.place(x=680,y=190)
        loanInfoIcon = Label(
            self.dashroot,
            image=loaIMG,
            border=0,
            bg='#e5e5e5',
        )
        loanInfoIcon.place(x=880,y=190)

        """
            Dashboard Info Bottom Label Graphic User Interface
        """
        cusInfoBottom = Label(
            self.dashroot,
            text='Customer',
            font=(
                'Segoe UI',
                16,
            ),
            bg='#e5e5e5',
            fg='#23374d'
        )
        cusInfoBottom.place(x=315,y=280)
        savingInfoBottom = Label(
            self.dashroot,
            text='Saving Account',
            font=(
                'Segoe UI',
                16,
            ),
            bg='#e5e5e5',
            fg='#23374d'
        )
        savingInfoBottom.place(x=486,y=280)
        checkingInfoBottom = Label(
            self.dashroot,
            text='Checking Account',
            font=(
                'Segoe UI',
                15,
            ),
            bg='#e5e5e5',
            fg='#23374d'
        )
        checkingInfoBottom.place(x=679,y=280)
        loanInfoBottom = Label(
            self.dashroot,
            text='Loan Account',
            font=(
                'Segoe UI',
                16,
            ),
            bg='#e5e5e5',
            fg='#23374d'
        )
        loanInfoBottom.place(x=895,y=280)

        """
            Dashboard Info Number Graphic User Interface
        """
        #TODO
        cusInfoNumber = Label(
            self.dashroot,
            text= len(self._customers),
            font=(
                'Segoe UI',
                40,
                BOLD
            ),
            bg='#e5e5e5',
        )
        cusInfoNumber.place(x=380,y=190)
        savingInfoNumber = Label(
            self.dashroot,
            text= len(self._savingAccounts),
            font=(
                'Segoe UI',
                40,
                BOLD
            ),
            bg='#e5e5e5',
        )
        savingInfoNumber.place(x=580,y=190)
        checkingInfoNumber = Label(
            self.dashroot,
            text= len(self._savingAccounts),
            font=(
                'Segoe UI',
                40,
                BOLD
            ),
            bg='#e5e5e5',
        )
        checkingInfoNumber.place(x=780,y=190)
        loanInfoNumber = Label(
            self.dashroot,
            text= len(self._loanAccounts),
            font=(
                'Segoe UI',
                40,
                BOLD
            ),
            bg='#e5e5e5',
        )
        loanInfoNumber.place(x=980,y=190)

        #Exit Button Property
        exitButton = Button(
            self.dashroot,
            image=imgExit,
            border=0,
            bg='#23374d',
            activebackground='#23374d',
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

    def bindingToCustomer(self, event):
        self.dashroot.destroy()
        from tampilan.Customer import Customer as CustWin
        CustWin()

    def bindingToSavingAccount(self, event):
        self.dashroot.destroy()
        from tampilan.SavingAccount import SavingAccount as SavWin
        SavWin()

    def bindingToCheckingAccount(self, event):
        self.dashroot.destroy()
        from tampilan.CheckingAccount import CheckingAccount as CheckWin
        CheckWin()

    def bindingToLoanAccount(self, event):
        self.dashroot.destroy()
        from tampilan.LoanAccount import LoanAccount as LoanWin
        LoanWin()

    def doLogout(self, event):
        self.dashroot.destroy()
        from tampilan.SplashScreen import SplashScreen as Splash
        Splash()