
from fileinput import close
from turtle import back, title, width
from winsound import PlaySound
from numpy import rec, size

from modules import *


""" from recognition import recog """
""" from embedding import register
from recognition import recog """

class Window:
    def __init__(self):
        self.window = Tk()
        self.window.title('Face Recognition Application')
        self.window.geometry("1200x600+100+50")
        self.window.resizable(False, False)
        self.window['bg'] = 'navy'
        self.label1 = Label(self.window,text='Next-Gen Personal Diary',font=("Bahnschrift",30,BOLD),fg="navy",background="light grey").place(x=370, y=50)
        """  self.btn1 = Button(self.wi) """
        self.frame1 = Frame(self.window,background='grey',width=600,height=300).place(x=300,y=150)
        self.btn1 = Button(self.frame1,text='Register',width=30,height=2,background="dark grey",font="Bahnschrift", command=self.register).place(x=460,y=225)
        self.btn2 = Button(self.frame1,text='Login',width=30,height=2,background="dark grey",font="Bahnschrift", command=self.detect).place(x=460,y=325)
        self.arr = []
    
    def register(self):
        self.window.destroy()
        import Register
        # print(self.arr)a
        # self.arr = []
        n,rfid = Register.ar[0],Register.ar[1]
        from embedding import register
        register(n,rfid)
    def detect(self):
        from recognition import accessname,recog
        self.name = recog()
        string = "Access Person : "+str.capitalize(self.name)
        self.msg1 = messagebox.showinfo('Face Recognized',string)
        self.window.destroy()
        import diary
        diary.Window(self.name)
        

rk = Window()
rk.window.mainloop()