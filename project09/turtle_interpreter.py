''' turtle_interpreter.py (adapted from Lab09) - this program aims to build integrated turtle, and the overall aim for the project is to build tree scenes.
Project09: Unique trees and shapes
CS151, fall 2020, Layton
Scottie YANG Miaoyi
Nov.10, 2020
'''

import turtle
import random


class TurtleInterpreter:

    # Create a Turtle object, set it as an instance variable 
    turt = turtle.Turtle()
    # Create a Screen object, set it as an instance variable.
    screen = turtle.Screen()
    def __init__(self, width=800, height=800, bgColor='white'):
        '''TurtleInterpreter constructor.
        Creates instance variables for a Turtle object and a Screen object with a particular window
        `width`, `height`, and background color `bgColor`.
        '''
        # Set the screen's height, width, and color based on the parameters
        self.screen.setup(width, height)
        self.screen.bgcolor(bgColor)
        # Turn the screen's tracer off.
        self.screen.tracer(False)


    def setColor(self, c):
        '''Set the turtle's pen color to the color c
        '''
        TurtleInterpreter.turt.color(c, c)


    def setWidth(self, w):
        '''Set the turtle's pen width to the int w
        '''
        TurtleInterpreter.turt.width(w)


    def goto(self, x, y, heading=0):
        '''A goto function that places the turtle at (x, y) and sets the heading to heading
        '''
        TurtleInterpreter.turt.penup()
        TurtleInterpreter.turt.goto(x, y)
        TurtleInterpreter.turt.pendown()
        TurtleInterpreter.turt.setheading(heading)


    def getScreenWidth(self):
        '''Get the screen's window width
        '''
        return self.screen.window_height()
    

    def getScreenHeight(self):
        '''Get the screen's window height
        '''
        return self.screen.window_height()


    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' key
        '''
        # Hide the turtle cursor and update the screen
        TurtleInterpreter.turt.hideturtle()
        self.screen.update()
        # Close the window when users presses the 'q' key
        self.screen.onkey(turtle.bye, 'q')
        # Listen for the q button press event
        self.screen.listen()
        # Have the turtle listen for a click
        self.screen.exitonclick()


    def drawString(self, lsysString, distance, angle):
        '''Interpret each character in an L-system string as a turtle command.
        '''
        # Walk through the lsysString character-by-character and
        # have the turtle object (instance variable) carry out the
        # appropriate commands
        turtPosition = []
        turtHeading = []
        turtFillColor = []
        turtPenColor = []
        turtFillColorL = []
        turtPenColorL = []
        for char in lsysString:
            if char == 'F':
                TurtleInterpreter.turt.forward(distance)
            if char == '+':
                TurtleInterpreter.turt.left(angle)
            if char == '-':
                TurtleInterpreter.turt.right(angle)
            if char == '[': # save the current turtle state (position and heading)
                turtPosition.append(TurtleInterpreter.turt.position())
                turtHeading.append(TurtleInterpreter.turt.heading())
            if char == ']': # restore the previous turtle state (position and heading)
                positionTuple = turtPosition.pop() # use pop for a reversed order of list read
                positionX = positionTuple[0]
                positionY = positionTuple[1]
                self.goto(positionX, positionY, turtHeading.pop())
            if char == '<': # save the current turtle color state
                turtPenColor.append(TurtleInterpreter.turt.pencolor())
                turtFillColor.append(TurtleInterpreter.turt.fillcolor())
            if char == '>': # restore the current turtle color state
                TurtleInterpreter.turt.pencolor(turtPenColor.pop())
                TurtleInterpreter.turt.fillcolor(turtFillColor.pop())
            if char == 'g': # to set the turtle's color to green (e.g. (0.15, 0.5, 0.2))
                self.setColor((0.15, 0.5, 0.2))
            if char == 'y': # to set the turtle's color to yellow (e.g. (0.8, 0.8, 0.3))
                self.setColor((0.8, 0.8, 0.3))
            if char == 'r': # to set the turtle's color to red (e.g. (0.8, 0.8, 0.3))
                self.setColor((0.8, 0.8, 0.3))
            if char == 'L': # draw a leaf at the current turtle position
                turtPenColorL = TurtleInterpreter.turt.pencolor()
                TurtleInterpreter.turt.begin_fill()
                TurtleInterpreter.turt.circle(7, 180)
                TurtleInterpreter.turt.end_fill()
                TurtleInterpreter.turt.pencolor(turtPenColorL)
            if char == 'B': # draw a red berry at the current turtle position
                turtFillColorL = TurtleInterpreter.turt.fillcolor()
                turtPenColorL = TurtleInterpreter.turt.pencolor()
                TurtleInterpreter.turt.color('red', 'red')
                TurtleInterpreter.turt.begin_fill()
                TurtleInterpreter.turt.circle(5)
                TurtleInterpreter.turt.end_fill()
                TurtleInterpreter.turt.fillcolor(turtFillColorL)
                TurtleInterpreter.turt.pencolor(turtPenColorL)
            if char == '{': # have the turtle start filling
                TurtleInterpreter.turt.begin_fill()
            if char == '}': # have the turtle end filling
                TurtleInterpreter.turt.end_fill()
        # Call the update method on the screen object to make sure everything drawn shows up at the very end of the method
        self.screen.update()