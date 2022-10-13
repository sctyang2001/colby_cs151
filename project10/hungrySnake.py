''' hungrySnake.py - this overall program aims to practice encapsulation and event-based programming.
Project10: Event-Based Programming
CS151, fall 2020, Layton
Scottie YANG Miaoyi
Nov.23, 2020
'''

import turtle as turt
import random


class HungrySnake:
    ''' HungrySnake class defines the initial state, motion state and direction, and the collision detection.
    '''
    # initialize the snake, this is the step length
    XStep = 10
    YStep = 0
    # use the position tuple to show the intial state
    SBody = []
    initialX = [0, 10, 20, 30, 40, 50, 60, 70, 80]
    initialY = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(9):
        SBody.append((initialX[i], initialY[i])) # generate 9 squares initially in one snake body

    
    def makeMoveSnake(self):
        ''' makes snake body, moves snake forward, pops the head and releases the last block(to show it's moving)
        '''
        for block in self.SBody: # Initialize and draw the snake.
            squareBlock(block[0], block[-1], 10, 'black')
        self.SBody.pop(0)
        self.SBody.append((self.SBody[-1][0]+self.XStep, self.SBody[-1][-1]+self.YStep)) # moves to east initially.


    def turnSnake(self, XInputStep, YInputStep):
        ''' turn the snake as input (how to turn the snake? to go different direction by changing the step (e.g.: east(10,0), north(0,10))with different keyboard input)
        '''
        HungrySnake.XStep = XInputStep
        HungrySnake.YStep = YInputStep


    def crashDetector(self):
        ''' check the crash status
        '''
        # Does it crash its own body? Check the start and edge of its body block
        if self.SBody[-1] in self.SBody[:-1]:
            return True
        # Does it crash into the wall? Check the boundary.
        elif self.SBody[-1][0] >= 230 or self.SBody[-1][0] <= -250 or self.SBody[-1][-1] >= 250 or self.SBody[-1][-1] <= -230: # boundary value
            return True
        else:
            return False


    def getApple(self):
        ''' get the apple, and append one block into its body
        '''
        self.SBody.append(self.SBody[-1])


def squareBlock(x, y, width, color):
    ''' the function that makes blocks, black snake body block and red apple block.
    '''
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.color(color)  # set color
    turt.begin_fill()
    for i in range(4): # draw the block
        turt.forward(width)
        turt.right(90)
    turt.end_fill()
    turt.penup()


def makeApple():
    ''' the main loop of game, calls previous builds together.
    '''
    global appleX, appleY
    if HungrySnake().SBody[-1] == (appleX, appleY): # if the snake meets the apple
        appleX = random.randrange(-22, 22) * 10 # randomly generates an apple around. (Why *10 is illustrated in the following)
        appleY = random.randrange(-22, 22) * 10
        HungrySnake().getApple() # getApple, to append one 
    else: # if the snake does not meet the apple
        squareBlock(appleX, appleY, 10, 'red') # remain the apple position


def mainloop():
    ''' the main loop of game, calls previous builds together.
    '''
    turt.clear()
    makeApple()
    HungrySnake().makeMoveSnake()
    HungrySnake().crashDetector() # print it as crashes.
    if HungrySnake().crashDetector(): # if crashed
        squareBlock(HungrySnake().SBody[-1][0], HungrySnake().SBody[-1][-1], 10, 'red') # show crashed block
        print("CRASHED! Try again by using SPACE key.") # and print "Try again"
        turt.done()
    else: # if not crash, refresh the frame to start the loop
        turt.ontimer(mainloop, 100) # loop through it by 100 ms.


def snakeRevive():
    ''' to set the snake to its original state.
    '''
    for i in range(9):
        HungrySnake().SBody[i] = (HungrySnake().initialX[i], HungrySnake().initialY[i]) # restart 9 squares initially in one snake body
    HungrySnake().crashDetector = False # put the state of True back to False to revive
    mainloop() # do the mainloop again.


# Main code starts here. ,
if __name__ == '__main__':
    appleX = random.randrange(-22, 22) * 10 # why *10? the width of the snake is 10, so that every turn they could meet perfectly.
    appleY = random.randrange(-22, 22) * 10

    turt.setup(500, 500) # setup turtle
    turt.hideturtle()
    turt.tracer(False)
    turt.listen() # to listen the key entered

    turt.onkeypress(quit, "q")
    turt.onkeypress(lambda: snakeRevive(), 'space')
    turt.onkeypress(lambda: HungrySnake().turnSnake(-10, 0), 'a') # only putting lambda put could it transformed "None" to a function.
    turt.onkeypress(lambda: HungrySnake().turnSnake(10, 0), 'd')
    turt.onkeypress(lambda: HungrySnake().turnSnake(0, 10), 'w')
    turt.onkeypress(lambda: HungrySnake().turnSnake(0, -10), 's')

    mainloop()
    turt.done()
