
from fileinput import close
from turtle import back, title, width
from winsound import PlaySound
from numpy import rec, size
from tkinter.ttk import Combobox
from modules import *
import os
class Window:
    def __init__(self,name):
        
        self.window = Tk()
        self.name = name
        self.window.title('Face Recognition Application')
        self.window.geometry("1200x600+100+50")
        self.window.resizable(False, False)
        self.window['bg'] = 'lawn green'
        self.label1 = Label(self.window,text='Welcome To Face Recognition Based Personal Diary',font=("Bahnschrift",30,BOLD),fg="black",background="lawn green").place(x = 150,y=20)
        """  self.btn1 = Button(self.wi) """
        self.frame1 = Frame(self.window,background='lawn green',width=600,height=300).place(x=300,y=100)
        self.label1 = Label(self.window,text='Choose A File ',font=('Bahnschrift',14),bg='lawn green').place(x=350,y=208.2)
        n = StringVar()
        self.file_list=Combobox(self.window,width=10,textvariable=n)
        self.path = "C:/xampp/htdocs/AI_PROJECT/DIARY_DATA/"
        self.path+=name
        dir_list = os.listdir(self.path)
        file_name_array = []
        from pathlib import Path
        for x in dir_list:
            file_name_array.append(Path(x).stem)
        self.file_list['values']=file_name_array
        self.file_list['state']='readonly'
        self.file_list.place(x=500,y=208.2,height=30,width=200)
        self.file_list.current(0)
        self.btn2 = Button(self.frame1,text='View The Diary',width=30,height=2,background="yellow",font="Bahnschrift",command=self.viewfile).place(x=470,y=400)
        self.btn2 = Button(self.frame1,text='Back To Diary Options',width=30,height=2,background="yellow",font="Bahnschrift",command=self.back).place(x=470,y=500)
        
    
    def viewfile(self):
        if self.file_list.get()=="":
            messagebox.showerror("Error","Fields Cannot Be Null")
        fn = self.file_list.get()
        f = open(self.path+"/"+fn+'.txt',"r")
        txt = f.read()
        self.window.destroy()
        import show_file_contents
        show_file_contents.Window(fn,txt,self.name)
    
    def back(self):
        self.window.destroy()
        import diary
        diary.Window(self.name)
        
'''rk = Window("Prerna")
rk.window.mainloop()'''