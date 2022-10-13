# shapes.py
# Project01: Turtle Shape Introduction
# CS151, fall 2020, Layton
# Scottie YANG Miaoyi
# Aug.31, 2020

import turtle

n=0

### shape A improved duplication ###
def shapeA():
    global n # globalized n for shape D use, controls times with length. 
    turtle.speed(10)
    round=0

    while round<6:
        turtle.pensize(5) 
        colorRGB=0.1*round

        turtle.begin_fill()
        turtle.fillcolor(colorRGB, colorRGB, colorRGB)
        turtle.forward(50)
        turtle.left(120)
        turtle.forward(165)
        turtle.left(120)
        turtle.forward(300+50*n) # length increase with n
        turtle.left(60)
        turtle.forward(50)
        turtle.left(120)
        turtle.forward(250+50*n) # length increase with n
        turtle.right(120)
        turtle.forward(65)

        turtle.end_fill()
        round+=1
    
### shape B duplication ###
def shapeB():
    import math
    turtle.speed(5)
    turtle.colormode(255)
    turtle.bgcolor(220,220,250)
    round = 0

    while round<3:
        turtle.penup()
        turtle.goto(0,-180)
        turtle.setheading(-30)
        
        turtle.left(round*120)
        turtle.forward((100/3)*(math.sqrt(3)))
        turtle.left(30)
        
        turtle.pendown()
        turtle.colormode(1)
        colorRGB=1-0.2*round
        turtle.begin_fill()
        turtle.fillcolor(colorRGB, colorRGB, colorRGB)
        
        turtle.pensize(3)
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
        
        turtle.end_fill()
        round+=1

### calls shape A and shape B ###
def shapeThree():
    shapeB()
    turtle.penup()
    turtle.goto(0,50)
    turtle.pendown()
    turtle.right(150)
    shapeA()
    turtle.hideturtle()


### shape A improved duplication, with length able to control ###
def shapeC(distance): #it is based on shape A
    turtle.speed(10)
    round=0

    while round<6:
        turtle.setposition(0,0)
        turtle.pensize(5) 
        colorRGB=0.1*round
        turtle.begin_fill()
        turtle.fillcolor(colorRGB, colorRGB, colorRGB)
        turtle.forward(50)
        turtle.left(120)
        turtle.forward(165)
        turtle.left(120)
        turtle.forward(50+distance)
        turtle.left(60)
        turtle.forward(50)
        turtle.left(120)
        turtle.forward(distance)
        turtle.right(120)
        turtle.forward(65)
        turtle.end_fill()
        round+=1

    else:
        turtle.hideturtle()

### shape Three improved duplication, with length and times able to control by times ###
def shapeD(times):  
    global n
    shapeB()
    turtle.penup()
    turtle.goto(0,50)
    turtle.pendown()
    
    while n<times: # times are able to specify
        turtle.right(150) # every time turn right 150 degrees colors not to be the same with leaves nearby
        shapeA() # refer to shapeA() to see the length change function
        n+=1
    
    else:
        turtle.hideturtle()

#shapeThree() #calls shapeThree (that is A+B) once, remove the # ahead only if use.

#shapeC(400) #calls shape C (an improved version of shape A) once, remove the # ahead and fill the "distance"(0-400) only if use.

#shapeD(times) #calls shapeThree (A+B) multiple times and automaticly lengthen the parameter, remove the # and fill the "times" (int 1-3) that desired for the shape to duplicate.

turtle.exitonclick()