#Deber1: RELOJ
import time
from tkinter import *

#Creamos la ventana
tk = Tk()
canvas = Canvas(tk, width = 300, height = 200)
canvas.pack()

def reloj():
	lblT = Label(canvas, text="Reloj").place(x=120, y=75)
	t = time.localtime()
	hora=t[3]
	minutos =t[4]
	segundos = t[5]
	lblHour = Label(canvas, text = str(hora)).place(x = 100, y = 95)
	lblC = Label(canvas, text = ":").place(x = 120, y = 95)
	lblMin = Label(canvas, text = str(minutos)).place(x = 130, y = 95)
	lclC2 = Label(canvas, text = ":").place(x = 150, y = 95)
	lblSec = Label(canvas, text = str(segundos)).place(x = 160, y = 95)

s = 0
while s == 0:
	reloj()
	canvas.update()

canvas.mainloop()



