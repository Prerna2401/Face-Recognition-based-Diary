from tkinter import *
from tkinter import messagebox
from weakref import ref

font1 ="lucida 30"
font2 = "lucida 14"
name = ""
refid = ""
ar = []
class Window:
    def __init__(self):
        
        self.window = Tk()
        self.window.title("Register New User")
        self.window.geometry("1300x600")
        self.window.resizable(False,False)
        
        self.f = Frame(self.window,bg="lawn green",height=600,width=1300).place(x = 0,y=0)
        self.lab = (Label(self.window,text="Enter Details for Registration",font=font1,bg="yellow").place(x=375,y=50))
    
        self.lab = Label(self.window,text="Enter Name: ",font=font2,bg="yellow").place(x =330,y=208.2 )
        self.name = Entry(self.window,width=40,bg="snow",fg="Red",font="Bahnschrift")
        self.name.place(x = 500,y =208.2,height=30)
        self.lab = Label(self.window,text="Enter Ref_ID: ",font=font2,bg="yellow").place(x =330,y=302 )
        self.ref_id = Entry(self.window,width=40,bg="snow",fg="Red",font="Bahnschrift")
        self.ref_id.place(x = 500,y =302,height=30)
        self.btn = Button(self.window,text="Register",background="Dark Orange",fg="Black",command=self.hello,cursor="hand2",font="Lucida ",width=10,height=2).place(x=600,y=400)
                        
    def send_data(self):
        return self.name.get(),self.ref_id.get()
            
    def hello(self):        
        self.msg =(messagebox.showinfo("Registered","Welcome to Next-Gen Diary!"))
        name= self.name.get()
        refid= self.ref_id.get()
        self.window.destroy()
        n1 = name
        n2 = refid
        
        ar.append(n1)
        ar.append(n2)
        #print(name,refid)
        import mainpage2
        

root = Window()
root.window.mainloop()