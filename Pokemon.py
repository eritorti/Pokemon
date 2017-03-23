from tkinter import ttk
from tkinter import *
import sndhdr

main=Tk()
main.geometry("1000x800")
main.resizable(width=False,height=False)


mainfarbe=PhotoImage(file="Pokemon_Bilder/main.gif")
fotoeich=PhotoImage(file="Pokemon_Bilder/Eich.gif")
sprechblase=PhotoImage(file="Pokemon_Bilder/sprechblase.gif")
mannfoto=PhotoImage(file="Pokemon_Bilder/ash.gif")
fraufoto=PhotoImage(file="Pokemon_Bilder/misty2.gif")
pokeballrot=PhotoImage(file="Pokemon_Bilder/pokeballrot.gif")
pokeballblau=PhotoImage(file="Pokemon_Bilder/pokeballblau.gif")
pokeballgrün=PhotoImage(file="Pokemon_Bilder/pokeballgrün.gif")
schiggypic=PhotoImage(file="Pokemon_Bilder/schiggy.gif")
glumandapic=PhotoImage(file="Pokemon_Bilder/glumanda.gif")
bisasampic=PhotoImage(file="Pokemon_Bilder/bisasam.gif")

hintergrund=Label(main,image=mainfarbe)
hintergrund.place(x=0,y=0)

geschlecht=None
v=StringVar()
name=v
starterpokemon=None
#print(name.get())
eichcounter=0
eichcounterpokemon=0
eicherzählt=0
eicherzähltpokemon=0
zählercounter=1
zählercounterpokemon=1
klickfürweiter=Label(main,text="Klick irgendwo hin für weiter!",fg="gray75",font=("Arial",25))
klickfürweiter2=Label(main,text="Klick irgendwo hin für weiter!",fg="gray75",font=("Arial",25))

def menü():
    global lgamename,bstart,bverlassen

    lgamename=Label(main,text="Pokèmon",fg="dark red",font=("Arial",80))
    bstart=Button(main,text="Spielen",bg="dark gray",activebackground="gray",font=("Arial",25),command=cstart)
    bverlassen=Button(main,text="Verlassen",bg="dark gray",activebackground="gray",font=("Arial",25),command=cverlassen)

    lgamename.place(x=270,y=140)
    bstart.place(x=430,y=380)
    
    bverlassen.place(x=415,y=460)

def cstart():
    global startback,eich,blase,mann,frau,blaseausfüllen
    lgamename.destroy()
    bstart.destroy()
    bverlassen.destroy()

    eich=Label(main,image=fotoeich)
    blase=Label(main,image=sprechblase,text="Hallo erstmal ,"+"\n"+"ich bin Professor Eich."+"\n"+"bist du ein Junge"+"\n"+"oder ein Mädchen?"+"\n"*3,compound="center",font=("Arial",9))
#    blaseausfüllen=Label(main,text="  ")
    
#    blaseausfüllen.place(x=320,y=190)
    eich.place(x=400,y=140)
    blase.place(x=320,y=60)
    geschlechter()

def abenteuerbeginnt():
    eich.place(x=800,y=430)
    blase.place(x=720,y=350)
    blase.configure(text="Sehr gut ,"+"\n"+"bitte such dir jetzt"+"\n"+"dein Pokèmon aus."+"\n"*4)
#    blaseausfüllen.destroy()
    jabereit.destroy()
    neinbereit.destroy()
    eichpluspokemon()
def pokemongewählt():
    global schiggycounter,glumandacounter,bisasamcounter,starterpokemon,eicherzähltpokemon,eicherzähltpokemon
    if(schiggycounter==1):
        schiggycounter -=1
        schiggy.destroy()
        jaschiggy.destroy()
        neinschiggy.destroy()
    if(glumandacounter==1):
        glumandacounter -=1
        glumanda.destroy()
        jaglumanda.destroy()
        neinglumanda.destroy()
    if(bisasamcounter==1):
        bisasamcounter -=1
        bisasam.destroy()
        jabisasam.destroy()
        neinbisasam.destroy()
    klickfürweiter2.place(x=320,y=750)
    eich.place(x=400,y=140)
    blase.place(x=320,y=60)
    gleichgehtslos()

def gleichgehtslos():
    global eichcounterpokemon,eicherzähltpokemon,klickfürweiter,zählercounterpokemon,eichzählerpokemon
    blase.configure(text=starterpokemon+" also ,"+"\n"+"ich habe sofort gesehen"+"\n"+"das ihr euch mögt."+"\n"*3)
    if(zählercounterpokemon==1):
        eichzählerpokemon() 
    if(eichcounterpokemon==1):
        blase.configure(text="Nun kann dein"+"\n"+"Abenteuer beginnen ,"+"\n"+"viel Spaß und Erfolg!"+"\n"*4)

    

def eichpluspokemon():
    global eicherzähltpokemon
    eicherzähltpokemon +=1
    pokemonwählen()

