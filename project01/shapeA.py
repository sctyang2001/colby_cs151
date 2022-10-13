# shapeA.py
# Project01: Turtle Shape Introduction
# CS151, fall 2020, Layton
# Scottie YANG Miaoyi
# Aug.30, 2020

import turtle 

turtle.speed(9) # set pen speed, fast
round=0 # set loop round, 6 rounds in this case

while round<6: # 6 rounds in this case, 0-5 will be 6 numbers.
    turtle.pensize(5) 
    colorRGB=0.1*round # As I use 1 as scale instead of 255, (0,0,0) is black and (1,1,1) is white.
    turtle.begin_fill() # begin fill with turtle
    turtle.fillcolor(colorRGB, colorRGB, colorRGB) # is linked with the colorRGB variable as every leaf will be 0.1 degree whiter.
    
    ### creating the "L" piece ###
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(165)
    turtle.left(120)
    turtle.forward(300)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(250)
    turtle.right(120)
    turtle.forward(65)
    
    turtle.end_fill() # filling ends while drawing ends
    round+=1 # finished and add 1

else:
    turtle.hideturtle() # hide while everything finishes
    turtle.exitonclick()