#Luci
from tkinter import *

#Luci Klasse
class Luci(object):

    def __init__(self, name, pokemon, items):
        self.name = name
        self.pokemon = pokemon
        self.items = items

    def guckrichtung(self, richtung, name):
        name.configure(image = "luci_"+str(richtung))


