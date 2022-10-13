# shapeB.py
# Project01: Turtle Shape Introduction
# CS151, fall 2020, Layton
# Scottie YANG Miaoyi
# Aug.31, 2020

import math # math module for squareroot
import turtle

turtle.speed(5)
turtle.colormode(255) # I want purple background but I only know the RGB of light purple in 1 scale, have to set 255 here and set back to 1 later.
turtle.bgcolor(220,220,250)
round = 0 # set loop round, 3 rounds in this case

while round<3: # 3 rounds in this case, 0-2 will be 3 numbers.
    turtle.penup()
    turtle.goto(0,-180) # Every round go back to start point
    turtle.setheading(-30) # and the start heading is the same
    
    turtle.left(round*120) # but the heading is adjusted while round differs. 360/3=120
    turtle.forward((100/3)*(math.sqrt(3))) # See draft attached with Req_Image_2 in Report 
    
    turtle.pendown()
    turtle.colormode(1) # set back to RGB 1 scale
    colorRGB=1-0.2*round # it fades every time a leaf is drown
    turtle.begin_fill()
    turtle.fillcolor(colorRGB, colorRGB, colorRGB)
    
    ### creating the "L" piece ###
    turtle.left(30)
    turtle.pensize(3) # I applied different pensizes here.
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(250)
    turtle.pensize(6)
    turtle.left(120)
    turtle.forward(300)
    turtle.left(60)
    turtle.forward(50)
    turtle.pensize(3)
    turtle.left(120)
    turtle.forward(250)
    turtle.right(120)
    turtle.forward(50)
    turtle.pensize(6)
    turtle.forward(100)
    
    turtle.end_fill() # filling ends while drawing ends
    round+=1 # finished and add 1
else:
    turtle.hideturtle() # hide while everything finishes
    turtle.exitonclick()