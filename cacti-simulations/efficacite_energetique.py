import matplotlib.pyplot as plt
import numpy as np


A15_size = [1024 * 2**i for i in range(1,6)] #erreur avec la première valeur 1024 bytes

A7_size = [1024 * 2**i for i in range(6)]



###### IPC Perf obtained with sim-outorder #######


A7_L1_dij_IPC = [0.3764, 0.3940, 0.4854, 0.4961, 0.5053, 0.5204]
A15_L1_dij_IPC = [0.7840, 1.2024, 1.2985, 1.3643, 1.4338, 1.5579]


A7_L1_blo_IPC = [0.3637, 0.3913, 0.4177, 0.4778, 0.4869, 0.5024]
A15_L1_blo_IPC = [0.7730, 0.9383, 1.3206, 1.3675, 1.4098, 2.1889]


#On a généré les output cacti avec les caches L1 variant de 2^0 à 2^5 pour les config A15 et A7, on récupère les conso avec le script python recupPowerData.py qui parcours les 11 outputs (cacti bug lorsqu'on fait tourner avec une taille de cache L1 à 2^0 pour la config A15)

A15_L1_conso = [0.721, 0.479, 1.087, 1.662, 3.914]
A7_L1_conso = [0.249, 0.781, 0.584, 1.281, 2.182, 4.789]


A7_L1_dij_IPC_energetique = [A7_L1_dij_IPC[i]/A7_L1_conso[i] for i in range(6)]
A7_L1_blo_IPC_energetique = [A7_L1_blo_IPC[i]/A7_L1_conso[i] for i in range(6)]

A15_L1_dij_IPC_energetique = [A15_L1_dij_IPC[i+1]/A15_L1_conso[i] for i in range(5)]
A15_L1_blo_IPC_energetique = [A15_L1_blo_IPC[i+1]/A15_L1_conso[i] for i in range(5)]



plt.plot(A15_size, A15_L1_dij_IPC_energetique, label = "A15 - dijkstra")
plt.plot(A15_size, A15_L1_blo_IPC_energetique, label = "A15 - blowfish")

plt.plot(A7_size, A7_L1_dij_IPC_energetique, label="A7 - dijkstra")
plt.plot(A7_size, A7_L1_blo_IPC_energetique, label="A7 - blowfish")

plt.xlabel("taille de cache L1 (Bytes)")
plt.ylabel("efficacité energetique")

plt.legend()
plt.show()