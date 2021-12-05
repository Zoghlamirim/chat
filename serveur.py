import socket   #permettre de faire interagir le serveur et le client
import select

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #créer une instance de module socket
host, port ='127.0.0.1', 4000
serveur.bind((host, port))
serveur.listen(4)
client_conecté = True
socket_obj = [serveur]

print('bienvenue dans le chat!')

while client_conecté:

	liste_lu, lisle_acce_ecrit,exception = select.select(socket_obj, [], socket_obj)

	for socket_obj in liste_lu:

		if socket_obj is serveur:
			client, adresse = serveur.accept()
			print(f'lobjet client socket: {client} - adresse: {adresse}')
			socket_obj.append(client)

		else:
			donnees_recue = socket_obj.recv(128).decode('utf-8')

			if donnees_recue:
				print(donnees_recue)

			else:
				socket_obj.remove(socket_obj)
				print('un participant est deconnecté')
				print(f"{len(socket_obj)-1}participants restants")






