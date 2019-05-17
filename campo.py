from tkinter import *
from tkinter import messagebox as mb
tk=Tk()
tk.title("FCB vs PSG")

canvas=Canvas(tk,width=960,height=678)
canvas.pack()
my_image=PhotoImage(file="fut.gif")
canvas.create_image(0,0,anchor=NW, image=my_image)
imagen=PhotoImage(file="ball.gif")
canvas.create_image(480,339,anchor=CENTER, image=imagen)
x,y=480,339

def moveball(event):
	global x,y

	if (event.keysym == 'Up'):
		canvas.move(2,0,-5)
		y=y-5
	elif (event.keysym == 'Down'):
		canvas.move(2,0,5)
		y=y+5
	elif (event.keysym == 'Left'):
		canvas.move(2,-5,0)
		x=x-5
	elif (event.keysym == 'Right'):
		canvas.move(2,5,0)
		x=x+5
	else:
		canvas.move(2,0,0)
	if  (x>920 and 265<y<415) :
		mb.showinfo(" ","Goooooooooooooooooool")
		
	elif (x<40 and 265<y<415) :
		mb.showinfo(" ","Goooooooooooooooooool")

canvas.bind_all('<KeyPress-Up>',moveball)
canvas.bind_all('<KeyPress-Down>',moveball)
canvas.bind_all('<KeyPress-Left>',moveball)
canvas.bind_all('<KeyPress-Right>',moveball)
tk.mainloop()