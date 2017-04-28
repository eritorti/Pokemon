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

    def attacke_zuweisen_step_1(self,attacke):
        self.attacken.append(attacke)
        self.attacken[0].schaden =self.atk*0.05*self.attacken[0].schaden
        round(self.attacken[0].schaden,0)

class Schiggy(pokemon):

    def __init__(self , minhp , atk , magicatk , defends , magicdefends , spd , acc , maxhp , momentanehp ,name , attacken , lvl ,ep ,epnextlvl,element,gewicht):
        pokemon.__init__(self , minhp , atk , magicatk , defends , magicdefends , spd , acc , maxhp , momentanehp ,name , attacken , lvl ,ep ,epnextlvl,element,gewicht)

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

class attacken_list(object):

    def __init__(self,name,schaden,effekt):
        self.schaden=schaden
        self.effekt=effekt
        self.name=name

#Attacken werden definiert
pfund=attacken_list("Pfund",10,None)
tackle=attacken_list("Tackle",10,None)
heuler=attacken_list("Heulen",0,None)

#Pokemon werden definiert
if __name__=="__main__":
    schiggy=Schiggy(0,7,7,9,6,8,11,13,13,"Schiggy",[],1,0,5,"Wasser",23)


