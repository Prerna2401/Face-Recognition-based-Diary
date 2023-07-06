
from fileinput import close
from turtle import back, title, width
from winsound import PlaySound
from numpy import rec, size
from tkinter.ttk import Combobox
from modules import *
import os
class Window:
    def __init__(self,name,contents,name1):
        
        self.window = Tk()
        self.name = name
        self.name1 = name1
        self.window.title('Face Recognition Application')
        self.window.geometry("1200x600+100+50")
        self.window.resizable(False, False)
        self.window['bg'] = 'lawn green'
        self.label1 = Label(self.window,text='Diary Entry Of File : '+name,font=("Bahnschrift",30,BOLD),fg="black",background="lawn green").place(x = 150,y=20)
        """ """  
        """
        """ 
        self.frame1 = Frame(self.window,background='lawn green',width=600,height=300).place(x=300,y=100)
        self.file_entry = Text(self.window,width=40,bg="yellow",fg="Red",font="Lucida 14")
        self.file_entry.place(x = 350,y =100.2,height=300,width=500)
        self.file_entry.insert(tkinter.END,contents)
        """
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
        self.file_list.place(x=500,y=208.2,height=30,width=80)
        self.file_list.current(0)
        self.btn2 = Button(self.frame1,text='View The Diary',width=30,height=2,background="Orange",font="Bahnschrift",command=self.registerfile).place(x=470,y=400)
        """
        self.btn2 = Button(self.frame1,text='Back To Diary Options',width=30,height=2,background="Orange",font="Bahnschrift",command=self.back).place(x=470,y=500)
        """
    
    def viewfile(self):
        if self.file_list.get=="":
            messagebox.showerror("Error","Fields Cannot Be Null")
        im """
    
    def back(self):
        self.window.destroy()
        import diary
        diary.Window(self.name1)
        
""" rk = Window("Aashrith","/Aashrith/hello.txt")
rk.window.mainloop() """