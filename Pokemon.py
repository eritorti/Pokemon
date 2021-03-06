from tkinter import ttk
from tkinter import *
import tkinter
import time
import random
from Kampf_system import *
from Kampf_system import pokemon
from Kampf_system import Schiggy
from Kampf_system import Bisasam
from Kampf_system import Glumanda
from Luci_klasse import *

#schiggy=Schiggy(0,7,7,10,6,8,11,13,13,"Schiggy",[],1,0,5,"Wasser",24,0)
#glumanda=Glumanda(0,9,6,8,6,10,9,14,14,"Glumanda",[],1,0,5,"Feuer",25,0)
#bisasam=Bisasam(0,6,10,7,8,11,10,12,12,"Bisasam",[],1,0,5,"Pflanze",28,0)

main=tkinter.Tk()
main.geometry("1000x800")
main.resizable(width=False,height=False)
main.title("Pokemon Gold")

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
ashfrontlinkesbein=PhotoImage(file="ash_front_linkes_bein.png")
ashfrontrechtesbein=PhotoImage(file="ash_front_rechtes_bein.png")
ashfrontsteht=PhotoImage(file="ash_front_stand.png")
ashbacksteht=PhotoImage(file="ash_back_stand.png")
ashbacklinkesbein=PhotoImage(file="ash_back_linkes_bein.png")
ashbackrechtesbein=PhotoImage(file="ash_back_rechtes_bein.png")
ashleftsteht=PhotoImage(file="ash_left_stand.png")
ashleftlinkesbein=PhotoImage(file="ash_left_linkes_bein.png")
ashleftrechtesbein=PhotoImage(file="ash_left_rechtes_bein.png")
ashrightsteht=PhotoImage(file="ash_right_stand.png")
ashrightlinkesbein=PhotoImage(file="ash_right_linkes_bein.png")
ashrightrechtesbein=PhotoImage(file="ash_right_rechtes_bein.png")
#################################################################################################
#Bilde pfade
luci_left = PhotoImage(file = "luci_left.gif")
luci_up = PhotoImage(file = "luci_up.gif")
luci_down = PhotoImage(file = "luci_down.gif")
luci_right = PhotoImage(file = "luci_right.gif")
luci_move_right_right = PhotoImage(file = "luci_right_move_right.gif")
luci_move_right_left = PhotoImage(file = "luci_right_move_left.gif")   
#############################################################################################
herohouseup=PhotoImage(file="herohouseoben.png")
herohousedown=PhotoImage(file="herohouseunten.png")
schwarz=PhotoImage(file="schwarz.gif")
aktionblase=PhotoImage(file="aktionsblase.png")

momentanespokemon=None
sprechen=None
Map=None
geschlecht=None
v=StringVar()
name=v
ashguckrichtung=None
starterpokemon=None
eichcounter=0
eichcounterpokemon=0
eicherzählt=0
eicherzähltpokemon=0
zählercounter=1
zählercounterpokemon=1
klickfürweiter=Label(main,text="Klick irgendwo hin für weiter!",fg="gray75",font=("Arial",25))
klickfürweiter2=Label(main,text="Klick irgendwo hin für weiter!",fg="gray75",font=("Arial",25))
itemsbeeren=[]
itemstränke=[]
ashs=0
fernash=0
wiiash=0
schildash=0
spüleash=0
kühlschrankash=0
pokemonbag=[]


#Tränke werden defeniert
wasser=tränke("Wasser",10,None)
trank=tränke("Trank",10,None)
supertrank=tränke("Supertrank",50,None)

#Beeren werden definiert
aprikoko=beeren("Aprikokobeere",0,"schlaf")
pirsif=beeren("Pirsifbeere",0,"vergiftung")
sinnoh=beeren("Sinnohbeere",10,None)
sinel=beeren("Sinelbeere",10,None)

passivname="Wasserschwert"
passivdescription="Wenn du unter wenig HP hast wirst du stärker!"


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
    global schiggycounter,glumandacounter,bisasamcounter,starterpokemon,eicherzähltpokemon,eicherzähltpokemon,pokemonbag
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
    pokemonbag.append(starterpokemon)
    klickfürweiter2.place(x=320,y=750)
    eich.place(x=400,y=140)
    blase.place(x=245,y=23)
    gleichgehtslos()

