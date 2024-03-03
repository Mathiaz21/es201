import matplotlib.pyplot as plt
import numpy as np


A15_size = [1024 * 2**i for i in range(1,6)] #erreur avec la première valeur 1024 bytes
A15_L1_surf = [0.00964784+0.000466222, 0.00440128+0.00071465, 0.010506+0.00127867, 0.0117623+0.0023357, 0.0301238+0.00444115]





A7_size = [1024 * 2**i for i in range(6)]
A7_L1_surf = [.00379037 + .000466222, 0.00964784+.00077853, .00440128+.00127867, .010506+.0023357,.0117623+.00444115,.0301238+.008308]

plt.plot(A15_size, A15_L1_surf, label = "cortex A15")
plt.plot(A7_size, A7_L1_surf, label="cortex A7")

plt.xlabel("taille de cache L1 (Bytes)")
plt.ylabel("Surface de cache L1 (mm²)")

plt.legend()
plt.show()


PrevTotalAreaA15 = 2
PrevL1AreaA15 = 2*0.03316055
NewTotalAreaA15 = [PrevTotalAreaA15 - PrevL1AreaA15 + NewL1AreaA15 for NewL1AreaA15 in A15_L1_surf]

PrevTotalAreaA7 = 0.45
PrevL1AreaA7 = 2*0.03698476
NewTotalAreaA7 = [PrevTotalAreaA7 - PrevL1AreaA7 + NewL1AreaA7 for NewL1AreaA7 in A7_L1_surf]



plt.plot(A15_size, NewTotalAreaA15, label = "cortex A15")
plt.plot(A7_size, NewTotalAreaA7, label="cortex A7")

plt.xlabel("taille de cache L1 (Bytes)")
plt.ylabel("Surface total (mm²)")

plt.legend()
plt.show()