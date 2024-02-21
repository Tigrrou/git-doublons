import os
import hashlib
from colorama import Fore, Style

def find_duplicate_files(directory):
    files_by_hash = {}

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)

            with open(file_path, "rb") as file:
                file_hash = hashlib.md5(file.read()).hexdigest()

            if file_hash in files_by_hash:
                files_by_hash[file_hash].append(file_path)
            else:
                files_by_hash[file_hash] = [file_path]

    duplicate_files = {hash: files for hash, files in files_by_hash.items() if len(files) > 1}

    return duplicate_files

def print_header():
    print("\n" + Fore.GREEN + r"""
                                                           ,--,
                  ,----..                               ,---.'|        ,----..             ,--.
    ,---,        /   /   \                      ,---,.  |   | :       /   /   \          ,--.'|   .--.--.
  .'  .' `\     /   .     :           ,--,    ,'  .'  \ :   : |      /   .     :     ,--,:  : |  /  /    '.
,---.'     \   .   /   ;.  \        ,'_ /|  ,---.' .' | |   ' :     .   /   ;.  \ ,`--.'`|  ' : |  :  /`. /
|   |  .`\  | .   ;   /  ` ;   .--. |  | :  |   |  |: | ;   ; '    .   ;   /  ` ; |   :  :  | | ;  |  |--`
:   : |  '  | ;   |  ; \ ; | ,'_ /| :  . |  :   :  :  / '   | |__  ;   |  ; \ ; | :   |   \ | : |  :  ;_
|   ' '  ;  : |   :  | ; | ' |  ' | |  . .  :   |    ;  |   | :.'| |   :  | ; | ' |   : '  '; |  \  \    `.
'   | ;  .  | .   |  ' ' ' : |  | ' |  | |  |   :     \ '   :    ; .   |  ' ' ' : '   ' ;.    ;   `----.   \
|   | :  |  ' '   ;  \; /  | :  | | :  ' ;  |   |   . | |   |  ./  '   ;  \; /  | |   | | \   |   __ \  \  |
'   : | /  ;   \   \  ',  /  |  ; ' |  | '  '   :  '; | ;   : ;     \   \  ',  /  '   : |  ; .'  /  /`--'  /
|   | '` ,/     ;   :    /   :  | : ;  ; |  |   |  | ;  |   ,/       ;   :    /   |   | '`--'   '--'.     /
;   :  .'        \   \ .'    '  :  `--'   \ |   :   /   '---'         \   \ .'    '   : |         `--'---'
|   ,.'           `---`      :  ,      .-./ |   | ,'                   `---`      ;   |.'
'---'                         `--`----'     `----'                                '---'


    """ + Style.RESET_ALL)

def main():
    print_header()
    directory = input("Entrez le chemin du dossier à scanner : ")
    duplicates = find_duplicate_files(directory)

    if not duplicates:
        print("\nAucun fichier en double trouvé dans le répertoire spécifié.")
        return

    print("\nFichiers en double trouvés :\n")
    for file_hash, files in duplicates.items():
        print(f"Empreinte : {file_hash}")
        for file_path in files:
            print(f"- {file_path}")

    choice = input("\nVoulez-vous supprimer tous les fichiers en double ? (O/N) : ").strip().lower()
    if choice == "o":
        for files in duplicates.values():
            for file_path in files[1:]:
                os.remove(file_path)
        print("\nTous les fichiers en double ont été supprimés.")
    else:
        print("\nOpération annulée.")

if __name__ == "__main__":
    main()
