class pokemon(object):

    def __init__(self , minhp , atk , magicatk , defends , magicdefends , spd , acc , maxhp , momentanehp ,name , attacke , lvl ,ep ,epnextlvl,element,gewicht):
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
        self.attacke=attacke
        self.lvl=lvl
        self.ep=ep
        self.epnextlvl=epnextlvl
        self.element=element
    def schadenskonsole(self , ziel , schaden):
        if(ziel.momentanehp - schaden < ziel.minhp):
            return False
        else:
            ziel.momentanehp -=schaden
            return True

    def lvlup(self ,menge):
        if(self.ep + menge >=self.epnextlvl):
            self.lvl +=1
            self.epnextlvl += self.epnextlvl*self.lvl
            self.ep = self.ep + menge
            print("Glückwunsch "+str(self.name)+" hat Level "+str(self.lvl)+" erreicht!")
        else:
            self.ep += menge

    def heilen(self,trank):
        self.momentanehp += trank.heilmenge

class Schiggy(pokemon):

    def __init__(self , minhp , atk , magicatk , defends , magicdefends , spd , acc , maxhp , momentanehp ,name , attacken , lvl ,ep ,epnextlvl,element,gewicht):
        
class tränke(object):

    def __init__(self ,name, heilmenge,effekt):
        self.name=name
        self.heilmenge=heilmenge
        self.effekt=effekt

class beeren(object):

    def __init__(self , name , heilmenge , effekt):
        self.name=name
        self.heilmenge=heilmenge
        self.effekt=effekt
class attacken(object):

    def __init__(self,schaden,effekt):
        self.schaden=schaden
        self.effekt=effekt
#Attacken werden definiert
pfund=attacken(self.atk*0.43,None)
tackle=attacken(self.gewicht/5*self.atk/5)

#Pokemon werden definiert
schiggy=Schiggy(0,7,7,9,6,8,11,13,13,"Schiggy",[],1,0,5,"Wasser",23)


