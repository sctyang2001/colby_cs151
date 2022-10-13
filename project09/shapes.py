''' shapes.py (1st in Project09) - this program aims to practice working with the L-system and class.
Project09: Unique trees and shapes
CS151, fall 2020, Layton
Scottie YANG Miaoyi
Nov.12, 2020
'''

import turtle_interpreter as ti


class Shape:

    def __init__(self, distance=100, angle=90, color=(0, 0, 0), lsysString=''):
        '''Shape constructor

        Parameters:
        -----------
        distance: float. Distance in pixels to go when moving the turtle forward
        angle: float. Angle in degrees to turn when turning the turtle left/right
        color: tuple of 3 floats. Default turtle pen color
        lsysString: str. The L-system string of drawing commands to draw the shape
            (e.g. made up of 'F', '+', '-', ...)
        '''
        # Create instance variables for all the parameters
        self.distance = distance
        self.angle = angle
        self.color = color
        self.lsysString = lsysString
        # Create an instance variable for a new TurtleInterpreter object
        self.TI = ti.TurtleInterpreter()

    
    def getTI(self):
        '''TODO: Get the TurtleInterpreter object
        '''
        return self.TI
    

    def getString(self):
        '''TODO: Get shape's L-system string
        '''
        return self.lsysString
    

    def setColor(self, c):
        '''TODO: Set the shape's color
        '''
        self.color = c
    

    def setDistance(self, dist):
        '''TODO: Set the shape's edge distance
        '''
        self.distance = dist
    

    def setAngle(self, a):
        '''TODO: Set the shape's turning angle
        '''
        self.angle = a
    

    def setString(self, s):
        '''TODO: Set the L-system string
        '''
        self.lsysString = s
    

    def draw(self, x_pos, y_pos, scale=1.0, heading=0):
        '''TODO: Draws the L-system string at the position `(x, y)` = `(x_pos, y_pos)` with the turtle
        facing the heading `heading`. The turtle drawing distance is scaled by `scale`.
        '''
        self.TI.goto(x_pos, y_pos, heading)
        self.TI.setColor(self.color)
        self.TI.drawString(self.lsysString, self.distance*scale, self.angle)


class Square(Shape):

    def __init__(self, distance=100, color=(0, 0, 0), fill=False):
        '''TODO: Draws the L-system string square
        '''
        # Create a variable for the L-system string that would draw a square.
        # if the fill parameter is true, concatenate the { and } characters to the beginning and end of the L-system string.
        if fill == True: 
            tempString = '{F-F-F-F-}'
        else:
            tempString = 'F-F-F-F-'
        # Call the parent's constructor, passing along values for all its parameters.
        super().__init__(distance, 90, color, tempString)


class Triangle(Shape):

    def __init__(self, distance=100, color=(0, 0, 0), fill=False):
        '''TODO: Draws the L-system string triangle
        '''
        if fill == True: 
            tempString = '{F-F-F-}'
        else:
            tempString = 'F-F-F-'
        super().__init__(distance, 120, color, '{F-F-F-}')


class Pentagon(Shape):

    def __init__(self, distance=100, color=(0, 0, 0), fill=False):
        '''TODO: Draws the L-system string pentagon
        '''
        if fill == True: 
            tempString = '{F-F-F-F-F-}'
        else:
            tempString = 'F-F-F-F-F-'
        super().__init__(distance, 72, color, tempString)


class Star(Shape):
    
    def __init__(self, distance=100, color=(0, 0, 0), fill=False):
        '''TODO: Draws the L-system string star
        '''
        if fill == True: 
            tempString = '{F---F++F---F++F---F++F---F++F---F++F---F++F---F++F---}'
        else:
            tempString = 'F---F++F---F++F---F++F---F++F---F++F---F++F---F++F---'
        super().__init__(distance, 103, color, tempString)


def test():
    '''TODO: Test method for displaying L-system shapes with scale
    '''
    # set up objects through lists first
    square = Square(color='blue', fill=True)
    triangle = Triangle(color='green', fill=True)
    pentagon = Pentagon(color='red', fill=True)
    star = Star(color='orange', fill=True)

    # finish drawing through process with scales and headings
    square.draw(-205, 200, scale=1.0, heading=0)
    triangle.draw(0, 0, scale=1.5, heading=0)
    pentagon.draw(-200, 0)
    star.draw(-10, 170, scale=0.7, heading=0)
    square.TI.hold()


# Main code starts here.
if __name__ == "__main__":
    test()