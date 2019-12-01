def collatz_indice(N : int)-> int:
    """ Retourne le premier indice de la suite de Collatz du nombre N pour
        lequel le terme vaut 1
    """
    # Les instructions assert sont utilisées pour vérifier les préconditions. 
    # Une telle instruction se compose d'une condition (une expression booléenne) 
    # éventuellement suivie d'une virgule et d'une phrase en langue naturelle, 
    # sous forme d'une chaine de caractères. L'instruction assert teste si sa condition est satisfaite. 
    # Si c'est le cas, elle ne fait rien et sinon elle arrête immédiatement l'exécution du programme 
    # en affichant éventuellement la phrase qui lui est associée.
    assert type(N) == int, "la variable N doit être de type int"
    assert N > 0, "la variable doit être un entier naturel non nul"
    
    # On commence la fonction
    indice = 0
    while N != 1:
        if N%2 == 0:
            N = N//2
        else:
            N = 3*N+1
        indice = indice + 1
    return indice

def collatz_liste(N : int)-> list:
    """ 
    Retourne une liste contenant les premiers termes de la uite de Collatz 
    du nombre N tronquée au premier terme égal à 1 
    """
    assert type(N) == int, "la variable N doit être de type int"
    assert N > 0, "la variable doit être un entier naturel non nul"
    
    U = [N]
    while N != 1:
        if N%2 == 0:
            N = N//2
        else:
            N = 3*N+1
        U.append(N)
    return U

def vol_altitude(N:int)->int:
    """
    Retourne le temps de vol en altitude de la suite de Collatz.
    On utilise la fonction collatz_liste() (assert inutile)
    """
    indice = 0
    U = collatz_liste(N)
    while U[indice+1] > N:
        indice = indice + 1
    return indice

def altitude_max(N:int)->int:
    """
    Retourne l'altitude maximale de la suite de Collatz.
    On utilise la fonction collatz_liste()
    """
    maximum = N
    U = collatz_liste(N)
    for element in U:
        if element > maximum:
            maximum = element
    return maximum