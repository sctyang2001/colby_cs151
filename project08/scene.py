''' scene.py.py (3rd in Project08) - this program aims to build a scene, and the overall aim for the project is to build tree scenes.
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
    width = 800
    height = 800
    terp = ti.TurtleInterpreter(width, height, bgColor='#CC7722') # setup screen and turtle_interpreter
    terp.setWidth(2)

    # image list, [0] and [1] is position x and y, [2] is angle, [3] is initerations, [4] is tree type
    imgListOfLists = [[0-width/6, 0-height/4, 22.5, 2, 'systemPineMod1.txt', 'brown'],
                      [0, 0-height/4, 22.5, 3, 'systemCL.txt', 'purple'],
                      [0+width/5, 0-height/4, 22.5, 4, 'systemPineMod1.txt', 'green']]
    for imgList in imgListOfLists:
        lsys = lsystem.Lsystem(filename=imgList[4]) # setup lsystem, treetype decided
        lsysString = lsys.buildString(imgList[3]) # lsys build string and process initeration number
        terp.setColor(imgList[5]) # setup color
        terp.goto(imgList[0], imgList[1], 90) # turt goto start point and head north
        terp.drawString(lsysString, 8, imgList[2]) # draw string within lsysString, length 7, and angle
    
    # background design
    terp.draw_background(0, int(width), height) # draw background (linked with project03)
    terp.setColor('grey')
    terp.goto(-40-width/6, 0-height/4, 90) # draw the greenhouse
    terp.drawString('F-F-F-F', 90, 90)
    
    terp.hold() # hold after ends to close

# Main code starts here
if __name__ == '__main__':
    display()
