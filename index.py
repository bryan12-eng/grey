import math
import turtle

def ky(e):
    return 16*math.sin(e)**3
def jy(e):
    return 13*math.cos(e)-5*\
           math.cos(2*e)-2*\
           math.cos(3*e)-\
           math.cos(4*e)

t = turtle.Turtle()
t.speed(300)
turtle.bgcolor('black')

for w in range (2000):
    t.goto((ky(w)*10, jy(w)*10))
    t.pencolor('red')
    t.goto(0,0)