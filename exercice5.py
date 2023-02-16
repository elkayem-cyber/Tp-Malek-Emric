import itertools

# Fonction pour obtenir toutes les combinaisons de dés qui donnent un total donné
def combinaisons_des(n):
    if n < 5 or n > 30:
        return None  # retourne None si l'argument n est invalide

    combinaisons = []
    for comb in itertools.product(range(1, 7), repeat=5):
        if sum(comb) == n:
            combinaisons.append(comb)

    return combinaisons


# Fonction pour calculer les scores possibles avec un nombre de dés et un nombre de faces donnés
def calcul_scores(n, m, j):
    if n < 1 or m < 1 or j < n or j > n * m:
        return None  # retourne None si un des arguments est invalide

    combinaisons = combinaisons_des(j)
    if combinaisons is None:
        return None  # retourne None si le total j n'est pas possible

    scores = [sum(comb) for comb in combinaisons]
    scores_min = min(scores)
    scores_max = max(scores)
    combinaisons_j = [comb for comb in combinaisons if sum(comb) == j]

    return {"score_min": scores_min, "score_max": scores_max, "combinaisons": combinaisons_j}


# Exemple d'utilisation de la fonction combinaisons_des
print(combinaisons_des(20))  # affiche toutes les combinaisons de dés qui donnent 20

# Exemple d'utilisation de la fonction calcul_scores
print(calcul_scores(4, 6, 10))  # affiche les scores possibles avec 4 dés à 6 faces pour un total de 10
