#Assignment 5
#Parts 0&1
#Casey Gilray
#Last edited: 10/3/11

#What data will the program need to keep track of?
#Positions of "lights", on/off for each light, surrounding lights to the one clicked
#As well as where the user clicks to change cells

#What will my program need to do with this data?
#Alter state of the lights from 0/1 and back based on where the user clicks

import time
from random import *
import sys
sys.setrecursionlimit(100000) #sets recusion limit of 100000


def runGenerations(L):
    '''Runs evolve and recurses
    '''
    print L # prints the list
    if allOnes(L) == True:
        return 0
    else:
        time.sleep(0.1) # waits for half a second
        newL = evolve(L) #Get a new evolved list
    return 1 + runGenerations(newL) #Recursion

    
    
    
def evolve( L ):
    """Evolve takes in a list of intergers, L,
    and returns a new list of integers considered to be the next generation
    """
    N = len(L) #N holds the size of L
    return [ setNewElement( L, i ) for i in range( N ) ]



def setNewElement( L, i, x=0 ):
    """setNewElement returns the new lists ith element
    input L: any list of integers
    input i: the index of the new element to return
    input x: an extra optional input for future use
    """
    return L[i] +1

'''
Run generations prints the current list, then makes a new one using
the evolve function.
The evolve function takes the input list and makes a list of the same length,
changing each element based on the parameters in setNewelement
'''


def setNewElement( L, i, x=0 ):
    """setNewElement returns the new lists ith element
    input L: any list of integers
    input i: the index of the new element to return
    input x: an extra optional input for future use"""
    return L[i] * 2

def setNewElement( L, i, x=0 ):
    """setNewElement returns the new lists ith element
    input L: any list of integers
    input i: the index of the new element to return
    input x: an extra optional input for future use"""
    return L[i] ** 2

def setNewElement( L, i, x=0 ):
    """setNewElement returns the new lists ith element
    input L: any list of integers
    input i: the index of the new element to return
    input x: an extra optional input for future use"""
    return L[i-1]

def setNewElement( L, i, x=0 ):
    """setNewElement returns the new lists ith element
    input L: any list of integers
    input i: the index of the new element to return
    input x: an extra optional input for future use"""
    if i == 5:
        return L[0]
    else:
        return L[i+1]
    

def setNewElement( L, i, x=0 ):
    """setNewElement returns the new lists ith element
    input L: any list of integers
    input i: the index of the new element to return
    input x: an extra optional input for future use"""
    return choice([0,1])
    
def allOnes(L):
    '''Checks each element to see if it is a one, returns false if not a 1
    '''
    if len(L) == numTimes(1,L):
        return True
    else:
        return False
    
def numTimes(x,L):
    '''Checks how many times x appears in l'''
    return sum([x==i for i in L])

print runGenerations([1,2,3,4])