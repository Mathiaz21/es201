
# Compte Rendu TP4 ES201
## Jean Acker ; Alexandre Drean ; Mathias Gilbert ; Édouard Clocheret


## Question 1 :

Commençons par traiter le cas du Blowfish :
Tableau retraçant l'utilisation des différentes opérations : 

| Opération | Pourcentage d'utilisation |
|:----------|:-------------------------:|
| load | 21.32 |
| store | 7.15 |
| uncond branch | 2.75 |
| cond branch | 8.83 |
| int computation | 59.95 |

Jean je compte qur toi pour commenter ce résultat :
| Opération | Pourcentage d'utilisation |
|:----------|:-------------------------:|
| lw | 17.44 |
| sw | 3.27 |

Plus précisément du côté des opérations arithmétiques standard on trouve :
| Opération | Pourcentage d'utilisation |
|:----------|:-------------------------:|
| add | 0.00 |
| addi | 0.00 |
| addu | 15.92 |
| addiu | 11.14 |
| sub | 0.00 |
| subu | 0.00 |
| mult | 0.00 |
| multu | 0.00 |
| div | 0.00 |
| divu | 0.00 |

On remarque que les opérations les plus fréquemment appelées sont les additions d'entiers non signés. Les autres opérations ne sont, hormis la soustraction d'entiers non-signés "subu" qui est appelée un nombre de fois négligeable, même pas appelées du tout.

Maintenant voyons quels résulats l'on obtient avec le profiling avec l'algorithme de Dijkstra :
| Opération | Pourcentage d'utilisation |
|:----------|:-------------------------:|
| load | 24.13 |
| store | 10.34 |
| uncond branch | 1.06 |
| cond branch | 14.69 |
| int computation | 49.77 |

Jean je compte qur toi pour commenter ce résultat :
| Opération | Pourcentage d'utilisation |
|:----------|:-------------------------:|
| lw | 24.08 |
| sw | 10.32 |

Plus précisément du côté des opérations arithmétiques standard on trouve :
| Opération | Pourcentage d'utilisation |
|:----------|:-------------------------:|
| add | 0.00 |
| addi | 0.00 |
| addu | 19.01 |
| addiu | 5.73 |
| sub | 0.00 |
| subu | 0.13 |
| mult | 0.01 |
| multu | 0.00 |
| div | 0.00 |
| divu | 0.01 |

Bien que le résultat soit un peu plus équilibré, les opérations d'addition d'entiers non-signés restent largement majoritaires.


## Question 2 :

Dans le cas de blowfish, les instructions majoritaires sont les écritures mémoires (41%) et les calculs en nombre entier (35%). Les branchements conditionelles occupent près de 12\% des instructions et les chargements depuis la mémoire 8%. Le profiling de dijkstra est assez simialaire, avec cette fois plus de chargement depuis la mémoire que d'écriture. Pour obtenir de meilleure performances, il serait judicieux de multiplier les ALUs pour paralléliser les calculs entier, et d'avoir un bon prédicteur de branchement. Le grand nombre d'accès mémoire reste néanmoins un problème.
