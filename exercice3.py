# Création du dictionnaire
dico = {"Nagaakira": 25, "Mitsuakira": 33, "Tsunaakira": 39}

# Fonction pour vérifier la présence d'une clé dans le dictionnaire
def verifier_cle(dico, cle):
    if cle in dico:
        return True
    else:
        return False

# Fonction pour ajouter une entrée dans le dictionnaire
def ajouter_entree(dico, cle, valeur):
    dico[cle] = valeur

# Test de la fonction pour vérifier la présence d'une clé
print(verifier_cle(dico, "Nagaakira"))  # renvoie True
print(verifier_cle(dico, "Tsunanaga"))  # renvoie False

# Test de la fonction pour ajouter une entrée
ajouter_entree(dico, "Tsunanaga", 42)
print(dico)  # affiche {'Nagaakira': 25, 'Mitsuakira': 33, 'Tsunaakira': 39, 'Tsunanaga': 42}
