from tkinter import *


main=Tk()
main.geometry("200x250")
main.title("Hauptfenster")



def popup():
    top=Toplevel()
    top.geometry("105x105")
    top.title("Popup")
    knopftop=Button(top,activebackground="gray",bg="white",text="Zurück",command=top.destroy)
    knopftop.pack(side=BOTTOM)



knopf=Button(main,text="Knopf",activebackground="gray",bg="white",command=popup)
knopf.place(y=100,x=75)



main.mainloop()
