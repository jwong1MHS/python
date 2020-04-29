import turtle

def square_spiral(t, size):
    if size > 0:
        t.fd(size)
        t.rt(90)
        square_spiral(t, size-5)
  
def koch_curve(t, depth, size):
    if depth == 0:
        t.fd(size)
    else:
       koch_curve(t, depth-1, size)
       t.lt(60)       
       koch_curve(t, depth-1, size)
       t.rt(120)
       koch_curve(t, depth-1, size)
       t.lt(60)
       koch_curve(t, depth-1, size)


def dragon(t, depth, size):
    if depth == 0:
        t.fd(size)
    else:
        dragon(t, depth-1, size)
        t.lt(120)
        dragon(t, depth-1, size)
        t.rt(120)
        dragon(t, depth-1, size)


raphael = turtle.Turtle()

#square_spiral(raphael, 200)


raphael.setx(200)
raphael.clear()

#koch_curve(raphael, 2, 50)
dragon(raphael, 3, 50)

window = turtle.Screen()
window.exitonclick()