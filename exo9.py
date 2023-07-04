def produitEntier(x, n):
    if n== 0:
        return 1
    else:
        return x * produitEntier(x,n-1)
x = int(input("Entrer un nombre x :"))
n = int(input("Entier un enter n :"))
res = produitEntier(x,n)
print(f"{x} à la puissance {n} est égale à {res} ")


    