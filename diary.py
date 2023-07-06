from cProfile import label
from cgitb import text
from tkinter import font
from modules import *

class Window:
    def __init__(self,name):
        self.name = str.capitalize(name)
        self.window = Tk()
        self.window.title('Personal Diary Of '+name)
        self.window.geometry("1300x600")
        self.fonts = 'Bahnschrift'
        self.window['bg'] = 'lawn green'
        
        self.label1 = Label(self.window,text='Welcome To Your Personal Diary, '+name,font=('Bahnschrift',30,BOLD)).place(x=280,y=30)
        self.btn1 = Button(self.window,text="View Diary",background='yellow',command=self.view_diary,font=(self.fonts,13,BOLD),width=20).place(x=520,y=200)
        self.btn1 = Button(self.window,text="Edit Diary",background='yellow',command=self.edit_diary,font=(self.fonts,13,BOLD),width=20).place(x=520,y=300)
        self.btn1 = Button(self.window,text="Back To Main Menu",background='yellow',command=self.back,font=(self.fonts,13,BOLD),width=20).place(x=520,y=400)
    
    def back(self):
        
        self.window.destroy()
        import mainpage2
        mainpage2.Window()
        
    def edit_diary(self):
        self.window.destroy()
        import edit_diary
        edit_diary.Window(self.name)
    
    def view_diary(self):
        self.window.destroy()
        import view_files
        view_files.Window(self.name)

'''rk = Window("Prer")
rk.window.mainloop()'''