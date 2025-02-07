import turtle
import math

# Inicializar turtle
t = turtle.Turtle()
t.speed(0)
t.color("Red")
turtle.bgcolor("Black")

# Función para calcular las coordenadas del corazón
def corazon(n):
    x = 200 * math.sin(n) ** 3  # Aumento el coeficiente para hacer el corazón más grande
    y = 150 * math.cos(n) - 50 * math.cos(2 * n) - 20 * math.cos(3 * n) - 10 * math.cos(4 * n)  # Ajuste en la fórmula
    return x, y

# Configurar la posición inicial
t.penup()
t.goto(0, 0)
t.pendown()

# Dibuja el corazón con relleno de líneas
for i in range(100):  # Dibujar múltiples líneas para rellenar el corazón
    t.penup()
    t.goto(0, 0)  # Regresar al centro para empezar una nueva línea
    t.pendown()
    
    for j in range(360):  # Aumentar el rango de iteraciones para asegurar que el corazón se complete
        n = j * math.pi / 180  # Convertir los grados a radianes
        x, y = corazon(n)
        t.goto(x + i, y + i)  # Desplazar la línea para darle un efecto de relleno con líneas

t.hideturtle()  # Esconder la tortuga después de terminar
turtle.done()  # Finaliza la ejecución de turtle
