from tkinter import *
from functools import partial
from tkinter.font import BOLD
from PIL import ImageTk, Image

class AddCustomer():
    def __init__(self):

        """
            Window Configuration
        """
        self.registerroot = Tk()
        window_height = 650                                         #Window Height
        window_width = 750                                          #Window Width
        screen_width = self.registerroot.winfo_screenwidth()        #Screen Width
        screen_height = self.registerroot.winfo_screenheight()      #Screen Height
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.registerroot.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))     #Implement and Center Window based on Device Screen
        self.registerroot.config(bg='#23374d')                      #Window Background
        self.registerroot.overrideredirect(True)                    #Remove Window Status Bar
        self.registerroot.resizable(False, False)                   #Disable Resizing Window

        """
            Image Declaration
        """
        imgButton = PhotoImage(file='tampilan/images/register-btn.png')
        imgExit = PhotoImage(file='tampilan/images/exit-btn.png')
        sideIMG = Image.open('tampilan/images/login-bg.png')
        sideimage = sideIMG.resize((300, 300), Image.ANTIALIAS)
        my_sideimg = ImageTk.PhotoImage(sideimage)

        """
            Input String Declaration
        """
        self.fullname = StringVar()
        self.address = StringVar()
        self.phone = StringVar()
        self.email = StringVar()
        self.password = StringVar()

        """
            Register Customer Graphic User Interface
        """
        #Page Title
        registerTitle = Label(
            text='REGISTER USER',
            font=(
                'Segoe UI',
                20,
                BOLD
            ),
            bg='#23374d',
            fg='#e5e5e5'
        )
        registerTitle.place(x=430, y=80)

        #Side Image 
        sideLabel = Label(
            self.registerroot,
            image=my_sideimg,
            bg='#23374d',
        )
        sideLabel.place(x=20, y=300)

        #Fullname Label
        fullnameLabel = Label(
            self.registerroot,
            text="FULLNAME",
            font=('Segoe UI', 18),
            bg='#23374d',
            fg='#e5e5e5'
        )
        fullnameLabel.place(x=300,y=200)
        #Fullname Entry
        fullnameEntry = Entry(
            self.registerroot,
            width=20,
            font=(
                'normal',
                13
            ),
            textvariable=self.fullname,
            bd=3
        )
        fullnameEntry.place(x=500, y=200)

        #Address Label
        addressLabel = Label(
            self.registerroot,
            text="ADDRESS",
            font=('Segoe UI', 18),
            bg='#23374d',
            fg='#e5e5e5'
        )
        addressLabel.place(x=300,y=250)
        #Address Entry
        addressEntry = Entry(
            self.registerroot,
            width=20,
            font=(
                'normal',
                13
            ),
            textvariable=self.address,
            bd=3
        )
        addressEntry.place(x=500, y=250)

        #Phone Number Label
        phoneLabel = Label(
            self.registerroot,
            text="PHONE NUMBER",
            font=('Segoe UI', 18),
            bg='#23374d',
            fg='#e5e5e5'
        )
        phoneLabel.place(x=300,y=300)
        #Phone Number Entry
        phoneEntry = Entry(
            self.registerroot,
            width=20,
            font=(
                'normal',
                13
            ),
            textvariable=self.phone,
            bd=3
        )
        phoneEntry.place(x=500, y=300)

        #Email Label
        emailLabel = Label(
            self.registerroot,
            text="E-MAIL",
            font=('Segoe UI', 18),
            bg='#23374d',
            fg='#e5e5e5'
        )
        emailLabel.place(x=300,y=350)
        #Email Entry
        emailEntry = Entry(
            self.registerroot,
            width=20,
            font=(
                'normal',
                13
            ),
            textvariable=self.email,
            bd=3
        )
        emailEntry.place(x=500, y=350)

        #Password Label
        passwordLabel = Label(
            self.registerroot,
            text="PASSWORD",
            font=('Segoe UI', 18),
            bg='#23374d',
            fg='#e5e5e5'
        )
        passwordLabel.place(x=300,y=400)
        #Password Entry
        passwordEntry = Entry(
            self.registerroot,
            width=20,
            textvariable=self.password,
            font=(
                'normal',
                13
            ),
            show=u'\u2022',
            bd=3
        )
        passwordEntry.place(x=500, y=400)

        #Login Button Property
        regiterButton = Button(
            self.registerroot,
            image=imgButton,
            border=0,
            bg='#23374d',
            activebackground='#23374d',
            command=self.doRegister,
            cursor='hand2'
        )
        regiterButton.place(x=500, y=480)

        #Exit Button Property
        exitButton = Button(
            self.registerroot,
            image=imgExit,
            border=0,
            bg='#23374d',
            activebackground='#23374d',
            command=self.registerroot.destroy,
            cursor='hand2'
        )
        exitButton.place(x=20, y=590)

        self.registerroot.mainloop()

    """
        Function Declaration
    """
    def doRegister(self):
        email = self.email.get()
        phone = self.phone.get()
        address = self.address.get()
        fullname = self.fullname.get()
        password = self.password.get()

        valid = True
        valid &= email!=""
        valid &= phone!=""
        valid &= address!=""
        valid &= fullname!=""
        valid &= password!=""

        if valid==True :
            from data.User import Customer
            newCust = Customer()
            newCust = newCust.create(email, phone, address, fullname, password)
            print("valid")
            print(newCust)
            if newCust!=False:
                from tampilan.Customer import Customer as CustWin
                self.registerroot.destroy()
                print("valid")
                CustWin()
            
    