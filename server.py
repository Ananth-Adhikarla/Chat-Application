"""
CHAT SERVER
"""

import socket
import sys
import time
import threading



class server(object):

	def __init__(self,host,port):

		self.host = host
		self.port = port
		self.sock = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
		
		# Set the value of the given socket option
		# When retrieving a socket option, or setting it, you specify the option name as well as the level. When level = SOL_SOCKET, the item will be searched for in the socket itself.
		# the SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state, without waiting for its natural timeout to expire.
		# Say we want to set the socket option to reuse the address to 1 (on/true), we pass in the "level" SOL_SOCKET and the value we want it set to.		
		# This will set the SO_REUSEADDR in my socket to 1. 		
		# the SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state, without waiting for its natural timeout to expire.
		self.sock.setsockopt( socket.SOL_SOCKET , socket.SO_REUSEADDR, 1 )
		
		# Bind the socket to address. The socket must not already be bound. 
		self.sock.bind((self.host , self.port))

		# list of usernames added to list later
		self.username = {}


	def listen(self):
		# Enable a server to accept connections. If backlog is specified, it must be at least 0 (if it is lower, it is set to 0); 
		# it specifies the number of unaccepted connections that the system will allow before refusing new connections. If not specified, a default reasonable value is chosen.
		self.sock.listen(2)
		
		while( True ):

			# Accept a connection. The socket must be bound to an address and listening for connections. 
			# The return value is a pair (conn, address) where conn is a new socket object usable to send and receive data on the connection, 
			# and address is the address bound to the socket on the other end of the connection.

			client , address = self.sock.accept()
			
			data = 'what is your desired username?'

			data = data.encode()

			# send to client 'What is your desired username'
			client.send(data)

			# recieve answer from client
			name = client.recv(1024)

			# decode answer as its encoded when sent from client
			name = name.decode()

			# append username to its specific address
			user = { address : name }	
			
			self.username.update( user )

			# connection expires if idle for 60 seconds 
			client.settimeout(60)

			# creates a thread for every new connection and target is the action to be performed by this thread 
			# client connect is a function defined below and client and address are variables recieved at top from socket.accept()

			threading.Thread(target = self.client_connect , args = (client,address)).start()


	def client_connect(self,client,address):
		
		# preset the buffer size 
		buff_size = 1024
		print(" What does client print ? " , client )
		print("\n")
		print("What does address print ? ", address)
		
		# prints in server
		print(sorted(self.username.values())[-1], " has just connected!")

		# prints the same message in client terminal
		joined = sorted(self.username.values())[-1] + " has just connected!"		
		joined = joined.encode()
		client.send(joined)
		
		while(True):
			try:
				
				data = client.recv(buff_size)
				# default decode is UTF-8 even without specifying it can be blank or other decode formats
				data = data.decode('UTF-8')
				if(data):
				
					print(self.username[address],">>", data)
					
					
				else:
					raise error("Client Disconected")
			except:
				# close the client from server and print the message that is has disconnected and delete the client from dictonary
				client.close()
				print(self.username[address], " has just disconnected!")
				del self.username[address]
				return False



if __name__ == '__main__' :

	# Return a string containing the hostname of the machine where the Python interpreter is currently executing.
	host = socket.gethostname()

	print("Host Name is :	",host)

	while(True):
		# enter port number here and client should connect to the server on same port

		port_num = input("Port Num ? ")
		try:
			port_num = int(port_num)
			break

		except ValueError:
			pass

	# call the server class here with listen as first function called
	
	server('',port_num).listen()

