def decaleCircDroite(tableau):
    dernier_element = tableau[-1]  # Stocke le dernier élément du tableau
    for i in range(len(tableau)-1, 0, -1):
        tableau[i] = tableau[i-1]  # Déplace chaque élément vers la droite
    
    tableau[0] = dernier_element  # Place le dernier élément à la première position

# Exemple d'utilisation
tableau = [12, 21, 10, 11, 0, 1, 6, 8]
print(f"Avant décalage circulaire à droite: {tableau}")
decaleCircDroite(tableau)
print(f"Après décalage circulaire à droite: {tableau}")
