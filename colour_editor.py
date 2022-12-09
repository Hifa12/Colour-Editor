import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.pylab as plt
import keyboard
import imageio.v2 as imageio
import pandas as pd
import os.path

#Remove images that would be present if program was run previously
def remfile(file):
    if os.path.exists(file):
        os.remove(file)
remfile('r_result.jpg')
remfile('g_result.jpg')
remfile('b_result.jpg')

#Load the original image
img = imageio.imread('colours.jpg')
plt.imshow(img)

#Read colors.csv with pandas and giving columns names
#colors.csv file retrieved from tutorial: https://data-flair.training/blogs/project-in-python-colour-detection/
columnnames =["colour","colour_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=columnnames, header=None)

#Define a function for getting colour name using colors.csv
def ColourName(R,G,B):
    minimum = 10000
    for a in range(len(csv)):
        distance = abs(R-int(csv.loc[a,"R"])) + abs(G-int(csv.loc[a,"G"])) + abs(B-int(csv.loc[a,"B"]))
        if(distance<=minimum):
            minimum = distance
            colourname = csv.loc[a,"colour_name"]
    return colourname

#Define a function so RGB values and colour name printed for point where clicked on image
def onmouseclick(event):
    rgbvals = event.inaxes.get_images()[0].get_cursor_data(event)
    colname = ColourName(rgbvals[0], rgbvals[1], rgbvals[2])
    print("RGB values of original image:",rgbvals)
    print("Colour name:",colname)
    #Define a function so that RGB values are changed based on key pressed and
    #new image is saved with changed RGB values
    def onkeypress(event):
        if event.key == 'r':
            img = imageio.imread('colours.jpg')
            img[ : , : , 2] = 255 #R is set at full intensity
            cv2.imwrite('r_result.jpg',img)
        if event.key == 'g':
            img = imageio.imread('colours.jpg')
            img[ : , : , 1] = 255 #G is set at full intensity
            cv2.imwrite('g_result.jpg',img)
        if event.key == 'b':
            img = imageio.imread('colours.jpg')
            img[ : , : , 0] = 255 #B is set at full intensity
            cv2.imwrite('b_result.jpg',img)
    plt.gcf().canvas.mpl_connect('key_press_event', onkeypress)
plt.gcf().canvas.mpl_connect('button_press_event', onmouseclick)
plt.title('Original Image')
plt.show(block=True)

#Define function so RGB values and colours printed for point where clicked on new image
def newimclick(image, maxRGB):
    nimg = imageio.imread(image)
    plt.figure(figsize = (5,5))
    plt.imshow(nimg)
    def onmouseclick(event):
        rgbvals = event.inaxes.get_images()[0].get_cursor_data(event)
        colname = ColourName(rgbvals[0], rgbvals[1], rgbvals[2])
        print("RGB values when " + maxRGB + " is at full intensity:",rgbvals)
        print("Colour name:",colname)
    plt.gcf().canvas.mpl_connect('button_press_event', onmouseclick)
    plt.title("Image With " + maxRGB + " at Full Intensity")
    plt.show(block=True)

#load new image with RGB values changed
try:
    newimclick('r_result.jpg', "R")
except:
    istr = -1

try:
    newimclick('g_result.jpg', "G")
except:
    istr = -1

try:
    newimclick('b_result.jpg', "B")
except:
    istr = -1
