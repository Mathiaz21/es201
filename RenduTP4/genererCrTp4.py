import subprocess
import re

# Ce code génère un compte rendu de TP 4 d'ES101, l'exécuter écrasera l'ancienne version et en reproduira une nouvelle version.
# Besoin d'avoir le fichier profiling dans le même répertoire

nom_rapport = "Compte_Rendu_Tp4_ES101.md"
f = open("profiling", "r")
str_profiling_blowfish = f.read()
f.close()

f = open("profiling_dij", "r")
str_profiling_dij = f.read()
f.close()

def findBlowfishPdf(nomParametre, str_profiling):
    # pattern = re.compile(r"\n{}[ \s]+\d+[ \s]+(\d+\.\d+)$".format(re.escape(nomParametre)))
    pattern = re.compile(r"\n{}\s+\d+\s+(\d+\.\d+)".format(re.escape(nomParametre)), re.DOTALL)
    match = re.search(pattern, str_profiling)
    if match:
        return match.group(1)
    else: 
        print("No correlation !")
        return match

# --------------------------------------------------------------------------

# ------------------- DÉBUT DU RAPPORT ET QUESTION 1 -----------------------

# --------------------------------------------------------------------------


contenu_rapport = """
# Compte Rendu TP4 ES201
## Jean Acker ; Alexandre Drean ; Mathias Gilbert ; Édouard Clocheret


## Question 1 :

Commençons par traiter le cas du Blowfish :
Tableau retraçant l'utilisation des différentes opérations : \n
| Opération | Pourcentage d'utilisation |
|:----------|:-------------------------:|
"""
liste_operations_1 = ["load", "store", "uncond branch", "cond branch", "int computation"]
for op in liste_operations_1:
    contenu_rapport += "| " + op + " | " + findBlowfishPdf(op, str_profiling_blowfish) + " |\n"

contenu_rapport += """
Jean je compte qur toi pour commenter ce résultat :
| Opération | Pourcentage d'utilisation |
|:----------|:-------------------------:|
"""
liste_operations_2 = [["lw       t,o(b)", "lw"], ["sw       t,o(b)", "sw"]]
for op in liste_operations_2:
    contenu_rapport += "| " + op[1] + " | " + findBlowfishPdf(op[0], str_profiling_blowfish) + " |\n"

contenu_rapport += """
Plus précisément du côté des opérations arithmétiques standard on trouve :
| Opération | Pourcentage d'utilisation |
|:----------|:-------------------------:|
"""
liste_operations_3 = [
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
for op in liste_operations_3:
    contenu_rapport += "| " + op[1] + " | " + findBlowfishPdf(op[0], str_profiling_blowfish) + " |\n"

contenu_rapport += """
On remarque que les opérations les plus fréquemment appelées sont les additions d'entiers non signés. Les autres opérations ne sont, hormis la soustraction d'entiers non-signés "subu" qui est appelée un nombre de fois négligeable, même pas appelées du tout.

Maintenant voyons quels résulats l'on obtient avec le profiling avec l'algorithme de Dijkstra :
| Opération | Pourcentage d'utilisation |
|:----------|:-------------------------:|
"""
liste_operations_1 = ["load", "store", "uncond branch", "cond branch", "int computation"]
for op in liste_operations_1:
    contenu_rapport += "| " + op + " | " + findBlowfishPdf(op, str_profiling_dij) + " |\n"

contenu_rapport += """
Jean je compte qur toi pour commenter ce résultat :
| Opération | Pourcentage d'utilisation |
|:----------|:-------------------------:|
"""
liste_operations_2 = [["lw       t,o(b)", "lw"], ["sw       t,o(b)", "sw"]]
for op in liste_operations_2:
    contenu_rapport += "| " + op[1] + " | " + findBlowfishPdf(op[0], str_profiling_dij) + " |\n"

contenu_rapport += """
Plus précisément du côté des opérations arithmétiques standard on trouve :
| Opération | Pourcentage d'utilisation |
|:----------|:-------------------------:|
"""
liste_operations_3 = [
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
for op in liste_operations_3:
    contenu_rapport += "| " + op[1] + " | " + findBlowfishPdf(op[0], str_profiling_dij) + " |\n"

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


with open(nom_rapport, "w") as file:
    file.write(contenu_rapport)