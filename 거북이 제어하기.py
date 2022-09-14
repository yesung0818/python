import turtle
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.shapesize(3,3)
while True:
        c=input("명령을 입력하시오: ")
        if c=="l":
            t.left(90)
            t.forward(100)
        if c=="r":
            t.right(90)
            t.forward(100)
        if c=="g":
            t.forward(100)
