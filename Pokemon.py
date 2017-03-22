from tkinter import ttk
from tkinter import *
import sndhdr

main=Tk()
main.geometry("1000x800")

fotoeich=PhotoImage(file="Eich.gif")
sprechblase=PhotoImage(file="sprechblase.gif")
mannfoto=PhotoImage(file="ash.gif")
fraufoto=PhotoImage(file="misty2.gif")
geschlecht=None
v=StringVar()
name=v
#print(name.get())
eichcounter=0
eicherzählt=0
zählercounter=1
klickfürweiter=Label(main,text="Klick irgendwo hin für weiter!",fg="gray75",font=("Arial",25))
def menü():
    global lgamename,bstart,bverlassen

    lgamename=Label(main,text="Pokèmon",fg="dark red",font=("Arial",50))
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
    blase=Label(main,image=sprechblase,text="Hallo erstmal ,"+"\n"+"ich bin Professor Eich."+"\n"+"bist du ein Junge"+"\n"+"oder ein Mädchen?"+"\n"*3,compound="center",font=("Arial",9))
    blaseausfüllen=Label(main,text="  ")
    
    blaseausfüllen.place(x=320,y=190)
    eich.place(x=400,y=140)
    blase.place(x=320,y=60)
    geschlechter()

def namensichern():
    global janame,neinname
    name=v
    nameeingeben.destroy()
    namenbestätigen.destroy()
    blase.configure(text="Ah,dein Name ist also "+"\n"+str(name.get())+"."+"\n"*3)
    janame=Button(main,text="Ja",width=40,height=3,bg="dark blue",command=eichplus)
    neinname=Button(main,text="Nein",width=40,height=3,bg="dark red",command=nochmalname)
    janame.place(x=400,y=500)
    neinname.place(x=400,y=570)

def abenteuerbeginnt():
    pass
def nochmalbereit():
    global jainsmenü,neinweiter
    jabereit.destroy()
    neinbereit.destroy()
    blase.configure(text="Bist du dir sicher?"+"\n"+"Wenn du Ja wählst"+"\n"+"kommst du ins Menü!"+"\n"*3)
    jainsmenü=Button(main,text="Ja",width=40,height=3,bg="dark blue",command=stop)
    neinweiter=Button(main,text="Nein",width=40,height=3,bg="dark red",command=nochmalnamebestätigt)
    jainsmenü.place(x=400,y=500)
    neinweiter.place(x=400,y=570)
def stop():
    jainsmenü.destroy()
    neinweiter.destroy()
    eich.destroy()
    blase.destroy()
    menü()
    
def eichplus():
    global eicherzählt
    eicherzählt +=1
    klickfürweiter.place(x=320,y=750)
    namebestätigt()
def eichzähler():
    global zählercounter
    zählercounter -=2
    if(eicherzählt==1):
        main.bind("<Button-1>",eicherzähltweiter)
def nochmalnamebestätigt():
    jainsmenü.destroy()
    neinweiter.destroy()
    namebestätigt()
def namebestätigt():
    global eichcounter,eicherzählt,name,jabereit,neinbereit,klickfürweiter,zählercounter,eichzähler
#    print(name)
    janame.destroy()
    neinname.destroy()
    jabereit=Button(main,text="Ja , na klar!",width=40,height=3,bg="dark blue",command=abenteuerbeginnt)
    neinbereit=Button(main,text="Nein",width=40,height=3,bg="dark red",command=nochmalbereit)
    blase.configure(text="Ah , das ist ein"+"\n"+"schöner Name"+"\n"*3)
    if(zählercounter==1):
        eichzähler()
    if(eichcounter==1):
        blase.configure(text="Weißt du "+str(name.get())+","+"\n"+"wir leben in einer Welt"+"\n"+"voller Kreaturen die"+"\n"+"man Pokèmon nennt."+"\n"*2)
    elif(eichcounter==2):
        blase.configure(text="Seit jeher Leben"+"\n"+"Pokèmon und Menschen"+"\n"+"zusammen , sie erleben"+"\n"+"Abenteuer und werden"+"\n"+"immer stärker."+"\n"*2)
    elif(eichcounter==3):
        blase.configure(text="Es gibt unzählig viele"+"\n"+"verschiedene Pokèmon"+"\n"+"auf dieser Erde ,"+"\n"+"und wir entdecken jeden"+"\n"+"Tag neue Pokèmon."+"\n"*2)
    elif(eichcounter==4):
        blase.configure(text="Und du "+str(name.get())+"\n"+"bestreitest nun auch"+"\n"+"dieses Abenteuer und"+"\n"+"findest viele"+"\n"+"neue Freunde."+"\n"*3)
    elif(eichcounter==5):
        klickzerstört()
        main.bind("<Button-1>",cpass)
        blase.configure(text="Nun , "+str(name.get())+"\n"+"bist du bereit?"+"\n"*4)
        jabereit.place(x=400,y=500)
        neinbereit.place(x=400,y=570)

def cpass(event):
    pass
def klickzerstört():
    klickfürweiter.destroy()
def eicherzähltweiter(event):
    global eichcounter
    eichcounter +=1
    namebestätigt()
    
def nochmalname():
    global nameeingeben,namenbestätigen,name
    janame.destroy()
    neinname.destroy()
    blase.configure(text="Ok , gib deinen"+"\n"+"Namen nochmal ein."+"\n"*3)
    nameeingeben=Entry(main,text="",font=("Arial",20))
    namenbestätigen=Button(main,text="Bestätigen",bg="dark blue",font=("Arial",30),command=namensichern)
    
    namenbestätigen.place(x=415,y=550)
    nameeingeben.place(x=370,y=500)
    
def namebestimmen():
    global nameeingeben,namenbestätigen,name
    jageschlecht.destroy()
    neingeschlecht.destroy()
    blase.configure(text="Ok sehr gut,"+"\n"+"und wie ist dein Name?"+"\n"*3)
    nameeingeben=Entry(main,text=v,font=("Arial",20))
    namenbestätigen=Button(main,text="Bestätigen",bg="dark blue",font=("Arial",30),command=namensichern)
    
    namenbestätigen.place(x=415,y=550)
    nameeingeben.place(x=370,y=500)

def geschlechter():
    global mann,frau
    mann=Button(main,image=mannfoto,command=männlich)
    frau=Button(main,image=fraufoto,command=weiblich)
    mann.place(x=130,y=440)
    frau.place(x=700,y=420)

def nochmalgeschlecht():
    jageschlecht.destroy()
    neingeschlecht.destroy()
    blase.configure(text="Bist du ein Junge"+"\n"+"oder ein Mädchen?"+"\n"*3)
    geschlechter()


def geschlechtjanein():
    global jageschlecht,neingeschlecht
    jageschlecht=Button(main,text="Ja",width=40,height=3,bg="dark blue",command=namebestimmen)
    neingeschlecht=Button(main,text="Nein",width=40,height=3,bg="dark red",command=nochmalgeschlecht)
    jageschlecht.place(x=400,y=500)
    neingeschlecht.place(x=400,y=570)

def nachfrage():
    mann.destroy()
    frau.destroy()
    blase.configure(text="Also bist du ein"+"\n"+geschlecht+"?"+"\n"*3)
    geschlechtjanein()

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
