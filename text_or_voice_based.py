from cProfile import label
from cgitb import text
from tkinter import font
from modules import *

class Window:
    def __init__(self,path,name):
        self.name = name
        self.path=path
        name = str.capitalize(name)
        self.window = Tk()
        self.window.title('Personal Diary Of '+name)
        self.window.geometry("1300x600")
        self.window['bg'] = 'lawn green'
        self.fonts = 'Bahnschrift'
        self.label1 = Label(self.window,text='Choose a Method',font=('Bahnschrift',30,BOLD)).place(x=460,y=30)
        self.btn1 = Button(self.window,text="Text Based Entry",background='yellow',command=self.text_based,font=(self.fonts,13,BOLD),width=20).place(x=520,y=200)
        self.btn1 = Button(self.window,text="Voice Based Entry",background='yellow',command=self.voice_based,font=(self.fonts,13,BOLD),width=20).place(x=520,y=300)
        self.btn1 = Button(self.window,text="Back To Main Menu",background='yellow',command=self.back,font=(self.fonts,13,BOLD),width=20).place(x=520,y=400)
    
    def back(self):
        
        self.window.destroy()
        import edit_diary
        edit_diary.Window(self.name)
        
    def voice_based(self):
        self.window.destroy()
        import voice_entry
        voice_entry.Window(self.name,self.path)
    
    def text_based(self):
        self.window.destroy()
        import file_entry
        file_entry.Window(self.name,self.path)
        print(self.path)
        
"""rk = Window("Aashrith")
rk.window.mainloop()"""