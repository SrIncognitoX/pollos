import turtle

# Configuración inicial
screen = turtle.Screen()
screen.bgcolor("lightgreen")
screen.title("Lirios del Valle")

# Función para dibujar un lirio del valle
def dibujar_lirio(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Tallo del lirio
    turtle.color("green")
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)

    # Flor del lirio
    turtle.color("white")
    turtle.circle(10)
    turtle.end_fill()

    # Detalles de la flor
    turtle.color("green")
    turtle.penup()
    turtle.goto(x, y + 10)
    turtle.pendown()
    turtle.circle(12, steps=4)

# Dibujar varios lirios del valle
for i in range(-200, 200, 100):
    dibujar_lirio(i, 0)

# Esconder la tortuga y finalizar
turtle.hideturtle()
turtle.done()
