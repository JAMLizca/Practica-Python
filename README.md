## 🐢 Turtle en Python: ¡Dibuja con código!

El módulo `turtle` en Python permite crear gráficos y dibujos de manera sencilla utilizando comandos basados en movimientos. Es ideal para aprender sobre programación visual y geometría de una forma divertida.

### 🎨 ¿Qué puedes hacer con `turtle`?
- Dibujar formas y figuras con comandos simples.
- Crear animaciones básicas.
- Simular movimientos y trayectorias.

Ejemplo de uso:

```python
import turtle

pantalla = turtle.Screen()
pantalla.bgcolor("white")

t = turtle.Turtle()
t.pensize(3)
t.pencolor("blue")
t.speed(3)

for _ in range(4):
    t.forward(100)
    t.right(90)

turtle.done()
```
