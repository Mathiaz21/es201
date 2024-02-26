# Rapport TP5

## Question 1

Dans le cas de la multiplication de la matrice A par la matrice B sur n threads, chaque lignes de la matrice A congruant
à p modulo n sont placées dans le cache du processus p. Comme la matrice A n'est pas modifié mais simplement lu, il n'y a pas de 
problème de cohérence (elle possède l'état Shared). La matrice B doit être accessible par tous les processus, comme il n'y a pas de mémoire cache 
L2 commune à tous les coeurs (d'après la figure 20), la matrice B doit être disponible dans le cache associée
à chaque coeur. Encore une fois, cette matrice est seulement lu, elle n'est pas modifié, elle à donc l'état Shared (pas de problème 
de cohérence de cache). Enfin, la matrice résultat C doit être commune à tous les coeurs, mais il n'y à pas de problème de concurrence de cache, 
puisque les lignes de la matrice C congruent à p modulo n ne sont modifié que par le processus p. 

## Question 2

Les problèmes...

## Question 3

parser.add_option("--l1d_size", type="string", default="64kB")
parser.add_option("--l1i_size", type="string", default="32kB")
parser.add_option("--l2_size", type="string", default="2MB")

parser.add_option("--l1d_assoc", type="int", default=2)
parser.add_option("--l1i_assoc", type="int", default=2)
parser.add_option("--l2_assoc", type="int", default=8)

parser.add_option("--cacheline_size", type="int", default=64)

|                        | **L1-données** | **L1-instructions** | **L2**  |
|------------------------|----------------|---------------------|---------|
| **Taille**             | 64kB           | 32kB                | 2MB     |
| **associativité**      | 2              | 2                   | 8       |
| **taille de la ligne** | 64             | 64                  | 64      |