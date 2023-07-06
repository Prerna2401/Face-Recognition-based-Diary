
from fileinput import close
from turtle import back, title, width
from winsound import PlaySound
from numpy import rec, size

from modules import *

class Window:
    def __init__(self,name):
        
        self.window = Tk()
        self.name = name
        self.window.title('Face Recognition Application')
        self.window.geometry("1200x600+100+50")
        self.window.resizable(False, False)
        self.window['bg'] = 'lawn green'
        self.label1 = Label(self.window,text='Welcome To Face Recognition Based Personal Diary',font=("Bahnschrift",30,BOLD),fg="black").place(x = 150,y=20)
        """  self.btn1 = Button(self.wi) """
        self.frame1 = Frame(self.window,background='lawn green',width=600,height=300).place(x=300,y=100)
        self.label1 = Label(self.window,text='Enter The File Name: ',font=('Bahnschrift',14,BOLD),bg='yellow').place(x=300,y=208.2)
        self.file_name = Entry(self.window,width=40, bg="yellow",fg="Red",font="Lucida 14")
        self.file_name.place(x = 500,y =208.2,height=30)
        self.btn2 = Button(self.frame1,text='Enter The Diary',width=30,height=2,background="yellow",font="Bahnschrift",command=self.registerfile).place(x=470,y=400)
        self.btn2 = Button(self.frame1,text='Back To Diary Options',width=30,height=2,background="yellow",font="Bahnschrift",command=self.back).place(x=470,y=500)
        
    
    def registerfile(self):
        filename = self.file_name.get()
        path = "C:/xampp/htdocs/AI_PROJECT/DIARY_DATA/"
        path+=self.name
        path+="/"
        path+=filename
        print(path)
        
        self.window.destroy()
        import text_or_voice_based
        text_or_voice_based.Window(path,self.name)
    
    def back(self):
        self.window.destroy()
        import diary
        diary.Window(self.name)
        
'''rk = Window("Prer")
rk.window.mainloop()'''