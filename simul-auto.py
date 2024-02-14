import subprocess
import re
import matplotlib.pyplot as plt
import numpy as np

def find_number_by_name(text, name):
    # Pattern pour extraire le nombre associé au nom spécifié
    pattern = r'{}.*?(\d+(?:\.\d+)?)'.format(re.escape(name))

    # Recherche du pattern dans le texte
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return float(match.group(1))  # Récupération du nombre en tant que flottant
    else:
        return None  # Retourne None si le nom n'est pas trouvé dans le texte



def simple_example():
    # Exécution de la commande à l'aide de subprocess et récupération de sa sortie
    result = subprocess.run(['python', 'test_sortie.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Exemple d'utilisation
    if result.returncode == 0:  # Vérification si la commande s'est exécutée avec succès
        text_output = result.stdout.decode('utf-8')  # Conversion de la sortie de la commande en texte
        name = "param1"
        number = find_number_by_name(text_output, name)
        if number is not None:
            print("Le nombre associé à '{}' est : {}".format(name, number))
        else:
            print("Le nom '{}' n'a pas été trouvé.".format(name))
    else:
        print("Erreur lors de l'exécution de la commande.")


def simulation_1():
    #variable que l'on veut plot
    name = "sim_num_insn"
    #abscisse1
    x1=[12, 15, 17]
    #abscisse2
    x2=[18, 15, 17]
    #ordonnée
    y=np.zeros(len(x1))

    valeur1 = x1[0]
    for valeur2 in x2:
        command = ["sim-cache", "-redir:sim", "fichier.txt", "-cache:il1", "il1:256:32:1:l", "-cache:dl1",
            "dl1:256:32:1:l", "-cache:dl2", "ul2:1024:64:4:l", "SSCA2.ss"]


        # Exécution de la commande avec subprocess.run()
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # print(result)
        
        if result.returncode == 0:  
            text_output = result.stdout.decode('utf-8')  # Conversion de la sortie de la commande en texte
            number = find_number_by_name(text_output, name)
            print(text_output)
            if number is not None:
                print("Le nombre associé à '{}' est : {}".format(name, number))
                y.append(number)
            else:
                print("Le nom '{}' n'a pas été trouvé.".format(name))
        else:
            print("Erreur lors de l'exécution de la commande.")

    # plt.plot(y,x2)




simulation_1()
