''' home.py (3rd in Project09) - this program aims to practice working with the L-system and class.
Project09: Unique trees and shapes
CS151, fall 2020, Layton
Scottie YANG Miaoyi
Nov.14, 2020
'''

import shapes
import tree
import turtle_interpreter as ti


def setHome():
	'''TODO: display method for displaying doghouse and trees and stars.		
    '''
	house = shapes.Square(150, 'thistle', fill=True) # draw doghouse with a square
	house.draw(-300, -290, 1, 90)

	roof = shapes.Triangle(150, 'olive', fill=True) # draw doghouse roof with a triangle
	roof.draw(-300, -140, 1, 60)

	door = shapes.Pentagon(30, 'dimgrey', fill=True) # draw doghouse door with a small pentagon
	door.draw(-180, -270, 1, 180)

	star = shapes.Star(65, 'Goldenrod', fill = True) # draw shaining star with a star
	star.draw(100, 250, 1, 90)

	treeJ = tree.Tree(filename = 'systemJ.txt') # draw medium tree with a treeJ model
	treeJ.setIterations(4)
	treeJ.setColor('lightseagreen')
	treeJ.draw(80, -270, scale = 2, heading = 90)

	treeCL = tree.Tree(filename = 'systemCL.txt') # draw big tree with a treeCL model
	treeCL.setIterations(3)
	treeCL.setColor('saddlebrown')
	treeCL.draw(200, -250, scale = 3, heading = 90)

	treePine = tree.Tree(filename = 'systemPineMod1.txt') # draw small colorful pine tree with treePineMod1 model
	treePine.setIterations(2)
	treePine.setColor('mediumseagreen')
	treePine.draw(-50, -190, scale = 3, heading = 90)

	house.TI.hold() # hold to make the window still


# Main code starts here.
if __name__ == "__main__":
	setHome()