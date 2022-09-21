"""
    Theme: Turtle Overview
    Tutor: Keith Galli
"""

import math
from secrets import choice
import turtle

# let's create the screen
ts = turtle.Screen()

""" 1.  """

# # let's create a turtle called 'jo'

# # jo will draw a simple parallelogram
# jo = turtle.Turtle()
# jo.shape("turtle")
# # jo.forward(100)
# # jo.left(45)
# # jo.forward(100)
# # jo.left(135)
# # jo.forward(100)
# # jo.left(45)
# # jo.forward(100)
# # #
# # jo.home()

# # let's recreate it but with filled in color
# jo.color("magenta", "cyan")
# jo.begin_fill()
# jo.forward(100)
# jo.left(45)
# jo.forward(100)
# jo.left(135)
# jo.forward(100)
# jo.left(45)
# jo.forward(100)
# jo.end_fill()
# #
# jo.home()



""" 2.  """


# # let's create a turtle named ann
# ann = turtle.Turtle()
# ann.shape("classic")

# # ann will draw a beautiful flower
# # ann.penup()
# # ann.backward(100)
# # ann.pendown()
# # ann.color("red", "yellow")
# # ann.speed(10)
# # ann.begin_fill()
# # for _ in range(32):
# #     ann.forward(240)
# #     ann.left(168.75)
# # ann.end_fill()
# # ann.home()

# # ann will draw a beautiful flower with random colors

# colors = ["red", "cyan", "yellow", "orange", "blue",
#           "green", "purple", "black", "brown", "pink",
#           "magenta", "teal"]
# bg = choice(colors)
# ts.bgcolor(bg)
# colors.remove(bg)
# ann.penup()
# ann.setpos(-120,0)
# ann.pendown()
# ann.begin_fill()
# for _ in range(32):
#     ann.speed(choice([0, 1, 3, 6, 10]))
#     ann.color(choice(colors))
#     ann.forward(240)
#     ann.left(168.75)
# ann.end_fill()
# ann.home()



""" 3.  """


# let's create a turtle named al
al = turtle.Turtle()

# al will draw the Fibonacci Sequence/Spiral (up to 21)

# let's make the screen a bit larger for that purpose
ts.setup(1000, 700)
ts.bgcolor("teal")
# and increse the pen size
al.pensize(3)
al.speed("fastest")

colors = ["red", "cyan", "yellow", "orange", "blue",
          "green", "purple", "brown", "pink", "magenta"]

# generate Fibonacci sequence (up to some number)
def fibo(limit: int) -> int:
    a, b = 1, 1
    while a < limit:
        yield a
        a, b = b, a + b

# number of squares
sqs = 6

# let's draw the squares

def draw_square(turtle, square_size):
    # bg = choice(colors)
    # turtle.color(bg)
    # colors.remove(bg)
    # turtle.begin_fill()
    for _ in range(6):
        turtle.forward(square_size)
        turtle.left(90)
    # turtle.end_fill()

side = 30

# N = (n-1) * (n-2) + 1
current = list(fibo((sqs - 1) * (sqs - 2) + 1))
for i in range(sqs):
    al.right(90)
    draw_square(al, current[i] * side)

# now let's draw the spiral
al.penup()
al.setpos(0,0)
al.left(90)
al.pendown()

for item in current:
    al.color(choice(colors))
    al.circle(item * side, 90)  # draw quartercicles (360 / 4 == 90)

turtle.exitonclick()
# turtle.done()

##############################################################################


# # draw a circle (the hard way, (and with extra))
# n = 100     # radius
# d = (360 / n, n)
# a = turtle.Turtle()
# for _ in range(d[-1]):
#     a.speed(choice([0, 1, 3, 6, 10]))
#     a.color(choice(colors))
#     a.left(d[0])
#     a.forward(5)