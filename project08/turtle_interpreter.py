''' turtle_interpreter.py (1st in Project08) - this program integrated Lab08 contents and aims to build integrated turtle, and the overall aim for the project is to build tree scenes.
Project08: Fractals and Trees
CS151, fall 2020, Layton
Scottie YANG Miaoyi
Nov.04, 2020
'''

import turtle
import random
import better_shapelib as bsl
import museum


class TurtleInterpreter:
    def __init__(self, width=800, height=800, bgColor='white'):
        '''TurtleInterpreter constructor.
        Creates instance variables for a Turtle object and a Screen object with a particular window
        `width`, `height`, and background color `bgColor`.
        '''
        # Create a Turtle object, set it as an instance variable
        self.turt = turtle.Turtle()
        # Create a Screen object, set it as an instance variable.
        self.screen = turtle.Screen()
        # Set the screen's height, width, and color based on the parameters
        self.screen.setup(width, height)
        self.screen.bgcolor(bgColor)
        # Turn the screen's tracer off.
        self.screen.tracer(False)


    def setColor(self, c):
        '''Set the turtle's pen color to the color c
        '''
        self.turt.color(c, c)


    def setWidth(self, w):
        '''Set the turtle's pen width to the int w
        '''
        self.turt.width(w)


    def goto(self, x, y, heading=None):
        '''A goto function that places the turtle at (x, y) and sets the heading to heading
        '''
        self.turt.penup()
        self.turt.goto(x, y)
        self.turt.pendown()
        self.turt.setheading(heading)


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
        self.turt.hideturtle()
        self.screen.update()
        # Close the window when users presses the 'q' key
        self.screen.onkey(turtle.bye, 'q')
        # Listen for the q button press event
        self.screen.listen()
        # Have the turtle listen for a click
        self.screen.exitonclick()


    def draw_background(self, x, y, sideL):
        '''Draws the background for scene.py, using Project03 code (better_shapelib.py)
        '''
        bsl.mondrian(x, y, sideL) # Mondrian scene
        bsl.draw_rocket(random.randint(-300, 300), 240, 1.4) # rocket scene
        museum.carpet()
        

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
                self.turt.forward(distance)
            if char == '+':
                self.turt.left(angle)
            if char == '-':
                self.turt.right(angle)
            if char == '[': # save the current turtle state (position and heading)
                turtPosition.append(self.turt.position())
                turtHeading.append(self.turt.heading())
            if char == ']': # restore the previous turtle state (position and heading)
                positionTuple = turtPosition.pop() # use pop for a reversed order of list read
                positionX = positionTuple[0]
                positionY = positionTuple[1]
                self.goto(positionX, positionY, turtHeading.pop())
            if char == '<': # save the current turtle color state
                turtPenColor.append(self.turt.pencolor())
                turtFillColor.append(self.turt.fillcolor())
            if char == '>': # restore the current turtle color state
                self.turt.pencolor(turtPenColor.pop())
                self.turt.fillcolor(turtFillColor.pop())
            if char == 'g': # to set the turtle's color to green (e.g. (0.15, 0.5, 0.2))
                self.setColor((0.15, 0.5, 0.2))
            if char == 'y': # to set the turtle's color to yellow (e.g. (0.8, 0.8, 0.3))
                self.setColor((0.8, 0.8, 0.3))
            if char == 'r': # to set the turtle's color to red (e.g. (0.8, 0.8, 0.3))
                self.setColor((0.8, 0.8, 0.3))
            if char == 'L': # draw a leaf at the current turtle position
                turtPenColorL = self.turt.pencolor()
                self.turt.begin_fill()
                self.turt.circle(7, 180)
                self.turt.end_fill()
                self.turt.pencolor(turtPenColorL)
            if char == 'B': # draw a red berry at the current turtle position
                turtFillColorL = self.turt.fillcolor()
                turtPenColorL = self.turt.pencolor()
                self.turt.color('red', 'red')
                self.turt.begin_fill()
                self.turt.circle(5)
                self.turt.end_fill()
                self.turt.fillcolor(turtFillColorL)
                self.turt.pencolor(turtPenColorL)
        # Call the update method on the screen object to make sure everything drawn shows up at the very end of the method
        self.screen.update()