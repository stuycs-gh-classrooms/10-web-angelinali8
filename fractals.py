import turtle
window = turtle.Screen()
window.setup(1000, 1000)

def koch_curve(t, depth, size):
    if (depth == 1):
        t.pencolor('darkgoldenrod')
        t.fd(size)
    else:
        koch_curve(t, depth-1, size)
        t.lt(120)
        koch_curve(t, depth-1, size)
        t.rt(60)
        koch_curve(t, depth-1, size)
        t.lt(120)
        koch_curve(t, depth-1, size)
        
spencer = turtle.Turtle()
spencer.lt(90)
spencer.width(4)
spencer.pu()
spencer.goto(-40, 40)
spencer.pd()
                
koch_curve(spencer, 4, 20)          
window.exitonclick()
#---------------------------------------------------------------------------
import turtle
from random import randint
window = turtle.Screen()
window.setup(1000, 1000)
window.colormode(255)

def triangle(t, size, width):
    t.width(width)
    t.lt(60)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(180)

def sierpinski(t, depth, size, width):
    r = randint(100, 230)
    g = randint(100, 230)
    b = randint(100, 230)
    t.fillcolor(r, g, b)
    t.width(width)
    if depth == 1:
        t.begin_fill()
        triangle(t, size, width)
        t.end_fill()
    else:
        sierpinski(t, depth-1, size/2.5, width-1.5)
        t.fd(size/2)
        sierpinski(t, depth-1, size/2.5, width-2)
        t.bk(size/2)
        t.lt(90)
        t.fd(size/2)
        t.rt(90)
        sierpinski(t, depth-1, size/2.5, width-2.5)
        t.rt(90)
        t.fd(size/2)
        t.lt(90)

spencer = turtle.Turtle()
spencer.pu()
spencer.speed(0)
spencer.goto(-200, 0)
spencer.pd()
sierpinski(spencer, 4, 300, 8.5)

window.exitonclick()

#---------------------------------------------------------------------------
import turtle
from random import randint
window = turtle.Screen()
window.setup(1000, 1000)
window.colormode(255)

def flower(t):
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.lt(72)
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.lt(72)
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.lt(72)
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.lt(72)
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.lt(72)

def tree(t, depth, size, angle, width):
    r = randint(100, 255)
    g = randint(100, 255)
    b = randint(100, 255)
    t.fillcolor(r, g, b)
    t.width(width)
    if depth == 0:
        t.fd(size)
        flower(t)
        t.bk(size)
    else:
        t.fd(size)
        t.rt(angle)
        tree(t, depth-1, size, angle, width-2)
        t.lt(2 * angle)
        tree(t, depth-1, size, angle, width-2)
        t.rt(angle)
        flower(t)
        t.bk(size)

spencer = turtle.Turtle()
spencer.lt(90)
spencer.speed(10)
spencer.pd()
tree(spencer, 4, 50, 20, 10)
window.exitonclick()
