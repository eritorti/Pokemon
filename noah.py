from tkinter import *

main=Tk()
main.configure(bg="pink")
main.geometry("500x500")

def NOAH():
    global gay
    gay=Label(main,bg="red",text="Noah hat einen kleinen!",font=("Arial",30))
    gay.place(x=50,y=150)

def menü():
    global knopfgay
    knopfgay=Button(main,bg="red",text="Wer hat einen kleinen?",font=("Arial",20),command=NOAH)
    knopfgay.place(x=50,y=300)

menü()
main.mainloop()
