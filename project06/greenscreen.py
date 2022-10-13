''' greenscreen.py (2nd in Project06) - this program aims to practice working with Greenscreen replacement.
Project06: The Warhol Project
CS151, fall 2020, Layton
Scottie YANG Miaoyi
Oct.20, 2020
'''

import filters
import display
import graphics as gr


# Main code starts here.
if __name__ == '__main__':
    ''' Main code, without command-line arguments
    NOTICE: Please first of all change the file directory to Project06 so that image finding could process.
    '''
    myImage = gr.Image(gr.Point(0, 0), 'myGreenScreen.ppm')
    otherImage= gr.Image(gr.Point(0, 0), 'exotic.ppm')
    filters.greenScreen(myImage, otherImage)
    screen = display.displayImage(myImage, 'Exotic beach!')
    myImage.save('greenscreen_output.ppm')
    screen.getMouse()