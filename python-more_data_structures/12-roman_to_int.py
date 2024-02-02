#!/usr/bin/python3

# Définir un dictionnaire qui associe chaque symbole romain à sa valeur num
valeurs = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_int(roman_string):
    # Initialiser le résultat à 0
    resultat = 0
    # Parcourir la chaîne romaine de gauche à droite
    for i in range(len(roman_string)):
        # Récupérer la valeur du symbole courant
        valeur = valeurs[roman_string[i]]
        # Si symbole courant +petit que symbole suivant =le soustraire
        if i < len(roman_string) - 1 and valeur < valeurs[roman_string[i + 1]]:
            resultat -= valeur
        # Sinon, il faut l'ajouter
        else:
            resultat += valeur
    # Retourner le résultat
    return resultat
