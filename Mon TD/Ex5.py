def dictionnaire(dico : dict, prefixe : str):
    for cle, valeur in dico.items():
        print(f"{prefixe} {cle} : {valeur}")

dico = {'nom': 'Alice', 'age' : 20, 'ville' : 'Paris'}
dictionnaire(dico, "info")        


