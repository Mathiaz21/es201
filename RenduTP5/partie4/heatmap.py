
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Données
nb_cycles = np.array([
    [218987, 158857, 128999],
    [154600, 123628, 107800],
    [151488, 121696, 106382]
])

Speedup = 218987 / nb_cycles

# Créer une grille de données régulièrement espacée
x = np.array([2, 4, 8])
y = np.array([1, 2, 4])
X, Y = np.meshgrid(x, y)

# Créer une figure et un plot
fig, ax = plt.subplots()

# Créer la heatmap
sns.heatmap(Speedup, xticklabels=x, yticklabels=y, annot=True, fmt='f', cmap='viridis')

# Ajouter des étiquettes aux axes
ax.set_xlabel('Largeur du processeur superscalaire')
ax.set_ylabel('Nombre de threads')
ax.set_title('SpeedUp')

# Afficher le plot
plt.show()
