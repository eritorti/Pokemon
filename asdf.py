from tkinter import *
class fe:
    def __init__(self,master):
        self.b=Button(master,justify = LEFT)
        photo=PhotoImage(file="pokeball.gif")
        self.b.config(image=photo,width="10",height="10")
        self.b.pack(side=LEFT)
root = Tk()
front_end=fe(root)
root.mainloop()



from Tkinter import *
root=Tk()
b=Button(root,justify = LEFT)
photo=PhotoImage(file="pokeball.gif")
b.config(image=photo,width="10",height="10")
b.pack(side=LEFT)
root.mainloop()
