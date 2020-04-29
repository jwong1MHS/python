import turtle

def regular_polygon(t, n, size):
    i = 0
    while i < n:
        t.fd(size)
        t.rt(360/n)
        i+= 1

def square_spiral(t, size):
    while size > 0:
        t.fd(size)
        t.rt(90)
        size-= 5
        
        
def spiral(t, size, angle):
    while size > 0:
        t.fd(size)
        t.rt(angle)
        size-= 1
        


raphael = turtle.Turtle()


#Testing a bunch of regular polygons
for i in range(3, 10):
    regular_polygon(raphael, i, 100)

raphael.clear()

square_spiral(raphael, 200)

raphael.clear()

spiral(raphael, 50, 20)

window = turtle.Screen()
window.exitonclick()