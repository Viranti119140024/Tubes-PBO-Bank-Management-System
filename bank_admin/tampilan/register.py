from tkinter import *
from functools import partial
from tkinter.font import BOLD
from PIL import ImageTk, Image

#Window Property
registerroot = Tk()
window_height = 650
window_width = 750

global screen_width
global screen_height
screen_width = registerroot.winfo_screenwidth()
screen_height = registerroot.winfo_screenheight()

#Centering Window when show
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
registerroot.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
registerroot.config(bg='#23374d')
registerroot.overrideredirect(True)
registerroot.resizable(False, False)

# Image Declaration
imgButton = PhotoImage(file='images/register-btn.png')
imgExit = PhotoImage(file='images/exit-btn.png')
sideIMG = Image.open('images/login-bg.png')
sideimage = sideIMG.resize((300, 300), Image.ANTIALIAS)
my_sideimg = ImageTk.PhotoImage(sideimage)

fullname = StringVar()
address = StringVar()
phone = StringVar()
email = StringVar()
password = StringVar()

def doRegister(fullnama, alamat, telp, mail, passw):
    print(fullnama.get())
    print(alamat.get())
    print(telp.get())
    print(mail.get())
    print(passw.get())

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

sideLabel = Label(
    registerroot,
    image=my_sideimg,
    bg='#23374d',
)
sideLabel.place(x=20, y=300)

fullnameLabel = Label(
    registerroot,
    text="FULLNAME",
    font=('Segoe UI', 18),
    bg='#23374d',
    fg='#e5e5e5'
)
fullnameLabel.place(x=300,y=200)

fullnameEntry = Entry(
    registerroot,
    width=20,
    font=(
        'normal',
        13
    ),
    textvariable=fullname,
    bd=3
)
fullnameEntry.place(x=500, y=200)

addressLabel = Label(
    registerroot,
    text="ADDRESS",
    font=('Segoe UI', 18),
    bg='#23374d',
    fg='#e5e5e5'
)
addressLabel.place(x=300,y=250)

addressEntry = Entry(
    registerroot,
    width=20,
    font=(
        'normal',
        13
    ),
    textvariable=address,
    bd=3
)
addressEntry.place(x=500, y=250)

phoneLabel = Label(
    registerroot,
    text="PHONE NUMBER",
    font=('Segoe UI', 18),
    bg='#23374d',
    fg='#e5e5e5'
)
phoneLabel.place(x=300,y=300)

phoneEntry = Entry(
    registerroot,
    width=20,
    font=(
        'normal',
        13
    ),
    textvariable=phone,
    bd=3
)
phoneEntry.place(x=500, y=300)

emailLabel = Label(
    registerroot,
    text="E-MAIL",
    font=('Segoe UI', 18),
    bg='#23374d',
    fg='#e5e5e5'
)
emailLabel.place(x=300,y=350)

emailEntry = Entry(
    registerroot,
    width=20,
    font=(
        'normal',
        13
    ),
    textvariable=email,
    bd=3
)
emailEntry.place(x=500, y=350)

passwordLabel = Label(
    registerroot,
    text="PASSWORD",
    font=('Segoe UI', 18),
    bg='#23374d',
    fg='#e5e5e5'
)
passwordLabel.place(x=300,y=400)

passwordEntry = Entry(
    registerroot,
    width=20,
    textvariable=password,
    font=(
        'normal',
        13
    ),
    show=u'\u2022',
    bd=3
)
passwordEntry.place(x=500, y=400)

# Action When Register Button Pressed
doRegister = partial(doRegister, fullname, address, phone, email, password)

#Login Button Property
regiterButton = Button(
    registerroot,
    image=imgButton,
    border=0,
    bg='#23374d',
    activebackground='#23374d',
    command=doRegister,
    cursor='hand2'
)
regiterButton.place(x=500, y=480)


#Exit Button Property
exitButton = Button(
    registerroot,
    image=imgExit,
    border=0,
    bg='#23374d',
    activebackground='#23374d',
    command=registerroot.destroy,
    cursor='hand2'
)
exitButton.place(x=20, y=590)

registerroot.mainloop()