def gleichgehtslos():
    global eichcounterpokemon,eicherzähltpokemon,klickfürweiter2,zählercounterpokemon,eichzählerpokemon
    blase.configure(text=pokemonbag[0].name+" also ,"+"\n"+"ich habe sofort gesehen"+"\n"+"das ihr euch mögt."+"\n"*3)
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
    global move,karte,ash_front_steht,ashmovecounter,x,y,frontlinksrechts,backlinksrechts,leftlinksrechts,rightlinksrechts,geschlecht,Map,ashguckrichtung,sprechlabel
    move=False
    ashmovecounter=0
    frontlinksrechts=0
    backlinksrechts=0
    leftlinksrechts=0
    rightlinksrechts=0
    y=139
    x=138
    Map="Herohouseoben"
    main.bind("<Button-1>",cpass)
    main.configure(bg="black")
    karte=tkinter.Canvas(main,width=158,height=158,bg="black")
    karte.create_image(80,80,image=herohouseup,tags="map")
    karte.create_image(x,y,image=ashfrontsteht,tags="Ash")
    ashguckrichtung="unten"
    sprechlabel=Button(main,text="Aktion(K)",bg="gray",fg="black",font=("Unciala",20),state="disabled",command=buttoneventSprechen)
    sprechlabel.place(x=600,y=400)
    main.bind("<Button-1>",cpass)
    main.configure(bg="black")
    karte.place(x=390,y=210)
    uiactive()
    herohouseoben()
    if(geschlecht=="Junge"):
        ashbewegung()

def uiactive():
    global ui,buileaven,buiinventar,buipokemon,pokemonbag,uipokemon1,uipokemon2,uipokemon3,uipokemon4,uipokemon5,uipokemon6
    ui=Frame(main,width=250,height=250,bg="light blue")
    ui.place(x=340,y=373)
    buileaven=Button(ui,text="Verlassen",font=("Arial",13),width=10,height=1,relief=FLAT,command=uileave)
    buileaven.place(x=125,y=200)
    buiinventar=Button(ui,text="Inventar",font=("Arial",13),width=10,height=1,relief=FLAT,command=uiinventar)
    buiinventar.place(x=10,y=100)
    buipokemon=Button(ui,text="Pokèmon",font=("Arial",13),width=10,height=1,relief=FLAT,command=uipokemon)
    buipokemon.place(x=10,y=20)

def uipokemon():
    global ui,buileaven,buiinventar,buipokemon,uipokemonback,uipokemon1
    buileaven.destroy()
    buiinventar.destroy()
    buipokemon.destroy()
#    print(pokemonbag[0])
    main.bind("<Key-Down>",cpass)
    main.bind("<Key-Up>",cpass)
    main.bind("<Key-Right>",cpass)
    main.bind("<Key-Left>",cpass)
    ui.configure(bg="cornflower blue")
    uipokemonback=Button(ui,text="Zurück",relief=FLAT,bg="dark red",activebackground="red",command=cuipokemonback)

    uipokemon1=Button(ui,text=pokemonbag[0].name,width=12,height=1,font=("Arial",10),command=showpokemon)

    uipokemon1.place(x=15,y=20)

    uipokemonback.place(x=90,y=220)

def showpokemon():
    global uipokemonback,uipokemon1,momentanespokemon,ui,showdisplay,pokemonbag,showpokemon1back,showpokemonstats,showpokemonangriffe,showpokemon1zähler
    uipokemon1.destroy()  

    showpokemon1zähler=1
    uipokemonback.destroy()
    showdisplay=Frame(ui,bg="orange",width=150,height=215)
    showpokemonstats=Button(ui,text="Stats",relief=FLAT,command=pokemonstats)
    showpokemonangriffe=Button(ui,text="Attacken",relief=FLAT,command=pokemonattacken)
    showpokemonstats.place(x=2,y=30)
    showpokemonangriffe.place(x=2,y=60)
    ui.configure(bg="dark orange")
    showdisplay.place(x=85,y=12)
    showpokemon1back=Button(ui,text="Zurück",bg="dark red",activebackground="red",command=showpokemonback)
    showpokemon1back.place(x=2,y=180)
pokemonattackentimer=0

