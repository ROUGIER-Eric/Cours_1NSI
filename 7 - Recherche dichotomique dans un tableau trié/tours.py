def recherche_dichotomique_tours(L : list, x : int or float) -> int:
    """renvoie une position de x dans le tableau L, supposé trié,
    et None si x ne s'y trouve pas"""
    g = 0
    d = len(L) - 1
    n = 0
    while g <= d:
        n = n + 1
        k = (g+d)//2
        if L[k] <= x:
            g = k + 1
        else:
            d = k - 1
    return n

n = 10**9
L = [0 for i in range(n)]
k = recherche_dichotomique_tours(L, 1)
print(f"Pour un tableau de taille {n}, il faut {k} tours de boucle")