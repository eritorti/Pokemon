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
    schiggy=Schiggy(0,7,7,9,6,8,11,13,13,"Schiggy",[],1,0,5,"Wasser",23)


