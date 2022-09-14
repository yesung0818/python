import turtle
t = turtle.Turtle()
def a(n, length):
    for i in range(n):
        t.forward(length)
        t.left(360//n)

for i in range(15):
    t.left(20)
    a(6, 100)
