import json

def AddTache(location, tache):
    with open(location, 'r') as f:
        data = json.load(f)

    f[tache] = ""


def DelTache(location, tache):
    with open(location, 'r') as f:
        data = json.load(f)

    del f[tache]