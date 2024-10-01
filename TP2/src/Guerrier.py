from Personnage import Personnage

#### Initialisation de la classe Guerrier ###

class Guerrier(Personnage) : 
    def __init__(self, pseudo, niveau = 1):
        super().__init__ (pseudo, niveau)
        self.pv = niveau*8+4
        self.initiative = niveau*4+6
        
        