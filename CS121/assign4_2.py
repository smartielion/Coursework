#Assignment 4
#Casey Gilray

from turtle import *
from time import *

def spiral(initialLength,turnAngle,multiplier):
    '''This function makes a spiral of initial side length, a turn angle(to the left) and a side multiplier)'''
    #base case, one pixel length
    if initialLength <= 1:
        #pen up and return
        done()
        return
    else:
        #pen down, draw side and recurse
        down()
        forward(initialLength)
        left(turnAngle)
        sleep(.75)
        spiral((initialLength*multiplier),turnAngle,multiplier)
        return
    

    
#*********************************************************************
        
def svTree(trunk,levels):
    '''This funtion makes a tree shape of initial length and a number of "splits"'''
    #base case, levels <1 draw line
    if levels <= 1:
        down()
        #base case, draws single trunk with no continued split
        forward(trunk)
        backward(trunk)
        return
    else:
        #pen down, forward trunk length, turn and recurse left)
        down()
        forward(trunk)
        left(20)
        sleep(.25)
        svTree((trunk*.7),(levels-1))
        #Turn to recurse right
        sleep(.25)
        right(40)
        svTree((trunk*.7),(levels-1))
        #return to original state
        left(20)
        backward(trunk)    
        return
        


    
#***********************************************************************


def snowflake(length,levels):
    '''Makes a kotch curve of base length, and number of levels'''
    #setup for making curve
    down()
    left(30)
    snowflakeside(length,levels)
    right(120)
    snowflakeside(length,levels)
    right(120)
    snowflakeside(length,levels)
    right(120)
    done()
    
    
    
def snowflakeside(lengthside,levels):
    '''Makes a single iteration of a kotch curve side with a set length'''
    down()
    if levels == 0:
        #draws the segment
        forward(lengthside)
        sleep(.75)
        return
    else:
        #thirds the length of the side and recurses to make the kotch side.
        lengthside = lengthside*0.333
        snowflakeside(lengthside,levels-1)
        left(60)
        snowflakeside(lengthside,levels-1)
        right(120)
        snowflakeside(lengthside,levels-1)
        left(60)
        snowflakeside(lengthside,levels-1)
        return

        