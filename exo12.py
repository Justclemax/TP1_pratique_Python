import random

def echanger(tableau, i, j):
    tableau[i], tableau[j] = tableau[j], tableau[i]

tableau = [random.randint(1, 100) for _ in range(10)]
print("Avant le tri :", tableau)

for i in range(len(tableau)):
    for j in range(i+1, len(tableau)):
        if tableau[j] < tableau[i]:
            echanger(tableau, i, j)

resultat = ", ".join(map(str, tableau))
print("Après le tri :", resultat)
