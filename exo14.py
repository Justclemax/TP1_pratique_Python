import random

def generer_phrase(tableau_mots):
    random.shuffle(tableau_mots)  # Mélange aléatoire des mots dans le tableau
    phrase = ' '.join(tableau_mots)  # Concaténation des mots avec un espace entre chaque mot
    return phrase

tableau_mots = ['Bonjour', 'tout','le','monde']
phrase_aleatoire = generer_phrase(tableau_mots)
print(phrase_aleatoire)
