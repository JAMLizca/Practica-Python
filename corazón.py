import turtle
import math

# Inicializar turtle
t = turtle.Turtle()
t.speed(0)
t.color("Red")
turtle.bgcolor("Black")

# Función para calcular las coordenadas del corazón (ajustada para mayor tamaño)
def corazon(n):
    x = 200 * math.sin(n) ** 3  # Aumento el coeficiente para hacer el corazón más grande
    y = 150 * math.cos(n) - 50 * math.cos(2 * n) - 20 * math.cos(3 * n) - 10 * math.cos(4 * n)  # Ajuste en la fórmula
    return x, y

# Configurar la posición inicial
t.penup()
t.goto(0, 0)
t.pendown()

# Dibuja el corazón con mayor tamaño y completitud
t.begin_fill()  # Comienza el relleno para un efecto visual más completo
for i in range(360):  # Aumentar el rango de iteraciones para asegurar que el corazón se complete
    n = i * math.pi / 180  # Convertir los grados a radianes para un recorrido completo
    x, y = corazon(n)
    t.goto(x, y)

t.end_fill()  # Finaliza el relleno

t.hideturtle()  # Esconder la tortuga después de terminar
turtle.done()  # Finaliza la ejecución de turtle
