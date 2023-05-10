import requests
import os 

# URL de téléchargement de MPV pour Windows 64-bit
mpv_url = 'https://sourceforge.net/projects/mpv-player-windows/files/'

# Nom du fichier téléchargé
mpv_filename = 'mpv.7z'

# Répertoire d'installation de MPV
install_dir = 'C:\\Program Files\\mpv'

# Téléchargement du fichier MPV
response = requests.get(mpv_url)
with open(mpv_filename, 'wb') as f:
    f.write(response.content)
    
# Extraction du fichier MPV
os.system(f'7z x {mpv_filename} -o{install_dir}')

# Suppression du fichier MPV téléchargé
os.remove(mpv_filename)

print('MPV a été installé avec succès.')

