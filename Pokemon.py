from tkinter import ttk
from tkinter import *
import tkinter
import time

main=tkinter.Tk()
main.geometry("1000x800")
main.resizable(width=False,height=False)


mainfarbe=PhotoImage(file="main.gif")
fotoeich=PhotoImage(file="Eich.gif")
sprechblase=PhotoImage(file="sprechblase.gif")
mannfoto=PhotoImage(file="ash.gif")
fraufoto=PhotoImage(file="misty2.gif")
pokeballrot=PhotoImage(file="pokeball.gif")
pokeballblau=PhotoImage(file="pokeball.gif")
pokeballgrün=PhotoImage(file="pokeball.gif")
schiggypic=PhotoImage(file="schiggy.gif")
glumandapic=PhotoImage(file="glumanda.gif")
bisasampic=PhotoImage(file="bisasam.gif")
##############################################################################################
ashfrontlinkesbein=PhotoImage(file="ash_front_linkes_bein.gif")
ashfrontrechtesbein=PhotoImage(file="ash_front_rechtes_bein.gif")
ashfrontsteht=PhotoImage(file="ash_front_stand.gif")
ashbacksteht=PhotoImage(file="ash_back_stand.gif")
ashbacklinkesbein=PhotoImage(file="ash_back_linkes_bein.gif")
ashbackrechtesbein=PhotoImage(file="ash_back_rechtes_bein.gif")
ashleftsteht=PhotoImage(file="ash_left_stand.gif")
ashleftlinkesbein=PhotoImage(file="ash_left_linkes_bein.gif")
ashleftrechtesbein=PhotoImage(file="ash_left_rechtes_bein.gif")
ashrightsteht=PhotoImage(file="ash_right_stand.gif")
ashrightlinkesbein=PhotoImage(file="ash_right_linkes_bein.gif")
ashrightrechtesbein=PhotoImage(file="ash_right_rechtes_bein.gif")
#############################################################################################
herohouseup=PhotoImage(file="herohouseoben.gif")
herohousedown=PhotoImage(file="herohouseunten.gif")
schwarz=PhotoImage(file="schwarz.gif")

Map=None
geschlecht=None
v=StringVar()
name=v
ashguckrichtung=None
Map=None
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
    blase=Label(main,image=sprechblase,text="Hallo erstmal ,"+"\n"+"ich bin Professor Eich."+"\n"+"bist du ein Junge"+"\n"+"oder ein Mädchen?"+"\n"*2,compound="center",font=("Arial",9),width=220,height=180)
#    blaseausfüllen=Label(main,text="  ")
    
#    blaseausfüllen.place(x=320,y=190)
    eich.place(x=400,y=140)
    blase.place(x=245,y=23)
    geschlechter()

def abenteuerbeginnt():
    eich.place(x=800,y=433)
    blase.place(x=645,y=316)
    blase.configure(text="Sehr gut ,"+"\n"+"bitte such dir jetzt"+"\n"+"dein Pokèmon aus."+"\n"*2)
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
    blase.place(x=245,y=23)
    gleichgehtslos()

def gleichgehtslos():
    global eichcounterpokemon,eicherzähltpokemon,klickfürweiter2,zählercounterpokemon,eichzählerpokemon
    blase.configure(text=starterpokemon+" also ,"+"\n"+"ich habe sofort gesehen"+"\n"+"das ihr euch mögt."+"\n"*3)
    if(zählercounterpokemon==1):
        eichzählerpokemon() 
    if(eichcounterpokemon==1):
        blase.configure(text="Nun kann dein"+"\n"+"Abenteuer beginnen ,"+"\n"+"viel Spaß und Erfolg!"+"\n"*4)
    if(eichcounterpokemon==2):
        eich.destroy()
        blase.destroy()
        klickfürweiter2.destroy()
        firstspawn()
def herohouseoben():
    global Map
    Map="Herohouseoben"
