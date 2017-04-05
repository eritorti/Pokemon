class pokemon(object):

    def __init__(self , minhp , atk , magicatk , defends , magicdefends , spd , acc , maxhp , momentanehp ,name , attacken , lvl ,ep ,epnextlvl):
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
        else:
            self.ep += menge
