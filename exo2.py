import random

# QUESTION 2.1
def lancer_deux_des():
    de1 = random.randint(1, 6)
    de2 = random.randint(1, 6)
    print(f'voici le prémier dès {de1}  \n et voici le deuxime des {de2}')
    somme = de1 + de2
    return somme

resultat_lancer = lancer_deux_des()
print(f"la somme d'un lancer de deux dés : {resultat_lancer } ")


# QUESTION 2.2
def lancer_des(nombre_des):
    somme = 0
    for _ in range(nombre_des):
        de = random.randint(1, 6)
        
        somme += de
        print(de , end='-')
    return somme

nombre_des = 3
resultat_lancer = lancer_des(nombre_des)
print(f"la somme d'un lancer de {nombre_des} dés : {resultat_lancer}")
