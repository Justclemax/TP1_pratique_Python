
import random 


def nbPairImpair(tableau):
    nb_pair = 0
    nb_impair = 0
    
    for element in tableau:
        if element % 2 == 0:  # Vérifie si l'élément est pair
            nb_pair += 1
        else:
            nb_impair += 1
    
    return nb_pair, nb_impair

tableau = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultat = nbPairImpair(tableau)
print("Nombre d'éléments pairs :", resultat[0])
print("Nombre d'éléments impairs :", resultat[1])

            
        
        
