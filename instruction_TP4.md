# TP 4

## Question 1

Dans la 1ère question on demande de faire profiler les classes d'instruction sut deux benchmark (blowfish et dijkstra). Enfait ce qu'on veut c'est le pourcentage d'instruction sur des flottants, sur des int, sur le chargement et le stockage de données dans la RAM, le nombres de branchment conditionnel...

### Pour Blowfish

```
cp /home/g/gbusnot/ES201/tools/blowfish_modified.tar.gz <your directory>
tar xzf <your_directory>/blowfish_modified.tar.gz
cd <your_directory>/blowfish
make
```

**pour lancer le profiling**

```
sim-profile -redir:sim ./profiling -iclass true -iprof true bf.ss e input_small.asc output.enc 123456789abcdeffedcba0987654321
```
les résultats sont chargés dans le fichier profiling, les lignes qui nous intéressent sont les suivantes:

>sim_inst_class_prof.start_dist
>load                 535756  21.32 
>store                179590   7.15 
>uncond branch         69208   2.75 
>cond branch          221901   8.83 
>int computation     1506430  59.95 
>fp computation            0   0.00 
>trap                     23   0.00 
>sim_inst_class_prof.end_dist

(compris entre les lignes 61 et 69)

et aussi les lignes 102 (lw), sw (110), et les lignes 136 à 145 qui correspondent aux additions, soustraction, multiplication et division. à chaque fois on regarde la dernière colonne qui 
correspond à la proportion de ce type d'instruction. Parmi les lignes 136 à 145, on retrouve :
 - add, addi, addu, addiu qui sont juste des additions, la différence entre ces 4 opérations, c'est le types des arguments, par exemple addu prend des entiers unsigned mais on s'en fou

 enfait il faut additionner la proportion des additions (lignes 136 à 139), la proporiton des soustraction (140 et 141)...

 C'est important parceque on peut spécifier le nombre de multiplieurs/diviseurs entiers et flottant du processeur qu'on construit. Historuquement, les ALUs ne pouvaient faire que des  additions et soustractions, et il peut y avoir des unité spécialisé dans la division et la multipication. 

**détaille des classes d'instruction**

- load : le nombre de chargement depuis la mémoire
- store : le nombre de chargement dans la mémoire
- uncond branch : le nombre de jump dans les instructions
- cond branch : le nombre de branchement conditionel
- int computation : le nombre de calcul en nombre entier
- fp computation : le nombre de calcul en nombre flottant
- trap : un trap c'est un interruption, typiquement quand il y a une erreur, une division par zéro, un *interrupt handler* s'occupent de ce genre d'événement

### Pour dijkstra

**Copier et compiler le benchmark dans votre répertoire local**
```
cp /home/g/gbusnot/ES201/tools/graph/dijkstra <your directory>
make clean
make all
```

**Pour lancer le profiling**

```
sim-profile -redir:sim ./profiling_dij -iclass true -iprof true dijkstra_small.ss input.dat et bf.ss input_small.asc
```
Pour l'analyse des résultats c'est le même principe que pour blowfish




## Question 2

Dans le cas de blowfish, les instructions majoritaires sont les écritures mémoires (41%) et les calculs en nombre entier (35%). Les branchements conditionelles occupent près de 12% des instructions et les chargements depuis la mémoire 8%. Le profiling de dijkstra est assez simialaire, avec cette fois plus de chargement depuis la mémoire que d'écriture. Pour obtenir de meilleure performances, il serait judicieux de multiplier les ALUs pour paralléliser les calculs entier, et d'avoir un bon prédicteur de branchement. Le grand nombre d'accès mémoire reste néanmoins un problème. 

## Question 3

La question 3 demande de comparer dijkstra, BlowFish, SSCA2-BCS, SHA-1 et le produit de polynômes

**Pour SSCA2**

**Copier et compiler le benchmark dans votre répertoire local**

`cp /home/g/gbusnot/ES201/tools/graph/SSCA2v2-C <your directory>`

**Pour lancer le profiling**

