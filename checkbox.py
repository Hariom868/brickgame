from tkinter import *
class list_box:
    def __init__(self,root):
        self.f = Frame(root, width=700, height=500, bg="blue")
        self.f.propagate(0)
        self.f.pack()

        self.l = Label(self.f, text="Select the items from the list", font=("Calibri", 15 , "bold italic"))
        self.l.place(x=50, y=50)

        self.lb = Listbox(self.f, font="Arial 15 bold", bg="yellow", fg="blue", height = 8, selectmode=MULTIPLE)

        for i in ["LPU", "CU", "AMITY", "IIT", "NIT"]:
            self.lb.insert(END,i)

        self.lb.bind("<<ListboxSelect>>", self.select)
        self.t=Text(self.f, width=40, height=10, wrap=WORD)
        self.t.place(x=300, y=100)

    def select(self,event):
        self.lst=[]
        indexes = self.lb.curselection()
        for i in indexes:
            self.lst.append(self.lb.get(i))               
        self.t.delete(END)
        self.t.insert(END, self.lst)
                       

        
root=Tk()

root.title("List box")
l_b=list_box(root)
root.mainloop()
