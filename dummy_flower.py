from turtle import *


warna1 = "black"
warna2 = "brown"
warna3 = "yellow"

shape("turtle")
speed("fast")
width(5)

# 1


def lingkaran(index):
    color(warna1, warna2)
    begin_fill()
    circle(index, 360)
    position()
    end_fill()


# 2


def garis():
    color(warna1, warna3)
    begin_fill()
    forward(100)
    circle(30, 180)
    position()
    forward(100)
    end_fill


degr = 90
x = 0

while x < 8:
    color(warna1, warna3)
    begin_fill()
    garis()
    end_fill()
    right(degr + 45)
    x += 1

left(67)
lingkaran(80)
done()