def eichzählerpokemon():
    global zählercounterpokemon
    zählercounterpokemon=0
    if(eicherzähltpokemon==1):
        main.bind("<Button-1>",eicherzähltweiterpokemon)

def eicherzähltweiterpokemon(event):
    global eichcounterpokemon
    eichcounterpokemon +=1
    print(eichcounterpokemon)
    gleichgehtslos()

def pokemonwählen():
    global pokeball1,pokeball2,pokeball3
    pokeball1=Button(main,image=pokeballrot,relief=FLAT,command=glumandafrage)
    pokeball2=Button(main,image=pokeballblau,relief=FLAT,command=schiggyfrage)
    pokeball3=Button(main,image=pokeballgrün,relief=FLAT,command=bisasamfrage)
    pokeball1.place(x=150,y=200)
    pokeball2.place(x=450,y=200)
    pokeball3.place(x=750,y=200)
schiggycounter=0
glumandacounter=0
bisasamcounter=0

def glumandafrage():
    global glumanda,glumandacounter,jaglumanda,neinglumanda,starterpokemon
    glumandacounter +=1
    starterpokemon="Glumanda"
    pokeball1.destroy()
    pokeball2.destroy()
    pokeball3.destroy()
    blase.configure(text="Das ist Glumanda ,"+"\n"+"ein Feuer Pokèmon ,"+"\n"+"willst du ihn nehmen?"+"\n"*3)    
    glumanda=Label(main,image=glumandapic)
    jaglumanda=Button(main,text="Ja , na klar!",width=40,height=3,bg="dark blue",command=pokemongewählt)
    neinglumanda=Button(main,text="Nein , ein anderes!",width=40,height=3,bg="dark red",command=nochmalpokemon)

    jaglumanda.place(x=360,y=500)
    neinglumanda.place(x=360,y=570)
    glumanda.place(x=400,y=200)    
def schiggyfrage():
    global schiggy,schiggycounter,jaschiggy,neinschiggy,starterpokemon
    schiggycounter +=1
    starterpokemon="Schiggy"
    pokeball1.destroy()
    pokeball2.destroy()
    pokeball3.destroy()
    blase.configure(text="Das ist Schiggy ,"+"\n"+"ein Wasser Pokèmon ,"+"\n"+"willst du ihn nehmen?"+"\n"*3)
    schiggy=Label(main,image=schiggypic)
    jaschiggy=Button(main,text="Ja , na klar!",width=40,height=3,bg="dark blue",command=pokemongewählt)
    neinschiggy=Button(main,text="Nein , ein anderes!",width=40,height=3,bg="dark red",command=nochmalpokemon)

    jaschiggy.place(x=360,y=500)
    neinschiggy.place(x=360,y=570)
    schiggy.place(x=400,y=200)
def bisasamfrage():
    global bisasam,bisasamcounter,jabisasam,neinbisasam,starterpokemon
    bisasamcounter +=1
    starterpokemon="Bisasam"
    pokeball1.destroy()
    pokeball2.destroy()
    pokeball3.destroy()
    blase.configure(text="Das ist Bisasam ,"+"\n"+"ein Blatt Pokèmon ,"+"\n"+"willst du ihn nehmen?"+"\n"*3)
    bisasam=Label(main,image=bisasampic)
    jabisasam=Button(main,text="Ja , na klar!",width=40,height=3,bg="dark blue",command=pokemongewählt)
    neinbisasam=Button(main,text="Nein , ein anderes!",width=40,height=3,bg="dark red",command=nochmalpokemon)

    jabisasam.place(x=360,y=500)
    neinbisasam.place(x=360,y=570)
    bisasam.place(x=400,y=200)
def nochmalpokemon():
    global schiggycounter,glumandacounter,bisasamcounter,starterpokemon
    if(schiggycounter==1):
        schiggycounter -=1
        schiggy.destroy()
        jaschiggy.destroy()
        neinschiggy.destroy()
    if(glumandacounter==1):
        glumandacounter -=1
        glumanda.destroy()
        jaglumanda.destroy()
        neinglumanda.destroy()
    if(bisasamcounter==1):
        bisasamcounter -=1
        bisasam.destroy()
        jabisasam.destroy()
        neinbisasam.destroy()
    starterpokemon=None
    blase.configure(text="Ok nochmal ,"+"\n"+"such dir jetzt"+"\n"+"dein Pokèmon aus."+"\n"*4)
    pokemonwählen()

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
    zählercounter =0
    if(eicherzählt==1):
        main.bind("<Button-1>",eicherzähltweiter)
def nochmalnamebestätigt():
    jainsmenü.destroy()
    neinweiter.destroy()
    namebestätigt()
def namebestätigt():
    global eichcounter,eicherzählt,name,jabereit,neinbereit,klickfürweiter,zählercounter,eichzähler
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
