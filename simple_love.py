import turtle as t

color1 = 'red'
color2 = 'black'

t.width(4)
t.speed(10)
t.title('dibuat fahri')


def love():
    t.begin_fill()
    t.color(color2, color1)
    t.left(45)
    t.forward(100)
    t.circle(50, 180)
    print(t.position())
    t.end_fill()

    t.penup()
    t.goto(0, 0)
    t.pendown()

    t.begin_fill()
    t.color(color2, color1)
    t.right(90)
    t.forward(100)
    t.circle(-50, 180)
    print(t.position())
    t.end_fill()
    t.hideturtle()


love()
t.done()
