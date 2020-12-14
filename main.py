#pythong game
#by Alex lozano


import turtle
import time

delay = 0.1

#Screen set up for game

window = turtle.Screen()
window.title("Mr. Grub Grub")
window.bgcolor("black")
window.setup(width=500, height=500)
window.tracer(0)

#Grub head

head = turtle.Turtle()
head.speed(0)
head.shape("triangle")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"


#functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)


def up():
    head.setheading(90)
    head.forward(100)

def down():
    head.setheading(270)
    head.forward(100)

def left():
    head.setheading(180)
    head.forward(100)

def right():
    head.setheading(0)
    head.forward(100)

window.listen()

window.onkey(up, "Up")  # This will call the up function if the "Left" arrow key is pressed
window.onkey(down, "Down")
window.onkey(left, "Left")
window.onkey(right, "Right")

#maingame loop
while True:
    window.update()

    move()

    time.sleep(delay)
