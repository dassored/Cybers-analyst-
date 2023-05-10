import os
from Crypto.Cipher import AES

# Générer une clé de chiffrement AES de 128 bits
key = os.urandom(16)

# Créer un objet de chiffrement AES avec la clé générée
cipher = AES.new(key, AES.MODE_EAX)

# Afficher la clé générée
print("La clé de chiffrement AES générée est : ", key.hex())
