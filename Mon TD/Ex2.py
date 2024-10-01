def superieur_seuil(seuil=10, a=float):
    """Donne si le nombre dépasse un seuil"""

    if a > seuil :
        return("Le seuil est dépassé")
    else :
        return("Le nombre est good")
    
print(superieur_seuil(10, 1))