def pokemonstats():
    global showdisplay,pokemonbag,momentanespokemon,showhp,showatk,showmagicatk,showdefends,showmagicdefends,showspd,showacc,schiggyinfos,pokemonstatstimer
    showdisplay.destroy()

    #Farbe der HP leiste wird hier geändert
    hpleistenfarbe=ttk.Style()
    hpleistenfarbe.theme_use("clam")
    hpleistenfarbe.configure("green.Horizontal.TProgressbar",foreground="green",background="green")

    #stats anzeigen werden generiert
    showdisplay=Frame(ui,bg="orange",width=150,height=215)
    showdisplay.place(x=85,y=12)
    showhp=ttk.Progressbar(showdisplay,style="green.Horizontal.TProgressbar",maximum=pokemonbag[0].maxhp,value=pokemonbag[0].momentanehp,)
    showhptext=Label(showdisplay,text="HP:",bg="orange")
    showatk=Label(showdisplay,bg="dark orange",text="Angriff:"+str(pokemonbag[0].atk)+" "*20,width=30,font=("Arial",10))
    showmagicatk=Label(showdisplay,bg="orange",text="Magischer Angriff:"+str(pokemonbag[0].magicatk)+" "*20,width=30,font=("Arial",10))
    showdefends=Label(showdisplay,bg="dark orange",text="Verteidigung:"+str(pokemonbag[0].defends)+" "*20,width=30,font=("Arial",10))
    showmagicdefends=Label(showdisplay,bg="orange",text="Magische"+" "*20+"\n"+"Vertdeidigung:"+str(pokemonbag[0].magicdefends)+" "*20,width=30,font=("Arial",10))
    showspd=Label(showdisplay,bg="dark orange",text="Agilität:"+str(pokemonbag[0].spd)+" "*20,width=30,font=("Arial",10))
    showacc=Label(showdisplay,bg="orange",text="Genauigkeit:"+str(pokemonbag[0].acc)+" "*20,width=30,font=("Arial",10))

    #stats werden platziert
    showatk.place(x=0,y=35)
    showmagicatk.place(x=0,y=60)
    showdefends.place(x=0,y=85)
    showmagicdefends.place(x=0,y=110)
    showspd.place(x=0,y=160)
    showacc.place(x=0,y=185)
    showhp.place(x=45,y=5)
    showhptext.place(x=10,y=5)

def pokemonattacken():
    global schiggyinfos,showdisplay,showattacke1,showattacke2,showattacke3,showattacke4,pokemonstatstimer
    showdisplay.destroy()
    showdisplay=Frame(ui,bg="white",width=150,height=185)
    showdisplay.place(x=90,y=12)
    zaehler = -1
    slot_y = 40

    for i in range(len(pokemonbag[0].attacken)):
        zaehler += 1
        slot = Label(showdisplay, text=str(pokemonbag[0].attacken[zaehler].name), width = 12, font = ("Arial", 15))
        slot.place(x = 0, y=slot_y)
        slot_y += 40
    
    showname=Label(showdisplay,text="Name:"+pokemonbag[0].name+" "*20,bg="white",width=30,font=("Arial",10))

    #attacken werden platziert
    showname.place(x=0,y=10)
    

def showpokemonback():
    global showhp,showatk,showmagicatk,showdefends,showmagicdefends,showspd,showacc,showdisplay,showpokemon1back,showpokemonstats,showpokemonangriffe,showpokemon1zähler
    showdisplay.destroy()
    showpokemon1back.destroy()
    showpokemonstats.destroy()
    showpokemonangriffe.destroy()
    uipokemon()

def cuipokemonback():
    global uipokemon1,uipokemon2,uipokemon3,uipokemon4,uipokemon5,uipokemon6,uipokemonback
    uipokemon1.destroy()  

    uipokemonback.destroy()
    main.bind("<Key-Down>",ashmovefront)
    main.bind("<Key-Up>",ashmoveback)
    main.bind("<Key-Right>",ashmoveright)
    main.bind("<Key-Left>",ashmoveleft)
    uiactive()

def uiinventar():
    global buiinventar,uiinventartränke,uiinventarback,uiinventardisplay,buileaven,reaktion,inventaranzeige,itemstränke,uiinventarbeeren,buipokemon
    buileaven.destroy()
    buiinventar.destroy()
    buipokemon.destroy()
    try:
        reaktion.destroy()
    except:
        pass
    main.bind("<Key-Down>",cpass)
    main.bind("<Key-Up>",cpass)
    main.bind("<Key-Right>",cpass)
    main.bind("<Key-Left>",cpass)
    ui.configure(bg="dark orange")
    uiinventardisplay=Frame(ui,width=151,height=181,bg="orange")
    uiinventartränke=Button(ui,text="Tränke",relief=FLAT,activeforeground="orange",bg="light blue",command=cuiinventartränke)
    uiinventarback=Button(ui,text="Zurück",relief=FLAT,bg="dark red",activebackground="red",command=cuiinventarback)
    uiinventarbeeren=Button(ui,text="Beeren",relief=FLAT,activeforeground="orange",bg="light blue",command=cuiinventarbeeren)
    inventaranzeige=Label(uiinventardisplay,text="",bg="orange")
    
    uiinventarback.place(x=90,y=215)
    uiinventardisplay.place(x=90,y=10)
    inventaranzeige.place(x=50,y=65)
    uiinventartränke.place(x=10,y=30)
    uiinventarbeeren.place(x=10,y=70)

