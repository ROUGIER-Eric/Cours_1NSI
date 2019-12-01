# La bibliothèque pour tracer des courbes
import matplotlib.pyplot as plt
# On importe la fonction nécessaire
from fonctions_collatz import collatz_liste

N = int(input("Saisir une valeur pour N : "))
Liste = collatz_liste(N)

# On crée la liste des indices par compréhension
indices = [i for i in range(len(Liste))]

plt.plot(indices, Liste)

plt.show() # affiche la figure a l'ecran