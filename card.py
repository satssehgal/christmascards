from turtle import *
from shapes import *
from random import randint

draw = Turtle()
draw.shape("turtle")
draw.speed(50)

window = turtle.Screen()
ts = turtle.getscreen()
canvas = ts.getcanvas()
height = ts.getcanvas()._canvas.winfo_height()
width = ts.getcanvas()._canvas.winfo_width()
print(height, width)
#window.bgcolor("#69D9FF")

draw_rectangle(turtle, '#69D9FF', -1278/2, -808/2, 1278, 808)

#draw snow
x=100
y=100
j=0

while j <100:
	draw_circle(draw, "white", x, y, 7)
	x=randint(-700,700)
	y=randint(-500,500)
	print(x,y)
	j+=1

draw.speed(12)
# draw the red hat
draw_triangle(draw, "red", -200, -130, 400)
#draw the white ball on top of the hat
draw_circle(draw, "white", 0, 200, 40)

#loop to draw the fur on the bottom of the cap
# x range in -200<x<200 in increments of 50

for i in range(9):
	draw_circle(draw, "white", (-200+(i*50)), -175, 40)

draw.penup()
draw.color("green")
draw.goto(-160, -250)
draw.write("Happy Holidays", font=("Arial", 42, "bold"))
draw.penup()
draw.color("red")
draw.goto(-115, -300)
draw.write("From [YOUR NAME]", font=("Arial", 42, "bold"))
draw.hideturtle()  

gs=draw.getscreen().getcanvas().postscript(file='outputname.ps')

