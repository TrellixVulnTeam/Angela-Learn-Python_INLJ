import turtle
t = turtle.Pen()
t.speed(0)
for x in range(100):
    t.forward(4 * x)
    t.left(91)

t.clear()
t.home()
for x in range(100):
    t.forward(4 * x)
    t.left(121)