def cuiinventarbeeren():
    global inventaranzeige,itemsbeeren,uiinventardisplay,uiinventarbeeren,uiinventartränke,beerenbutton,tränkebutton
    uiinventarbeeren.configure(bg="blue")
    uiinventartränke.configure(bg="light blue")
    beerenbutton=Button(uiinventardisplay,text="")

    try:
        tränkebutton.destroy()
    except:
        beerenbutton.destroy()

    if(itemsbeeren==[]):
        beerenbutton.place(x=50,y=65)
        beerenbutton.configure(text="Leer",font=("Arial",20),relief=FLAT,state="disabled",bg="orange",bd=0,fg="black")
    elif(itemsbeeren!=[]):
        beerenbutton.destroy()
        beerenbutton=Button(uiinventardisplay,text="")
        beerenbutton.place(x=5,y=10)
        beerenbutton.configure(text=itemsbeeren[0].name,relief=FLAT,state="normal",bg="orange",activebackground="orange")

def cuiinventartränke():
    global inventaranzeige,itemstränke,uiinventardisplay,uiinventartränke,uiinventarbeeren,beerenbutton,tränkebutton
    uiinventartränke.configure(bg="blue")
    uiinventarbeeren.configure(bg="light blue")
    tränkebutton=Button(uiinventardisplay,text="")
    try:
        beerenbutton.destroy()
    except:
        tränkebutton.destroy()
    if(itemstränke==[]):
        tränkebutton.place(x=50,y=65)
        tränkebutton.configure(text="Leer",font=("Arial",20),relief=FLAT,state="disabled",bg="orange",bd=0,fg="black")
    elif(itemstränke!=[]):
        tränkebutton=Button(uiinventardisplay,text="")
        tränkebutton.place(x=5,y=10)
        tränkebutton.configure(text=itemstränke[0].name,relief=FLAT,state="normal",bg="orange",activebackground="orange")

def cuiinventarback():
    global uiinventardisplay,uiinventartränke,uiinventarback,inventaranzeige
    uiinventardisplay.destroy()
    uiinventartränke.destroy()
    uiinventarback.destroy()
    inventaranzeige.destroy()
    main.bind("<Key-Down>",ashmovefront)
    main.bind("<Key-Up>",ashmoveback)
    main.bind("<Key-Right>",ashmoveright)
    main.bind("<Key-Left>",ashmoveleft)
    uiactive()

def uileave():
    global ui,buileaven,uileaveyes,uileaveno,uileavequestion,buiinventar,buipokemon
    main.bind("<Key-Down>",cpass)
    main.bind("<Key-Up>",cpass)
    main.bind("<Key-Right>",cpass)
    main.bind("<Key-Left>",cpass)
    buileaven.destroy()
    buiinventar.destroy()
    buipokemon.destroy()
    uileavequestion=Label(ui,text="Wirklich verlassen?",bg="light blue")
    uileaveyes=Button(ui,text="Ja",bg="dark red",relief=FLAT,command=cverlassen)
    uileaveno=Button(ui,text="Nein",bg="blue",relief=FLAT,command=cuileaveno)
    uileavequestion.place(x=30,y=50)
    uileaveyes.place(x=40,y=80)
    uileaveno.place(x=80,y=80)
def cuileaveno():
    global uileaveyes,uileaveno,uileavequestion
    main.bind("<Key-Down>",ashmovefront)
    main.bind("<Key-Up>",ashmoveback)
    main.bind("<Key-Right>",ashmoveright)
    main.bind("<Key-Left>",ashmoveleft)
    uileaveyes.destroy()
    uileaveno.destroy()
    uileavequestion.destroy()
    uiactive()

def ashbewegung():
    global ashmovecounter
    ashmovecounter +=1
    if(ashmovecounter==1):
        main.bind("<Key-Down>",ashmovefront)
        main.bind("<Key-Up>",ashmoveback)
        main.bind("<Key-Right>",ashmoveright)
        main.bind("<Key-Left>",ashmoveleft)

