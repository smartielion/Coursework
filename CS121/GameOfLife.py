#Game of Life - Assignment 8
#Casey Gilray
#Last edit: 11/16/11
#This program shows the "game of life" developed by John Conway

from csplot import *
from time import *
from random import *

def createOneRow(n):
    #Creates a list of zeros to define a row
    r = []
    for col in range(n):
        r +=[0]
    return r

def createBoard(r,c):
    #Creates a 2d grid of zeros
    t = []
    for i in range(r):
        t += [createOneRow(c)]
    return t

def update1(b):
    '''takes an empty board and modifies it to turn on some of the cells'''
    width = len(b[0])
    height = len(b)
    
    for row in range(height):
        for col in range(width):
            if row == col:
                b[row][col] =1
            else:
                b[row][col] = 0
    return

def update2(b):
    '''takes an empty board and modifies it to turn all the cells except the boarder'''
    width = len(b[0])
    height = len(b)
    
    for row in range(height):
        for col in range(width):
            if (row==0) or (row == height-1):
                b[row][col]=0
            elif (col==0) or (col ==width-1):
                b[row][col] = 0
            else:
                b[row][col]=1
    return

            
def updateRandom(b):
    '''Takes an empty board and modifies to to turn on random cellls, but leave a dead boarder of cells'''
    width = len(b[0])
    height = len(b)
    
    for row in range(height):
        for col in range(width):
            if (row==0) or (row == height-1):
                b[row][col]=0
            elif (col==0) or (col ==width-1):
                b[row][col] = 0
            else:
                b[row][col]= choice([0,1])
    return

def updateReversed(b,newb):
    '''Takes an old board and reverses all the non-boarder cells into a new board'''
    width = len(b[0])
    height = len(b)
    
    for row in range(height):
        for col in range(width):
            if (row==0) or (row == height-1):
                newb[row][col]=0
            elif (col==0) or (col ==width-1):
                newb[row][col] = 0
            else:
                newb[row][col]= abs(b[row][col]-1)
    return

def life(width,height):
    '''This will show the game of life
    Keycodes:
    p: Pauses the game
    r: resumes from a pause
    q: Ends the game
    c: swaps colors
    b: Adds a set of random cells, used to continue playing without reseting the game
    1: Continues one generation and pauses
    '''
    B = createBoard(width,height)
    showAndClickInIdle(B)
    d = {0:'white', 1:'green'}
    pause = False
    while True:  #Run forever
        show(B,d)   #Show baord
        keyList = getKeysDown() #Gets keys pressed
        sleep(0.2)   #add wait time
        #adds pause and resume keys
        if 'p' in keyList: pause = True
        if 'r' in keyList: pause = False
        #adds quitting key
        if 'q' in keyList: break
        #Colorchanging key, picking a set elements of a dictionary to select new colors
        if 'c' in keyList: d= colorSwap()
            
        oldB = B   #Set oldB to B, to show change
        if pause == False:
            if '1' in keyList: pause = True
            B = createBoard(width,height) #Creates new board
            if 'b' in keyList:
                updateRandom(B)
            else: updateNextLife(oldB,B)
        
def updateNextLife(oldB,newB):
    '''Takes an old board and applys the game of life rules to it'''
    
    width = len(oldB[0])
    height = len(oldB)
    
    for row in range(height):
        for col in range(width):
            if (row==0) or (row == height-1):
                newB[row][col] = 0
            elif (col==0) or (col ==width-1):
                newB[row][col] = 0
            else:
                #Lonely cell, dies
                if numNeighbor(oldB,row,col) < 2: newB[row][col] =  0
                #Crowded cell, dies
                if numNeighbor(oldB,row,col) > 3: newB[row][col] = 0
                #three neighbors, comes to life
                if numNeighbor(oldB,row,col) == 3: newB[row][col] = 1
    return
    
def numNeighbor(oldB,row,col):
    '''Counts the number of live neihbors a specific cell has'''
    neighbors = 0
    for n in range(3):
        for m in range(3):
            #Do not count self
            if not ((m==1) and (n ==1)):
                #If a neighbor is alive, count it
                if oldB[(row+n-1)][(col+m-1)] == 1:
                    neighbors += 1
    return neighbors
            

def colorSwap():
    #Chooses from the list of color sets.
    c1 = {0:'red',1:'blue'}
    c2 = {0:'white',1:'green'}
    c3 = {0:'black',1:'blue'}
    c4 = {0:'purple',1:'pink'}
    c5 = {0:'brown',1:'orange'}
    return choice([c1,c2,c3,c4,c5])
    