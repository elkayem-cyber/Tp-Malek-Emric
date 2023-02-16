# Création de la variable
phrase = "Malek le tricheur n’est pas un vrai samouraï"

# Transformation en liste de mots
mots = phrase.split()

# Affichage du nombre de mots
print("Nombre de mots :", len(mots))

# Fusion des mots en une chaîne de caractères
nouvelle_phrase = " ".join(mots)
print("Nouvelle phrase :", nouvelle_phrase)

# Vérification de la présence de "tricheur" dans la variable
if "tricheur" in phrase:
    print("Le mot 'tricheur' est présent dans la phrase")
else:
    print("Le mot 'tricheur' n'est pas présent dans la phrase")
