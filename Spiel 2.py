from tkinter import *
import random
import time

main=Tk()
main.geometry("500x500")
main.configure(bg="black")

spielen=False

def Menü():
    global start
    global option
    global verlassen
    spielen=False
    start=Button(main,text="Spielen",bg="light gray",fg="black",activebackground="gray",command=starten)
    start.place(x=230,y=200)
    option=Button(main,text="Optionen",bg="light gray",fg="black",activebackground="gray",command=optionen)
    option.place(x=225,y=230)
    verlassen=Button(main,text="Verlassen",bg="light gray",fg="black",activebackground="gray",command=left)
    verlassen.place(x=226,y=260)



def starten():
    global schwierigkeit
    global easy
    global middle
    global hard
    global impossible
    global zurück3
    spielen=False
    start.destroy()
    option.destroy()
    verlassen.destroy()
    schwierigkeit=Label(main,text="Schwierigkeits stufen",bg="gray",fg="black",activebackground="gray",font=("Arial",15))
    schwierigkeit.place(x=150,y=70)
    easy=Button(main,text="Leicht",bg="light gray",fg="dark blue",activebackground="gray",command=easyspiel)
    easy.place(x=230,y=200)
    middle=Button(main,text="Mittel",bg="light gray",fg="dark orange",activebackground="gray")
    middle.place(x=230,y=230)
    hard=Button(main,text="Schwer",bg="light gray",fg="SteelBlue1",activebackground="gray")
    hard.place(x=230,y=260)
    impossible=Button(main,text="Unmöglich",bg="light gray",fg="black",activebackground="gray")
    impossible.place(x=210,y=290)
    zurück3=Button(main,text="Zurück",bg="light gray",fg="black",activebackground="gray",command=back3)
    zurück3.place(x=230,y=470)
zähler=0
x=240
def easyspiel():
    global rdy
    spielen=False
    schwierigkeit.destroy()
    easy.destroy()
    middle.destroy()
    hard.destroy()
    impossible.destroy()
    zurück3.destroy()
    rdy=Button(main,text="Spiel starten",bg="gray30",fg="dark red",activebackground="gray",command=go)
    rdy.place(x=200,y=200)

canvas_width=250
canvas_height=250
schachbrett=Canvas(main,width=canvas_width,height=canvas_height)


def go():
    global schachbrett
    global zähler
    zähler=0
    zähler +=1
    spielen=True
    rdy.destroy()
    main.bind("<Escape>",escape)
    schachbrett.place(y=120,x=120)
    def checkered(canvas, line_distance):  
        for x in range(line_distance,canvas_width,line_distance):
            canvas.create_line(x, 0, x, canvas_height, fill="#476042")
        for y in range(line_distance,canvas_height,line_distance):
            canvas.create_line(5, y, canvas_width, y, fill="#476042")
    checkered(schachbrett,20)

master = Tk()
canvas_width = 200
canvas_height = 100 
def escape(event):
    global zähler
    global weiter
    global new
    global leave
    spielen=False
    zähler -=1
    if(zähler >=0):
        weiter=Button(main,text="Weiter",bg="light gray",fg="black",command=weiter1)
        weiter.place(x=230,y=140)
        new=Button(main,text="Neustarten",bg="light gray",fg="black",command=new1)
        new.place(x=218,y=170)
        leave=Button(main,text="Verlassen",bg="light gray",fg="black",command=leave1)
        leave.place(x=223,y=200)


def weiter1():
    spielen=False
    weiter.destroy()
    new.destroy()
    leave.destroy()
    go()

def new1():
    global x
    spielen=False
    weiter.destroy()
    new.destroy()
    leave.destroy()
    x=240
    easyspiel()

def links(event):
    global x
    x -=10
    easyspieler.place(x=x)
    if(x==0):
        x +=10
        easyspieler.place(x=x)

def rechts(event):
    global x
    x +=10
    easyspieler.place(x=x)
    if(x==490):
        x -=10
        easyspieler.place(x=x)


def optionen():
    global farbe
    global zurück1
    spielen=False
    start.destroy()
    option.destroy()
    verlassen.destroy()
    farbe=Button(main,text="Hintergrundfarbe ändern",bg="light gray",fg="black",activebackground="gray",command=farbe1)
    farbe.place(x=170,y=220)
    zurück1=Button(main,text="Zurück",bg="light gray",fg="black",activebackground="gray",command=back1)
    zurück1.place(x=230,y=470)



def farbe1():
    global fschwarz
    global fweiß
    global zurück2
    spielen=False
    farbe.destroy()
    zurück1.destroy()
    fschwarz=Button(main,text="Schwarz",bg="light gray",fg="black",activebackground="gray",command=fschwarz1)
    fschwarz.place(x=230,y=170)
    fweiß=Button(main,text="Weiß",bg="light gray",fg="black",activebackground="gray",command=fweiß1)
    fweiß.place(x=232,y=200)
    zurück2=Button(main,text="Zurück",bg="light gray",fg="black",activebackground="gray",command=back2)
    zurück2.place(x=230,y=470)



def fschwarz1():
    main.configure(bg="black")



def fweiß1():
    main.configure(bg="white")



def back1():
    spielen=False
    zurück1.destroy()
    farbe.destroy()
    Menü()



def back2():
    spielen=False
    fschwarz.destroy()
    fweiß.destroy()
    zurück2.destroy()
    optionen()



def back3():
    spielen=False
    schwierigkeit.destroy()
    easy.destroy()
    middle.destroy()
    hard.destroy()
    impossible.destroy()
    zurück3.destroy()
    Menü()



def left():
    main.destroy()

def leave1():
    spielen=False
    weiter.destroy()
    leave.destroy()
    new.destroy()
    Menü()


main.bind("<Left>",links)
main.bind("<Right>",rechts)

Menü()
main.mainloop()