def ashmovefront(event):
    global frontlinksrechts,backlinksrechts,leftlinksrechts,rightlinksrechts,x,y,Map,ashguckrichtung,sprechen,Ash,ashs,Map,fernash,reaktion,wiiash,sprechlabel,kühlschrankash,spüleash,schildash
    frontlinksrechts+=1
    backlinksrechts=0
    leftlinksrechts=0
    rightlinksrechts=0
    ashguckrichtung="unten"
    print(x,y)
    aktion=None
    ashs+=1
    if(frontlinksrechts==1):
        karte.delete("Ash")
        karte.create_image(x,y,image=ashfrontsteht,tags="Ash")
    elif(frontlinksrechts==3):
        karte.delete("Ash")
        y +=4
        karte.create_image(x,y,image=ashfrontrechtesbein,tags="Ash")
    elif(frontlinksrechts==5):
        karte.delete("Ash")
        y +=4
        karte.create_image(x,y,image=ashfrontsteht,tags="Ash")
    elif(frontlinksrechts==7):
        karte.delete("Ash")
        y +=4
        karte.create_image(x,y,image=ashfrontlinkesbein,tags="Ash")
        frontlinksrechts=2
    if(Map=="Herohouseoben"):
        #wand
        if(y==147):
            y -=4
        #pflanze
        elif(y==119 and x<=18):
            y-=4
        #bett obere kante
        elif(y==111 and x>=118):
            y-=4
        #bett untere kante
        elif(x>=118 and y==143):
            y-=4
        #treppe
        elif(x>=126 and y==59):
            y-=4
        elif(ashguckrichtung!="hinten" and fernash==1 or ashguckrichtung!="hinten" and wiiash==1 or ashguckrichtung!="hinten" and schildash==1):
            try:
                reaktion.destroy()
                main.bind("<Key-k>",cpass)
                main.bind("<Key-K>",cpass)
            except:
                pass
            fernash=0
            wiiash=0
            schildash=0
            sprechlabel.configure(bg="gray",state="disabled")
    elif(Map=="Herohouseunten"):
        #wand
        if(y==146):
            y-=4
        #busch
        elif(x<=16 and y==118):
            y-=4
        #bar
        elif(x<=48 and y==50):
            y-=4
        #tisch
        elif(x<=64 and x>=28 and y==98):
            y-=4
        elif(ashguckrichtung!="hinten" and fernash ==1 or ashguckrichtung!="hinten" and spüleash==1 or ashguckrichtung!="hinten" and kühlschrankash==1):
            try:
                reaktion.destroy()
                main.bind("<Key-k>",cpass)
                main.bind("<Key-K>",cpass)
            except:
                pass
            fernash=0
            spüleash=0
            kühlschrankash=0            
            sprechlabel.configure(bg="gray",state="disabled")

def ashmoveback(event):
    global backlinksrechts,leftlinksrechts,rightlinksrechts,frontlinksrechts,x,y,Map,ashguckrichtung,sprechen,Ash,ashs,map,fernash,reaktion,wiiash,sprechlabel,kühlschrankash,spüleash,schildash
    backlinksrechts+=1
    frontlinksrechts=0
    leftlinksrechts=0
    rightlinksrechts=0
    ashguckrichtung="hinten"
    print(x,y)
    ashs+=1
    aktion=None
    if(backlinksrechts==1):
        karte.delete("Ash")
        karte.create_image(x,y,image=ashbacksteht,tags="Ash")
    elif(backlinksrechts==3):
        karte.delete("Ash")
        y -=4
        karte.create_image(x,y,image=ashbackrechtesbein,tags="Ash")
    elif(backlinksrechts==5):
        karte.delete("Ash")
        y -=4
        karte.create_image(x,y,image=ashbacksteht,tags="Ash")
    elif(backlinksrechts==7):
        karte.delete("Ash")
        y -=4
        karte.create_image(x,y,image=ashbacklinkesbein,tags="Ash")
        backlinksrechts=2
    if(Map=="Herohouseoben"):
        #wand
        if(y==47):
            y+=4
         #fernseher schreibtisch und wii
        elif(y==63 and x<=82):
            y +=4
            if(x>=36 and x<=60 and y<=71):
                sprechen="fernseherash"
                main.bind("<Key-k>",eventSprechen)
                main.bind("<Key-K>",eventSprechen)
                fernash=1
                sprechlabel.configure(bg="dark red",state="normal",activebackground="red")
            elif(x>=60 and x<=84 and y<=71):
                sprechen="wiiash"
                main.bind("<Key-k>",eventSprechen)
                main.bind("<Key-K>",eventSprechen)
                wiiash=1
                sprechlabel.configure(bg="dark red",state="normal",activebackground="red")
        #treppe
        elif(x>=126 and y==75):
            y+=4
        #bett
        elif(x>=122 and x<=146 and y==131):
            y+=4
        #schild
        elif(x>=102 and x<=106 and y<=51):
            sprechen="schildash"
            main.bind("<Key-k>",eventSprechen)
            main.bind("<Key-K>",eventSprechen)
            schildash=1
            sprechlabel.configure(bg="dark red",state="normal",activebackground="red")
        elif(ashguckrichtung!="hinten" and fernash==1 or ashguckrichtung!="hinten" and wiiash==1 or ashguckrichtung!="hinten" and schildash==1):
            try:
                reaktion.destroy()
                main.bind("<Key-k>",cpass)
                main.bind("<Key-K>",cpass)
            except:
                pass
            fernash=0
            wiiash=0
            schildash=0
            sprechlabel.configure(bg="gray",state="disabled")
    elif(Map=="Herohouseunten"):

        #wand
        if(y==26):
            y +=4
        #treppe
        elif(x<=144 and x>=88 and y==50):
            y +=4
        #kühlschrank
        elif(x<=72 and x>=60 and y==42):
            y+=4
            sprechen="kühlschrankash"
            main.bind("<Key-k>",eventSprechen)
            main.bind("<Key-K>",eventSprechen)
            sprechlabel.configure(bg="dark red",state="normal",activebackground="red")
            kühlschrankash=1
        #fernseher
        elif(x>=76 and x<=112 and y==74):
            y+=4
            sprechen="fernseherash"
            main.bind("<Key-k>",eventSprechen)
            main.bind("<Key-K>",eventSprechen)
            fernash=1
            sprechlabel.configure(bg="dark red",state="normal",activebackground="red")
        #bar
        elif(x<=48 and y==78):
            y+=4
        #tisch
        elif(x<=64 and x>=28 and y==134):
            y+=4
        #spüle
        elif(x<=32 and y==42):
            y+=4
            sprechen="spüleash"
            main.bind("<Key-k>",eventSprechen)
            main.bind("<Key-K>",eventSprechen)
            sprechlabel.configure(bg="dark red",state="normal",activebackground="red")
            spüleash=1
        elif(ashguckrichtung!="hinten" and fernash==1 or ashguckrichtung!="hinten" and spüleash==1 or ashguckrichtung!="hinten" and kühlschrankash==1):
            try:
                reaktion.destroy()
                main.bind("<Key-k>",cpass)
                main.bind("<Key-K>",cpass)
            except:
                pass
            fernash=0
            spüleash=0
            kühlschrankash=0            
            sprechlabel.configure(bg="gray",state="disabled")
