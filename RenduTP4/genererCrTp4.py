import subprocess
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Ce code génère un compte rendu de TP 4 d'ES101, l'exécuter écrasera l'ancienne version et en reproduira une nouvelle version.
# Besoin d'avoir les fichiers de profiling compilés dans le même répertoire, sous les noms suivants :
# profiling, profiling_dij, profiling_dij_ssca2v2, profiling_POLY

nom_rapport = "Compte_Rendu_Tp4_ES101.md"
f = open("simulations/profiling", "r")
str_profiling_blowfish = f.read()
f.close()

f = open("simulations/profiling_dij", "r")
str_profiling_dij = f.read()
f.close()

def findBlowfishPdf(nomParametre, str_profiling):
    pattern = re.compile(r"\n{}\s+\d+\s+(\d+\.\d+)".format(re.escape(nomParametre)), re.DOTALL)
    match = re.search(pattern, str_profiling)
    if match:
        return match.group(1)
    else: 
        print("No correlation !")
        return None

def tableauDePerfs(str_profiling):
    result_str = """
| Opération | Pourcentage d'utilisation |
|:----------|:-------------------------:|
"""
    liste_operations_1 = ["load", "store", "uncond branch", "cond branch", "int computation"]
    for op in liste_operations_1:
        result_str += "| " + op + " | " + findBlowfishPdf(op, str_profiling) + " |\n"
    liste_operations_2 = [  
            ["lw       t,o(b)", "lw"],
            ["sw       t,o(b)", "sw"],
            ["add      d,s,t", "add"],
            ["addi     t,s,i", "addi"],
            ["addu     d,s,t", "addu"], 
            ["addiu    t,s,i", "addiu"], 
            ["sub      d,s,t", "sub"], 
            ["subu     d,s,t", "subu"], 
            ["mult     s,t", "mult"],
            ["multu    s,t", "multu"],
            ["div      s,t", "div"],
            ["divu     s,t", "divu"]
                        ]
    for op in liste_operations_2:
        result_str += "| " + op[1] + " | " + findBlowfishPdf(op[0], str_profiling) + " |\n"
    return result_str

# --------------------------------------------------------------------------

# ------------------- DÉBUT DU RAPPORT ET QUESTION 1 -----------------------

# --------------------------------------------------------------------------


contenu_rapport = """
# Compte Rendu TP4 ES201
## Jean Acker ; Alexandre Drean ; Mathias Gilbert ; Édouard Clocheret


## Question 1 :

Commençons par traiter le cas du Blowfish :
Tableau retraçant l'utilisation des différentes opérations : \n
"""

contenu_rapport += tableauDePerfs(str_profiling_blowfish)

contenu_rapport += """
On remarque que les opérations les plus fréquemment appelées sont les additions d'entiers non signés. Les autres opérations ne sont, hormis la soustraction d'entiers non-signés "subu" qui est appelée un nombre de fois négligeable, même pas appelées du tout.

Maintenant voyons quels résulats l'on obtient avec le profiling avec l'algorithme de Dijkstra :
"""

contenu_rapport += tableauDePerfs(str_profiling_dij)

contenu_rapport += """
Bien que le résultat soit un peu plus équilibré, les opérations d'addition d'entiers non-signés restent largement majoritaires.
"""


# --------------------------------------------------------------------------

# ------------------------------- QUESTION 2 -------------------------------

# --------------------------------------------------------------------------

contenu_rapport += """

## Question 2 :

Dans le cas de blowfish, les instructions majoritaires sont les écritures mémoires (41%) et les calculs en nombre entier (35%). Les branchements conditionelles occupent près de 12\% des instructions et les chargements depuis la mémoire 8%. Le profiling de dijkstra est assez simialaire, avec cette fois plus de chargement depuis la mémoire que d'écriture. Pour obtenir de meilleure performances, il serait judicieux de multiplier les ALUs pour paralléliser les calculs entier, et d'avoir un bon prédicteur de branchement. Le grand nombre d'accès mémoire reste néanmoins un problème.
"""

# --------------------------------------------------------------------------

# ------------------------------- QUESTION 3 -------------------------------

# --------------------------------------------------------------------------
f = open("simulations/profiling_dij_ssca2v2", "r")
str_profiling_SSCA2 = f.read()
f.close()

f = open("simulations/profiling_POLY", "r")
str_profiling_poly = f.read()
f.close()

contenu_rapport += """
## Question 3 :

Comparons les résultats précédents avec 3 profilings supplémentaires : SSCA2-BCH, SHA-1 et le produit de polynômes.

Voici les résultats pour le profiling de SSCA2-BCH :
"""

contenu_rapport += tableauDePerfs(str_profiling_SSCA2)

contenu_rapport += "\nVoici les résultats du profiling pour SHA-1 \n (Echec de ma part de les faire marcher)"

contenu_rapport += "\nVoici les résultats du profiling pour le produit de pôlynomes :\n"

contenu_rapport += tableauDePerfs(str_profiling_poly)

