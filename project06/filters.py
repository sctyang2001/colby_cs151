''' filters.py (1st in Project06) - this program aims to practice working with Image pixels.
Project06: The Warhol Project
CS151, fall 2020, Layton
Scottie YANG Miaoyi
Oct.20, 2020
'''

import display
import graphics as gr
import sys


def creativeSwap(img, filter):
    '''Swaps the green and blue values of every pixel of a Zelle image `img`'''
    for x in range(img.getWidth()):
        for y in range(img.getHeight()):
            (r, g, b) = img.getPixel(x, y)
            if filter == 'none' or 'original':
                img.setPixel(x, y, gr.color_rgb(r, g, b)) # shows original picture
            if filter == 'swapGreenBlue':
                img.setPixel(x, y, gr.color_rgb(r, b, g)) # swaps between blue and green pixels.
            if filter == 'filterFilm':
                img.setPixel(x, y, gr.color_rgb(int(r/2), int(g/4), int(b/8))) # every pixel darker.
            if filter == 'filterOverExpose':
                r = int((r*1.5))%255
                g = int((g*1.5))%255
                b = int((b*1.5))%255
                img.setPixel(x, y, gr.color_rgb(r, g, b)) # every pixel show its status of over-exposure.
            if filter == 'filterColorReduce':
                r = (r//120)*120
                g = (g//120)*120
                b = (b//120)*120
                img.setPixel(x, y, gr.color_rgb(r, g, b)) # every pixel have a ten-level color reduce.
            if filter == 'filterBW':
                img.setPixel(x, y, gr.color_rgb(int((r+g+b)/3), int((r+g+b)/3), int((r+g+b)/3))) # every pixel have B&W style change.


def test(filename, filter):
    '''Shows the image and test the swap'''
    myImage = gr.Image(gr.Point(0, 0), filename)
    creativeSwap(myImage, filter)
    screen = display.displayImage(myImage, 'Great Filters!')
    myImage.save('filters_output.ppm')
    screen.getMouse()


def greenScreen(greenImg, otherImg):
    ''' If a pixel in `greenImg` is very green, replace it with the corresponding pixel in `otherImg`.
    A reasonable test for 'very green' is if the green pixel is 1.5 times the blue channel and also bigger than the red pixel.
    Play around with the 1.5 number to see if you can get better results.
    '''
    for y in range(greenImg.getHeight()):
        for x in range(greenImg.getWidth()):
            p = greenImg.getPixel(x,y)
            (ro,go,bo) = otherImg.getPixel(x,y) # another image's tuple
            list(p) # make a tuple into a list, so that be able to compare single numbers
            r = p[0] # (r, g, b) to [r, g, b]. r is the first one
            g = p[1]
            b = p[2]
            if g >= int(b*1.5) and g >= r:
                greenImg.setPixel(x, y, gr.color_rgb(ro,go,bo)) # set pixel to another's
            else:
                pass


# Main code starts here.
if __name__ == '__main__':
    ''' Main code, within command-line arguments
    NOTICE: Please first of all change the file directory to Project06 so that image finding and command-line arguments could process.
    Input: 
        an image name <image_name(str)> and a filter name <filter_name(str)>
    Example:
        python3 filter.py flowers.ppm filterFilm
    - Available image names:
        [flowers.ppm, foliage.ppm, geraniums.ppm, lake.ppm, lovejoy.ppm, miller.ppm, mudd.ppm, winter.ppm]
    - Available filter names: 
        [none, original, swapGreenBlue, filterFilm, filterOverExpose, filterColorReduce, filterBW]
    '''
    if len(sys.argv) != 3:
        print('Usage: python3 filters.py <image_name(str)> <filter_name(str)>')
        exit
    else:
        test(sys.argv[1], sys.argv[2])