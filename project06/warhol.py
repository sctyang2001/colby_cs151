''' warhol.py (3rd in Project06) - this program aims to practice working with Image arrangement and create a Warhol scene.
Project06: The Warhol Project
CS151, fall 2020, Layton
Scottie YANG Miaoyi
Oct.20, 2020
'''

import display
import graphics as gr


def placeImageInCanvas(canvas, img, topleft_x, topleft_y):
    '''Place the image `img` into the larger canvas `canvas`. The image `img` should be positioned
    so that its top-left corner appears at (row , col) = (topleft_row, topleft_col) in the large canvas.
    NOTE: (0, 0) is the top-left corner.

    Parameters:
    -----------
    canvas: Image. Larger canvas that fits two images side-by-side horizontally in a row
    img: Image. Image to be placed in one of the 2 "slots" on the canvas.
    topleft_x: int. x pixel position (column) in `canvas` where the top-left corner of `img` should go
    topleft_y: int. y pixel position (row) in `canvas` where the top-left corner of `img` should go
    '''
    for y in range(img.getHeight()):
        for x in range(img.getWidth()):
            (r, g, b) = img.getPixel(x, y)
            canvas.setPixel(x + topleft_x, y + topleft_y, gr.color_rgb(r, g, b))


def creativeSwap(img, filter):
    '''Swaps the green and blue values of every pixel of a Zelle image `img`
    It was moved from filters.py
    '''
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
                img.setPixel(x, y, gr.color_rgb(r, g, b)) # every pixel have a 120-level color reduce.
            if filter == 'filterBW':
                img.setPixel(x, y, gr.color_rgb(int((r+g+b)/3), int((r+g+b)/3), int((r+g+b)/3))) # every pixel have B&W style change.
    return img


def sideBySideList():
    '''Function to test out placing an image (left) next to
    its filtered version (right)
    '''
    # Create an image, the same as miller.ppm, 320x256 pixels.
    width = 320
    height = 256
    img = gr.Image(gr.Point(0, 0), 'miller.ppm')

    # Make image list, with x, y placement info, how to process it (str),
    # six images at different positions.
    imgListOfLists = [[0, 0, 'none', img],
                      [width, 0, 'swapGreenBlue', img],
                      [0, height, 'filterBW', img],
                      [width, height, 'filterFilm', img],
                      [0, 2*height, 'filterOverExpose', img],
                      [width, 2*height, 'filterColorReduce', img]]
    
    # Make 2x3 canvas
    canvas = gr.Image(gr.Point(0, 0), 2*width, 3*height)
    
    '''Process is:
    - Loop thru list, deal with one sublist at a time.
    - Clone the image object (original image by default).
    - Apply the solid color depending on the color name in the sublist.
    - Place it on the canvas.
    - Display the canvas.
    '''
    for imgList in imgListOfLists:  # imgList is a SUBLIST
        currImg = imgList[-1].clone()
        currImg = creativeSwap(currImg, imgList[2]) # moves the creativeSwap function I created in "filters.py" here.
        placeImageInCanvas(canvas, currImg, imgList[0], imgList[1])
        # imgList[-1] = currImg # Update image object in list of lists

    screen = display.displayImage(canvas, 'Powerful Warhol!') # Display canvas
    canvas.save('warhol_output.ppm') # saves the Warhol project pics
    screen.getMouse() # Wait for mouse click to close window and end program


# Main code starts here.
if __name__ == '__main__':
    ''' Main code, without command-line arguments
    NOTICE: Please first of all change the file directory to Project06 so that image finding could process.
    '''
    sideBySideList()