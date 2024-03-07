import taskTool
import dataTask

Choix = input("Que voulez vous faire ? \nEntrer O si vous voulez charger une liste de taches ou 1 si vous voulez créer une liste de taches : ")

if Choix == "1":
    Dico = {}
    
elif Choix == "0":
    Dico = dataTask.Load()

else:
    print("Entrer une des valeurs proposées")


Choix = "0"

while Choix != "3":
    
    print()
    Choix = input("Que voulez vous faire maintenant ? \nEntrer O si vous voulez ajouter des taches, 1 si vous voulez supprimer une tache, 2 si vous voulez marquer une tache comme terminer ou 3 si vous voulez sauvegarder : ")
    print()
    
    if Choix == "0":
        Nombre = int(input("Combien de tache voulez vous ajouter ? : "))
        for indice in range(Nombre):
            print("Quel est la valeur de la tache numéro ", indice + 1, " ? : ", end = "")
            Tache = input()
            taskTool.AddTache(Dico, Tache)
        
    elif Choix == "1":
        NomTache = input("Quel est le nom de la tache que vous voulez supprimer ? : ")
        taskTool.DelTache(Dico, NomTache)
        
    elif Choix == "2":
        NomTache = input("Quel est le nom de la tache que vous voulez marquer comme terminer ? : ")
        taskTool.EndTache(Dico, NomTache)
    
    elif Choix == "3":
        Nom = input("Quel est le nom de votre fichier ? : ")
        dataTask.SaveDic(Dico, Nom)
    
    else:
        print("Entrer une des valeurs proposées")
    