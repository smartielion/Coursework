#Casey Gilray
#Assignment 7
#Last Edited: 10/26/11

from math import *
from bmp import *

#Coordinate list(for zooming in on function mSet
#coordinateList =[-0.8,-0.6,-0.1,0.1]
#Original coordinate list
coordinateList = [-2.0,1.0,-1.0,1.0]

def inMSet(c,n):
    '''Checks a complex number to see if it is in the Madlebrot set.
    Will use up to n itterations'''
    index = 0
    for i in range(n):
        index = (index**2) + c
        if abs(index) >= 2.0: return False
    return True

def testImage():
    '''A function to emonstate how to create and save a bitmap file'''
    width = 200
    height = 200
    image = BitMap(width,height)
    
    #Create a loop in order to draw some pixels
    
    for col in range(width):
        if col % 10 == 0: print 'Col is', col
        for row in range(height):
            if col % 10 ==0 and row %10 == 0:
                image.plotPoint(col,row)
    #looped through every pixel
    #Write to save file
    image.saveFile("test.bmp")
    
    '''If when changing the and to an or, it will instead make vertical and horizonal bars'''

def scale(pix,pixNum,floatMin,floatMax):
    '''Returns a scaled float value that corresponds with our dataset'''
    #Get the scale of the pixel on the frame
    colscale = float(pix)/pixNum
    #Get the distance between real min and max
    floatscale = floatMax - floatMin
    #Scale to get real location of pixel by adding real value to the "zero", Floatmin
    scaledPix = floatMin+(colscale*floatscale) 
    return scaledPix

def mSet(width,coordinateList):
    '''Shows the mandelbrot set of a certain width of pixels scaled to fit the coordinate list'''
    #Magic Numbers
    numItterations = 50 #We assume max divergence of 25 steps.
    #Coordinate "Window"
    XMin = coordinateList[0]
    XMax = coordinateList[1]
    YMin = coordinateList[2]
    YMax = coordinateList[3]
    #Calculate height based on scaled of the window
    height = int(width*((YMax-YMin)/(XMax - XMin)))
    #Create an image
    image = BitMap(width,height)
    #Get scaled X and Y values
    for col in range(width):
        x = scale(col,width,XMin,XMax)
        for row in range(height):
            y= scale(row,height,YMin,YMax) 
            #If the scaled x,y coord is in the mandelbrot set, plot a point
            if inMSet(x+(y*1j),numItterations): image.plotPoint(col,row)
    #looped through every pixel
    #Write to save file
    image.saveFile("baseset.bmp")
    
def mSetColor(width,coordinateList):
    '''Shows a mandelbrot set in color of width in pixels scaled to set coordinates'''
    #Magic Numbers
    numItterations = 256 #We assume max divergence of 25 steps.
    #Coordinate "Window"
    XMin = coordinateList[0]
    XMax = coordinateList[1]
    YMin = coordinateList[2]
    YMax = coordinateList[3]
    #Calculate height based on scaled of the window
    height = int(width*((YMax-YMin)/(XMax - XMin)))
    #Create an image
    image = BitMap(width,height)
    #Get scaled X and Y values
    for col in range(width):
        x = scale(col,width,XMin,XMax)
        for row in range(height):
            y= scale(row,height,YMin,YMax) 
            #If the scaled x,y coord is in the mandelbrot set, plot a point
            if inMSet(x+(y*1j),numItterations):
                image.setPenColor(Color.BLACK)
                image.plotPoint(col,row)
            else:
                diverge = divergeCount(x+(y*1j),numItterations)
                image.setPenColor(divColor(diverge))
                image.plotPoint(col,row)
    #looped through every pixel
    #Write to save file
    image.saveFile("colorSet.bmp")

def divergeCount(c,n):
    '''Checks a complex number to see if it is in the Madlebrot set.
    Will use up to n itterations, returns value for divergence.'''
    index = 0
    for i in range(n):
        index = (index**2) + c
        if abs(index) >= 2.0: return i
    return

def divColor(n):
    '''returns a color representing the degree of divergence. (blue = low divergence, red is fast)'''
    #Itterations is less than or equal to 1/3 the total tries
    if (0 <= n <= 5):
        return Color((20*n),0,0)
    elif (5 < n <= 20):
        return Color(0,(10*n),0)
    elif (n > 20):
        return Color(0,0,(5*n))