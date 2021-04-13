import sys
import os

def display_current_dir():
    current = os.getcwd().split('/')[-1]
    contenu = os.listdir()

    print(f"le dossier courant est le suivant : {current}")
    print("le dossier contient les fichiers / dossiers suivant: ")
    len_file = 0
    len_dir = 0
    for file in contenu:
        if os.path.isdir(file):
            len_dir += 1
            name = "dossier"
        else:
            len_file += 1
            name = "fichier"
        print(f"\t{file} qui est un {name}")

    print(f"le dossier courant contient {len_file} fichiers et {len_dir}  dossier")

display_current_dir()