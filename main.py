import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
michelangelo.speed(1)
leonardo.speed(1)
x = random.randrange(1,100)
michelangelo.fd(x)
y = random.randrange(1,100)
leonardo.fd(y)
michelangelo.undo()
leonardo.undo()

for x in range (10):
  michelangelo.fd(x)
  leonardo.fd(x)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Part B - complete part B here
leonardo.hideturtle()
michelangelo.pendown()
michelangelo.pencolor('orange')

sides=3
for y in range (sides):
    michelangelo.fd(50)
    michelangelo.lt(360/sides)
michelangelo.goto(-100,20)
michelangelo.clear()

sides=4
for y in range (sides):
    michelangelo.fd(50)
    michelangelo.lt(360/sides)
michelangelo.goto(-100,20)
michelangelo.clear()

sides=6
for y in range (sides):
    michelangelo.fd(50)
    michelangelo.lt(360/sides)
michelangelo.goto(-100,20)
michelangelo.clear()

sides=9
for y in range (sides):
    michelangelo.fd(50)
    michelangelo.lt(360/sides)
michelangelo.goto(-100,20)
michelangelo.clear()

sides=12
for y in range (sides):
    michelangelo.fd(50)
    michelangelo.lt(360/sides)
michelangelo.goto(-100,20)
michelangelo.clear()

window.exitonclick()