`sim-profile -redir:sim ./profiling_SSCA -iclass true -iprof true SSCA2.ss`

**Pour SHA-1**

**Copier et compiler le benchmark dans votre répertoire local**

```
cp /home/g/gbusnot/ES201/tools/sha_modified.tar.gz <your_directory>
tar xzf <your_directory>/sha_modified.tar.gz <your directory>
```

**Pour lancer le profiling**
```
sim-profile -redir:sim ./profiling_SSCA -iclass true -iprof true SSCA2.ss input_small.asc
```

**Pour le produit de polynômes**

**Copier et compiler le benchmark dans votre répertoire local**
`cp -r /home/g/gbusnot/ES201/TPs/TP2 ./polynome`

**Pour lancer le profiling**
`sim-profile -redir:sim ./profiling_POLY -iclass true -iprof true poly_mult.ss`

On remarque que ces 5 benchmarks ont tous une répartition des classes d'instruction similaire, avec une majorité d'opération en nombre entier, et une grande part d'accès mémoire et de branchements conditionels. On remarquera que la multiplication de polynôme requiert également - et à la différence des autres benchmark- une grande part de calcul en nombre flottant (15%).


## Question 4

### utilisation de sim-outorder : 

```
sim-outorder -redir:sim ./sim_dij -fetch:ifqsize 8 -decode:width 4 -issue:inorder false -issue:width 8 -commit:width 4 -ruu:size 16 -lsq:size 16 -res:imult 1 -res:ialu 5 -res:fpalu 1 -res:fpmult 1 -bpred:2lev 1 1024 8 0 -bpred:btb 256 2 -bpred:comb 1024 -fetch:mplat 15 -cache:dl1 dl1:32:64:2:l -cache:il1 il1:32:64:2:l -cache:dl2 ul2:512:64:16:l  dijkstra_small.ss input.dat et bf.ss input_small.asc
```

*Remarque* : les paramètres pour les les prédicteurs de branchements sont ceux par défauts à l'exception du premier paramètres pour le btb qui est indiqué dans le tableau

### Détail sur les paramètres du cache : 
- Il y a deux types de caches, le Dcache (pour data cache) et le Icache (pour instruction cache), l'Icache permet de sotcker les prochaines instructions dans un cache dédié
- les arguments du cache sont la taille du cache, la taille des lignes de cache et l'associativité
- la taille du cache est la taille totale du cache en KB
- les données de la mémoire sont stocker dans des lignes de cache, une grande ligne de cache peut améliroer la localité des données mais une trop grande ligne de cache risque de laisser 
une partie du cache inexploité 
- Il existe différent type de cache:
  - Le *direct-mapped cache*, pour lequel il y a une unique ligne de cache pour chaque block mémoire
  - Le *set-associative cache*, pour lequel il est associé à chaque block mémoire un unique set (déterminé par une fonction de hash tel que modulo). Chaque set contient plusieurs ligne de cache qui sont autant d'emplacement possible pour le block mémoire. C'est ici qu'entre en jeu la notion d'associativité, une associativité *n* signifie qu'il y à *n* ligne de cache par set
  - Le *Fully associative cache* Chaque block mémoire peut être associé à n'importe quelle ligne de cache. C'est l'option la plus flexible mais elle nécessite plus d'hardware.

### Les lignes importantes 

