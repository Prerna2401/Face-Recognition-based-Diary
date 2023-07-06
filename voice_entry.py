
from fileinput import close
from turtle import back, title, width
from winsound import PlaySound
from numpy import rec, size

from modules import *

class Window:
    def __init__(self,name,path):
        self.window = Tk()
        self.file_name= name
        self.name=name
        self.path = path
        self.window.title('Face Recognition Application')
        self.window.geometry("1200x600+100+50")
        self.window.resizable(False, False)
        self.window['bg'] = 'lawn green'
        self.label1 = Label(self.window,text='Enter Data',font=("Bahnschrift",30,BOLD),fg="black",background="lawn green").place(x = 500,y=20)
        """  self.btn1 = Button(self.wi) """
        self.frame1 = Frame(self.window,background='lawn green',width=600,height=300).place(x=300,y=100)
        self.actual_file_entry = Text(self.window,width=40,bg="yellow",fg="Red",font="Lucida 14")
        self.actual_file_entry.place(x = 150,y =100.2,height=300,width=450)
        self.temp_file_entry = Text(self.window,width=40,bg="yellow",fg="Red",font="Lucida 14")
        self.temp_file_entry.place(x = 650,y =100.2,height=300,width=300)
        self.btn2 = Button(self.frame1,text='Enter The Diary',command=self.registerfile,width=30,height=2,background="yellow",font="Bahnschrift",).place(x=470,y=430)
        self.bg3 = ImageTk.PhotoImage(file="mic.png")
        self.bg33 = Button(self.window, image=self.bg3, cursor="hand2",command=self.get_text_from_voice).place(x=975, y=150)
        self.btn2 = Button(self.frame1,text='Back',width=30,height=2,background="yellow",font="Bahnschrift",command=self.back).place(x=470,y=500)
    
    def actual_file_contents(self,data):
        st1='. '
        st1+=data
        self.actual_file_entry.insert(tkinter.END,st1)
            
    def get_text_from_voice(self):
        self.temp_file_entry.delete('1.0',END)
        import speech
        text = speech.text()
        self.temp_file_entry.insert(tkinter.END,text)
        self.actual_file_contents(text)
    
    def registerfile(self):
        print(self.file_name)
        entry = self.actual_file_entry.get("1.0",'end-1c')
        print(self.file_name)
        f = open(self.path+'.txt',"w")
        f.write(entry)
    
    def back(self):
        self.window.destroy()
        import text_or_voice_based
        text_or_voice_based.Window(self.path,self.file_name)
        
""" rk = Window("Prer","")
rk.window.mainloop() """