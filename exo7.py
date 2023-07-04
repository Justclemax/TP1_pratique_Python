#QUESTION 7.1 : DU BINAIRE VERS LE DÉCIMAL.
def bin2Dec(nBin):
    decimal = 0
    puissance = 0
    for i in range(len(nBin)-1, -1, -1):
        if nBin[i] == '1':
            decimal += 2 ** puissance
        puissance += 1
    return decimal

# Exemple d'utilisation
nBin = '10000001'
decimal = bin2Dec(nBin)
print(f"{nBin} en decimal est egale à {decimal}")

#QUESTION 7.2 : DU DÉCIMAL VERS LE BINAIRE
def Decbin2(decimal):
    nombre_binaire = ''
    quotient = -1
    while quotient != 0:
        q = decimal//2
        reste = decimal%2
        nombre_binaire = str(reste) + nombre_binaire 
        
        
    return nombre_binaire

def dec2Bin(decimal):
    nombre_binaire = ''
    if decimal == 0:
        return '0'
    else:
        while decimal > 0:
            nombre_binaire= str(decimal % 2) + nombre_binaire
            decimal //= 2
    
    return nombre_binaire

# Exemple d'utilisation
decimal = int(input("Entrer un nombre decimal \n"))
binaire = dec2Bin(decimal)
print(f"{decimal} binaire: {binaire}")






