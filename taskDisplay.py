import taskTool
import dataTask

Choix = int(input("Que voulez vous faire ? \nEntrer O si vous voulez charger une liste de taches ou 1 si vous voulez créer une liste de taches : "))

if Choix == 1:
    Dico = {}
    Nombre = int(input("Combien de tache voulez vous créer ? : "))
    for indice in range(Nombre):
        print("Quel est la valeur de la tache numéro ", indice + 1, " ? : ", end = "")
        Tache = input()
        taskTool.AddTache(Dico, Tache)
    
elif Choix == 0:
    Dico = dataTask.Load()

Choix = int(input("Voulez vous sauvegarder ?/nEntrer O pour "Oui" et 1 pour "Non""))

if Choix == 0:
    Nom = input("Quel est le nom de votre fichier ? : ")
    dataTask.SaveDic(Dico, Nom)
