import sys
sys.path.append('manageTask/taskTool.py')

import taskTool

Choix = int(input("Que voulez vous faire ? \nEntrer O si vous voulez charger une liste de taches ou 1 si vous voulez créer une liste de taches : "))

Dico = {}

taskTool.AddTache(Dico, "nom")

print(Dico)