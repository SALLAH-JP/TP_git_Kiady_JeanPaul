import json 
import os
def SaveDic (dictionary,  file_name):

    with open(file_name, "w") as fichier:
        json.dump(dictionary , fichier )	


def Load ():
    filename = input("Quel est le nom de la liste que vous voulez generer: ")
    with open(filename, 'r') as json_files:
        data = json.load(json_file)
    return data



def delete_database(filename):
	
    if os.path.exits(filename):
        os.remove(filename)			
    	
