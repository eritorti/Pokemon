print("Bei fehlern bitte 'klassen_help()' eingeben.")
class pokemon(object):

    def __init__(self , minhp , atk , magicatk , defends , magicdefends , spd , acc , maxhp , momentanehp ,name , attacken , lvl ,ep ,epnextlvl,element,gewicht):
        self.atk=atk
        self.magicatk=magicatk
        self.defends=defends
        self.magicdefends=magicdefends
        self.spd=spd
        self.acc=acc
        self.maxhp=maxhp
        self.momentanehp=momentanehp
        self.name=name
        self.minhp=minhp
        self.attacken=attacken
        self.lvl=lvl
        self.ep=ep
        self.epnextlvl=epnextlvl
        self.element=element
        self.gewicht=gewicht

    #Hier wird der Schaden verteilt , zB im Kampf
    #Muss noch für den Kampf bei wilden und trainer Pokemon optimiert werden !!!!!!
    def schadenskonsole(self , ziel , attacken_platz):        
        if(ziel.momentanehp - self.attacken[attacken_platz].schaden < ziel.minhp):
            print("Pokemon ist schon besiegt!")
            return False
        elif(ziel.momentanehp - self.attacken[attacken_platz].schaden > ziel.minhp):
            ziel.momentanehp -= self.attacken[attacken_platz].schaden
            return True
        else:
            print("Ein fehler ist aufgetreten!")

    #Hier wird einem Pokemon EP gegeben und bei ausreichenden EP auch ein LVL-UP vergeben
    def lvlup(self ,menge):
        if(self.ep + menge >=self.epnextlvl):
            self.lvl +=1
            self.epnextlvl += self.epnextlvl*self.lvl
            self.ep = self.ep + menge
            print("Glückwunsch "+str(self.name)+" hat Level "+str(self.lvl)+" erreicht!")
        else:
            self.ep += menge

    #Hier kann ein Pokemon geheilt werden
    def heilen(self,trank):
        self.momentanehp += trank.heilmenge

    #Hier wird einem Pokemon eine Attacke zugewiesen und der schaden wird den Stats entsprechend angepasst
    def attacke_zuweisen(self,attacke):

        #Attacken mit atk skalierung
        if(attacke.stats_skalierung=="atk"):
            self.attacken.append(attacke)
            platz=self.attacken.index(attacke)
            self.attacken[platz].schaden =self.atk*attacke.skalierung*self.attacken[platz].schaden
            self.attacken[platz].schaden=int(round(self.attacken[platz].schaden,0))

        #Attacken mit gewicht skalierung
        elif(attacke.stats_skalierung=="gewicht"):
            self.attacken.append(attacke)
            platz=self.attacken.index(attacke)
            self.attacken[platz].schaden = self.gewicht*attacke.skalierung*self.attacken[platz].schaden*self.atk/5
            self.attacken[platz].schaden = int(round(self.attacken[platz].schaden,0))

        #elif():

#Klassen für die Pokemon        
class Schiggy(pokemon):

    def __init__(self , minhp , atk , magicatk , defends , magicdefends , spd , acc , maxhp , momentanehp ,name , attacken , lvl ,ep ,epnextlvl,element,gewicht):
        pokemon.__init__(self , minhp , atk , magicatk , defends , magicdefends , spd , acc , maxhp , momentanehp ,name , attacken , lvl ,ep ,epnextlvl,element,gewicht)
    
class Glumanda(pokemon):

    def __init__(self , minhp , atk , magicatk , defends , magicdefends , spd , acc , maxhp , momentanehp ,name , attacken , lvl ,ep ,epnextlvl,element,gewicht):
        pokemon.__init__(self , minhp , atk , magicatk , defends , magicdefends , spd , acc , maxhp , momentanehp ,name , attacken , lvl ,ep ,epnextlvl,element,gewicht)

class Bisasam(pokemon):

    def __init__(self , minhp , atk , magicatk , defends , magicdefends , spd , acc , maxhp , momentanehp ,name , attacken , lvl ,ep ,epnextlvl,element,gewicht):
        pokemon.__init__(self , minhp , atk , magicatk , defends , magicdefends , spd , acc , maxhp , momentanehp ,name , attacken , lvl ,ep ,epnextlvl,element,gewicht)

#Klasse für Heiltränke usw.
class tränke(object):

    def __init__(self ,name, heilmenge,effekt):
        self.name=name
        self.heilmenge=heilmenge
        self.effekt=effekt

#Klasse für Beeren
class beeren(object):

    def __init__(self , name , heilmenge , effekt):
        self.name=name
        self.heilmenge=heilmenge
        self.effekt=effekt

#Klasse für Attacken
class attacken_list(object):

    def __init__(self,name,schaden,effekt,skalierung,stats_skalierung):
        self.schaden=schaden
        self.effekt=effekt
        self.name=name
        self.skalierung=skalierung
        self.stats_skalierung=stats_skalierung

