import json 

def SaveDic (dictionary,  file_name):

    with open(file_name, "w") as fichier:
	json.dump(dictionary , fichier )	


def Load ( file_name):
    
    with open("filename, 'r') as json_files:
	data = json.load(json_file)
    return data

import os

def delete_database(filename):
	
    if os.path.exits(filename):
        os.remove(filename)			
    	
