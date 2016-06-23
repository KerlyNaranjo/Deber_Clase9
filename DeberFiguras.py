from tkinter import *
tk = Tk()

canvas = Canvas(tk, widt = 400, height = 400)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
canvas.create_rectangle(10, 150, 50, 200, fill="black")
canvas.create_oval(10,340,50,300, fill="black")

def moverFiguras(event):
	if event.keysym == 'Up':
		canvas.move(1, 0, -3)
		canvas.move(2,0,2)
		canvas.move(3,1,4)
	elif event.keysym == 'Down':
		canvas.move(1, 0, 3)
		canvas.move(2,0,2)
		canvas.move(3,1,-4)
	elif event.keysym == 'Left':
		canvas.move(1, -3, 0)
		canvas.move(2,-2,0)
		canvas.move(3,-4,1)
	else:
		canvas.move(1, 3, 0)
		canvas.move(2,2,0)
		canvas.move(3,4,1)

canvas.bind_all('<KeyPress-Up>', moverFiguras)
canvas.bind_all('<KeyPress-Down>', moverFiguras)
canvas.bind_all('<KeyPress-Left>', moverFiguras)
canvas.bind_all('<KeyPress-Right>', moverFiguras)
tk.mainloop()