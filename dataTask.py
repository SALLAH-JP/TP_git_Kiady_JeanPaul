import json 

def SaveDic (dictionary,  file_name):

    with open(file_name, "w") as fichier:
	json.dump(dictionary , fichier )	


