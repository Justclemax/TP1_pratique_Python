def SommeEntier(entier):
    somme = 0
    if entier == 1:
        return 1
    else:
        return entier + SommeEntier(entier-1)
n = int(input("Entrer un nombre entier "))
res = SommeEntier(n)
print(f"la somme des {n} premier entier est égale à {res} ")


    