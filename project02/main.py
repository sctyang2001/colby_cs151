''' main.py - this program aims to explore the shape colletion space scene.
Project02: A Shape Collection
CS151, fall 2020, Layton
Scottie YANG Miaoyi
Sep.08, 2020
'''

import turtle
import random
import shapelib


def draw_space1():
    ''' allows turtle to draw space, combining black background and 2 types of bg stars, dots and hexagons in random position, sizes, numbers and colors.
    '''
    # My code for space1 is here.
    turtle.bgcolor(0, 0, 0)
    turtle.speed(0)
    turtle.tracer(100) # disable turtle move so background forms faster
    for i in range(int(random.randrange(300, 500))): # 300-500 dots in different position, sizes and color
        turtle.penup()
        turtle.goto(random.randrange(-450, 450), random.randrange(-450, 450))
        turtle.setheading(0)
        turtle.pendown()
        turtle.dot(random.randrange(0, 3), shapelib.random_color()) # utilizes random_color() function built in shapelib.py to generate random color
    for i in range(int(random.randrange(150, 250))): # 150-250 hexagons in different position, sizes and color
        turtle.penup()
        turtle.goto(random.randrange(-450, 450), random.randrange(-450, 450))
        turtle.setheading(0)
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor(shapelib.random_color()) # utilizes random_color() function built in shapelib.py to generate random color
        shapelib.hexagon(random.randrange(-450, 450), random.randrange(-450, 450), random.randrange(0, 4))
        turtle.end_fill()
    turtle.hideturtle()
    turtle.tracer(1)


# Main code from here.
''' These are for global use in shapelib.py, serving draw_star and orbit_stage'''
original_x = 0
original_y = 0
original_scale = 0
''' draw the space scene as a background '''
draw_space1()
''' draw the simple shape, hexagon as a meterite '''
turtle.color('green')
turtle.width(4)
shapelib.hexagon(140,-220,30)
''' draw the simple/compound shape, the planet '''
shapelib.draw_star(-100,0,1.4)
''' draw the compound shape, the rocket. '''
shapelib.draw_rocket(300,60,1.5)
''' draw the simple/compound shape, the planet sets. Drop the beat, let planets fly! '''
shapelib.orbit_stage(1.6)
turtle.exitonclick()
