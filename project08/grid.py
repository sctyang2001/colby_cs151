''' grid.py.py (2nd in Project08) - this program aims to build a 3x3 grid of trees, and the overall aim for the project is to build tree scenes.
Project08: Fractals and Trees
CS151, fall 2020, Layton
Scottie YANG Miaoyi
Nov.04, 2020
'''

import lsystem
import turtle_interpreter as ti


def display():
    '''Function to test out placing an image (left) next to
    its filtered version (right)
    '''
    # Make image list, with x, y placement info, how to process it (str),
    # six images at different positions.
    width = 650
    height = 650
    lsys = lsystem.Lsystem(filename='systemPineMod1.txt') # setup lsystem
    terp = ti.TurtleInterpreter(width, height, bgColor='white') # setup screen and turtle_interpreter
    terp.setColor('green')
    terp.setWidth(2)
    # image list, [0] and [1] is position x and y, [2] is angle, [3] is initerations
    imgListOfLists = [[-35-width/3, 35+height/6, 22, 1], 
                      [-35, 35+height/6, 22, 2],
                      [-35+width/3, 35+height/6, 22, 3],
                      [-35-width/3, 35-height/6, 46, 1],
                      [-35, 35-height/6, 46, 2],
                      [-35+width/3, 35-height/6, 46, 3],
                      [-35-width/3, 35-height/2, 60, 1],
                      [-35, 35-height/2, 60, 2],
                      [-35+width/3, 35-height/2, 60, 3]]
    for imgList in imgListOfLists:
        lsysString = lsys.buildString(imgList[3]) # lsys build string and process iteration number
        terp.goto(imgList[0], imgList[1], 90) # turt goto start point and head north
        terp.drawString(lsysString, 7, imgList[2]) # draw string within lsysString, length 7, and angle
    terp.hold() # hold after ends to close


# Main code starts here
if __name__ == '__main__':
    display()
