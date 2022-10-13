''' compound_shapes.py (LIBRARY for scene.py) - this program aims to create a compound shape objects with motion.
Project05: Animated Scene
CS151, fall 2020, Layton
Scottie YANG Miaoyi
Oct.6, 2020
'''

import graphics as gr
import time


def door_init(x, y, scale):
    '''1st function that creates the door scene, draws it to the screen.
    '''
    doorShapes = []
    shapeProperties = [gr.Rectangle(gr.Point(x-50*scale, y-65*scale), gr.Point(x, y+65*scale)), gr.Rectangle(gr.Point(x, y-65*scale), gr.Point(x+50*scale, y+65*scale)), gr.Circle(gr.Point(x-6*scale, y), 3*scale), gr.Circle(gr.Point(x+6*scale, y), 3*scale)] # All in a list.
    for i in range(len(shapeProperties)):
        doorShapes.append(shapeProperties[i])
    return doorShapes


def door_animation(doorShapes, frame, screen):
    '''2nd function that creates the door scene, animates it in a frame.
    '''
    for k in range(len(doorShapes)):
        if k%2 == 0: # different positions in the list determines a different direction the door moves
            doorShapes[k].move(-1, 0)
        else:
            doorShapes[k].move(1, 0)
    time.sleep(0.01)


def door_test(x, y, scale, screen):
    '''Main function that creates the door scene, put together last two and make it appear and move.
    '''
    doorShapes = door_init(x, y, scale)
    for i in range(len(doorShapes)):
        if i <= 1:
            doorShapes[i].setFill(gr.color_rgb(240,39,39))
        else:
            doorShapes[i].setFill(gr.color_rgb(255,225,31))
        doorShapes[i].draw(screen)
    for n in range(40):
        door_animation(doorShapes, n, screen)


def ball_init(x, y, scale):
    '''1st function that creates the ball scene, draws it to the screen.
    '''
    ballShapes = []
    ballProperties = [gr.Circle(gr.Point(x, y+100*scale), 50*scale), gr.Circle(gr.Point(x, y+100*scale), 30*scale), gr.Polygon(gr.Point(x, y+100*scale+20), gr.Point(x-20, y+100*scale), gr.Point(x+20, y+100*scale))] # All in a list.
    for i in range(len(ballProperties)):
        ballShapes.append(ballProperties[i])
    return ballShapes


def ball_animation(ballShapes, frame, screen):
    '''2nd function that creates the ball scene, animates it in a frame.
    '''
    for k in range(len(ballShapes)): # falls down by 5 points in the change of frame
        ballShapes[k].move(0, 5)
    time.sleep(0.01)


def ball_test(x, y, scale, screen):
    '''Main function that creates the door scene, put together last two and make it appear and move.
    '''
    ballShapes = ball_init(x, y, scale)
    for i in range(len(ballShapes)): # set different colors
        if i == 0:
            ballShapes[i].setFill(gr.color_rgb(56,144,202))
        elif i == 1:
            ballShapes[i].setFill(gr.color_rgb(157,206,58))
        else:
            ballShapes[i].setFill(gr.color_rgb(255,225,31))
        ballShapes[i].draw(screen)
    for n in range(80):
        ball_animation(ballShapes, n, screen)
