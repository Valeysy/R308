from Personnage import Personnage

class Joueur : 
    
    """Définition de la classe personnage"""
    
    def __init__(self, nom : str, maximum : int) :
        self.__nom = nom
        self.__liste_personnage = list()
        self.__maximum = maximum
         
    def ajout_personnage (self, personnage : Personnage) :
        """
        Fonction d'ajout de personnage
        """
    
        if len(self.__liste_personnage) < self.__maximum :
            self.__liste_personnage.append(personnage)
            
            return len(self.__liste_personnage)
        
        else : 
            exit("AYAYAYAYYAyAYA trop de personnage")
            
    def rechercher_personnage_num(self, id : int) : 
        """Rechercher un personnage en fonction de son nom"""
        try :
            return self.__liste_personnage[id]
        except all as err:
            exit("erreur")
            
    def rechercher_personnage_pseudo(self, pseudo : str) :
        try :
            return self.__liste_personnage[pseudo]
        except all as err:
            exit("erreur")
            
    def rechercher_personnage_perso(self, personnage : Personnage): 
        for liste in self.__liste_personnage:
            if  personnage.__eq__ == liste.__eq__ :
                return liste
            
    def supp_personnage_num(self, id : int) : 
            """Supprimer un personnage en fonction de son ID"""
            try :
                self.__liste_personnage.pop(id)
            except all as err:
                exit("erreur")
            
    def supp_personnage_pseudo(self, pseudo: str):
        """Supprimer un personnage en fonction de son Pseudo"""
        e = 0
        for personnage in self.__liste_personnage:
            if personnage.pseudo == pseudo:
                self.__liste_personnage.remove(personnage)
                e = 1
                print(f"Personnage {pseudo} supprimé.")
                break
        
        if e == 0:
            print(f"Aucun personnage trouvé avec le pseudo {pseudo}.")
                
            
    def supp_personnage(self, personnage_a_supprimer):
        """Supprimer un personnage en fonction de l'objet Personnage avec __eq__"""
        if personnage_a_supprimer in self.__liste_personnage:
            self.__liste_personnage.remove(personnage_a_supprimer)
            print(f"Personnage {personnage_a_supprimer.pseudo} supprimé.")
        else:
            print("Personnage non trouvé.")
                

