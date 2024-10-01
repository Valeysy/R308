from Personnage import Personnage

### Initialisation de la classe Guerrier ###

class Mage(Personnage) : 
    def __init__(self, pseudo, niveau = 1):
        super().__init__ (pseudo, niveau)
        self.pv = niveau*5+10
        self.initiative = niveau*6+4
        self.mana = niveau*5
        
        
        
    