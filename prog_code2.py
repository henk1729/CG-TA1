import turtle
from typing import List

lst: list[list[str]]=[]
n=int(input("Size: "))
for i in range(n):
    x=input()
    lst.append(x)

turtle.Screen().bgcolor("black")
t = turtle.Turtle()

t.goto(0, 0)
t.width(7)
t.color("red")
t.circle(120, -180)
t.circle(120, -180)

t.penup()
t.goto(0, 20)
t.pendown()
t.width(7)
t.color("blue")
t.circle(100, -180)
t.circle(100, -180)

t.penup()
t.goto(-100, 100)
t.pendown()
t.width(7)
t.color("yellow")
t.forward(420)

t.penup()
t.goto(140, 100)
t.pendown()
t.width(7)
t.color("white")

for i in range(len(lst)):
    for j in range(len(lst[i])):
        t.write(lst[i][j], font=("Verdana", 45, "normal"))
        t.forward(30)
    t.forward(60)

turtle.done()