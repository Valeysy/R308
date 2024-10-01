from Joueur import Joueur
from Personnage import Personnage


def test():
    a = Joueur("Angeloladeboruille", 3)
    b = Personnage ("Helldriver", 4)
    a.ajout_personnage(b)
    
    assert a.rechercher_personnage_num(0) == b
    
    print(a._Joueur__liste_personnage)
    
    for  i in a._Joueur__liste_personnage:
        print(i.pseudo)
test()