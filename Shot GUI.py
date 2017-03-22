from tkinter import *
import random
import time

spielen=False

main=Tk()
main.geometry("500x500")
main.configure(bg="light gray")
main.title("Sternenkrieg")

def Menü():
    global start
    global verlassen
    global option
    global credit
    start=Button(main,text="Spielen",bg="dark gray",activebackground="gray",command=starten)
    start.place(x=210,y=210)
    option=Button(main,text="Optionen",bg="dark gray",activebackground="gray",command=opt)
    option.place(x=205,y=240)
    credit=Button(main,text="Credits",bg="dark gray",activebackground="gray",command=danke)
    credit.place(x=212,y=270)
    verlassen=Button(main,text="Verlassen",bg="dark gray",activebackground="gray",command=mainds)
    verlassen.place(x=205,y=300)

def starten():
    global zurück
    start.destroy()
    option.destroy()
    credit.destroy()
    verlassen.destroy()
    zurück=Button(main,text="Zurück",bg="dark gray",activebackground="gray",command=zurück3)
    zurück.place(x=210,y=470)

def opt():
    global nichts
    global zurück
    start.destroy()
    option.destroy()
    credit.destroy()
    verlassen.destroy()
    nichts=Label(main,text="Hier ist noch nichts!",fg="dark red",bg="black",font=("Arial",20))
    nichts.place(x=130,y=240)
    zurück=Button(main,text="Zurück",bg="dark gray",activebackground="gray",command=zurück1)
    zurück.place(x=210,y=470)

def danke():
    global namen
    global zurück
    start.destroy()
    option.destroy()
    credit.destroy()
    verlassen.destroy()
    namen=Label(main,text="Eliseo als programmierer"+"\n"*2+"Noah als GROßE hilfe"+"\n"*2+"Michel als Mentale stütze"+"\n"*2+"Danke!",fg="dark red",bg="black",font=("Arial",15))
    namen.place(x=130,y=170)
    zurück=Button(main,text="Zurück",bg="dark gray",activebackground="gray",command=zurück2)
    zurück.place(x=210,y=470)

def zurück3():
    zurück.destroy()
    Menü()

def zurück2():
    zurück.destroy()
    namen.destroy()
    Menü()

def zurück1():
    nichts.destroy()
    zurück.destroy()
    Menü()

def mainds():
    main.destroy()

Menü()

main.mainloop()
