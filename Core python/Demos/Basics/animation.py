import turtle
import time

screen = turtle.Screen()
screen.title("Simple Animation")
screen.bgcolor("black")

box = turtle.Turtle()
box.shape("square")
box.color("cyan")
box.penup()
box.speed(0)

x = -200

while True:
    box.goto(x, 0)
    x += 5

    if x > 200:
        x = -200

    time.sleep(0.02)
