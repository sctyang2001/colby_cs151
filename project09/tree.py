''' shapes.py (2nd in Project09) - this program aims to practice working with the L-system and class.
Project09: Unique trees and shapes
CS151, fall 2020, Layton
Scottie YANG Miaoyi
Nov.12, 2020
'''

import shapes
import lsystem as ls
import turtle_interpreter as ti


class Tree(shapes.Shape):

    def __init__(self, distance=5, angle=22.5, color=(0.5, 0.4, 0.3),
        iterations=3, filename=None):
        '''Tree constructor
        Parameters:
        -----------
        distance: float. Distance in pixels to go when moving the turtle forward
        angle: float. Angle in degrees to turn when turning the turtle left/right
        color: tuple of 3 floats. Default turtle pen color
        iterations: int. Number of iterations to apply the replacement rules on the tree base string.
        filename: str. Filename for the text file that contains the treett L-system base string and 1+ replacement rules.
        '''
        super().__init__(distance, angle, color, lsysString = '')
        self.LS = ls.Lsystem(filename) # A L-system object that reads in the tree L-system base string and replacement rules stored in the text file filename.
        self.iterations = iterations # The number of L-system iterations that will be used when building the string that will be used to draw the tree.


    def setIterations(self, iterations):
        '''TODO: Set the number of L-system iterations.
        '''
        self.iterations = iterations


    def read(self, filename):
        '''TODO: Have the L-system object read in a base string and replacement rules from a file.
        '''
        self.LS.read(filename)
        

    def draw(self, x_pos, y_pos, scale=1.0, heading=90): # by default make it so that the tree is drawn right-side up
        '''TODO: Draws the L-system string at the position `(x, y)` = `(x_pos, y_pos)` with the turtle
        facing the heading `heading`. The turtle drawing distance is scaled by `scale`.
        '''
        self.lsysString = self.LS.buildString(self.iterations) # build the L-system string that is appropriate for drawing a tree
        super().draw(x_pos, y_pos, scale, heading)


def test(filename):
    '''TODO: Test method for displaying L-system trees with scale. Starbuck sizes name applies here.
    '''
    tall = Tree(filename = filename)
    tall.setIterations(2)
    tall.setColor('Green')
    grande = Tree(filename = filename)
    grande.setIterations(4)
    grande.setColor('Orange')
    venti = Tree(filename = filename)
    venti.setIterations(6)
    venti.setColor('Olive')
    tall.draw(-200, -300, scale = 3, heading = 90) # arrange positions and scales and headings
    grande.draw(-50, -300, scale = 2.5, heading = 90)
    venti.draw(200, -300, scale = 2, heading = 90)
    tall.TI.hold()


# Main code starts here.
if __name__ == "__main__":
    test('systemJ.txt')