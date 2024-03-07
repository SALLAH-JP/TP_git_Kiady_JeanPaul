import json

def AddTache(location, tache):
    with open(location, 'r') as f:
        data = json.load(f)

    data[tache] = False


def DelTache(location, tache):
    with open(location, 'r') as f:
        data = json.load(f)

    del data[tache]
    
def EndTache(location, tache):
    with open(location, 'r') as f:
        data = json.load(f)

    data[tache] = True