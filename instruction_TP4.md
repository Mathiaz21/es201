# TP 4

## Question 1

Dans la 1ère question on demande de faire profiler les classes d'instruction sut deux benchmark (blowfish et dijkstra). Enfait ce qu'on veut c'est le pourcentage d'instruction sur des flottants, sur des int, sur le chargement et le stockage de données dans la RAM, le nombres de branchment conditionnel...

### Pour Blowfish
cp /home/g/gbusnot/ES201/tools/blowfish_modified.tar.gz <your directory>
tar xzf <your_directory>/blowfish_modified.tar.gz

cd <your_directory>/blowfish
make

**pour lancer le profiling**

sim-profile -redir:sim ./profiling -iclass true -iprof true bf.ss e input_small.asc output.enc 123456789abcdeffedcba0987654321

les résultats sont chargés dans le fichier profiling, les lignes qui nous intéressent sont les suivantes:

sim_inst_class_prof.start_dist
load                 535756  21.32 
store                179590   7.15 
uncond branch         69208   2.75 
cond branch          221901   8.83 
int computation     1506430  59.95 
fp computation            0   0.00 
trap                     23   0.00 
sim_inst_class_prof.end_dist

(compris entre les lignes 61 et 69)

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

- cp /home/g/gbusnot/ES201/tools/graph/ dijkstra <your directory>
- make clean
- make all

**Pour lancer le profiling**

sim-profile -redir:sim ./profiling_dij -iclass true -iprof true dijkstra_small.ss input.dat et bf.ss input_small.asc

Pour l'analyse des résultats c'est le même principe que pour blowfish




