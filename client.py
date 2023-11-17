import socket

# Créer un objet socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Se connecter au serveur
serveur_address = ('192.0.0.1', 49152) # exemple de port privé
client_socket.connect(serveur_address)
print(f"Connecté à {serveur_address}")

# Envoyer des données au serveur
message = "Bonjour, serveur!"
client_socket.send(message.encode('utf-8'))

# Fermer le socket client
client_socket.close()