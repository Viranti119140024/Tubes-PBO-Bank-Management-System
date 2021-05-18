from tkinter import *
from tksheet import Sheet
from functools import partial
from tkinter.font import BOLD
from PIL import ImageTk, Image
from data.Account import Account as DataAkun

class Account():
    def __init__(self, customer_id):
        self.customer_id = customer_id
        '''
            DATA
        '''
        akun = DataAkun()
        self.akun = akun.getAccountsByCustomerId(customer_id)

        """
            Window Configuration
        """
        self.aroot = Tk()
        self.window_height = 700                                         #Window Height
        self.window_width = 1100                                         #Window Width
        self.screen_width = self.aroot.winfo_screenwidth()               #Screen Width
        self.screen_height = self.aroot.winfo_screenheight()             #Screen Height
        self.x_cordinate = int((self.screen_width/2) - (self.window_width/2))
        self.y_cordinate = int((self.screen_height/2) - (self.window_height/2))
        self.aroot.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, self.x_cordinate, 5))     #Implement and Center Window based on Device Screen
        self.aroot.config(bg='#00bd56')                                  #Window Background
        self.aroot.overrideredirect(True)                              #Remove Window Status Bar
        self.aroot.resizable(False, False)                               #Disable Resizing Window


        """
            Image Declaration
        """
        imgTambah = PhotoImage(file='tampilan/images/tambah-btn.png')
        imgHapus = PhotoImage(file='tampilan/images/hapus-btn.png')
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
            self.aroot,
            bg='#e5e5e5',
            width=30,
            height=self.window_height
        )
        navbarLabel.place(x=0,y=0)
        
        #Dashboard Icon Navbar
        dashboardNavIcon = Label(
            self.aroot,
            image=dashboardIMG,
            bg='#e5e5e5',
            cursor='hand2'
        )
        dashboardNavIcon.place(x=15,y=25)
        dashboardNavIcon.bind("<Button>",self.bindingToDashboard)
        #Dashboard Label Navbar
        dashboardNavLabel = Label(
            self.aroot,
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
            self.aroot,
            image=accountImage,
            bg='#e5e5e5',
            cursor='hand2'
        )
        accNavIcon.place(x=15,y=80)
        accNavIcon.bind("<Button>",self.bindingToAccount)
        #Account Label Navbar
        accNavLabel = Label(
            self.aroot,
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
            self.aroot,
            image=transImage,
            bg='#e5e5e5',
            cursor='hand2'
        )
        transNavIcon.place(x=15,y=140)
        transNavIcon.bind("<Button>",self.bindingToTranscation)
        #Transaction Label Navbar
        transNavLabel = Label(
            self.aroot,
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
            self.aroot,
            image=logoutImage,
            bg='#e5e5e5',
            cursor='hand2'
        )
        logoutNavIcon.place(x=10,y=650)
        logoutNavIcon.bind("<Button>",self.doLogout)
        #Logout Label Navbar
        logoutNavLabel = Label(
            self.aroot,
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
            self.aroot,
            text="Customer's Account",
            font=(
                'Segoe UI',
                20,
                BOLD
            ),
            bg='#00bd56',
            fg='#e5e5e5'
        )
        cusTitle.place(x =500, y=20)

        #Add Account Button Property
        addCButton = Button(
            self.aroot,
            image=imgTambah,
            border=0,
            bg='#00bd56',
            activebackground='#00bd56',
            command=self.tambahAkun,
            cursor='hand2'
        )
        addCButton.place(x=960, y=550)
        
        headerLabel = ["Account Type","Balance"]
        data = []
        for raw in self.akun:
            tmpData = (raw.getType(), raw.getBalance())
            data.append(tmpData)

        #Account Table
        frame = Frame(self.aroot)
        frame.grid_columnconfigure(0, weight = 1)
        frame.grid_rowconfigure(0, weight = 1)
        sheet = Sheet(frame,
            page_up_down_select_row = True,
            column_width = 120,
            startup_select = (0,1,"rows"),
            data = data, # [[f"{data_example[1][1]}" for c in range(4)] for r in range(5)],
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
        frame.place(x=250,y=100)
        sheet.grid(row = 0, column = 0, sticky = "nswe")

        #Hapus Account Button Property
        hapusButton = Button(
            self.aroot,
            image=imgHapus,
            border=0,
            bg='#00bd56',
            activebackground='#00bd56',
            command=self.hapusAkun,
            cursor='hand2'
        )
        hapusButton.place(x=960, y=600)

        #Exit Button Property
        exitButton = Button(
            self.aroot,
            image=imgExit,
            border=0,
            bg='#00bd56',
            activebackground='#00bd56',
            command=self.aroot.destroy,
            cursor='hand2'
        )
        exitButton.place(x=970, y=650)

        self.aroot.mainloop()
    """
        Function Declaration
    """
    def tambahAkun(self):
        from tampilan.OpenAccount import OpenAccount
        self.aroot.destroy()
        OpenAccount(self.customer_id)

    def hapusAkun(self):
        self.aroot.destroy()
        from tampilan.DeleteAccount import DeleteAccount
        DeleteAccount(self.customer_id)

    def bindingToDashboard(self, event):
        self.aroot.destroy()
        from tampilan.Dashboard import Dashboard
        Dashboard(self.customer_id)

    def bindingToAccount(self, event):
        pass

    def bindingToTranscation(self, event):
        self.aroot.destroy()
        from tampilan.Transaction import Transaction
        Transaction(self.customer_id)

    def doLogout(self, event):
        self.aroot.destroy()
        from tampilan.SplashScreen import SplashScreen
        SplashScreen()