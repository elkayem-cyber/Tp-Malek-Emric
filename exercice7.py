def fusion_sets(set1, set2):
    # Fusion des deux sets sans éléments dupliqués
    set_fusion = set1.union(set2)
    # Tri des éléments des deux sets par ordre décroissant
    set1_trie = sorted(set1, reverse=True)
    set2_trie = sorted(set2, reverse=True)
    # Liste contenant la somme des valeurs uniques de set1 et set2
    valeurs_uniques = list(set1.symmetric_difference(set2))
    somme_valeurs = sum(valeurs_uniques)
    # Création de la chaîne de caractères lorem ipsum
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " * somme_valeurs
    # Construction du dictionnaire contenant toutes les informations
    dico = {"set_fusion": set_fusion,
            "set1_trie": set1_trie,
            "set2_trie": set2_trie,
            "somme_valeurs": valeurs_uniques,
            "lorem": lorem}
    return dico