#Attacken werden definiert
pfund=attacken_list("Pfund",10,None,0.06,"atk")
tackle=attacken_list("Tackle",10,None,0.02,"gewicht")
heuler=attacken_list("Heulen",0,None,0,None)

#Pokemon werden definiert
if __name__=="__main__":
    schiggy=Schiggy(0,7,7,10,6,8,11,13,13,"Schiggy",[],1,0,5,"Wasser",24)
    glumanda=Glumanda(0,9,6,8,6,10,9,14,14,"Glumanda",[],1,0,5,"Feuer",25)
    bisasam=Bisasam(0,6,10,7,8,11,10,12,12,"Bisasam",[],1,0,5,"Pflanze",28)

#Hier wird eine Hilf-funktion erstellt
def klassen_help():
    print("Liste der fehlersuch möglichkeiten:\n \n schadenskonsole \n lvlup \n heilen \n attacke_zuweisen \n")
    listen_auswahl=input("Wo kann ich helfen?:")
    #Hilfe für die schadenskonsole
    if(listen_auswahl=="schadenskonsole"):
        print("-"*20)
        print("Liste der möglichkeiten:\n \n funktion \n ziel \n attacken_platz \n")
        schadenskonsole_auswahl=input("Wo liegt das problem?:")
        if(schadenskonsole_auswahl=="funktion"):
            print("-"*20)
            print("Damit kann man ein Pokemon ein angriff ausführen lassen bzw. den schaden berechnen lassen.\n \nBsp.: angreifer_name.schadenskonsole(ziel_name , attacken_platz).")
        elif(schadenskonsole_auswahl=="ziel"):
            print("-"*20)
            print("Wenn als fehlermeldung:\n \n NameError: name 'ziel_eingabe' is not defined \n steht , ist der name des ziels falsch , beachte für ziel muss ein pokemon name hin!")
        elif(schadenskonsole_auswahl=="attacken_platz"):
            print("-"*20)
            print("Wenn als fehlermeldung:\n \n IndexError: list index out of range \n steht , ist die zahl bzw. der attacken_platz nicht vorhanden , beachte für attacken_platz muss eine zahl zwischen 0-3 hin!")
    #Hilfe für lvlup
    elif(listen_auswahl=="lvlup"):
        print("-"*20)
        print("Liste der möglichkeiten:\n \n funktion \n menge \n")
        lvlup_auswahl=input("Wo liegt das problem?:")
        if(lvlup_auswahl=="funktion"):
            print("-"*20)
            print("Damit kann man ein Pokemon ein lvlup bzw. EP geben. \n \nBsp.: lvlup_name.lvlup(menge_der_ep).")
        elif(lvlup_auswahl=="menge"):
            print("-"*20)
            print("Wenn als fehlermeldung:\n \n NameError: name 'menge_eingabe' is not defined \n steht , haben sie eine entweder unzulässige zahl eingeben zB '-1' , sie haben einen string zB 'eins' eingeben , oder sie haben eine zu hohe zahl einegegeben , beachte für menge muss eine positive zahle zB '10' eingegeben werde")
    #Hilfe für heilen
    elif(listen_auswahl=="heilen"):
        print("-"*20)
        print("Liste der möglichkeiten:\n \n funktion \n trank \n")
        heilen_auswahl=input("Wo liegt das problem):")
        if(heilen_auswahl=="funktion"):
            print("-"*20)
            print("Damit kann man ein Pokemon heilen. \n \nBsp.: ziel_der_heilung_name.heilen(trank_name)")
        elif(heilen_auswahl=="trank"):
            print("-"*20)
            print("Wenn als fehlermeldung: \n \n NameError: name 'trank_eingabe' is not defined \n steht , haben sie entweder einen falschen Namen bzw. einen nicht vorhanden trank namen eingeben , oder sie haben eine zahl eingegeben , beachte für trank muss ein trank name hin!")
    #Hilfe für attacke_zuweisen
    elif(listen_auswahl=="attacke_zuweisen"):
        print("-"*20)
        print("Liste der möglichkeiten:\n \n funktion \n attacke \n")
        attacke_zuweisen_auswahl=input("Wo liegt das problem?:")
        if(attacke_zuweisen_auswahl=="funktion"):
            print("-"*20)
            print("Damit kann man einem Pokemon eine attacke zuweisen bzw. erlernen lassen. \n \nBsp.: ziel_der_zuweisung_name.attacke_zuweisen(attacken_name)")
        elif(attacke_zuweisen_auswahl=="attacke"):
            print("-"*20)
            print("Wenn als fehlermeldung: \n \n NameError: name 'attacke_eingabe' is not defined \n steht , haben sie entweder einen falschen namen bzw. einen nicht vorhandenen attacke namen eingegeben , oder sie haben eine zahl eingegeben , beachte für attacke muss ein attacken name hin!")



        

    


