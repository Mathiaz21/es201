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

