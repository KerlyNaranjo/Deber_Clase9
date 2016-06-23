#Deber2: Estrella de n lados impares
import turtle
t = turtle.Pen()
t.reset()

n = int(input('Ingrese el numero (impar) de lados: '))
grado = 180 + (180/n)

for x in range(1, n+1):
	t.forward(100)
	t.left(grado)

turtle.getscreen()._root.mainloop()