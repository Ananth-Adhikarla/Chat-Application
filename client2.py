"""
CHAT CLIENT 2
"""

import socket
import sys
import time
from tkinter import *
from threading import Thread
from tkinter import messagebox


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = 'ananth-VirtualBox'
port = 8080
thread_status = True
sock.connect((host,port))
print("Connected to the chat server")


# server sends message back to client
def recieve():

	global thread_status
	
	while(True):
		try:
			mess= sock.recv(1024)
			mess = mess.decode()
			print("Server message : ",mess)
			# insert message into the message box that is recieved from the server
			message.insert(INSERT , '%s \n' %(mess))
			
		except OSError:
			break

		except RuntimeError:
			sys.exit(0)


# send message to the server
def send(event = None):

	global thread_status 
	
	mess = input_field.get("1.0","end-1c")
	input_field.delete("1.0","end-1c")
	if( 'quit' in mess ):
		thread_status = on_closing()
		return thread_status
	
	mess = mess.encode()
	sock.send(mess)

# close messagebox
def on_closing():
	global thread_status

	if( messagebox.askokcancel("Quit","Do you want to Quit?")):
		window.destroy()
		thread_status = False
		return thread_status

# creates a window 
window = Tk()
# adds the title to the window
window.title("Python Chat v.1.0")
# sets the size of window / can also use window.minsize()
window.geometry("600x580")
# adds color to the window
window.configure(bg="#2471a3")

# main message box where all the inputs recieved are printed 
message = Text(window , width = 80 , height = 20 , bg="#17202a", foreground="#edfc03" , font=(None, 15))
message.pack()
# .pack() ends the message widget and cannot be modified further and places it in the window

# this is where you enter your text
input_field = Text(window , width = 70, height = 1)
input_field.pack(side = LEFT , pady = 15 , padx = 15)

# creates a button widget that is clickable
button1 = Button(window , text = "Submit",width = 3, height = 2 , fg="#a1dbcd", bg="#383a39", command = send)
button1.pack(side = LEFT , padx = 0)

# widget.bind( event , handler )
# event is the <Return> which is the Enter key / button on keyboard 	
input_field.bind("<Return>",send)

# creates a pop up window on pressing 'x' to close program
window.protocol("WM_DELETE_WINDOW",on_closing)

while(thread_status):

	if(thread_status == False):
		recieve_thread._stop()
		break
		sys.exit(0)
		
	# create a recieve thread and keep appending to the box	
	recieve_thread = Thread(target=recieve)
	
	# Daemons are only useful when the main program is running, and it's okay to kill them off once the other non-daemon threads have exited. 
	# Without daemon threads, we have to keep track of them, and tell them to exit, before our program can completely quit. 
	# By setting them as daemon threads, we can let them run and forget about them, and when our program quits, any daemon threads are killed automatically.
	recieve_thread.daemon = True

	recieve_thread.start()
	
	# keep the window running forever until you close it in someway
	window.mainloop()
	
	
	
