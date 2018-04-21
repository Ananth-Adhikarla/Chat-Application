"""
WEEKEND MINI PROJECT Q2 : 

You have been pretty disappointed at the current quality of chat room applications and vow to create your own, start up a new Internet company, obtain venture capital funding, integrate advertisement into your chat program, quintuple revenues in a six-month period, go public, and retire. However, none of this will happen if you do not have a pretty cool chat application. There are three classes you will need: a Message class containing a message string and any additional information such as broadcast or single recipient, and a User class that contains all the information for a person entering your chat rooms. To really wow the VCs to get your start-up capital, you add a class Room that represents a more sophisticated chat system where users can create separate "rooms" within the chat area and invite others to join. Extra credit: Develop graphical user interface (GUI) applications for the users.

"""


# Sockets are low level networking interface

"""
CHAT CLIENT
"""

import socket
import sys
import time
from tkinter import *

# full form- socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
# Create a new socket using the given address family, socket type and protocol number. The address family should be AF_INET (the default), AF_INET6, AF_UNIX, AF_CAN or AF_RDS. 
# The socket type should be SOCK_STREAM (the default), SOCK_DGRAM, SOCK_RAW or perhaps one of the other SOCK_ constants. The protocol number is usually zero.

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# enter the hostname manually as user input
#host = input("Please enter the hostname of the sever")

# hostname predefined - can change depending on where the server is hosted
host = 'ananth-VirtualBox'

# Port numbers range from 0 to 65535, but only port numbers 0 to 1023 are reserved for privileged services and designated as well-known ports.
# 8080 is alternative port number for HTTP
# portnumber predefined can be dynamic auto configure by fetching the ip address (advance stuff ) or assigned by developer 
port = 8080

# Connect to a remote socket at address.
# so basically we are connecting to the server host on the specific port number

sock.connect((host,port))

print("Connected to the chat server")

# Receive data from the socket. The return value is a bytes object representing the data received. The maximum amount of data to be received at once is specified by bufsize. 
# See the Unix manual page recv(2) for the meaning of the optional argument flags; it defaults to zero.
# 1024 is the buffer size or number of bytes you can recieve at a time. For fastest recv or send its best to keep the buffer size at 20 also reduces load on servers on processing too much data

mess = sock.recv(1024)

# the decode() method translates them to code points and returns the sequence as a unicode instance. default decode format is 'UTF-8'
mess = mess.decode()

print("Server message : ",mess)


while(True):
	
	message = input(str(">>"))
	# The result of encoding a unicode string is a str object.
	message = message.encode()
	# sends the message to the server or client you are connected to in the start of the program
	sock.send(message)

	print("Message has been sent ")

	if( 'quit' in str(message) ):
		# closes the socket connection and will not be able to recieve or send any messages or perform any actions
		sock.close()	
		break


