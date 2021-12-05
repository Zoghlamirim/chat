import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #créer une instance de module socket
host, port ='127.0.0.1', 9000
client_socket.connect((host, port))

nom = input('quelle est votre nom? ')

if __name__ =='__main__':
	while True:
		message = input(f'{nom}> ')
		client_socket.send(f'{nom}> {message}'.encode('utf_8'))
