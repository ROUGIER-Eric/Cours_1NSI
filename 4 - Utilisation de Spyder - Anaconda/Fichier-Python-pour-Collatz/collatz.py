from fonctions_collatz import collatz_indice, vol_altitude, altitude_max

# On définit une fonction
def valeurs_max(N : int)->tuple:
    """La fonction retourne un tuple contenant
       les trois listes vol_max, vol_altitude_max, max_altitude_max
       """
    vol_max = [0,0]
    vol_altitude_max = [0,0]
    max_altitude_max = [0,0]
    for i in range(3, N+1):
        if collatz_indice(i) > vol_max[0]:
            vol_max = [collatz_indice(i), i]
        if vol_altitude(i) > vol_altitude_max[0]:
            vol_altitude_max = [vol_altitude(i), i]
        if altitude_max(i) > max_altitude_max[0]:
            max_altitude_max = [altitude_max(i), i]
    return vol_max, vol_altitude_max, max_altitude_max

# Ne s'exécute pas lorsque le fichier est importé comme module
# dans le fichier des tests unitaires
if __name__ == '__main__':
    entier = int(input("Saisir un entier : "))
    (vol_max, vol_altitude_max, max_altitude_max) = valeurs_max(entier)

    print(f"Le temps de vol maximal est {vol_max[0]} pour N = {vol_max[1]}")
    print(f"Le temps de en altitude maximal est {vol_altitude_max[0]} pour N = {vol_altitude_max[1]}")
    print(f"L'altitude maximale est {max_altitude_max[0]} pour N = {max_altitude_max[1]}")