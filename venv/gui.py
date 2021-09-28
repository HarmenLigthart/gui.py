from tkinter import *

class Window:
    def __init__(self, window):
        self.btn1 = Button(window, text="Log in", command=self.login)
        self.btn1.place(x = 290, y = 45)

        self.lbl1 = Label(window, text="Username")
        self.lbl1.place(x = 20, y = 30)

        self.lbl2 = Label(window, text="Password")
        self.lbl2.place(x = 20, y = 50)

        self.entry = Entry(window, text="Entry username", width=30)
        self.entry.place(x = 100, y = 30)

        self.entry2 = Entry(window, text="Entry password", width=30, show = "*")
        self.entry2.place(x = 100, y = 52)

        self.lbl3 = Label(window, text="", fg="red", font=("",8))
        self.lbl3.place(x=100, y=72)

    def login(self):
        self.usr = "admin"
        self.pwd = "admin"
        self.usr_entry = str(self.entry.get())
        self.pwd_entry = str(self.entry2.get())

        if self.usr_entry == self.usr and self.pwd_entry == self.pwd:
            self.entry2.delete(0, END)
            self.lbl3.config(text="Log in succesfull")
            return True
        self.entry2.delete(0, END)
        self.lbl3.config(text="Invalid username and/or password")

window = Tk()
mywin = Window(window)
window.title('Password Manager')
window.geometry("360x150+300+300")
window.mainloop()