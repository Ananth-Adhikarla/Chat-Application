"""
CHAT SERVER 2
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

		self.sock.setsockopt( socket.SOL_SOCKET , socket.SO_REUSEADDR, 1 )
		
		self.sock.bind((self.host , self.port))
		self.username = {}

		# added clientlist and mess = message list 
		self.clientlist = []
		self.mess = []

	def listen(self):

		
		while( True ):
			
			self.sock.listen(2)
	
			client , address = self.sock.accept()

			data = 'what is your desired username?'
			data = data.encode()
			client.send(data)
			name = client.recv(1024)
			name = name.decode()
			user = { address : name }
			self.clientlist.append(client)
			self.username.update( user )
			client.settimeout(60)
			threading.Thread(target = self.client_connect , args = (client,address)).start()


	def client_connect(self,client,address):

		buff_size = 1024

		print(sorted(self.username.values())[-1], " has just connected!")
		
		# display to all users connected to server that a new person has joined  - self.clientjoin is a function 
		threading.Thread(target = self.clientjoin).start()
		

		while(True):
			try:
				data = client.recv(buff_size)
				data = data.decode('UTF-8')
				if(data):
					response = data
									
					print(self.username[address],">>", data.strip("\n"))
					
					msg = self.username[address]+ " >> " + data.strip("\n")
					msg = msg.encode()
					
					# append the encoded message to a list 
					self.mess.append(msg)

					# call the self.sendmessage thread
					threading.Thread(target = self.sendmessage).start()
					
				else:
					raise Exception("Client Disconected")
					break
			except:
				client.close()
				print(self.username[address], " has just disconnected!")
				msg = (self.username[address]+" has just disconnected!").encode()
				del self.username[address]
				self.clientlist.remove(client)		

				# display to all clients someone has disconnected
				if(self.clientlist == None):
					return
				else:
					for i in self.clientlist:
						i.send(msg)
				
				return False


	def sendmessage(self):

		if(self.clientlist == None):
			return
		else:
			for i in self.clientlist:
				i.send(self.mess[-1])

	def clientjoin(self):

		if(self.clientlist == None):
			return
		else:
			for i in self.clientlist:		
				joined = sorted(self.username.values())[-1] + " has just connected!"
				joined = joined.encode()
				i.send(joined)

	def clientend(self,msg):
	
		if(self.clientlist == None):
			return
		else:
			for i in self.clientlist:
				i.send(msg)
			



if __name__ == '__main__' :


	host = socket.gethostname()
	print("Host Name is :	",host)
	while(True):
		port_num = input("Port Num ? ")
		try:
			port_num = int(port_num)
			break
		except ValueError:
			pass


	server('',port_num).listen()

