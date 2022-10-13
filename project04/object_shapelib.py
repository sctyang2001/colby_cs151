''' object_shapelib.py (LIBRARY for museum.py) - this program aims to explore the complex turtle moving scenes.
Project04: Turtle Race
CS151, fall 2020, Layton
Scottie YANG Miaoyi
Sep.21, 2020
'''

import turtle
import random


def goto(turt, x, y, heading=0):
    ''' allows the turtle to go position x and y, no matter where it currently is on the canvas
    '''
    # My code for goto function is here.
    turt.penup()
    turt.goto(x,y)
    turt.setheading(heading)
    turt.pendown()


def circle(turt, x, y, radius, penWidth=7, penColor='#E8696F', fill=True, fillColor='#75BBE5'):
    ''' allows the turtle to go and draw the circle, defining different colors
    '''
    # My code for circle function is here.
    goto(turt, x, y-radius)
    turt.hideturtle()
    turt.width(penWidth)
    turt.color(penColor)
    if fill:
        turt.fillcolor(fillColor)
        turt.begin_fill()
    turt.circle(radius)
    turt.end_fill()


def rectangle(turt, x, y, aL, bL, fill=False, edgeColor='black', fillColor='red', penWidth=2):
    ''' Draws a `width` x `height` rectangle with bottom-left corner positioned at (`x`, `y`).
    '''
    # My code for rectangle is here.
    goto(turt, x, y)
    turt.width(penWidth)
    turt.color(0.5-0.5*random.random(), 0.5-0.5*random.random(), 0.5-0.5*random.random())
    if fill:
        turt.begin_fill()
        turt.fillcolor(fillColor)
    for i in range(4):
        turt.forward((aL*((i+1)%2))+(bL*((i)%2))) # follow the order drawing aL, bL, aL, bL.
        turt.right(90)
    turt.end_fill()


def mondrian(turt):
    ''' allows the turtle to go and draw the Mondrian background, which represents audience.
    '''
    # My code for draw_race_scene function is here, aims to display at the bottoms of the screen.
    for i in range(450):
        if i <= 150:
            rectangle(turt, random.randint(-450, 450),random.randint(-400, -240), random.randint(10, 40), random.randint(15, 35), fill=False)
        else:
            rectangle(turt, random.randint(-450, 450),random.randint(-400, -240), random.randint(10, 40), random.randint(15, 35), fillColor=(random.random(),random.random(),random.random()), fill=True)


def draw_race_scene(screen):
    ''' allows the turtle to go and draw the background, combining goto() and circle() function.
    '''
    # My code for draw_race_scene function is here.

    turtRC = turtle.Turtle() # calls turtle and draw the race course, four circles
    screen.tracer(10)
    circle(turtRC, 0, 0, 220)
    circle(turtRC, 0, 0, 180, penWidth=4, penColor='red')
    circle(turtRC, 0, 0, 140, penWidth=4, penColor='red')
    circle(turtRC, 0, 0, 100, fillColor='#15A906')
    
    screen.tracer(False) 
    turtRC.penup()
    turtGo = [(190,310),(190,260),(190,210)] # calls turtle and write the description of each turtle, with their colors.
    turtColor = ['yellow','blue','purple']
    turtPrint = ['turt R1:::','turt R2:::','turt R3:::']
    for i in range(3):
        turtRC.goto(turtGo[i])
        turtRC.color(turtColor[i])
        turtRC.write(turtPrint[i], font=('Arial', 30, 'normal'))

    mondrian(turtRC) # draws a mondrian scene.


# Main code starts here.
if __name__ == '__main__':
    screen = turtle.Screen()
    screen.tracer(10)
    screen.bgcolor('#15A906')
    draw_race_scene(screen)
    screen.exitonclick()