#### Concernant la prédiction de branche
>- lookups (ligne 171) : nombre total de prediction prisent par le processeur
>- updates (ligne 172) : le nombre de fois où le prédicteur à changer d'état
>- addr_hits et dir_hits (ligne 173 et 174) : addr_hits et le nombre de fois où l'adresse de l'instruction déterminer par le branchement est correctement prédite
>le dirrection hits est le nombre de fois où le prédicteur à pris la bonne décision (*taken* ou *not taken*), ce nombre inclu donc le nombre d'address hit (il est possible que le 
>prédicteur prenne la bonne décision, mais qu'il se trompe sur l'adresse de l'instruction suivante)
>- misses (ligne 175) : le nombre de mauvaise prédiction
>- jr_hits (ligne 176) : le nombre de jump pour lequel le prédicteur à correctement prédit l'adresse du saut
>- jr_seen (ligne 177) : le nombre de jump total rencontré par le GPU
>- **RAS** : Return Adress Stack pour bien comprendre, prenons un exemple, une fonction A appelle une fonction B, lorsque la fonction A appelle la fonction B, il faut enregeistrer 
l'adresse de l'instruction immédiate après l'appel de la fonction B, (pour savoir ou reprendre une fois que la fonction B aura fini de s'exécuter). cette adress est ajoutée dans une stack,
elle est ensuite pop de la stack pour récupérer l'adresse de l'instruction suivante. La RAS est donc très importante pour le prédicteur, car on peut par exemple continuer l'éxecution du code de la fonction A de manière spéculative pendant l'exécution de la fonction B. 
>- jr_non_ras_hits.PP (ligne 178) : le nombre de fois où le prédicteur à eu raison de ne pas stocker l'adresse de retour, typiquement, dans le cas d'un branchement inconditionel, il ne faut pas push l'adresse de retour dansla RAS puisqu'il ne faut pas retourner à l'instruction suivant le jump.
>- jr_non_ras_seen.PP (ligne 179) : le nombre de saut sans retour rencontrer par le CPU
>- bpred_addr_rate (ligne 180) : le ratio de bonne prédiction d'adresse
>- bpred_dir_rate (ligne 181) : le ration de bonne prédiction de direction
>- bpred_jr_rate (ligne 182) : le ratio de bonne préidction de l'adresse suite à un saut sur le nombre total de saut
>- bpred_jr_non_ras_rate.PP (ligne 183) : le ratio du nombre de fois où le CPU à eu raison de ne pas sotcker l'adress de retour dans le RAS sur le nombre total
>- bpred_bimod.ras_rate.PP (ligne 188) : le ratio de RAS hits sur le nombre total de RAS utilisé

**Les lignes qui nous intéressent sont les lignes : 171, 172, 180, 181, 182, 183 et 188**

#### Concernant les performances 

>- sim_IPC (ligne 147) : le nombre d'instruction exécuté par cycle d'horloge
>- sim_cycle (ligne 146) : le nombre de cycles

**Les lignes qui nous intéressent sont les lignes : 147 et 146**

#### Concernant le cache L1

>- il1.accesses (ligne 195) : le nombre d'accès au cache 
>- il1.hits (ligne 190) : le nombre de fois où la data était effectivement dans le cache 
>- il1.misses (ligne 191) : le nombre de fois où la data n'était pas dans le cache, le CPU doit donc chercher plus haut dans la hiérachie mémoire (L2, mémoire principale...)
>- il1.remplacements (ligne 192) : le nombre de fois où une ligne de cache doit être remplacer par une nouvelle
>- il1.writebacks (ligne 193) : quand on enlève une ligne de cache de L1 et qu'elle doit être réécrit plus haut dans la hiérarchie de la mémoire
>- il1.invalidation (ligne 194) : quand une ligne de cache n'est plus valide, typiquement dans des cas mutli-coeurs (ce qui n'est pas le cas ici), où la donnée est mise à jour dans le 
cache d'un autre coeur

**Les lignes qui nous intéressent sont les lignes : 195 à 198, 205 à 208, 215 à 218**

#### Pour dijkstra
J'ai fait un fichier bash pour exécuter le fichier `generate_output_dijkstra.sh`, il faut lui donner des privilèges d'exécution et le placer dans le dossier dijkstra

`chmod +x generate_output_dijkstra.sh`
`./generate_output_dijkstra 1 2 4 8 16 32`

Cela créer les fichiers sim_dij_1 à sim_dij_32.
 
#### Pour Blowfish
J'ai fait un fichier bash pour exécuter le fichier `generate_output_blowfish.sh`, il faut lui donner des privilèges d'exécution et le placer dans le dossier blowfish

`chmod +x generate_output_blowfish.sh`
`./generate_output_blowfish 1 2 4 8 16 32`

Cela créer les fichiers sim_blow_1 à sim_blow_32.