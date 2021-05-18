from tkinter import *
from tampilan.Login import Login

class SplashScreen:
    def __init__(self):
        self.splashroot = Tk()
        self.splashroot.geometry("640x480")
        self.splashroot.overrideredirect(True)
        self.splashroot.resizable(False, False)

        self.window_height = 480
        self.window_width = 640
        self.screen_width = self.splashroot.winfo_screenwidth()
        self.screen_height = self.splashroot.winfo_screenheight()
        self.x_cordinate = int((self.screen_width/2) - (self.window_width/2))
        self.y_cordinate = int((self.screen_height/2) - (self.window_height/2))
        self.splashroot.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, self.x_cordinate, self.y_cordinate))

        #Show SplashScreen Image
        canvas = Canvas(self.splashroot, width = 640, height = 480)
        canvas.pack()
        img = PhotoImage(file="tampilan/images/login-bg.png")
        canvas.create_image(70,canvas.winfo_height()/2, anchor=NW, image=img)

        self.splashroot.after(2000, self.login_window)
        self.splashroot.mainloop()
        
    def login_window(self):
        self.splashroot.destroy()
        login = Login()
        # self.loginroot = Tk()
        # window_height = 650
        # window_width = 750

        # x_cordinate = int((self.screen_width/2) - (window_width/2))
        # y_cordinate = int((self.screen_height/2) - (window_height/2))

        # self.loginroot.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        # #Show background Image
        # canvas1 = Canvas(self.loginroot, width = 640, height = 480)
        # canvas1.pack()
        # img1 = PhotoImage(file="tampilan/images/login-bg.png")
        # canvas1.create_image(0,2, anchor=NW, image=img1) 
        # # background_label.pack()

        # label2 = Label(self.loginroot,text="Halaman Login")
        # label2.pack()

