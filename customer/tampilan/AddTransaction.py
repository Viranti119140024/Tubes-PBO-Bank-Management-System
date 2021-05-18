from tkinter import *
from functools import partial
from tkinter.font import BOLD
from PIL import ImageTk, Image
from data.Account import Account as DataAkun

class AddTransaction():
    def __init__(self, customer_id, account=False):
        self.customer_id = customer_id
        self.account_id = account.getId()
        self.transact_account = account
        """
            Window Configuration
        """
        self.addTransRoot = Tk()
        window_height = 650                                         #Window Height
        window_width = 750                                          #Window Width
        screen_width = self.addTransRoot.winfo_screenwidth()        #Screen Width
        screen_height = self.addTransRoot.winfo_screenheight()      #Screen Height
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.addTransRoot.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))     #Implement and Center Window based on Device Screen
        self.addTransRoot.config(bg='#00bd56')                      #Window Background
        # self.addTransRoot.overrideredirect(True)                    #Remove Window Status Bar
        self.addTransRoot.resizable(False, False)                   #Disable Resizing Window

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

        """
            Input String Declaration
        """
        self.clickedTransType = StringVar()
        self.amount = IntVar()

        transType = [
            "Withdraw",
            "Deposit"
        ]

        ##############################################################################
        ############                   OPEN ACCOUNT CONTENT                 ##########
        ##############################################################################
        # Top Title
        addTransRootTitle = Label(
            text='ADD TRANSACTION PAGE',
            font=(
                'Segoe UI',
                20,
                BOLD
            ),
            bg='#00bd56',
            fg='#e5e5e5'
        )
        addTransRootTitle.place(x=330, y=80)

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
            text="TRANSACTION TYPE",
            fg='#e5e5e5',
            bg='#00bd56',
            font=(
                'Segoe UI',
                18
            )
        )
        transTypeLabel.place(x=250,y=170)

        self.clickedTransType.set( "Withdraw" )

        # Create Transaction Type Dropdown menu
        transTypeDropdown = OptionMenu( self.addTransRoot , self.clickedTransType , *transType)
        transTypeDropdown.config(
            width=26,
            font=(
                'normal',
                10,
                BOLD
            )
        )
        transTypeDropdown.place(x=500,y=170)

        accTypeLabel=Label(
            text="ACCOUNT",
            fg='#e5e5e5',
            bg='#00bd56',
            font=(
                'Segoe UI',
                18
            )
        )
        accTypeLabel.place(x=250,y=220)
        
        accDescLabel = Label(
            text=str(account.getType()) + str(account.getId()),
            fg='#e5e5e5',
            bg='#00bd56',
            font=(
                'Segoe UI',
                18
            )
        )
        accDescLabel.place(x=500, y=220)


        amountLabel =Label(
            text="AMOUNT",
            fg='#e5e5e5',
            bg='#00bd56',
            font=(
                'Segoe UI',
                18
            )
        )
        amountLabel.place(x=250,y=270)

        amountEntry = Entry(
            self.addTransRoot,
            width=20,
            font=(
                'normal',
                15
            ),
            textvariable=self.amount,
            bd=2
        )
        amountEntry.place(x=500, y=270)

        #Submit Button Property
        submitButton = Button(
            self.addTransRoot,
            image=imgSubmit,
            border=0,
            bg='#00bd56',
            activebackground='#00bd56',
            command=self.storeNewTransaction,
            cursor='hand2'
        )
        submitButton.place(x=610, y=330)

        #Exit Button Property
        exitButton = Button(
            self.addTransRoot,
            image=imgExit,
            border=0,
            bg='#00bd56',
            activebackground='#00bd56',
            command=self.exit,
            cursor='hand2'
        )
        exitButton.place(x=20, y=590)

        self.addTransRoot.mainloop()

    """
        Function Declaration
    """
    def storeNewTransaction(self):
        trans_amount = int(self.amount.get())
        if self.transact_account == False:
            return
        
        if(self.transact_account.getType()=="saving"):
            from data.Account import AccountSaving
            sv = AccountSaving()
            sv = sv.getSavingByAccountId(self.account_id)
            if(self.clickedTransType.get()=="Withdraw"):
                sv.withdraw(trans_amount)
            if(self.clickedTransType.get()=="Deposit"):
                sv.deposit(trans_amount)

        if(self.transact_account.getType()=="loan"):
            from data.Account import AccountLoan
            lo = AccountLoan()
            lo = lo.getLoanByAccountId(self.account_id)
            # if(self.clickedTransType.get()=="Withdraw"):
            #     lo.withdraw(trans_amount)
            if(self.clickedTransType.get()=="Deposit"):
                lo.deposit(trans_amount)

        if(self.transact_account.getType()=="checking"):
            from data.Account import AccountChecking
            ch = AccountChecking()
            ch = ch.getCheckingByAccountId(self.account_id)
            if(self.clickedTransType.get()=="Withdraw"):
                ch.withdraw(trans_amount)
            if(self.clickedTransType.get()=="Deposit"):
                ch.deposit(trans_amount)
        
        self.exit()
    def exit(self):
        from tampilan.Transaction import Transaction as WinTransaction

        self.addTransRoot.destroy()
        WinTransaction(self.customer_id, self.account_id)
    
    def doBack(self, event):
        from tampilan.Transaction import Transaction as WinTransaction

        self.addTransRoot.destroy()
        WinTransaction(self.customer_id, self.account_id)
