import taskTool
import dataTask

Choix = int(input("Que voulez vous faire ? \nEntrer O si vous voulez charger une liste de taches ou 1 si vous voulez créer une liste de taches : "))

if Choix == 1:
    Dico = {}
    
elif Choix == 0:
    Dico = dataTask.Load()

else:
    print("Entrer une des valeurs proposées")

print()
Choix = int(input("Voulez vous sauvegarder ?\nEntrer O pour Oui et 1 pour Non : "))

if Choix == 0:
    Nom = input("Quel est le nom de votre fichier ? : ")
    dataTask.SaveDic(Dico, Nom)

print()
Choix = int(input("Que voulez vous faire maintenant ? \nEntrer O si vous voulez ajouter des taches, 1 si vous voulez supprimer une tache ou 2 si vous voulez marquer une tache comme terminer : "))
print()

if Choix == 0:
    Nombre = int(input("Combien de tache voulez vous créer ? : "))
    for indice in range(Nombre):
        print("Quel est la valeur de la tache numéro ", indice + 1, " ? : ", end = "")
        Tache = input()
        taskTool.AddTache(Dico, Tache)
    
elif Choix == 1:
    NomTache = input("Quel est le nom de la tache que vous voulez supprimer ? : ")
    tastTool.DelTache(Dico, NomTache)
    
elif Choix == 2:
    NomTache = input("Quel est le nom de la tache que vous voulez marquer comme terminer ? : ")
    tastTool.EndTache(Dico, NomTache)

else:
    print("Entrer une des valeurs proposées")
