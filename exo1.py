def AnneeBiss(n):
    if (n%4==0 and n%100!=0) or n%400==0:
        print("{} est une année bissextile".format(n))   
    else:
        print("{} n'est pas une année bissextile".format(n))

    return None
annee = int(input("Entrer une annee :"))
AnneeBiss(annee)