contenu_rapport += """
On remarque que ces 5 benchmarks ont tous une répartition des classes d'instruction similaire, avec une majorité d'opérations en nombre entier, et une grande part d'accès mémoire et de branchements conditionels. On remarquera que la multiplication de polynôme requiert également - et à la différence des autres benchmark- une grande part de calcul en nombres flottants (15%), ainsi qu'une part conséquente de soustraction de nombres entiers non-signés.
"""

# --------------------------------------------------------------------------

# ------------------------------- QUESTION 4 -------------------------------

# --------------------------------------------------------------------------

def extraire_valeur(parametre, str_profiling):
    pattern = re.compile(r"{}\s+(\d+\.?\d*)\s".format(re.escape(parametre)), re.DOTALL)
    match = re.search(pattern, str_profiling)
    if match:
        return match.group(1)
    else: 
        print("Error : no correlation !")
        return match

def tableau_de_perfs2(str_profiling, tab_parametres):

    result_str = """
| Opération | Nombre d'utilisations | Description de l'opération |
|:----------|:---------------------:|:---------------------------|
"""
    for par in tab_parametres:
        result_str += "| " + par[0] + " | " + extraire_valeur(par[0], str_profiling) + " | " + par[1] + " |\n"
    return result_str

def imprimer_plot(is_A7, liste_simulations, parametre, nom_fichier_sortie,
                  titre_plot="un plot", axe_x="x axis", axe_y="y axis"):
    if(is_A7):
        X = [1,2,4,8,16]
    else:
        X = [2,4,8,16,32]
    X_positions = range(len(X))
    Y = []
    for sim in liste_simulations:
        y = extraire_valeur(parametre, sim)
        if "." in y:
            y = float(y)
        else:
            y = int(y)
        Y.append(y)
    plt.bar(X_positions, Y)
    plt.xticks(X_positions, X)
    plt.title(titre_plot)
    plt.xlabel(axe_x)
    plt.ylabel(axe_y)
    plt.savefig("plots/"+nom_fichier_sortie)

def imprimer_triple_plot(is_A7, liste_simulations, liste_parametres, nom_fichier_sortie,
                  titres_plot=["Fig 1", "Fig 2", "Fig 3"], axes_x=["x1", "x2", "x3"],
                  axes_y=["y1", "y2", "y3"]):
    if(is_A7):
        X = [1,2,4,8,16]
    else:
        X = [2,4,8,16,32]
    X_positions = range(len(X))
    plt.figure(figsize=(3*len(liste_parametres), 3))
    for i in range(len(liste_parametres)):
        Y = []
        for sim in liste_simulations:
            y = extraire_valeur(liste_parametres[i], sim)
            if "." in y:
                y = float(y)
            else:
                y = int(y)
            Y.append(y)
        print(Y)
        plt.subplot(101 + 10*(len(liste_parametres)) + i)
        plt.bar(X_positions, Y)
        plt.xticks(X_positions, X)
        plt.title(titres_plot[i])
        plt.xlabel(axes_x[i])
        plt.ylabel(axes_y[i])
    plt.subplots_adjust(wspace=0.3) 
    plt.tight_layout()
    plt.savefig("plots/"+nom_fichier_sortie)
    

contenu_rapport += """
## Question 4 :

Dans un premier temps listons les différents paramètres clefs ressortant des simulations sim-outorder. Les valeurs associées aux paramètres dans les tableaux suivants proviennent du profiling pour l'algorithme de dijkstra.

Ici nous nous intéressons aux performances en terme de prédiction de branche du processeur :
"""


f = open("simulations/sim_dij", "r")
str_sim_outorder = f.read()
f.close()

tab_pred_branche = [
    ["lookups", "Nombre total de prédictions prises par le processeur"],
    ["updates", "Le nombre de fois où le prédicteur a changé d'état"],
    ["addr_hits", "Addr_hits est le nombre de fois où l'adresse de l'instruction déterminée par le branchement est correctement prédite"],
    ["dir_hits", "Le nombre de fois où le prédicteur a pris la bonne décision (*taken* ou *not taken*), ce nombre inclut donc le nombre d'address hits (il est possible que le prédicteur prenne la bonne décision, mais qu'il se trompe sur l'adresse de l'instruction suivante)"],
    ["misses", "Le nombre de mauvaises prédictions"],
    ["jr_hits", "Le nombre de jumps pour lesquels le prédicteur a correctement prédit l'adresse du saut"],
    ["jr_seen", "Le nombre total de jumps rencontrés par le GPU"],
    ["jr_non_ras_hits.PP", "Le nombre de fois où le prédicteur a eu raison de ne pas stocker l'adresse de retour. Typiquement, dans le cas d'un branchement inconditionnel, il ne faut pas pousser l'adresse de retour dans la RAS puisqu'il ne faut pas retourner à l'instruction suivant le jump."],
    ["jr_non_ras_seen.PP", "Le nombre de sauts sans retour rencontrés par le CPU"],
    ["bpred_addr_rate", "Le taux de bonnes prédictions d'adresse"],
    ["bpred_dir_rate", "Le taux de bonnes prédictions de direction"],
    ["bpred_jr_rate", "Le taux de bonnes prédictions d'adresse suite à un saut sur le nombre total de sauts"],
    ["bpred_jr_non_ras_rate.PP", "Le taux du nombre de fois où le CPU a eu raison de ne pas stocker l'adresse de retour dans la RAS sur le nombre total"],
    ["bpred_bimod.ras_rate.PP", "Le taux de RAS hits sur le nombre total de RAS utilisés"]
]


