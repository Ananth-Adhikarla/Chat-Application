from tkinter import *


window = Tk()
window.title("Python Chat v.1.0")

window.geometry("600x400")

message = Text(window , width = 80 , height = 20 )
message.pack()

input_field = Text(window , width = 70, height = 3 )
input_field.pack(side = LEFT , pady = 15 , padx = 15)

button1 = Button(window , text = "Submit",width = 3, height = 2 )
button1.pack(side = LEFT , padx = 0)


def entry(event):

	text = input_field.get("1.0","end-1c")
	print(text)
	
	message.insert(INSERT , '%s \n' %(text))

	input_field.delete("1.0","end-1c")

	return "break"


input_field.bind("<Return>",entry)
button1.bind("<Return>",entry)



window.mainloop()

