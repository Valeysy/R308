def max_liste_seuil(liste : list, seuil = 3) -> int:
    valeur = 0
    for i in liste:
        if i < seuil:
            valeur += 1
    return valeur
            
    
print(max_liste_seuil([1,2,3, 2, 9,5,5]))