import json

def AddTache(location, tache):
    with open(location, 'r') as f:
        data = json.load(f)

    f["NewTache"] = tache