def eventSprechen(event):
    global reaktion,fernash,wiiash,schildash,spüleash,kühlschrankash
    try:
        reaktion.destroy()
    except:
        pass
    reaktion=Label(main,image=aktionblase,text="",font=("Arial",7), compound =CENTER)
    reaktion.place(x=388,y=370)
    if(fernash==1):
        fernsehashevent()
    elif(wiiash==1):
        wiiashevent()
    elif(schildash==1):
        reaktion.place(x=388,y=370)
        schildashevent()
    elif(kühlschrankash==1):
        reaktion.place(x=388,y=370)
        kühlschrankashevent()
    elif(spüleash==1):
        reaktion.place(x=388,y=370)
        spüleashevent()
        
def buttoneventSprechen():
    global reaktion,fernash,wiiash,schildash,spüleash,kühlschrankash
    try:
        reaktion.destroy()
    except:
        pass
    reaktion=Label(main,image=aktionblase,text="",font=("Arial",7), compound =CENTER)
    if(fernash==1):
        reaktion.place(x=388,y=370)
        fernsehashevent()
    elif(wiiash==1):
        reaktion.place(x=388,y=370)
        wiiashevent()
    elif(schildash==1):
        reaktion.place(x=388,y=370)
        schildashevent()
    elif(kühlschrankash==1):
        reaktion.place(x=388,y=370)
        kühlschrankashevent()
    elif(spüleash==1):
        reaktion.place(x=388,y=370)
        spüleashevent()
kühlschrankasheventzähler=1
spüleasheventzähler=1
Itemstv=["Sinobeere","Schutz","Drachenklaue","EP-teiler","Sonderbonbon","Para-Heiler","Aufwecker","Mondstein"]
eichtv=[",,Seit immer freundlich zu Pokèmon,"+"\n"+"sie sind eure Freunde!",",,Hab immer genügend"+"\n"+"Pokèbälle mit!",",,Benutzt nie ein Fahrrad in Höhlen ,"+"\n"+"das ist gefährlich!",",,Erkundet die Welt und sammelt"+"\n"+"viele neue Freunde und Erfahrung!"]
beerenlist=[sinnoh,sinel,aprikoko,pirsif]
tränkelist=[wasser,trank,supertrank]

def fernsehashevent():
    global ashguckrichtung,reaktion,Itemstv,eichtv,sprechen
    sendungen=['Prof. Eich:'+'\n'+eichtv[random.randint(0,3)]+'!"','Das Item des tages'+'\n'+'ist '+Itemstv[random.randint(0,7)],"Besondere Pokemon","Legendäre Pokemon"]
    reaktion.configure(text=sendungen[random.randint(0,3)],font=("Arial",7))
    sprechen=None

def wiiashevent():
    global ashguckrichtung,reaktion,sprechen
    reaktion.configure(text="Da ist kein Spiel drin...")
    sprechen=None

