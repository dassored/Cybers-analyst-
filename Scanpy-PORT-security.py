
import socket

target_host = input("Entrez le nom d'hôte ou l'adresse IP à scanner: ")
target_ports = [22, 25,50,53,69, 80,137,139, 443, 3306, 3389, 1433, 1434,8080]

for port in target_ports:
    # Créer un objet socket
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # Définir un temps d'attente pour la connexion
    client.settimeout(0.5)

    # Tentative de connexion au port spécifié
    try:
        client.connect((target_host,port))
        print("warning !Le port {} est ouvert".format(port))
        client.close()

    except:
        print("Le port {} est fermé et securiser".format(port))
