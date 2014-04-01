#Assignment 4
#Casey Gilray

from turtle import *
from time import *
def spiral(initialLength, turnAngle, multiplier);
"""Makes a spiral of beggining length, specified angle, and
multplierof the initial legnth """
   #Base case 1 pixel or less
   if initiallength <= 1:
       #pen up and return
      up()
      return
   else:
       #Pen down, draw side and turn, recurs with multiplier added.
      down()
      forward(initialLength)
      sleep(.75)
      left(turnangle)
      spiral((initialLength*multiplier,turnAngle,multiplier)
      return

def svTree(trunkLength,levels):
   """Makes a tree like figure of initial length and a number of
levels, each
   level half as long as the previous"""
   if levels <=0:
       return
   else:
       down()
       forward(trunklLength)
       left(30)
       sleep(.75)
       svTree((0.5*trunkLength),levels-1)
       back(trunklength)
       right(30)
       sleep(.75)
       svTree((0.5*trunkLength),levels-1)
       return

def snowflake(lengthSide,levels):
   '''Makes a kotch curve, with a base side of lengthside, and depth of
levels.'''
   if levels <= 0:
       forward(lengthSide)