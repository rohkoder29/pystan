""" Draw a 5-point star """

import turtle

s = turtle.getscreen()
t = turtle.Turtle()
t.shape("turtle")

t.left(36)

for _ in range(5):
    t.forward(150)
    t.left(144)

# surround it

t.right(36)

for _ in range(5):
    t.forward(92.7045)
    t.left(72)
