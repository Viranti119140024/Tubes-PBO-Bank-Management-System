from tkinter import *
from functools import partial
from tkinter.font import BOLD
from PIL import ImageTk, Image
from data.Account import Account
# from data.Account import Account as DataAkun

class DeleteAccount():
    def __init__(self, customer_id):
        """
            Window Configuration
        """
        self.customer_id = customer_id
        self.destroyAccRoot = Tk()
        window_height = 650                                         #Window Height
        window_width = 750                                          #Window Width
        screen_width = self.destroyAccRoot.winfo_screenwidth()        #Screen Width
        screen_height = self.destroyAccRoot.winfo_screenheight()      #Screen Height
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.destroyAccRoot.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))     #Implement and Center Window based on Device Screen
        self.destroyAccRoot.config(bg='#00bd56')                      #Window Background
        # self.destroyAccRoot.overrideredirect(True)                    #Remove Window Status Bar
        self.destroyAccRoot.resizable(False, False)                   #Disable Resizing Window

        """
            Image Declaration
        """
        imgSubmit = PhotoImage(file='tampilan/images/submit-btn.png')
        imgExit = PhotoImage(file='tampilan/images/exit-btn.png')

        sideIMG = Image.open('tampilan/images/ca.png')
        sideimage = sideIMG.resize((300, 200), Image.ANTIALIAS)
        my_sideimg = ImageTk.PhotoImage(sideimage)
        
        backIMG = Image.open('tampilan/images/back-btn.png')
        backimage = backIMG.resize((60, 50), Image.ANTIALIAS)
        BACKimg = ImageTk.PhotoImage(backimage)

        ac = Account()
        self.accounts = ac.getAccountsByCustomerId(self.customer_id)

        self.opt = []
        self.opt_id = []
        account_on_opt = 0
        for ac in self.accounts:
            self.opt.append(str(ac.getType())+str(ac.getId()))
            self.opt_id.append(ac.getId())
        accountOption = self.opt


        """
            Input String Declaration
        """
        self.clickedAccountOpt = StringVar()
        self.amount = IntVar()

        accountList = self.opt

        ##############################################################################
        ############                   OPEN ACCOUNT CONTENT                 ##########
        ##############################################################################
        # Top Title
        destroyAccRootTitle = Label(
            text='DELETE ACCOUNT PAGE',
            font=(
                'Segoe UI',
                20,
                BOLD
            ),
            bg='#00bd56',
            fg='#e5e5e5'
        )
        destroyAccRootTitle.place(x=330, y=80)

        # Side Image
        backLabel = Label(
            image=BACKimg,
            bg='#00bd56',
            cursor="hand2"
        )
        backLabel.place(x=20, y=15)
        backLabel.bind("<Button>",self.doBack)

        # Side Image
        sideLabel = Label(
            image=my_sideimg,
            bg='#00bd56',
        )
        sideLabel.place(x=50, y=350)

        transTypeLabel =Label(
            text="ACCOUNT TYPE",
            fg='#e5e5e5',
            bg='#00bd56',
            font=(
                'Segoe UI',
                18
            )
        )
        transTypeLabel.place(x=250,y=180)

        self.clickedAccountOpt.set(accountList[0])

        # Create Transaction Type Dropdown menu
        transTypeDropdown = OptionMenu( self.destroyAccRoot , self.clickedAccountOpt , *accountList)
        transTypeDropdown.config(
            width=26,
            font=(
                'normal',
                10,
                BOLD
            )
        )
        transTypeDropdown.place(x=500,y=180)

        #Submit Button Property
        submitButton = Button(
            self.destroyAccRoot,
            image=imgSubmit,
            border=0,
            bg='#00bd56',
            activebackground='#00bd56',
            command=self.submitDelete,
            cursor='hand2'
        )
        submitButton.place(x=610, y=270)

        #Exit Button Property
        exitButton = Button(
            self.destroyAccRoot,
            image=imgExit,
            border=0,
            bg='#00bd56',
            activebackground='#00bd56',
            command=self.exit,
            cursor='hand2'
        )
        exitButton.place(x=20, y=590)

        self.destroyAccRoot.mainloop()

    """
        Function Declaration
    """
    def submitDelete(self):
        idx = self.opt.index(self.clickedAccountOpt.get())
        choosen = self.accounts[idx]

        # find
        if choosen.getType()=='saving':
            from data.Account import AccountSaving
            sv = AccountSaving()
            sv = sv.getSavingByAccountId(choosen.getId())
            sv.destroy()

        if choosen.getType()=='loan':
            from data.Account import AccountLoan
            ac = AccountLoan()
            ac = ac.getLoanByAccountId(choosen.getId())
            ac.destroy()

        if choosen.getType()=='checking':
            from data.Account import AccountChecking
            ck = AccountChecking()
            ck = ck.getCheckingByAccountId(choosen.getId())
            ck.destroy()

        self.exit()

    def exit(self):
        from tampilan.Account import Account as WinAccount

        self.destroyAccRoot.destroy()
        WinAccount(self.customer_id)

    def doBack(self, event):
        from tampilan.Account import Account
        self.destroyAccRoot.destroy()
        Account(self.customer_id)