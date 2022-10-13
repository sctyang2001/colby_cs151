''' race.py - this program aims to explore the turtle racing using objects.
Project04: Turtle Race
CS151, fall 2020, Layton
Scottie YANG Miaoyi
Sep.21, 2020
'''

import turtle
import random
import object_shapelib


def make_turtle(shape='turtle', penColor='white'):
    ''' Makes a `Turtle` object.
    '''
    # your code here
    turt = turtle.Turtle()
    turt.shape(shape)
    turt.color(penColor, penColor)
    turt.penup()
    return turt


def move_turtle(turt, radius, speed):
    '''Moves the `Turtle` object `turt` `speed` units
    '''
    # your code here
    turt.circle(radius, speed)


def writeNumStrides(turtC, numStrides):
    ''' This function will have a Turtle object write your current stride count on the screen.
    '''
    # your code here
    turtC.clear()
    turtC.write(numStrides, font=('Arial', 30, 'normal'))
    turtC.hideturtle()


# Main code starts here.
if __name__ == '__main__':
    screen = turtle.Screen()
    screen.bgcolor('#15A906')
    object_shapelib.draw_race_scene(screen)

    screen.tracer(False)
    turtR1 = make_turtle('turtle','yellow')
    turtR2 = make_turtle('turtle','blue')
    turtR3 = make_turtle('turtle','purple')
    turtR = [turtR1, turtR2, turtR3] # moving turtle list
    turtC1= make_turtle()
    turtC2= make_turtle()
    turtC3= make_turtle()
    turtC = [turtC1, turtC2, turtC3] # count turtle list

    turtRGo = [(0,-200), (0,-160), (0, -120)]
    turtCGo = [(320,310), (320,260), (320, 210)]
    for i in range(3):  # let turtle go to their positions
        turtR[i].goto(turtRGo[i])
        turtC[i].goto(turtCGo[i])
    
    screen.tracer(10) 
    cumulateR = [0, 0, 0]
    for i in range(3): # display initial rounds, which is 0
        turtR[i].pendown()
        writeNumStrides(turtC[i], cumulateR[i])

    # Below are turtle movement codes.
    for i in range(3000): 
        ''' generates moving turtle '''
        roundOR = [cumulateR[0]//360, cumulateR[1]//360, cumulateR[2]//360] # check round original, uses previous round data
        moveR = [4+2*random.random(), 3.9+2*random.random(), 4.1+2*random.random()]
        moveL = [200, 160, 120]

        ''' moves turtle, and accumulates the round by the angle it swings over.'''
        for i in range(3): 
            move_turtle(turtR[i], moveL[i], moveR[i])
            cumulateR[i] += moveR[i]
        roundR = [cumulateR[0]//360, cumulateR[1]//360, cumulateR[2]//360] # check round current, add previous round data together

        ''' aims for round count, if round original not equal to round current, refresh the number displayed. ''' 
        for i in range(3): 
            if roundR[i] != roundOR[i]:
                writeNumStrides(turtC[i], int(roundR[i]))

    screen.exitonclick()