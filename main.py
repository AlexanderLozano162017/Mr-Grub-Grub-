# !/usr/bin/env python3
# pythong game
# by Alex lozano


import random
import time
import turtle
from turtle import Turtle

import segment as segment

delay = 0.1



# Screen set up for game
window = turtle.Screen()
window.title("Mr. Grub Grub")
window.bgcolor("black")
window.setup(width=1000, height=1000)
window.tracer(0)

#score
score = 0
high_score: int = 0


#turtle writing text
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("orange")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("SCORE: 0  HIGHSCORE: 0", align="center", font=("Courier", 18, "normal"))

# Grub head

head: Turtle = turtle.Turtle()
head.speed(0)
head.shape("triangle")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# food for Mr. Grub
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(1, 100)
food.direction = "up"

segments = []



# Grub body
grub_body = turtle.Turtle()
grub_body.speed(0)
grub_body.shape("triangle")
grub_body.color("white")
grub_body.penup()
segments.append(grub_body)

#increasing score
score += 23

if score > high_score:
    high_score = score
pen.clear()
pen.write("Score: {}  HIGHSCORE: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

# functions





def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)


def up():

         head.setheading(90)
         head.forward(50)


def down():

             head.setheading(270)
             head.forward(50)


def left():

             head.setheading(180)
             head.forward(50)


def right():

            head.setheading(0)
            head.forward(50)


# keyboard bindings
window.listen()

window.onkey(up, "Up")
window.onkey(down, "Down")
window.onkey(left, "Left")
window.onkey(right, "Right")

# maingame loop

# check for collison
if head.xcor() > 295 or head.xcor() < -295 or head.ycor() > 295 or head.ycor() < -295:
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    #reset score
    score = 0
pen.clear()
pen.write("Score: {}  HIGHSCORE: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

#clearing list of segments
segments.clear()

#hiding the segments
for segments in segments:
    segment.goto(300, 300)




    while True:
        window.update()
        # check for collision for food
        if head.distance(food) < 35:
            # moves food to random spot on screen
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

#scoring system


    # moving the segments with the body and growth with the consumption of food
for index in range(len(segments) - 1, 0, -1):
    x = segments[index - 1].xcor()
    y = segments[index - 1].ycor()
    segments[index].goto(x, y)

# move segment 0 to head
if len(segments) <= 0:
    pass
else:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x, y)

    move()
#colliaions with body
segments: Turtle
segment: object
for segment in segments:
    if segment.distance(head) < 20:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
    # clearing list of segments
    segments.clear()

    # hiding the segments
    for segment in segments:
        segment.goto(1000, 1000)



window.update()
time.sleep(delay)

window.mainloop()
