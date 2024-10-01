class Personnage : 
### initialisation de la classe Personnage ###
    def __init__(self, pseudo, niveau = 1):
        self.pseudo = pseudo
        self.niveau = niveau
        self.pv = niveau
        self.initiative = niveau
    
### Méthode attaque ###

    def attaque(self, opposant : 'Personnage'):
        if self.initiative > opposant.initiative:
            opposant.pv -= self.niveau
            if opposant.pv > 0 :
                self.pv -= opposant.niveau
        elif self.initiative < opposant.initiative:
            self.pv -= opposant.niveau
            if opposant.pv > 0 :
                opposant.pv -= self.niveau
        if self.initiative == opposant.initiative :
            self.pv -= opposant.niveau
            opposant -= self.pv

### Méthode combat ###

    def combat(self, opposant : 'Personnage'):
        while self.pv > 0 and opposant.pv > 0:
            self.attaque(opposant)
            opposant.attaque(self)
        if self.pv <= 0 :
            print(f"{self.pseudo} est mort")
        if opposant.pv <= 0 :
            print(f"{opposant.pseudo} est mort")

            
            
### Méthode combat ###

    def soin(self):
        self.pv = self.niveau
        
