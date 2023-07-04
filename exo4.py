def Produit(n, m):
    produit =1
    if n <m :
        for i in range (n, m+1):
            produit *= i
    else:
        print(f"{n} doit etre inferireur à {m}")
    print(produit)
n = int(input("Entrer le premier entier :"))
m = int(input("Entrer le deuxieme entier :"))
Produit(n, m)