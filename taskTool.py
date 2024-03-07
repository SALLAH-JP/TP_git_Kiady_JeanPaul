import json

def AddTache(Dico, Tache):
    Dico[Tache] = False



def DelTache(Dico, Tache):
    del Dico[Tache]



def EndTache(Dico, Tache):
    Dico[Tache] = True