def  schildashevent():
    global reaktion,sprechen
    reaktion.configure(text="TO DO LISTE:"+"\n"+"1.Kühlschrank aufräumen."+"\n"+"2.Einkaufen gehen."+"\n"+"3.Spülen.")
    sprechen=None

def kühlschrankashevent():
    global reaktion,kühlschrankasheventzähler,itemsbeeren,beerenlist,sprechen
    if(kühlschrankasheventzähler==1):
        kühlschrankasheventitem=beerenlist[random.randint(0,3)]
        reaktion.configure(text="Du hast"+"\n"+kühlschrankasheventitem.name+" erhalten!",font=("Delphin",10),fg="dark blue")
        itemsbeeren.append(kühlschrankasheventitem)
        kühlschrankasheventzähler-=1
    elif(kühlschrankasheventzähler==0):
        reaktion.configure(text="Wow,der Kühlschrank ist"+"\n"+"ja ordentlich")

def spüleashevent():
    global itemstränke,reaktion,tränke,sprechen,spüleasheventzähler,tränkelist
    if(spüleasheventzähler==1):
        itemstränke.append(tränkelist[0])
        reaktion.configure(text="Du hast"+"\n"+tränkelist[0].name+" erhalten!",fg="dark blue",font=("Delphin",10))
        spüleasheventzähler-=1
    elif(spüleasheventzähler==0):
        reaktion.configure(text="Puh , alles ist Sauber")
    
def ashmoveleft(event):
    global leftlinksrechts,backlinksrechts,rightlinksrechts,frontlinksrechts,x,y,Map,ashguckrichtung,Ash,ashs,map,sprechen,fernash,reaktion,wiiash,sprechlabel,kühlschrankash,spüleash,schildash
    leftlinksrechts+=1
    backlinksrechts=0
    frontlinksrechts=0
    rightlinksrechts=0
    ashguckrichtung="links"
    print(x,y)
    ashs+=1
    aktion=None
    if(leftlinksrechts==1):
        karte.delete("Ash")
        karte.create_image(x,y,image=ashleftsteht,tags="Ash")
    elif(leftlinksrechts==3):
        karte.delete("Ash")
        x -=4
        karte.create_image(x,y,image=ashleftrechtesbein,tags="Ash")
    elif(leftlinksrechts==5):
        karte.delete("Ash")
        x -=4
        karte.create_image(x,y,image=ashleftsteht,tags="Ash")
    elif(leftlinksrechts==7):
        karte.delete("Ash")
        x -=4
        karte.create_image(x,y,image=ashleftlinkesbein,tags="Ash")
        leftlinksrechts=2
    if(Map=="Herohouseoben"):
        #wand
        if(x<=10):
            x +=4
        #pflanze
        elif(y>=123 and x<=22):
            x+=4
        #wii
        elif(x<=82 and y<=59):
            x+=4
        elif(ashguckrichtung!="hinten" and fernash==1 or ashguckrichtung!="hinten" and wiiash==1 or ashguckrichtung!="hinten" and schildash==1):
            try:
                reaktion.destroy()
                main.bind("<Key-k>",cpass)
                main.bind("<Key-K>",cpass)
            except:
                pass
            fernash=0
            wiiash=0
            schildash=0
            sprechlabel.configure(bg="gray",state="disabled")
    elif(Map=="Herohouseunten"):
        #wand
        if(x==8):
            x +=4
        #treppenwand
        elif(x==112 and y>=46 and y<=70):
            x+=4
        #tisch
        elif(x==68 and y>=102 and y<=134):
            x+=4
        #bar
        elif(x==48 and y>=54 and y<=74):
            x+=4
        #spüle
        elif(y<=42 and x==36):
            x+=4
        #busch
        elif(y>=122 and x==20):
            x+=4
        #treppe
        elif(y>=42 and y<=50 and x==144):
            x+=4
        elif(ashguckrichtung!="hinten" and fernash==1 or ashguckrichtung!="hinten" and spüleash==1 or ashguckrichtung!="hinten" and kühlschrankash==1):
            try:
                reaktion.destroy()
                main.bind("<Key-k>",cpass)
                main.bind("<Key-K>",cpass)
            except:
                pass
            fernash=0
            spüleash=0
            kühlschrankash=0
            sprechlabel.configure(bg="gray",state="disabled")
        elif(x<=136 and x>=120 and y<=38):
            main.bind("<Key-Down>",cpass)
            main.bind("<Key-Up>",cpass)
            main.bind("<Key-Right>",cpass)
            main.bind("<Key-Left>",cpass);time.sleep(0.5)
            karte.delete("map")
            Map="Herohouseoben"
            x==123
            y=51
            karte.create_image(80,80,image=herohouseup,tags="map")
            fontlinksrechts=0
            leftlinksrechts=0
            rightlinksrechts=0
            backlinksrechts=0
            main.bind("<Key-Down>",ashmovefront)
            main.bind("<Key-Up>",ashmoveback)
            main.bind("<Key-Right>",ashmoveright)
            main.bind("<Key-Left>",ashmoveleft)            
            
              

