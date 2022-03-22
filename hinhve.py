from  turtle import *

spi = Turtle()
spi.speed(10)
spi.pensize(1)
bgcolor("#131417")
spi.hideturtle()

def circulo(veces, angulo):
    for x in range(veces):
        spi.color("#FFAC12")
        spi.left(angulo)
        spi.circle(50)
        spi.forward(5)

circulo(20, 18)
done()