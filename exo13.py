def factorielle(n):
    if n ==0:
        return 1
    else:
        return n* factorielle(n-1)
n = int(input("Entrer un entier"))
res = factorielle(n)
print(f"{n} ! = {res}")