contenu_rapport += tableau_de_perfs2(str_sim_outorder, tab_pred_branche)

contenu_rapport += """
Nous nous intéressons également aux performances brutes du processeur :
"""
tab_performances = [
    ["sim_IPC", "Nombre d'instructions exécutées par cycle d'horloge"],
    ["sim_cycle", "Nombre de cycles"]
]

contenu_rapport += tableau_de_perfs2(str_sim_outorder, tab_performances)

contenu_rapport += """
Du point de vue du cache L1 nous avons aussi les informations suivantes :
"""
tab_L1 = [
    ["il1.accesses", "Le nombre d'accès au cache"],
    ["il1.hits", "Le nombre de fois où la donnée était effectivement dans le cache"],
    ["il1.misses", "Le nombre de fois où la donnée n'était pas dans le cache, le CPU doit donc chercher plus haut dans la hiérarchie mémoire (L2, mémoire principale...)"],
    ["il1.replacements", "Le nombre de fois où une ligne de cache doit être remplacée par une nouvelle"],
    ["il1.writebacks", "Quand on enlève une ligne de cache de L1 et qu'elle doit être réécrite plus haut dans la hiérarchie de la mémoire"],
    ["il1.invalidations", "Quand une ligne de cache n'est plus valide, typiquement dans des cas multi-cœurs (ce qui n'est pas le cas ici), où la donnée est mise à jour dans le cache d'un autre cœur"]
]

contenu_rapport += tableau_de_perfs2(str_sim_outorder, tab_L1)

liste_simulations_dij_A7 = []
for L1_size in ["1", "2", "4", "8", "16"]:
    f = open("simulations/sim_dij_A7_" + L1_size, "r")
    liste_simulations_dij_A7.append(f.read())
    f.close

contenu_rapport += """
Voici maintenant quelques graphes montrant les différences de performances pour différentes tailles de cache L1 :

### Diagramme en barres de 3 indicateurs de performance de prédiction de branche lors de l'exécution de l'algorithme de Djsktra
"""

titles = ["Nombre Lookups", "Nombre Updates", "Nombre Addr Hits"]
axesX = ["Taille cache L1 en KB"] * 3
axesY = [""] * 3
imprimer_triple_plot(True, liste_simulations_dij_A7, ["lookups", "updates", "addr_hits"], "Triple_plot_branche_A7_dij", titres_plot=titles, axes_x=axesX, axes_y=axesY)

contenu_rapport += """
<div style="text-align:center;">
  <img src="plots/Triple_plot_branche_A7_dij.png" alt="Description of the image" style="width:75%;" />
</div>

On constate que les différences de performance pour la prédiction de branche sont négligeables. À titre d'exemple, la liste des différents nombre de lookups est la suivante : [9886841, 9869054, 9878877, 9879047, 9879450]. Les variations sont négligeables, de l'ordre de 0.2%, et ne sont pas visibles sur le plot.

### Diagramme en barres de 3 indicateurs de performance du processeur lors de l'exécution de l'algorithme de Djsktra
"""

titles = ["Instructions / cycle d'horloge", "Nombre de Cycles"]
axesX = ["Taille cache L1 en KB"] * 3
axesY = [""] * 3
imprimer_triple_plot(True, liste_simulations_dij_A7, ["sim_IPC", "sim_cycle"], "Double_plot_perf_A7_dij", titres_plot=titles, axes_x=axesX, axes_y=axesY)

contenu_rapport += """
<div style="text-align:center;">
  <img src="plots/Double_plot_perf_A7_dij.png" alt="Description of the image" style="width:75%;" />
</div>
"""


liste_simulations_blowfish_A7 = []
for L1_size in ["1", "2", "4", "8", "16"]:
    f = open("simulations/sim_blow_A7_" + L1_size, "r")
    liste_simulations_blowfish_A7.append(f.read())
    f.close

contenu_rapport += """
"""

# --------------------------------------------------------------------------

# ----------------------------- QUESTION 5 ---------------------------------

# --------------------------------------------------------------------------

liste_simulations_dij_A15 = []
for L1_size in ["2", "4", "8", "16", "32"]:
    f = open("simulations/sim_dij_A15_" + L1_size, "r")
    liste_simulations_dij_A15.append(f.read())
    f.close

liste_simulations_blow_A15 = []
for L1_size in ["2", "4", "8", "16", "32"]:
    f = open("simulations/sim_blow_A15_" + L1_size, "r")
    liste_simulations_blow_A15.append(f.read())
    f.close



# --------------------------------------------------------------------------

# ------------------------- ÉCRITURE DU RAPPORT ----------------------------

# --------------------------------------------------------------------------

with open(nom_rapport, "w") as file:
    file.write(contenu_rapport)