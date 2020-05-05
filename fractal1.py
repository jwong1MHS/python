import turtle
import random

def triangle(t, length):
    t.fd(length)
    t.lt(120)
    t.fd(length)
    t.lt(120)
    t.fd(length)
    t.lt(120)

def sep_triangle(t, depth, length):
    if depth == 0:
        triangle(t, length)
    else:
        sep_triangle(t, depth-1, length/2)
        t.fd(length/2)
        sep_triangle(t, depth-1, length/2)
        t.bk(length/2)
        t.lt(60)
        t.fd(length/2)
        t.rt(60)
        sep_triangle(t, depth-1, length/2)
        t.rt(120)
        t.fd(length/2)
        t.lt(120)

def draw_tree(t, depth, length, angle):
    if depth == 1:
        t.fd(length)
        t.bk(length)
    else:
        t.fd(length)
        t.lt(angle)
        draw_tree(t, depth-1, length, angle)
        t.rt(angle * 2)
        draw_tree(t, depth-1, length, angle)
        t.lt(angle)
        t.bk(length)

def fancy_tree(t, length, angle):
    angle+= random.randrange(-10, 10)
    #print(depth, angle)
    if length <= 5:
        t.fd(length)
        t.bk(length)
    else:
        t.fd(length)
        t.lt(angle)
        fancy_tree(t, length * .75, angle)
        t.rt(angle * 2)
        fancy_tree(t, length * .75, angle)
        t.lt(angle)
        t.bk(length)
raphael = turtle.Turtle()


#raphael.lt(60)
#sep_triangle(raphael, 5, 300)

raphael.lt(90)
fancy_tree(raphael, 100, 30)


window = turtle.Screen()
window.exitonclick()