def firstspawn():
    global move,karte,ash_front_steht,ashmovecounter,x,y,frontlinksrechts,backlinksrechts,leftlinksrechts,rightlinksrechts,geschlecht,Map,ashguckrichtung
    move=False
    ashmovecounter=0
    frontlinksrechts=0
    backlinksrechts=0
    leftlinksrechts=0
    rightlinksrechts=0
    x=128
    y=130
    Map="Herohouseoben"
    main.bind("<Button-1>",cpass)
    main.configure(bg="black")
    karte=tkinter.Canvas(main,width=158,height=158,bg="black")
    karte.create_image(80,80,image=herohouseup)
    ash_front_steht=Label(karte,image=ashfrontsteht)
    ashguckrichtung="unten"
    main.bind("<Button-1>",cpass)
    main.configure(bg="black")
#    karte.create_image(80,80,image=herohouseup)
    ash_front_steht=Label(karte,image=ashfrontsteht)
    karte.focus_set()
    karte.place(x=380,y=260)
    herohouseoben()
    if(geschlecht=="Junge"):
        ashbewegung()
        ash_front_steht.place(x=x,y=y)
        
def ashbewegung():
    global ashmovecounter
    ashmovecounter +=1
    if(ashmovecounter==1):
        main.bind("<Key-Down>",ashmovefront)
        main.bind("<Key-Up>",ashmoveback)
        main.bind("<Key-Right>",ashmoveright)
        main.bind("<Key-Left>",ashmoveleft)

def ashmovefront(event):
    global frontlinksrechts,backlinksrechts,leftlinksrechts,rightlinksrechts,x,y,Map
    global frontlinksrechts,backlinksrechts,leftlinksrechts,rightlinksrechts,x,y,Map,ashguckrichtung
    frontlinksrechts+=1
    backlinksrechts=0
    leftlinksrechts=0
    rightlinksrechts=0
    ashguckrichtung="unten"
    print(x,y)
    ash_front_steht.configure(image=ashfrontsteht)
    ash_front_steht.place(x=x,y=y)
    if(frontlinksrechts==2):
        y +=4
        ash_front_steht.configure(image=ashfrontrechtesbein)
        ash_front_steht.place(x=x,y=y)
    elif(frontlinksrechts==4):
        y +=4
        ash_front_steht.configure(image=ashfrontsteht)
        ash_front_steht.place(x=x,y=y)
    elif(frontlinksrechts==5):
        y +=4
        ash_front_steht.configure(image=ashfrontlinkesbein)
        ash_front_steht.place(x=x,y=y)
        frontlinksrechts=0
    if(Map=="Herohouseoben"):
        if(y==138):
            y -=4
            ash_front_steht.place(y=y)
        elif(x<=15 and y>=110):        
            y -=4
            ash_front_steht.place(y=y,x=x)
        elif(x>=108 and x<=140 and y==134 or x>=108 and x<=140 and y==102 or x>=112 and y==50):
            y -=4
            ash_front_steht.place(x=x,y=y)
    elif(Map=="Herohouseunten"):
        #wand
        if(y==142):
            y-=4
            ash_front_steht.place(x=x,y=y)
        #busch
        elif(x<=12 and y==110):
            y-=4
            ash_front_steht.place(x=x,y=y)
        #bar
        elif(x<=40 and y==42):
            y-=4
            ash_front_steht.place(x=x,y=y)
        #tisch
        elif(x<=60 and x>=20 and y==90):
            y-=4
            ash_front_steht.place(x=x,y=y)



