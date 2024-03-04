import matplotlib.pyplot as plt
import numpy as np


A15_size = [1024 * 2**i for i in range(1,6)] #erreur avec la première valeur 1024 bytes

A7_size = [1024 * 2**i for i in range(6)]




A15_L1_surf = [0.00964784+0.000466222, 0.00440128+0.00071465, 0.010506+0.00127867, 0.0117623+0.0023357, 0.0301238+0.00444115]


A7_L1_surf = [.00379037 + .000466222, 0.00964784+.00077853, .00440128+.00127867, .010506+.0023357,.0117623+.00444115,.0301238+.008308]




PrevTotalAreaA15 = 2
PrevL1AreaA15 = 2*0.03316055
NewTotalAreaA15 = [PrevTotalAreaA15 - PrevL1AreaA15 + NewL1AreaA15 for NewL1AreaA15 in A15_L1_surf]

PrevTotalAreaA7 = 0.45
PrevL1AreaA7 = 2*0.03698476
NewTotalAreaA7 = [PrevTotalAreaA7 - PrevL1AreaA7 + NewL1AreaA7 for NewL1AreaA7 in A7_L1_surf]



###### IPC Perf obtained with sim-outorder #######


A7_L1_dij_IPC = [0.3764, 0.3940, 0.4854, 0.4961, 0.5053, 0.5204]
A15_L1_dij_IPC = [0.7840, 1.2024, 1.2985, 1.3643, 1.4338, 1.5579]


A7_L1_blo_IPC = [0.3637, 0.3913, 0.4177, 0.4778, 0.4869, 0.5024]
A15_L1_blo_IPC = [0.7730, 0.9383, 1.3206, 1.3675, 1.4098, 2.1889]



A7_L1_dij_IPC_perf_surfaciques = [A7_L1_dij_IPC[i]/NewTotalAreaA7[i] for i in range(6)]
A7_L1_blo_IPC_perf_surfaciques = [A7_L1_blo_IPC[i]/NewTotalAreaA7[i] for i in range(6)]

A15_L1_dij_IPC_perf_surfaciques = [A15_L1_dij_IPC[i+1]/NewTotalAreaA15[i] for i in range(5)]
A15_L1_blo_IPC_perf_surfaciques = [A15_L1_blo_IPC[i+1]/NewTotalAreaA15[i] for i in range(5)]



plt.plot(A15_size, A15_L1_dij_IPC_perf_surfaciques, label = "A15 - dijkstra")
plt.plot(A15_size, A15_L1_blo_IPC_perf_surfaciques, label = "A15 - blowfish")

plt.plot(A7_size, A7_L1_dij_IPC_perf_surfaciques, label="A7 - dijkstra")
plt.plot(A7_size, A7_L1_blo_IPC_perf_surfaciques, label="A7 - blowfish")

plt.xlabel("taille de cache L1 (Bytes)")
plt.ylabel("IPC surfacique")

plt.legend()
plt.show()