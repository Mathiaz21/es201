
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
| lw | 17.44 |
| sw | 3.27 |
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
| lw | 24.08 |
| sw | 10.32 |
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

## Question 3 :

Comparons les résultats précédents avec 3 profilings supplémentaires : SSCA2-BCH, SHA-1 et le produit de polynômes.

Voici les résultats pour le profiling de SSCA2-BCH :

| Opération | Pourcentage d'utilisation |
|:----------|:-------------------------:|
| load | 24.13 |
| store | 10.34 |
| uncond branch | 1.06 |
| cond branch | 14.69 |
| int computation | 49.77 |
| lw | 24.08 |
| sw | 10.32 |
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

Voici les résultats du profiling pour SHA-1 
 (Echec de ma part de les faire marcher)
Voici les résultats du profiling pour le produit de pôlynomes :

| Opération | Pourcentage d'utilisation |
|:----------|:-------------------------:|
| load | 23.06 |
| store | 7.71 |
| uncond branch | 0.00 |
| cond branch | 7.70 |
| int computation | 46.16 |
| lw | 0.00 |
| sw | 0.02 |
| add | 0.00 |
| addi | 0.00 |
| addu | 7.71 |
| addiu | 15.39 |
| sub | 0.00 |
| subu | 7.69 |
| mult | 0.00 |
| multu | 0.00 |
| div | 0.00 |
| divu | 0.00 |

On remarque que ces 5 benchmarks ont tous une répartition des classes d'instruction similaire, avec une majorité d'opérations en nombre entier, et une grande part d'accès mémoire et de branchements conditionels. On remarquera que la multiplication de polynôme requiert également - et à la différence des autres benchmark- une grande part de calcul en nombres flottants (15%), ainsi qu'une part conséquente de soustraction de nombres entiers non-signés.

## Question 4 :

Dans un premier temps listons les différents paramètres clefs ressortant des simulations sim-outorder. Les valeurs associées aux paramètres dans les tableaux suivants proviennent du profiling pour l'algorithme de dijkstra.

Ici nous nous intéressons aux performances en terme de prédiction de branche du processeur :

| Opération | Nombre d'utilisations | Description de l'opération |
|:----------|:---------------------:|:---------------------------|
| lookups | 1122480 | Nombre total de prédictions prises par le processeur |
| updates | 1097223 | Le nombre de fois où le prédicteur a changé d'état |
| addr_hits | 1088664 | Addr_hits est le nombre de fois où l'adresse de l'instruction déterminée par le branchement est correctement prédite |
| dir_hits | 1089342 | Le nombre de fois où le prédicteur a pris la bonne décision (*taken* ou *not taken*), ce nombre inclut donc le nombre d'address hits (il est possible que le prédicteur prenne la bonne décision, mais qu'il se trompe sur l'adresse de l'instruction suivante) |
| misses | 7881 | Le nombre de mauvaises prédictions |
| jr_hits | 28074 | Le nombre de jumps pour lesquels le prédicteur a correctement prédit l'adresse du saut |
| jr_seen | 28141 | Le nombre total de jumps rencontrés par le GPU |
| jr_non_ras_hits.PP | 0 | Le nombre de fois où le prédicteur a eu raison de ne pas stocker l'adresse de retour. Typiquement, dans le cas d'un branchement inconditionnel, il ne faut pas pousser l'adresse de retour dans la RAS puisqu'il ne faut pas retourner à l'instruction suivant le jump. |
| jr_non_ras_seen.PP | 60 | Le nombre de sauts sans retour rencontrés par le CPU |
| bpred_addr_rate | 0.9922 | Le taux de bonnes prédictions d'adresse |
| bpred_dir_rate | 0.9928 | Le taux de bonnes prédictions de direction |
| bpred_jr_rate | 0.9976 | Le taux de bonnes prédictions d'adresse suite à un saut sur le nombre total de sauts |
| bpred_jr_non_ras_rate.PP | 0.0000 | Le taux du nombre de fois où le CPU a eu raison de ne pas stocker l'adresse de retour dans la RAS sur le nombre total |
| bpred_bimod.ras_rate.PP | 0.9998 | Le taux de RAS hits sur le nombre total de RAS utilisés |

Nous nous intéressons également aux performances brutes du processeur :

| Opération | Nombre d'utilisations | Description de l'opération |
|:----------|:---------------------:|:---------------------------|
| sim_IPC | 1.8691 | Nombre d'instructions exécutées par cycle d'horloge |
| sim_cycle | 3725311 | Nombre de cycles |

Du point de vue du cache L1 nous avons aussi les informations suivantes :

| Opération | Nombre d'utilisations | Description de l'opération |
|:----------|:---------------------:|:---------------------------|
| il1.accesses | 7108576 | Le nombre d'accès au cache |
| il1.hits | 7065662 | Le nombre de fois où la donnée était effectivement dans le cache |
| il1.misses | 42914 | Le nombre de fois où la donnée n'était pas dans le cache, le CPU doit donc chercher plus haut dans la hiérarchie mémoire (L2, mémoire principale...) |
| il1.replacements | 42850 | Le nombre de fois où une ligne de cache doit être remplacée par une nouvelle |
| il1.writebacks | 0 | Quand on enlève une ligne de cache de L1 et qu'elle doit être réécrite plus haut dans la hiérarchie de la mémoire |
| il1.invalidations | 0 | Quand une ligne de cache n'est plus valide, typiquement dans des cas multi-cœurs (ce qui n'est pas le cas ici), où la donnée est mise à jour dans le cache d'un autre cœur |

Voici maintenant quelques graphes montrant les différences de performances pour différentes tailles de cache L1 :

### Diagramme en barres de 3 indicateurs de performance de prédiction de branche lors de l'exécution de l'algorithme de Djsktra

<div style="text-align:center;">
  <img src="plots/Triple_plot_branche_A7_dij.png" alt="Description of the image" style="width:75%;" />
</div>

On constate que les différences de performance pour la prédiction de branche sont négligeables. À titre d'exemple, la liste des différents nombre de lookups est la suivante : [9886841, 9869054, 9878877, 9879047, 9879450]. Les variations sont négligeables, de l'ordre de 0.2%, et ne sont pas visibles sur le plot.

### Diagramme en barres de 3 indicateurs de performance du processeur lors de l'exécution de l'algorithme de Djsktra

<div style="text-align:center;">
  <img src="plots/Double_plot_perf_A7_dij.png" alt="Description of the image" style="width:75%;" />
</div>

