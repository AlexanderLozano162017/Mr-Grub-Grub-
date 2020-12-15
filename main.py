#!/usr/bin/env python3
#pythong game
#by Alex lozano


import turtle
import time
import random

delay = 0.1

#Screen set up for game

window = turtle.Screen()
window.title("Mr. Grub Grub")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

#Grub head

head = turtle.Turtle()
head.speed(1)
head.shape("triangle")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"


#food for Mr. Grub
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(1,100)
food.direction = "stop"

segments = []



#functions
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

#keyboard bindings
window.listen()

window.onkey(up, "Up")
window.onkey(down, "Down")
window.onkey(left, "Left")
window.onkey(right, "Right")

#maingame loop
while True:
    window.update()
#check for collision for food
    if head.distance(food) < 30:
        #moves food to random spot on screen
        x = random.randint(-295, 295)
        y = random.randint(-295, 295)
        food.goto(x, y)

#add segments
    new_segments = turtle.Turtle()
    new_segments.speed(0)
    new_segments.shape("circle")
    new_segments.color("white")
    new_segments.penup()
    segments.append(new_segments)


#moving the segments with the body and growth with the consumption of food
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

#move segment 0 to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

        move()



time.sleep(delay)



window.mainloop()