import shutil
import datetime
import os

# Chemin d'accès au dossier à sauvegarder
source_folder = "C:\\Users\\user\\Documents"

# Chemin d'accès au dossier de destination pour la sauvegarde
backup_folder = "D:\\backup"

# Nom du dossier de sauvegarde (utilisez la date et l'heure actuelles pour le nom du dossier)
now = datetime.datetime.now()
backup_name = "Backup_" + now.strftime("%Y-%m-%d_%H-%M-%S")

# Chemin d'accès complet au dossier de sauvegarde
backup_folder_path = os.path.join(backup_folder, backup_name)

# Création du dossier de sauvegarde
os.makedirs(backup_folder_path)

# Copie des fichiers dans le dossier de sauvegarde
for root, dirs, files in os.walk(source_folder):
    for file in files:
        source_file_path = os.path.join(root, file)
        destination_file_path = os.path.join(backup_folder_path, file)
        shutil.copy2(source_file_path, destination_file_path)

print("Sauvegarde terminée")
