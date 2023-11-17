import socket

# Créer un objet socket
serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lier le socket à une adresse et un port locaux
adresse = ('192.0.0.1',  49152)# exemple de port privé
serveur_socket.bind(adresse)

# Mettre le socket en mode écoute
serveur_socket.listen(1)
print(f"Le serveur écoute sur {adresse}")

# Attendre la connexion d'un client
client_socket, client_address = serveur_socket.accept()
print(f"Connexion de {client_address}")

# Recevoir des données du client
data = client_socket.recv(1024)
print(f"Données reçues : {data.decode('utf-8')}")

a = False
x = input("Entrez Q puis valider pour quitter : ")
if x == 'Q':
    a = True

while a == True:
    # Fermer les sockets
    client_socket.close()
    serveur_socket.close()