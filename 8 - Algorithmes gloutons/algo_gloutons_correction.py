###############################################################################
###
###                   Rendu de monnaie
###
###############################################################################

euros = [1, 2, 5, 10, 20, 50, 100, 200]

def rendu_monnaie(somme : int) -> list:
    """retourne une liste de tuples (v, n) où v est la valeur
    des pièces ou billets à rendre et n le nombre"""
    i = len(euros) - 1
    a_rendre = []
    # Pas de monnaie à rendre pour l'instant
    n = 0
    monnaie = None
    while somme > 0:
        if somme >= euros[i]:
            n = n + 1 # On ajoute la valeur euros[i]
            monnaie = (euros[i], n)  # On  met à jour la monnaie à rendre
            somme = somme - euros[i] # La somme à rendre diminue
        else:
            n = 0  # On ne peut plus rendre cette valeur
            i = i - 1 # On passe à la valeur inférieure
            if monnaie != None:
                a_rendre.append(monnaie)  # On ajoute monnaie aux valeurs à rendre
                monnaie = None
    a_rendre.append(monnaie)  # Il n'y a plus rien à rendre, mais il faut ajouter la dernière monnaie à rendre
    return a_rendre

# Quelques assert pour vérifier
assert rendu_monnaie(9) == [(5, 1), (2, 2)]
assert rendu_monnaie(0) == [None]
assert rendu_monnaie(20) == [(20, 1)]
assert rendu_monnaie(145) == [(100, 1), (20, 2), (5, 1)]
assert rendu_monnaie(347) == [(200, 1), (100, 1), (20, 2), (5, 1), (2, 1)]

villes = ("Nancy", "Metz", "Paris", "Reims", "Troyes")
dist = ((0, 55, 303, 188, 183),
        (55, 0, 306, 176, 203),
        (303, 306, 0, 142, 153),
        (188, 176, 142, 0, 123),
        (183, 203, 153, 123, 0))

###############################################################################
###
###                   Voyageur de commerce
###
###############################################################################


def plus_proche(ville : int, dist : tuple, visitees : list) -> int:
    """Retourne le numéro de la ville non encore listée la plus
    proche, en supposant qu’il en existe au moins une."""
    pp = None
    for i in range(len(visitees)):
        if not visitees[i]:
            if (pp == None or dist[ville][i] < dist[ville][pp]):
                pp = i
    return pp

# La ville la plus proche de Nancy est Metz
assert plus_proche(0, dist, [True, False, False, False, False]) == 1
# La ville la plus proche de Paris est Reims
assert plus_proche(2, dist, [False, False, True, False, False]) == 3

def voyageur(villes : tuple, dist : tuple, depart : int) -> list:
    """Retourne l'ordre des villes à visité et
    en fin de tableau la distance de ce parcours"""
    n = len(villes)
    visitees = [False] * n
    courante = depart
    distance = 0
    trajet = [villes[depart]]
    for _ in range(n-1):
        visitees[courante] = True
        suivante = plus_proche(courante, dist, visitees)
        distance = distance + dist[courante][suivante]
        courante = suivante
        trajet.append(villes[courante])
    distance = distance + dist[courante][depart]
    trajet.append(distance)
    return trajet

print(voyageur(villes, dist, 0))

###############################################################################
###
###                   Sac à dos
###
###############################################################################


