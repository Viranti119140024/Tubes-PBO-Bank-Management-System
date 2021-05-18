from tkinter import *
from tksheet import Sheet
from functools import partial
from tkinter.font import BOLD
from PIL import ImageTk, Image
from data.Account import Account
from data.Transaction import Transaction as DataTransaction
from tampilan.AddTransaction import AddTransaction

class Transaction():
    def __init__(self, customer_id, account_id=False):
        self.customer_id = customer_id
        
        """
            Window Configuration
        """
        self.transroot = Tk()
        self.window_height = 700                                         #Window Height
        self.window_width = 1100                                         #Window Width
        self.screen_width = self.transroot.winfo_screenwidth()               #Screen Width
        self.screen_height = self.transroot.winfo_screenheight()             #Screen Height
        self.x_cordinate = int((self.screen_width/2) - (self.window_width/2))
        self.y_cordinate = int((self.screen_height/2) - (self.window_height/2))
        self.transroot.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, self.x_cordinate, 5))     #Implement and Center Window based on Device Screen
        self.transroot.config(bg='#00bd56')                                  #Window Background
        self.transroot.overrideredirect(True)                              #Remove Window Status Bar
        self.transroot.resizable(False, False)                               #Disable Resizing Window


        """
            Image Declaration
        """
        imgTambah = PhotoImage(file='tampilan/images/tambah-btn.png')
        imgTampil = PhotoImage(file='tampilan/images/tampil-btn.png')
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
            self.transroot,
            bg='#e5e5e5',
            width=30,
            height=self.window_height
        )
        navbarLabel.place(x=0,y=0)
        
        #Dashboard Icon Navbar
        dashboardNavIcon = Label(
            self.transroot,
            image=dashboardIMG,
            bg='#e5e5e5',
            cursor='hand2'
        )
        dashboardNavIcon.place(x=15,y=25)
        dashboardNavIcon.bind("<Button>",self.bindingToDashboard)
        #Dashboard Label Navbar
        dashboardNavLabel = Label(
            self.transroot,
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
            self.transroot,
            image=accountImage,
            bg='#e5e5e5',
            cursor='hand2'
        )
        accNavIcon.place(x=15,y=80)
        accNavIcon.bind("<Button>",self.bindingToAccount)
        #Account Label Navbar
        accNavLabel = Label(
            self.transroot,
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
            self.transroot,
            image=transImage,
            bg='#e5e5e5',
            cursor='hand2'
        )
        transNavIcon.place(x=15,y=140)
        transNavIcon.bind("<Button>",self.bindingToTranscation)
        #Transaction Label Navbar
        transNavLabel = Label(
            self.transroot,
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
            self.transroot,
            image=logoutImage,
            bg='#e5e5e5',
            cursor='hand2'
        )
        logoutNavIcon.place(x=10,y=650)
        logoutNavIcon.bind("<Button>",self.doLogout)
        #Logout Label Navbar
        logoutNavLabel = Label(
            self.transroot,
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
            self.transroot,
            text="Customer's Transaction History",
            font=(
                'Segoe UI',
                20,
                BOLD
            ),
            bg='#00bd56',
            fg='#e5e5e5'
        )
        cusTitle.place(x =450, y=20)

        self.clickedAccount = StringVar()

        ac = Account()
        self.accounts = ac.getAccountsByCustomerId(self.customer_id)
        
        self.opt = []
        self.opt_id = []
        account_on_opt = 0
        for ac in self.accounts:
            self.opt.append(str(ac.getType())+str(ac.getId()))
            self.opt_id.append(ac.getId())
        accountOption = self.opt

        if account_id!=False:
            optidx = self.opt_id.index(account_id)
        else:
            optidx = 0
            
        self.clickedAccount.set(self.opt[optidx])
        # Create Dropdown menu
        accountType = OptionMenu( self.transroot, self.clickedAccount , *accountOption)
        accountType.config(
            width=53,
            height=2,
            font=(
                'normal',
                10,
                BOLD
            )
        )
        accountType.place(x=280,y=85)

        #Show Account Button Property
        showButton = Button(
            self.transroot,
            image=imgTampil,
            border=0,
            bg='#00bd56',
            activebackground='#00bd56',
            command=self.showTransaction,
            cursor='hand2'
        )
        showButton.place(x=710, y=80)

        #Add Account Button Property
        addCButton = Button(
            self.transroot,
            image=imgTambah,
            border=0,
            bg='#00bd56',
            activebackground='#00bd56',
            command=self.addTransaction,
            cursor='hand2'
        )
        addCButton.place(x=850, y=80)
        
        if account_id != False:
            t = DataTransaction()
            transactions = t.getTransactionsByAccountId(account_id)
            headerLabel = ["Account Id","Date/Time","Transaction Type","Amount", "Note"]

            if transactions != []:
                datas = [(str(dt.getAccountId()), str(dt.getTime()), str(dt.getType()), str(dt.getAmount()), str(dt.getNote())) for dt in transactions]
            else:
                datas = []
            #Account Table
            frame = Frame(self.transroot)
            frame.grid_columnconfigure(0, weight = 1)
            frame.grid_rowconfigure(0, weight = 1)
            sheet = Sheet(frame,
                page_up_down_select_row = True,
                column_width = 120,
                startup_select = (0,1,"rows"),
                data = datas, 
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

        #Exit Button Property
        exitButton = Button(
            self.transroot,
            image=imgExit,
            border=0,
            bg='#00bd56',
            activebackground='#00bd56',
            command=self.transroot.destroy,
            cursor='hand2'
        )
        exitButton.place(x=980, y=650)

        self.transroot.mainloop()
    
    """
        Function Declaration
    """
    def showTransaction(self):
        idx = self.opt.index(self.clickedAccount.get())
        choosen = self.accounts[idx]

        self.transroot.destroy()
        Transaction(self.customer_id, choosen.getId())

    def addTransaction(self):
        idx = self.opt.index(self.clickedAccount.get())
        choosen = self.accounts[idx]
        self.transroot.destroy()
        AddTransaction(self.customer_id, choosen)


    def bindingToDashboard(self, event):
        self.transroot.destroy()
        from tampilan.Dashboard import Dashboard
        Dashboard(self.customer_id)

    def bindingToAccount(self, event):
        self.transroot.destroy()
        from tampilan.Account import Account
        Account(self.customer_id)

    def bindingToTranscation(self, event):
        pass

    def doLogout(self, event):
        self.transroot.destroy()
        from tampilan.SplashScreen import SplashScreen
        SplashScreen()