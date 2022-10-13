''' shapelib.py - this program is a duplication of lab02.py and serves as a shape library for main.py.
Project02: A Shape Collection
CS151, fall 2020, Layton
Scottie YANG Miaoyi
Sep.07, 2020
'''

import turtle
import random
import math


def goto(x, y):
    ''' allows the turtle to go position x and y, no matter where it currently is on the canvas
    '''
    # My code for goto function is here.
    # print('goto(): going to', x, y)
    # print('goto(): before move, turtle at', turtle.position())
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    # print('goto(): after move, turtle now at', turtle.position())


def random_color():
    ''' aims to generate random 6-digit HEX colorset for random starry background
    '''
    # My code for color is here.
    colorSet='' # define 'colorSet' as a string
    list = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'] # arrays for all possible choices
    for m in range(6): # six digits
        colorSet += list[random.randint(0,14)] # every time, choose one from the 'list' array and put into 'colorSet'
    return '#' + colorSet


def triangle(x, y, sideL):
    ''' have the turtle draw a triangle in a side length of 'sideL'
    '''
    # My code for triangle is here.
    goto(x, y)
    turtle.forward(sideL)
    turtle.left(120)
    turtle.forward(sideL)
    turtle.left(120)
    turtle.forward(sideL)
    turtle.left(120)


def hexagon(x, y, sideL):
    ''' draws simple shape 1, a hexagon in a side length of 'sideL'
    '''
    # My code for hexagon is here.
    goto(x-sideL/2, y-(sideL/2)*(3**0.5))
    for i in range(6):
        turtle.forward(sideL)
        turtle.left(60)


def rectangle(x, y, aL, bL):
    ''' have the turtle draw a rectangle in a side length of 'sideL'
    '''
    # My code for rectangle is here.
    goto(x,y)
    turtle.forward(aL)
    turtle.left(90)
    turtle.forward(bL)
    turtle.left(90)
    turtle.forward(aL)
    turtle.left(90)
    turtle.forward(bL)
    turtle.left(90)


def circle(x, y, radiusL):
    ''' have the turtle draw a triangle in a side length of 'radiusL'
    '''
    # My code for circle is here.
    goto(x, y-radiusL)
    turtle.circle(radiusL)


def draw_star(x, y, scale):
    ''' draws compound shape, the star, combined by a circle and a hexagon.
    '''
    # My code for star is here.
    global original_x
    global original_y
    global original_scale
    original_x = x
    original_y = y
    original_scale = scale

    turtle.speed(10)
    turtle.color('#ffffff')
    turtle.begin_fill() # outside part for star, circle
    turtle.fillcolor('#00a5a9')
    turtle.width(2)
    circle(x, y, scale*55)
    turtle.end_fill()

    turtle.begin_fill() # inner part for star, hexagon
    turtle.fillcolor('#00c9b0')
    turtle.width(1)
    hexagon(x, y, scale*55)
    turtle.end_fill()

    turtle.color('#ffff00') # exterior rings
    turtle.width(4)
    circle(x, y, scale*65)


def draw_rocket(x, y, scale):
    ''' draws compound shape, the rocket, combined by a semicircle, a rectangle, and three different triangles.
    '''
    # My code for rocket is here.
    turtle.speed(10)
    turtle.width(2)
    turtle.color('#ffffff')

    turtle.begin_fill() # rectangle part in the rocket
    turtle.fillcolor('#1970d2')
    rectangle(x, y, scale*20, scale*40)
    turtle.end_fill()

    turtle.setheading(-60) # base triangle part in the rocket
    turtle.begin_fill()
    turtle.fillcolor('#ff0000')
    triangle(x, y, scale*20)
    turtle.end_fill()

    turtle.setheading(210) # wing triangle part 1 in the rocket
    turtle.begin_fill()
    turtle.fillcolor('#880049')
    triangle(x, y+scale*27.5, scale*15)
    turtle.end_fill()
    
    turtle.setheading(30) # wing triangle part 2 in the rocket
    turtle.begin_fill()
    turtle.fillcolor('#880049')
    triangle(x+scale*20, y+scale*12.5, scale*15)
    turtle.end_fill()

    goto(x+scale*20, y+scale*40)  # top semicircle part in the rocket
    turtle.setheading(90)
    turtle.begin_fill()
    turtle.fillcolor('#4b2665')
    turtle.circle(scale*10,180)
    turtle.end_fill()


def orbit_generation(planet, x, y, color, scale):
    ''' 1st step of orbit stage; generates dots (two orbits) which parameters come from orbit_stage.
    '''
    # My code for generating dots is here.
    planet.color('') # transparent pen
    planet.shape('circle') # ask turtle to change its shape to circle, not arrow
    planet.shapesize(scale) # the 2 circle turtle has its size by scale in orbit_stage
    planet.fillcolor(color) # the 2 circle turtle has its color by scale in orbit_stage
    planet.penup()
    planet.setposition(x, y) # go to the starting position.
    planet.pendown()


def orbit_motion(planet1, planet2):
    ''' 2nd step of orbit stage; makes two orbits move! by the way of calculation in every frame.
    '''
    # My code for orbit motion is here.
    planet1_degree = 0
    planet2_degree = 0
    
    while True:
    # in every loop to infinity, we have degrees which are counting and refreshing, while the coordinate is refreshing by the distance to the center and its relative angle to the center
        planet1_degree += 0.5 #
        current_x = planet1.xcor()
        current_y = planet1.ycor()
        center_x = original_x # Planet 1 moves around the star, so center should be the star.
        center_y = original_y
        planet1_distance = math.sqrt((current_x-center_x)**2 + (current_y-center_y)**2) # distance to the center star, settled by sqrt((x-x0)^2+(y-y0)^2)
        planet1_rad = math.radians(planet1_degree) # radians to center
        current_x = center_x + planet1_distance*math.cos(planet1_rad) # refresh x, for the center star's coordinate adds on new calculation output (cosine(rad)*distance) is the new x coordinate
        current_y = center_y + planet1_distance*math.sin(planet1_rad) # refresh y, for the center star's coordinate adds on new calculation output (sine(rad)*distance) is the new y coordinate
        planet1.setposition(current_x, current_y) # now the new position is set

        planet2_degree += 6
        current_x = planet2.xcor()
        current_y = planet2.ycor()
        center_x = planet1.xcor() # Planet 2 moves around planet 1, so center should be planet 1.
        center_y = planet1.ycor()
        planet2_distance = math.sqrt((current_x-center_x)**2 + (current_y-center_y)**2) # distance to the center Planet 1, settled by sqrt((x-x0)^2+(y-y0)^2)
        planet2_rad = math.radians(planet2_degree)
        current_x = center_x + planet2_distance*math.cos(planet2_rad)
        current_y = center_y + planet2_distance*math.sin(planet2_rad)
        planet2.setposition(current_x, current_y)


def orbit_stage(scale):
    ''' 3rd step of orbit stage; put together step 1 and 2 so that call in main.py would be integrated.
    '''
    # My code for final orbit stage is here.
    # use contructer method to duplicate two turtles, as two movements are seperated, each assigned a name
    TN794 = turtle.Turtle()
    B612 = turtle.Turtle()
    orbit_generation(TN794, original_x + original_scale*130, original_y, '#cfa29f', 2*scale)
    orbit_generation(B612, original_x + original_scale*130+scale*60, original_y, '#8ea7c7', scale)
    orbit_motion(TN794, B612)