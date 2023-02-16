noms = ["Malek le tricheur", "Nagaakira", "Mitsuakira", "Tsunaakira", "Tsunanaga"]

def extraire_element(liste, index):
    if index < 0 or index >= len(liste):
        return "Erreur : index hors limites"
    else:
        return liste[index]

print(extraire_element(noms, 2))  # renvoie "Mitsuakira"
print(extraire_element(noms, 5))  # renvoie "Erreur : index hors limites"



