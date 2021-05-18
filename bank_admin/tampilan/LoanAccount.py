from tkinter import *
from tksheet import Sheet
from functools import partial
from tkinter.font import BOLD
from PIL import ImageTk, Image
from data.Account import AccountLoan as DataLoanAccount
from data.User import Customer as DataCustomer
class LoanAccount:
    def __init__(self):

        """
            Window Configuration
        """
        self.loan = Tk()
        self.window_height = 700                                            #Window Height
        self.window_width = 1100                                            #Window Width
        self.screen_width = self.loan.winfo_screenwidth()               #Screen Width
        self.screen_height = self.loan.winfo_screenheight()             #Screen Height
        self.x_cordinate = int((self.screen_width/2) - (self.window_width/2))
        self.y_cordinate = int((self.screen_height/2) - (self.window_height/2))
        self.loan.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, self.x_cordinate, 5))     #Implement and Center Window based on Device Screen
        self.loan.config(bg='#23374d')                                  #Window Background
        self.loan.overrideredirect(True)                                #Remove Window Status Bar
        self.loan.resizable(False, False)                               #Disable Resizing Window

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

        ##############################################################################
        ############                    SIDEBAR                             ##########
        ##############################################################################

        navbarLabel = Label(
            self.loan,
            bg='#e5e5e5',
            width=30,
            height=self.window_height
        )
        navbarLabel.place(x=0,y=0)

        #Dashboard Icon Navbar
        dashboardNavIcon = Label(
            self.loan,
            image=dashboardIMG,
            bg='#e5e5e5',
            cursor='hand2'
        )
        dashboardNavIcon.place(x=15,y=23)
        dashboardNavIcon.bind("<Button>",self.bindingToDashboard)
        #Dashboard Label Navbar
        dashboardNavLabel = Label(
            self.loan,
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
            self.loan,
            image=cusImage,
            bg='#e5e5e5',
            cursor='hand2'
        )
        allcusicon.place(x=10,y=73)
        allcusicon.bind("<Button>",self.bindingToCustomer)
        #Customer Label Navbar
        cusNavLabel = Label(
            self.loan,
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
            self.loan,
            image=savingImage,
            bg='#e5e5e5',
            cursor='hand2'
        )
        savingNavIcon.place(x=15,y=155)
        savingNavIcon.bind("<Button>",self.bindingToSavingAccount)
        #Saving Account Label Navbar
        savingNavLabel = Label(
            self.loan,
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
            self.loan,
            image=checkImage,
            bg='#e5e5e5',
            cursor='hand2'
        )
        checkNavIcon.place(x=15,y=245)
        checkNavIcon.bind("<Button>",self.bindingToCheckingAccount)
        #Checking Account Label Navbar
        checkNavLabel = Label(
            self.loan,
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
            self.loan,
            image=loanImage,
            bg='#e5e5e5',
            cursor='hand2'
        )
        loanNavIcon.place(x=15,y=335)
        loanNavIcon.bind("<Button>",self.bindingToLoanAccount)
        #Loan Account Label Navbar
        loanNavLabel = Label(
            self.loan,
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
            self.loan,
            image=logoutImage,
            bg='#e5e5e5',
            cursor='hand2'
        )
        logoutNavIcon.place(x=10,y=650)
        logoutNavIcon.bind("<Button>",self.doLogout)
        #Logout Label Navbar
        logoutNavLabel = Label(
            self.loan,
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

        #Customer Page Title
        cusTitle = Label(
            self.loan,
            text="Loan Account Bank",
            font=(
                'Segoe UI',
                20,
                BOLD
            ),
            bg='#23374d',
            fg='#e5e5e5'
        )
        cusTitle.place(x =550, y=20)

        #Exit Button Property
        exitButton = Button(
            self.loan,
            image=imgExit,
            border=0,
            bg='#23374d',
            activebackground='#23374d',
            command=self.loan.destroy,
            cursor='hand2'
        )
        exitButton.place(x=980, y=650)


        ##############################################################################
        ############                   LOAN ACCOUNT CONTENT                 ##########
        ##############################################################################

        loanAccount = DataLoanAccount()
        tmpData = loanAccount.getAllLoans()
        customer = DataCustomer()

        datas = []
        for dt in tmpData:
            tmpCustomer = customer.getCustomerById(dt.getId())

            tmpDt = (tmpCustomer.getName(), dt.getBalance())
            datas.append(tmpDt)
        
        headerLabel = ["Customer Name", "Account Balance"]
        #Account Table
        frame = Frame(self.loan)
        frame.grid_columnconfigure(0, weight = 1)
        frame.grid_rowconfigure(0, weight = 1)
        sheet = Sheet(frame,
            page_up_down_select_row = True,
            column_width = 120,
            startup_select = (0,1,"rows"),
            data = datas, #[[f"{data_example[1][1]}" for c in range(2)] for r in range(5)],
            headers = [f"{c}" for c in headerLabel],
            theme = "light green",
            height = 480,
            width = 700
        )
        sheet.enable_bindings((
            "single_select",
            "drag_select",
            "select_all",
            "column_drag_and_drop",
            "row_drag_and_drop",
            "column_select",
            "row_select",
            "column_width_resize",
            "double_click_column_resize",
            "row_width_resize",
            "column_height_resize",
            "arrowkeys",
            "row_height_resize",
            "double_click_row_resize",
            "right_click_popup_menu",
            "rc_select",
            "rc_insert_column",
            "rc_delete_column",
            "rc_insert_row",
            "rc_delete_row",
            "copy",
            "cut",
            "paste",
            "delete",
            "undo"
        ))
        frame.place(x=280,y=150)
        sheet.grid(row = 0, column = 0, sticky = "nswe")

        self.loan.mainloop()

    """
        Function Declaration
    """
    def bindingToDashboard(self, event):
        self.loan.destroy()
        from tampilan.Dashboard import Dashboard as DashWin
        DashWin()

    def bindingToCustomer(self, event):
        self.loan.destroy()
        from tampilan.Customer import Customer as CustWin
        CustWin()

    def bindingToSavingAccount(self, event):
        self.loan.destroy()
        from tampilan.CheckingAccount import CheckingAccount as CheckWin
        SavWin()

    def bindingToCheckingAccount(self, event):
        self.loan.destroy()
        from tampilan.CheckingAccount import CheckingAccount as CheckWin
        CheckWin()

    def bindingToLoanAccount(self, event):
        pass

    def doLogout(self, event):
        self.loan.destroy()
        from tampilan.SplashScreen import SplashScreen as Splash
        Splash()