''' compound_shapes.py - this program serves aims to create a compound shape objects with motion.
Project05: Animated Scene
CS151, fall 2020, Layton
Scottie YANG Miaoyi
Oct.6, 2020
'''

import graphics as gr
import time
import compound_shapes as cs


# Main code starts here.
if __name__ == "__main__":
    w = 500
    h = 500
    screen = gr.GraphWin('Project05: Balls Scene', width=w, height=h)
    cs.door_test(250, 250, 1, screen) # calls door scene
    cs.ball_test(250, 0, 0.5, screen) # calls ball scene
    screen.getMouse()