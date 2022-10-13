''' museum.py - this program aims to explore the museum building and use encapsulation.
Project03: Scenes Within Scenes
CS151, fall 2020, Layton
Scottie YANG Miaoyi
Sep.16, 2020
'''

import turtle
import random
import math
import sys
import better_shapelib as bsl


def square(x, y, L, fill=False, edgeColor='black', fillColor='red'):
    ''' draws square to control frame'''
    turtle.penup()
    turtle.goto(x-L/2,y-L/2)
    turtle.pendown()
    turtle.setheading(90)
    if fill:
        turtle.begin_fill()
        turtle.color(edgeColor, fillColor)
    for i in range(4):
        turtle.forward(L)
        turtle.right(90)
    turtle.end_fill()


def frame(a, b, c):
    ''' draws frames from the square '''
    turtle.tracer(False)
    square(-275,225,220, fill=True, fillColor=a) # links to a command-line argument, a, as a color
    square(-275,225,200, fill=True, fillColor='white')
    square(0,125,220, fill=True, fillColor=b) # links to a command-line argument, b, as a color
    square(0,125,200, fill=True, fillColor='white')
    square(275,25,220, fill=True, fillColor=c) # links to a command-line argument, c, as a color
    square(275,25,200, fill=True, fillColor='black')
    bsl.mondrian(-275,225,180)
    bsl.orbits(0,125,200)
    bsl.rocketScene(275,25,200)


def carpet():
    ''' draws the carpet'''
    bsl.rectangle(-500,-200,1000,50, fill=True)
    bsl.rectangle(-500,-240,1000,40, fill=True,fillColor='#ff3300')
    bsl.rectangle(-500,-270,1000,30, fill=True,fillColor='#ff4400')
    bsl.rectangle(-500,-290,1000,20, fill=True,fillColor='#ff5500')
    bsl.rectangle(-500,-300,1000,10, fill=True,fillColor='#ff6600')


def museum(a, b, c):
    ''' draws the integral museum scene
    '''
    frame(a, b, c)
    carpet()
    turtle.exitonclick()


# main code starts here
if __name__== '__main__':
    '''Draws my museum scene. Requires ***THREE** command-line arguments to change the color of a artwork's frame. 
    - The following makes the three frame red/green/yellow:
        python3 museum.py red green yellow
    - The following makes it blue/grey/pink:
        python3 museum.py blue grey pink
    '''
    a=sys.argv[1] # a, as a stringed command-line argument, links to the first frame color.
    b=sys.argv[2] # b, as a stringed command-line argument, links to the second frame color.
    c=sys.argv[3] # c, as a stringed command-line argument, links to the third frames color.
    museum(a, b, c)
    turtle.exitonclick()