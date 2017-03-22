from tkinter import ttk
from tkinter import *

main=Tk()
main.geometry("1000x800")

fotoeich=PhotoImage(file="Eich.gif")
sprechblase=PhotoImage(file="sprechblase.gif")
mannfoto=PhotoImage(file="ash.gif")
fraufoto=PhotoImage(file="misty2.gif")
geschlecht=None

def menü():
    global lgamename,bstart,bverlassen

    lgamename=Label(main,text="Pokemon",fg="dark red",font=("Arial",50))
    bstart=Button(main,text="Spielen",bg="dark gray",activebackground="gray",command=cstart)
    bverlassen=Button(main,text="Verlassen",bg="dark gray",activebackground="gray",command=cverlassen)

    lgamename.place(x=430,y=260)
    bstart.place(x=540,y=450)
    
    bverlassen.place(x=533,y=480)

def cstart():
    global startback,eich,blase,mann,frau
    lgamename.destroy()
    bstart.destroy()
    bverlassen.destroy()

    eich=Label(main,image=fotoeich)
    blase=Label(main,image=sprechblase,text="Hallo , erstmal bist du"+"\n"+"ein Junge oder"+"\n"+"ein Mädchen?"+"\n"*3,compound="center",font=("Arial",9))
    blaseausfüllen=Label(main,text="  ")
    mann=Button(main,image=mannfoto,command=männlich)
    frau=Button(main,image=fraufoto,command=weiblich)
    
    blaseausfüllen.place(x=320,y=190)
    eich.place(x=400,y=140)
    blase.place(x=320,y=60)
    geschlechter()
def geschlechter():
    mann.place(x=130,y=440)
    frau.place(x=700,y=420)
def nochmalgeschlecht():
    jaeinmädchen.destroy()
    jaeinjunge.destroy()
    blase.configure(text="Bist du ein Junge"+"\n"+"oder ein Mädchen?"+"\n"*3)
def nachfrage():
    global geschlecht,jaeinmädchen,jaeinjunge
    mann.destroy()
    frau.destroy()
    blase.configure(text="Also bist du ein"+"\n"+geschlecht+"?"+"\n"*3)
    jaeinjunge=Button(main,text="Ja",width=40,height=3,bg="dark blue",command=weiter)
    jaeinmädchen=Button(main,text="Nein",width=40,height=3,bg="dark red",command=nochmalgeschlecht)
    jaeinjunge.place(x=400,y=500)
    jaeinmädchen.place(x=400,y=570)
def männlich():
    global geschlecht
    geschlecht="Junge"
    nachfrage()
def weiblich():
    global geschlecht
    geschlecht="Mädchen"
    nachfrage()

def cstartback():
    startback.destroy()
    menü()

def cverlassen():
    main.destroy()

menü()
main.mainloop()