def ashmoveright(event):
    global rightlinksrechts,backlinksrechts,leftlinksrechts,frontlinksrechts,x,y,Map,karte,ashguckrichtung,Ash,ashs,map,sprechen,fernash,reaktion,wiiash,sprechlabel,kühlschrankash,spüleash,schildash
    rightlinksrechts+=1
    backlinksrechts=0
    leftlinksrechts=0
    frontlinksrechts=0
    ashguckrichtung="rechts"
    print(x,y)
    aktion=None
    ashs+=1
    if(rightlinksrechts==1):
        karte.delete("Ash")
        karte.create_image(x,y,image=ashrightsteht,tags="Ash")
    if(rightlinksrechts==3):
        karte.delete("Ash")
        x +=4
        karte.create_image(x,y,image=ashrightrechtesbein,tags="Ash")
    elif(rightlinksrechts==5):
        karte.delete("Ash")
        x +=4
        karte.create_image(x,y,image=ashrightsteht,tags="Ash")
    elif(rightlinksrechts==7):
        karte.delete("Ash")
        x +=4
        karte.create_image(x,y,image=ashrightlinkesbein,tags="Ash")
        rightlinksrechts=2
    if(Map=="Herohouseoben"):
        #wand
        if(x>=150):
            x -=4
        #bett untere kante
        elif(x==118 and y==147):
            x-=4
        #bett obere kante
        elif(x==118 and y>=115 and y<=127):
            x-=4
        #treppe
        elif(x==122 and y<=75 and y>=63):
            x-=4
        elif(ashguckrichtung!="hinten" and fernash==1 or ashguckrichtung!="hinten" and wiiash==1 or ashguckrichtung!="hinten" and schildash==1):
            try:
                reaktion.destroy()
                main.bind("<Key-k>",cpass)
                main.bind("<Key-K>",cpass)
                
            except:
                pass
            fernash=0
            wiiash=0
            schildash=0
            sprechlabel.configure(bg="gray",state="disabled")

        elif(x>=134 and y<=59): 
            main.bind("<Key-Down>",cpass)
            main.bind("<Key-Up>",cpass)
            main.bind("<Key-Right>",cpass)
            main.bind("<Key-Left>",cpass);time.sleep(0.5)
            karte.delete("map")
            fontlinksrechts=0
            leftlinksrechts=0
            rightlinksrechts=0
            backlinksrechts=0
            main.bind("<Key-Down>",ashmovefront)
            main.bind("<Key-Up>",ashmoveback)
            main.bind("<Key-Right>",ashmoveright)
            main.bind("<Key-Left>",ashmoveleft)
            Map="Herohouseunten"
            x=148
            y=38
            karte.create_image(88,81,image=herohousedown,tags="map")
            try:
                luci.destroy()
            except:
                luci = Label(karte, image = luci_right)
                luci.place(x = 116, y = 62)

    elif(Map=="Herohouseunten"):
        #wand
        if(x==152):
            x -=4
        #kühlschrank
        elif(y>=26 and y<=42 and x==60):
            x-=4
        #treppenwand
        elif(y>=40 and y<=74 and x==72):
            x-=4
        #tisch
        elif(x==28 and y>=86 and y<=134):
            x-=4
        elif(ashguckrichtung!="hinten" and fernash==1 or ashguckrichtung!="hinten" and spüleash==1 or ashguckrichtung!="hinten" and kühlschrankash==1):
            try:
                reaktion.destroy()
                main.bind("<Key-k>",cpass)
                main.bind("<Key-K>",cpass)
            except:
                pass
            fernash=0
            spüleash=0
            kühlschrankash=0
            sprechlabel.configure(bg="gray",state="disabled")
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
    global glumanda,glumandacounter,jaglumanda,neinglumanda,starterpokemon,pokemonbag,glumandainfos
    glumandacounter +=1
    starterpokemon=glumanda
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
    global schiggy,schiggycounter,jaschiggy,neinschiggy,starterpokemon,pokemonbag,schiggyinfos
    schiggycounter +=1
    starterpokemon=schiggy
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
    global bisasam,bisasamcounter,jabisasam,neinbisasam,starterpokemon,pokemonbag,bisasaminfos
    bisasamcounter +=1
    starterpokemon=bisasam

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
    global schiggycounter,glumandacounter,bisasamcounter,starterpokemon,pokemonbag
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
    pokemonbag=[]
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
