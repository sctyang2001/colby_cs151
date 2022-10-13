''' ascii_art_image.py (1st in Project07) - this program aims to practice working with ASCII Art images, please see ASCII_output for resizable output.
Project07: ASCII Art
CS151, fall 2020, Layton
Scottie YANG Miaoyi
Oct.27, 2020
'''

import graphics as gr
import sys


def creativeSwap(img, filter):
    ''' The function that creates a list and transfer the avg value of the pixels into different values into lists.
    '''
    numList = [] # the list putting numbers, or strings, or emojis that the image simulates.
    for y in range(img.getHeight()): # y is at the outer place because after each y (height) value there is a '\n' new line character.
        for x in range(img.getWidth()):
            (r, g, b) = img.getPixel(x, y) # read RGB value of the pixel
            colorAvg = int((r+g+b)/3) # avg the pixel to see its brightness
            if filter == 'characterDoub': # double characters, 0-128, 128-255.
                if colorAvg <= 128:
                    numList.append('1')
                else:
                    numList.append('0')
            if filter == 'characterQuad': # four characters, 0-63, 63-126, 126-189, 189-255.
                if colorAvg <= 63:
                    numList.append('.')
                elif colorAvg <= 126:
                    numList.append('1')
                elif colorAvg <= 189:
                    numList.append('8')
                else:
                    numList.append('M')
            if filter == 'characterEmoji': # three characters, 0-85, 85-170, 170-255.
                if colorAvg <= 85:
                    numList.append('😡')
                elif colorAvg <= 170:
                    numList.append('😏')
                else:
                    numList.append('🥶')
        numList.append('\n') # changes the line after each height value.
    numList = ''.join(numList) # join the numList together without space to show
    return numList


def test(img, filter):
    ''' The function tests out and prints the art, and saves it to a text file.
    '''
    myImage = gr.Image(gr.Point(0, 0), img) # read original image
    numList = creativeSwap(myImage, filter)
    print(numList)
    resultsFile = open('ASCII_output.txt', 'w') # saves the art string to the file
    resultsFile.write('WILDLIFE OUTPUT:\n' + str(numList))
    resultsFile.close()


# Main code starts here.
if __name__ == '__main__':
    ''' Main code, within command-line arguments
    NOTICE: Please first of all change the file directory to Project07 so that image finding and command-line arguments could process.
    Input: 
        2 in total, <image_name(str)> and <filter_name(str)>.
    Example:
        python3 ascii_art_image.py wwf.ppm characterQuad
    - Available character names:
        [exotic.ppm, wwf.ppm, wildlife.ppm]
    - Available filter names: 
        [characterDoub, characterQuad, characterEmoji]
    '''
    if len(sys.argv) != 3:
        print('Usage: python3 filters.py <image_name(str)> <filter_name(str)>')
        exit
    else:
        test(sys.argv[1], sys.argv[2])