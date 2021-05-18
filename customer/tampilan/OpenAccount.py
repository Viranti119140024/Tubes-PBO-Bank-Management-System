from tkinter import *
from functools import partial
from tkinter.font import BOLD
from PIL import ImageTk, Image
from data.Account import *

class OpenAccount():
    def __init__(self, customer_id):
        self.customer_id = customer_id
        """
            Window Configuration
        """
        self.ca = Tk()
        window_height = 650                                         #Window Height
        window_width = 750                                          #Window Width
        screen_width = self.ca.winfo_screenwidth()        #Screen Width
        screen_height = self.ca.winfo_screenheight()      #Screen Height
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.ca.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))     #Implement and Center Window based on Device Screen
        self.ca.config(bg='#00bd56')                      #Window Background
        # self.ca.overrideredirect(True)                    #Remove Window Status Bar
        self.ca.resizable(False, False)                   #Disable Resizing Window

        """
            Image Declaration
        """
        imgSubmit = PhotoImage(file='tampilan/images/submit-btn.png')
        imgExit = PhotoImage(file='tampilan/images/exit-btn.png')
        sideIMG = Image.open('tampilan/images/ca.png')
        sideimage = sideIMG.resize((350, 250), Image.ANTIALIAS)
        my_sideimg = ImageTk.PhotoImage(sideimage)
        backIMG = Image.open('tampilan/images/back-btn.png')
        backimage = backIMG.resize((60, 50), Image.ANTIALIAS)
        BACKimg = ImageTk.PhotoImage(backimage)

        """
            Input String Declaration
        """
        
        self.clickedType = StringVar()
        self.balance = IntVar()

        typeOption = [
            "Saving",
            "Check",
            "Loan"
        ]

        ##############################################################################
        ############                   OPEN ACCOUNT CONTENT                 ##########
        ##############################################################################
        # Top Title
        caTitle = Label(
            text='CREATE ACCOUNT PAGE',
            font=(
                'Segoe UI',
                20,
                BOLD
            ),
            bg='#00bd56',
            fg='#e5e5e5'
        )
        caTitle.place(x=330, y=80)

        # Side Image
        backLabel = Label(
            image=BACKimg,
            bg='#00bd56',
            cursor="hand2",
        )
        backLabel.place(x=20, y=15)
        backLabel.bind("<Button>",self.doBack)

        # Side Image
        sideLabel = Label(
            image=my_sideimg,
            bg='#00bd56',
        )
        sideLabel.place(x=50, y=300)

        typeLabel=Label(
            text="ACCOUNT TYPE",
            fg='#e5e5e5',
            bg='#00bd56',
            font=(
                'Segoe UI',
                18
            )
        )
        typeLabel.place(x=250,y=170)

        self.clickedType.set( "Saving" )

        # Create Dropdown menu
        typeDropdown = OptionMenu( self.ca , self.clickedType , *typeOption)
        typeDropdown.config(
            width=26,
            font=(
                'normal',
                10,
                BOLD
            )
        )
        typeDropdown.place(x=500,y=170)

        balanceLabel =Label(
            text="ACCOUNT BALANCE",
            fg='#e5e5e5',
            bg='#00bd56',
            font=(
                'Segoe UI',
                18
            )
        )
        balanceLabel.place(x=250,y=220)

        balanceEntry = Entry(
            self.ca,
            width=20,
            font=(
                'normal',
                15
            ),
            textvariable=self.balance,
            bd=2
        )
        balanceEntry.place(x=500, y=220)

        #Login Button Property
        submitButton = Button(
            self.ca,
            image=imgSubmit,
            border=0,
            bg='#00bd56',
            activebackground='#00bd56',
            command=self.storeNewAccount,
            cursor='hand2'
        )
        submitButton.place(x=610, y=295)

        #Exit Button Property
        exitButton = Button(
            self.ca,
            image=imgExit,
            border=0,
            bg='#00bd56',
            activebackground='#00bd56',
            command=self.ca.destroy,
            cursor='hand2'
        )
        exitButton.place(x=20, y=590)

        self.ca.mainloop()
    
    """
        Function Declaration
    """
    def storeNewAccount(self):
        print(self.clickedType.get())
        if(self.clickedType.get()=='Saving'):
            print("saving")
            new = AccountSaving()
            new = new.create(self.customer_id, self.balance.get(), 0)

        if(self.clickedType.get()=='Check'):
            print("checking")
            new = AccountChecking()
            new = new.create(self.customer_id, self.balance.get(), 0)

        if(self.clickedType.get()=='Loan'):
            print("loan")
            new = AccountLoan()
            new = new.create(self.customer_id, self.balance.get(), 0, 0, 0)
        
        from tampilan.Account import Account
        self.ca.destroy()
        Account(self.customer_id)
    
    def doBack(self, event):
        from tampilan.Account import Account
        self.ca.destroy()
        Account(self.customer_id)