def ashmoveback(event):
    global backlinksrechts,leftlinksrechts,rightlinksrechts,frontlinksrechts,x,y,Map,ashguckrichtung
    backlinksrechts+=1
    frontlinksrechts=0
    leftlinksrechts=0
    rightlinksrechts=0
    ashguckrichtung="hinten"
    print(x,y)
    ash_front_steht.configure(image=ashbacksteht)
    ash_front_steht.place(x=x,y=y)
    if(backlinksrechts==2):
        y -=4
        ash_front_steht.configure(image=ashbackrechtesbein)
        ash_front_steht.place(x=x,y=y)
    elif(backlinksrechts==4):
        y -=4
        ash_front_steht.configure(image=ashbacksteht)
        ash_front_steht.place(x=x,y=y)
    elif(backlinksrechts==5):
        y -=4
        ash_front_steht.configure(image=ashbacklinkesbein)
        ash_front_steht.place(x=x,y=y)
        backlinksrechts=0
    if(Map=="Herohouseoben"):
        if(y==42):
            y +=4
            ash_front_steht.place(y=y,x=x)
        elif(x<=76 and y==58):
            y +=4
            ash_front_steht.place(x=x,y=y)

        elif(x<=76 and y==58):
            y +=4
            ash_front_steht.place(x=x,y=y)
        elif(x>=108 and x<=140 and y==126 or x>=112 and y==74):
            y +=4
            ash_front_steht.place(x=x,y=y)
    elif(Map=="Herohouseunten"):

        #wand
        if(y==26):
            y +=4
            ash_front_steht.place(x=x,y=y)
        #treppe
        elif(x<=140 and x>=88 and y==50):
            y +=4
            ash_front_steht.place(x=x,y=y)
        #kühlschrank
        elif(x<=68 and x>=48 and y==42):
            y+=4
            ash_front_steht.place(x=x,y=y)
        #fernseher
        elif(x>=64 and x<=108 and y==74):
            y+=4
            ash_front_steht.place(x=x,y=y)
        #bar
        elif(x<=40 and y==78):
            y+=4
            ash_front_steht.place(x=x,y=y)
        #tisch
        elif(x<=60 and x>=20 and y==134):
            y+=4
            ash_front_steht.place(x=x,y=y)
        #spüle
        elif(x<=28 and y==34):
            y+=4
            ash_front_steht.place(x=x,y=y)


def ashmoveleft(event):
    global leftlinksrechts,backlinksrechts,rightlinksrechts,frontlinksrechts,x,y,Map,ashguckrichtung

    leftlinksrechts+=1
    backlinksrechts=0
    frontlinksrechts=0
    rightlinksrechts=0
    ashguckrichtung="links"
    print(x,y)
    ash_front_steht.configure(image=ashleftsteht)
    ash_front_steht.place(x=x,y=y)

    if(leftlinksrechts==2):
        x -=4
        ash_front_steht.configure(image=ashleftrechtesbein)
        ash_front_steht.place(x=x,y=y)
    elif(leftlinksrechts==4):
        x -=4
        ash_front_steht.configure(image=ashleftsteht)
        ash_front_steht.place(x=x,y=y)
    elif(leftlinksrechts==5):
        x -=4
        ash_front_steht.configure(image=ashleftlinkesbein)
        ash_front_steht.place(x=x,y=y)
        leftlinksrechts=0
    if(Map=="Herohouseoben"):        
        if(x==-4):
            x +=4
            ash_front_steht.place(y=y,x=x)
        if(x==12 and y>=110 or x==76 and y<=58):
            x +=4
            ash_front_steht.place(x=x,y=y)
    elif(Map=="Herohouseunten"):
        #wand
        if(x==-4):
            x +=4
            ash_front_steht.place(x=x,y=y)
        #treppenwand
        elif(x==108 and y>=46 and y<=74):
            x+=4
            ash_front_steht.place(x=x,y=y)
        #tisch
        elif(x==60 and y>=90 and y<=134):
            x+=4
            ash_front_steht.place(x=x,y=y)
        #bar
        elif(x==40 and y>=42 and y<=74):
            x+=4
            ash_front_steht.place(x=x,y=y)
        #spüle
        elif(y>=26 and y<=34 and x==28):
            x+=4
            ash_front_steht.place(x=x,y=y)
        #busch
        elif(y>=110 and x==12):
            x+=4
            ash_front_steht.place(x=x,y=y)
        #treppe
        elif(y>=34 and y<=50 and x==140):
            x+=4
            ash_front_steht.place(x=x,y=y)
        elif(x<=136 and x>=120 and y==30):
            main.bind("<Key-Down>",cpass)
            main.bind("<Key-Up>",cpass)
            main.bind("<Key-Right>",cpass)
            main.bind("<Key-Left>",cpass)
            karte.create_image(88,81,image=schwarz);time.sleep(0.5)
            Map="Herohouseoben"
            x==104
            y=46
            ash_front_steht.place(x=x,y=y)
            karte.create_image(80,80,image=herohouseup)
            main.bind("<Key-Down>",ashmovefront)
            main.bind("<Key-Up>",ashmoveback)
            main.bind("<Key-Right>",ashmoveright)
            main.bind("<Key-Left>",ashmoveleft)            
            
                

