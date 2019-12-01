from fonctions_collatz import collatz_indice, vol_altitude, altitude_max
from collatz import valeurs_max

def test_valeurs_max():
    assert valeurs_max(200) == ([124,171], [95,27], [9232,27])

def test_collatz_indice():
    assert collatz_indice(15) == 17
    assert collatz_indice(127) == 46