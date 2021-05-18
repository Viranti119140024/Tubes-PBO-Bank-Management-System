from tkinter import *
from tksheet import Sheet
from functools import partial
from tkinter.font import BOLD
from PIL import ImageTk, Image
from data.Account import AccountSaving as DataSavingAccount
from data.User import Customer as DataCustomer
class SavingAccount:
    def __init__(self):

        """
            Window Configuration
        """
        self.savingroot = Tk()
        self.window_height = 700                                            #Window Height
        self.window_width = 1100                                            #Window Width
        self.screen_width = self.savingroot.winfo_screenwidth()               #Screen Width
        self.screen_height = self.savingroot.winfo_screenheight()             #Screen Height
        self.x_cordinate = int((self.screen_width/2) - (self.window_width/2))
        self.y_cordinate = int((self.screen_height/2) - (self.window_height/2))
        self.savingroot.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, self.x_cordinate, 5))     #Implement and Center Window based on Device Screen
        self.savingroot.config(bg='#23374d')                                  #Window Background
        self.savingroot.overrideredirect(True)                                #Remove Window Status Bar
        self.savingroot.resizable(False, False)                               #Disable Resizing Window

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

        """
            Function Declaration
        """
        def bindingToDashboard(event):
            print('Binded to Dashboard Window')

        def bindingToCustomer(event):
            print('Binded to Customer Window')

        def bindingToSavingAccount(event):
            print('Binded to Saving Account Window')

        def bindingToCheckingAccount(event):
            print('Binded to Checking Account Window')

        def bindingToLoanAccount(event):
            print('Binded to Loan Account Window')

        def doLogout(event):
            print('Successfully Logged Out')


        ##############################################################################
        ############                    SIDEBAR                             ##########
        ##############################################################################
        
        navbarLabel = Label(
            self.savingroot,
            bg='#e5e5e5',
            width=30,
            height=self.window_height
        )
        navbarLabel.place(x=0,y=0)

        #Dashboard Icon Navbar
        dashboardNavIcon = Label(
            self.savingroot,
            image=dashboardIMG,
            bg='#e5e5e5',
            cursor='hand2'
        )
        dashboardNavIcon.place(x=15,y=23)
        dashboardNavIcon.bind("<Button>",self.bindingToDashboard)
        #Dashboard Label Navbar
        dashboardNavLabel = Label(
            self.savingroot,
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
            self.savingroot,
            image=cusImage,
            bg='#e5e5e5',
            cursor='hand2'
        )
        allcusicon.place(x=10,y=73)
        allcusicon.bind("<Button>",self.bindingToCustomer)
        #Customer Label Navbar
        cusNavLabel = Label(
            self.savingroot,
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
            self.savingroot,
            image=savingImage,
            bg='#e5e5e5',
            cursor='hand2'
        )
        savingNavIcon.place(x=15,y=155)
        savingNavIcon.bind("<Button>",self.bindingToSavingAccount)
        #Saving Account Label Navbar
        savingNavLabel = Label(
            self.savingroot,
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
            self.savingroot,
            image=checkImage,
            bg='#e5e5e5',
            cursor='hand2'
        )
        checkNavIcon.place(x=15,y=245)
        checkNavIcon.bind("<Button>",self.bindingToCheckingAccount)
        #Checking Account Label Navbar
        checkNavLabel = Label(
            self.savingroot,
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
            self.savingroot,
            image=loanImage,
            bg='#e5e5e5',
            cursor='hand2'
        )
        loanNavIcon.place(x=15,y=335)
        loanNavIcon.bind("<Button>",self.bindingToLoanAccount)
        #Loan Account Label Navbar
        loanNavLabel = Label(
            self.savingroot,
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
            self.savingroot,
            image=logoutImage,
            bg='#e5e5e5',
            cursor='hand2'
        )
        logoutNavIcon.place(x=10,y=650)
        logoutNavIcon.bind("<Button>",doLogout)
        #Logout Label Navbar
        logoutNavLabel = Label(
            self.savingroot,
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
        logoutNavLabel.bind("<Button>",doLogout)

        #Checking Account Page Title
        cusTitle = Label(
            self.savingroot,
            text="Saving Account Bank",
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
            self.savingroot,
            image=imgExit,
            border=0,
            bg='#23374d',
            activebackground='#23374d',
            command=self.savingroot.destroy,
            cursor='hand2'
        )
        exitButton.place(x=980, y=650)


        ##############################################################################
        ############                 SAVING ACCOUNT CONTENT                 ##########
        ##############################################################################

        savingAccount = DataSavingAccount()
        tmpData = savingAccount.getAllSavings()
        query = "SELECT a.id, b.customer_id, b.balance, a.interest_rate FROM saving a, accounts b WHERE a.account_id=b.id"
        customer = DataCustomer()

        datas = []
        for dt in tmpData:
            tmpCustomer = customer.getCustomerById(dt.getCustomerId())
            
            tmpDt = (tmpCustomer.getName(), dt.getBalance())
            datas.append(tmpDt)
        
        headerLabel = ["Customer Name","Account Balance"]
        
        #Account Table
        frame = Frame(self.savingroot)
        frame.grid_columnconfigure(0, weight = 1)
        frame.grid_rowconfigure(0, weight = 1)
        sheet = Sheet(frame,
            page_up_down_select_row = True,
            column_width = 120,
            startup_select = (0,1,"rows"),
            data = datas, # [[f"{data_example[1][1]}" for c in range(2)] for r in range(5)],
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

        self.savingroot.mainloop()

    """
        Function Declaration
    """
    
    def bindingToDashboard(self, event):
        self.savingroot.destroy()
        from tampilan.Dashboard import Dashboard as DashWin
        DashWin()

    def bindingToCustomer(self, event):
        self.savingroot.destroy()
        from tampilan.Customer import Customer as CustWin
        CustWin()

    def bindingToSavingAccount(self, event):
        pass

    def bindingToCheckingAccount(self, event):
        self.savingroot.destroy()
        from tampilan.CheckingAccount import CheckingAccount as CheckWin
        CheckWin()

    def bindingToLoanAccount(self, event):
        self.savingroot.destroy()
        from tampilan.LoanAccount import LoanAccount as LoanWin
        LoanWin()

    def doLogout(self, event):
        self.savingroot.destroy()
        from tampilan.SplashScreen import SplashScreen as Splash
        Splash()