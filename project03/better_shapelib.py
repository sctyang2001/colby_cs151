''' better_shapelib.py (LIBRARY for museum.py) - this program aims to explore the complex scenes and use encapsulation.
Project03: Scenes Within Scenes
CS151, fall 2020, Layton
Scottie YANG Miaoyi
Sep.16, 2020
'''

import turtle
import random
import math
import sys


### the first artwork - Mondrain ###
def goto(x, y):
    ''' allows the turtle to go position x and y, no matter where it currently is on the canvas
    '''
    # My code for goto function is here.
    turtle.penup()
    turtle.goto(x, y)
    turtle.left(90)
    turtle.pendown()
    # print('goto(): after move, turtle now at', turtle.position())


def rectangle(x, y, aL, bL, fill=False, edgeColor='black', fillColor='red', penWidth=2):
    ''' Draws a `width` x `height` rectangle with bottom-left corner positioned at (`x`, `y`).
    '''
    # My code for rectangle is here.
    goto(x,y)
    turtle.setheading(0)
    turtle.width(penWidth)
    if fill:
        turtle.begin_fill()
        turtle.color(edgeColor, fillColor)
    for i in range(4):
        turtle.forward((aL*((i+1)%2))+(bL*((i)%2))) # follow the order drawing aL, bL, aL, bL.
        turtle.right(90)
    turtle.end_fill()
    turtle.width(1)

    
