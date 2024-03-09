import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Données
nb_cycles = np.array([
    [218987, 158857, 128999],
    [154600, 123628, 107800],
    [151488, 121696, 106382]
])

Speedup = 218987 / nb_cycles

nb_instr = np.array([[274203, 294011, 334665],
                     [274203, 299102, 345963],
                     [274203, 306251, 373498]])

instrPcycle = nb_instr / nb_cycles

# Créer une grille de données
x = np.array([2,4,8])
y = np.array([1,2,4])
X, Y = np.meshgrid(x, y)

# Créer une figure et un plot 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Créer la surface
ax.plot_surface(X, Y, Speedup, cmap='viridis')

# Ajouter des étiquettes aux axes
# ax.set_xlabel('Largeur du processeur superscalaire')
# ax.set_ylabel('Nombre de threads')
# ax.set_zlabel('SpeedUp')

ax.set_xlabel('Largeur du processeur superscalaire')
ax.set_ylabel('Nombre de threads')
ax.set_zlabel("SpeedUp")

# Afficher le plot
plt.show()