def ashmoveright(event):
    global rightlinksrechts,backlinksrechts,leftlinksrechts,frontlinksrechts,x,y,Map,karte,ashguckrichtung
    rightlinksrechts+=1
    backlinksrechts=0
    leftlinksrechts=0
    frontlinksrechts=0
    ashguckrichtung="rechts"
    print(x,y)
    ash_front_steht.configure(image=ashrightsteht)
    ash_front_steht.place(x=x,y=y)
    if(rightlinksrechts==2):
        x +=4
        ash_front_steht.configure(image=ashrightrechtesbein)
        ash_front_steht.place(x=x,y=y)
    elif(rightlinksrechts==4):
        x +=4
        ash_front_steht.configure(image=ashrightsteht)
        ash_front_steht.place(x=x,y=y)
    elif(rightlinksrechts==5):
        x +=4
        ash_front_steht.configure(image=ashrightlinkesbein)
        ash_front_steht.place(x=x,y=y)
        rightlinksrechts=0
    if(Map=="Herohouseoben"):        
        if(x==144):
            x -=4
            ash_front_steht.place(y=y,x=x)
        elif(x>=108 and y>=102 and y<=126 or x>=108 and y==134 or x>=112 and y>=50 and y<=74):
            x-=4
            ash_front_steht.place(x=x,y=y)
        elif(x==136 and y==46):
            main.bind("<Key-Down>",cpass)
            main.bind("<Key-Up>",cpass)
            main.bind("<Key-Right>",cpass)
            main.bind("<Key-Left>",cpass)
            karte.create_image(88,81,image=schwarz);time.sleep(0.5)
            main.bind("<Key-Down>",ashmovefront)
            main.bind("<Key-Up>",ashmoveback)
            main.bind("<Key-Right>",ashmoveright)
            main.bind("<Key-Left>",ashmoveleft)
            Map="Herohouseunten"
            x=144
            y=30
            ash_front_steht.place(x=x,y=y)
            karte.create_image(88,81,image=herohousedown)


    elif(Map=="Herohouseunten"):
        #wand
        if(x==148):
            x -=4
            ash_front_steht.place(x=x,y=y)
        #kühlschrank
        elif(y>=26 and y<=42 and x==48):
            x-=4
            ash_front_steht.place(x=x,y=y)
        #treppenwand
        elif(y>=40 and y<=74 and x==64):
            x-=4
            ash_front_steht.place(x=x,y=y)
        #tisch
        elif(x==20 and y>=86 and y<=134):
            x-=4
            ash_front_steht.place(x=x,y=y)
            karte.configure(image=herohousedown)
            ash_front_steht.place(x=x,y=y)
    elif(Map=="Herohouseunten"):
        if(x==144):
            x -=4
            ash_front_steht.place(y=y,x=x)
        elif(x==64 and y<=74 and y>=22):
            x -=4
            ash_front_steht.place(x=x,y=y)
def ashmovepass(event):
    pass
            
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
    mann=Button(main,image=mannfoto,relief=FLAT,command=männlich)
    frau=Button(main,image=fraufoto,relief=FLAT,command=weiblich)
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
