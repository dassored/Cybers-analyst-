 import psutil

# Fonction pour tuer un processus spécifique
def kill_process(process_name):
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            proc.kill()
            print(f"{process_name} a été terminé.")

# Fonction pour démarrer un nouveau processus
def start_process(process_path):
    try:
        new_proc = psutil.Popen(process_path)
        print(f"{process_path} a été démarré avec succès.")
    except FileNotFoundError:
        print(f"Impossible de trouver le fichier {process_path}.")

# Afficher la liste des processus en cours d'exécution
def list_processes():
    for proc in psutil.process_iter():
        print(f"{proc.pid} - {proc.name()}")

# Exemple d'utilisation : tuer un processus spécifique
process_name = "chrome.exe"
kill_process(process_name)

# Exemple d'utilisation : démarrer un nouveau processus
process_path = "C:\\Windows\\System32\\notepad.exe"
start_process(process_path)

# Exemple d'utilisation : afficher la liste des processus en cours d'exécution
list_processes()