def mondrian(x, y, sideL, numRectangles=300):
    ''' Draws a Mondrian scene.
    '''
    # My code for Mondrain is here.
    for i in range(numRectangles):
        if i <= numRectangles*0.6: # selecting 60% for transparent, rest for colored
            rectangle(random.randint(x-sideL/2, x+sideL/2), random.randint(y-sideL/2, y+sideL/2), random.randint(8*(sideL//100),13*(sideL//100)), random.randint(8*(sideL//100),13*(sideL//100)), fill=False)
        else:
            rectangle(random.randint(x-sideL/2, x+sideL/2), random.randint(y-sideL/2, y+sideL/2), random.randint(10*(sideL//100),25*(sideL//100)), random.randint(10*(sideL//100),25*(sideL//100)), fillColor=(random.random(),random.random(),random.random()), fill=True)
### end of the first artwork - Mondrain


### the second artwork - Scened Rocket
def random_color():
    ''' aims to generate random 6-digit HEX colorset for random starry background
    '''
    # My code for color is here.
    colorSet='' # define 'colorSet' as a string
    list = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'] # arrays for all possible choices
    for m in range(6): # six digits
        colorSet += list[random.randint(0,14)] # every time, choose one from the 'list' array and put into 'colorSet'
    return '#' + colorSet


def triangle(x, y, sideL, fill=False, edgeColor='black', fillColor='red'):
    ''' have the turtle draw a triangle in a side length of 'sideL'
    '''
    # My code for triangle is here.
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    if fill:
        turtle.begin_fill()
        turtle.color(edgeColor, fillColor)
    for i in range(3):
        turtle.forward(sideL)
        turtle.left(120)
    turtle.end_fill()


def hexagon(x, y, sideL, fill=False, edgeColor='black', fillColor='red'):
    ''' draws simple shape 1, a hexagon in a side length of 'sideL'
    '''
    # My code for hexagon is here.
    goto(x-sideL/2, y-(sideL/2)*(3**0.5))
    if fill:
        turtle.begin_fill()
        turtle.color(edgeColor, fillColor)
    for i in range(6):
        turtle.forward(sideL)
        turtle.left(60)
    turtle.end_fill()


def scene(x, y, sideL):
    ''' allows turtle to draw space, combining black background and 2 types of bg stars, dots and hexagons in random position, sizes, numbers and colors.
    '''
    # My code for space1 is here.
    turtle.hideturtle()
    goto(x-sideL/2,y-sideL/2)
    turtle.begin_fill()
    turtle.color('','black')
    for i in range(4):
        turtle.forward(sideL) # follow the order sideL
        turtle.right(90)
    turtle.end_fill()
    turtle.speed(0)
    turtle.tracer(100) # disable turtle move so background forms faster
    for i in range(int(random.randrange(150, 300))): # 300-500 dots in different position, sizes and color
        turtle.penup()
        turtle.goto(random.randrange(x-sideL/2, x+sideL/2), random.randrange(y-sideL/2, y+sideL/2))
        turtle.pendown()
        turtle.dot(random.randrange(0, 3), random_color()) # utilizes random_color() function built in shapelib.py to generate random color
    for i in range(int(random.randrange(100, 150))): # 150-250 hexagons in different position, sizes and color
        turtle.begin_fill()
        turtle.fillcolor(random_color()) # utilizes random_color() function built in shapelib.py to generate random color
        hexagon(random.randrange(x-sideL/2, x+sideL/2), random.randrange(y-sideL/2, y+sideL/2), random.randrange(0, 3))
        turtle.end_fill()


def draw_rocket(x, y, scale, fill=False, edgeColor='black', fillColor='red'):
    ''' draws compound shape, the rocket, combined by a semicircle, a rectangle, and three different triangles.
    '''
    # My code for rocket is here.
    turtle.width(2)
    turtle.color('#ffffff')

    goto(x,y)
    turtle.setheading(90)
    turtle.begin_fill() # rectangle part in the rocket
    turtle.fillcolor('#1970d2')
    for i in range(4):
        turtle.forward((scale*40*((i+1)%2))+(scale*20*((i)%2))) # follow the order drawing aL, bL, aL, bL.
        turtle.right(90)
    turtle.end_fill()

    turtle.setheading(-60) # base triangle part in the rocket
    triangle(x, y, scale*20, fill=True, edgeColor='#ffffff', fillColor='#ff0000')

    turtle.setheading(210) # wing triangle part 1 in the rocket
    triangle(x, y+scale*27.5, scale*15, fill=True, edgeColor='#ffffff', fillColor='#880049')
    
    turtle.setheading(30) # wing triangle part 2 in the rocket
    triangle(x+scale*20, y+scale*12.5, scale*15, fill=True, edgeColor='#ffffff', fillColor='#880049')

    goto(x+scale*20, y+scale*40) # top circle part in the rocket
    turtle.setheading(90)
    turtle.begin_fill()
    turtle.fillcolor('#4b2665')
    turtle.circle(scale*10,180)
    turtle.end_fill()


def rocketScene(x, y, sideL):
    ''' draws the rocket scene
    '''
    scene(x, y, sideL)
    draw_rocket(random.randrange(x-sideL/2, x+sideL/2), random.randrange(y-sideL/2, y+sideL/2), 2)
### end of the second artwork - Scened Rocket


### the third artwork - Orbits
def circle(x, y, radiusL, fill=False, edgeColor='black', fillColor='red'):
    ''' have the turtle draw a triangle in a side length of 'radiusL'
    '''
    # My code for circle is here.
    turtle.setheading(0)
    turtle.penup()
    turtle.goto(x, y-radiusL)
    turtle.pendown()
    if fill:
        turtle.begin_fill()
        turtle.color(edgeColor, fillColor)
    turtle.circle(radiusL)
    turtle.end_fill()


def draw_star(x, y, sideL, fill=False, edgeColor='black', fillColor='red'):
    ''' draws compound shape, the star, combined by a circle and a hexagon.
    '''
    # My code for star is here.
    turtle.width(2)
    circle(x, y, sideL/3, fill=True, edgeColor='#ffffff', fillColor='#00a5a9')

    turtle.width(1)
    turtle.begin_fill()
    turtle.color('#ffffff','#00c9b0')
    turtle.goto(x-sideL/6, y-(sideL/6)*(3**0.5))
    for i in range(6):
        turtle.forward(sideL/3)
        turtle.left(60)
    turtle.end_fill()

    turtle.width(4)
    circle(x, y, sideL/3+6, fill=True, edgeColor='#ffee00', fillColor='')


def orbit_generation(x, y, radiusL, fill=False, edgeColor='black', fillColor='red'):
    ''' 1st step of orbit stage; generates dots (two orbits) which parameters come from orbit_stage.
    '''
    for i in range(10):
        circle(x+60*random.random(), y+(-100)+200*random.random(), radiusL/2, fill=True, edgeColor='#ffffff', fillColor='grey')


def orbits(x, y, sideL):
    ''' draws the orbits scene
    '''
    draw_star(x-30, y-30, sideL)
    orbit_generation(x+5, y+5, sideL/9)
### end of the third artwork - Orbits


# Main code starts here.
if __name__== '__main__':
    turtle.tracer(False)
    mondrian(-275,225,180)
    rocketScene(275,225,200)
    orbits(0,225,200)
    mondrian(200,-225,10)
    rocketScene(300,-155,160)
    orbits(-80,-75,140)
    mondrian(145,0,300)
    turtle.exitonclick()
