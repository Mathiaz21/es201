import matplotlib.pyplot as plt
import numpy as np


nb_th = np.array([1,2,4])
largeur = np.array([2,4,8])
temp = np.array([1,1,1])
nb_instruction = np.array([1.25,1.85, 2.60, 1.77,2.4, 3.21, 1.81, 2.52, 3.51])

def cartesian_product(*arrays):
    la = len(arrays)
    dtype = np.result_type(*arrays)
    arr = np.empty([len(a) for a in arrays] + [la], dtype=dtype)
    for i, a in enumerate(np.ix_(*arrays)):
        arr[...,i] = a
    return arr.reshape(-1, la)

def taille(arr1, arr2):
    arr3 = []
    for elem1 in arr1:
        for elem2 in arr2:
            arr3.append(elem1*elem2)
    return arr3

#t = taille(nb_th, largeur)
t = taille(nb_th, temp)
couple = cartesian_product(nb_th, largeur)
couple_str = [str(couple[i]) for i in range(9)]
eff = [nb_instruction[i]/t[i] for i in range(9)]

print(couple_str)

plt.title("Efficacité surfacique en fonction de l'architecture")
plt.xlabel("couple (nb_threads;largeur)")
plt.ylabel("efficacité surfacique")
plt.bar(couple_str, eff)
plt.savefig("./efficacite_surfacique2.png")
plt.show()
