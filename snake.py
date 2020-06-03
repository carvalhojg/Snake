# Simplistic Snake Game

import turtle
import time
import random

delay = 0.1

# Screen
wn = turtle.Screen()
wn.title("Snake Game by @carvalhojg")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake
## Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Main game loop
while True:
    wn.update()

    time.sleep(delay)


wn.mainloop()