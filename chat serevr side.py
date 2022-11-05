

import socket
import time
import sys
 
new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
 
port = 8080
 
new_socket.bind((host_name, port))
print("Binding successful!")
print("This is your IP: ", s_ip)
 
name = input('Enter name: ')
 
new_socket.listen(1) 
 
 
conn, add = new_socket.accept()
 
print("Received connection from ", add[0])
print('Connection Established. Connected From: ',add[0])
 
client = (conn.recv(1024)).decode()
print(client + ' has connected.')
 
conn.send(name.encode())
while True:
    message = input('Me : ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)



























# import socket
# import select
# import sys
# from thread import *

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# if len(sys.argv) != 3:
# 	print ("Correct usage: script, IP address, port number")
# 	exit()

# IP_address = str(sys.argv[1])

# Port = int(sys.argv[2])

# server.bind((IP_address, Port))


# server.listen(100)

# list_of_clients = []

# def clientthread(conn, addr):

# 	conn.send("Welcome to this chatroom!")

# 	while True:
# 			try:
# 				message = conn.recv(2048)
# 				if message:
# 					print ("<" + addr[0] + "> " + message)

# 					message_to_send = "<" + addr[0] + "> " + message
# 					broadcast(message_to_send, conn)

# 				else:
# 					remove(conn)

# 			except:
# 				continue


# def broadcast(message, connection):
# 	for clients in list_of_clients:
# 		if clients!=connection:
# 			try:
# 				clients.send(message)
# 			except:
# 				clients.close()

# 				remove(clients)

# """The following function simply removes the object
# from the list that was created at the beginning of
# the program"""
# def remove(connection):
# 	if connection in list_of_clients:
# 		list_of_clients.remove(connection)

# while True:

# 	conn, addr = server.accept()

# 	list_of_clients.append(conn)

# 	print (addr[0] + " connected")

# 	start_new_thread(clientthread,(conn,addr))	

# conn.close()
# server.close()
