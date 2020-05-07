# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:49:41 2020
Rev 1.6.3
@author: Ethan
This superclass is where the two options given to the user have been built
"""
import GridWork
import matplotlib.pyplot as plt
import random
import time
import math
import GridWork as grid
import backend
class FPB():
    #Takes in the width, height and number of bots to use
    def __init__(self,myX,myY,bots):
        self.x = myX
        self.y = myY
        self.b = bots
        self.cHit = [] #list of successful visits
        self.cAtt = [] #list of attempted coordinates
        self.cDup = [] #list of duplicate coordinates
        self.numDup = 0 #Number of duplicate hits
        self.spaces = 1 #number of spaces bots can move in a direction
    #The function for the first option that determines how much space can be
    #covered in a given amount of time, 't'
    #Runs the movement of the bots
    def bots(self,t,p):
        x = 0 
        y = 0
        #Creates a grid for bot placement
        myGrid = grid.GridPlotting(self.x,self.y)
        tiles = myGrid.get_num_tiles()
        oneTile = (1/tiles)*100
        tilesCovered = 0
        runTime = time.time()# Starts the timer
        #The following code will place the bots as long as there is time
        #as specified by the user and there are tiles left to cover 
        #or if the percentage covered is less than what the user specified
        while(tilesCovered < 100 and time.time()<=runTime+t or tilesCovered<p): 
            #builds the grid for the bot placement                                 
            plt.figure()
            plt.ion()  
            myGrid.setup_grid() 
            num = 1
            #The following code places the number of bots determined by
            #the user, it will stop placing bots if 100% tile coverage
            #is reached
            while (num <= self.b and tilesCovered < 100):   
                #If there have been no bots placed, start them in a random
                #spot. Otherwise move the bot one tile in a random
                #direction
                if(x == 0 and y == 0):
                    x = random.randint(1,self.x)
                    y = random.randint(1,self.y)
                else:                    
                    moveBots = backend.FPB(self.x,self.y,self.b)
                    spaces = moveBots.moveSpace(x,y)
                    x = spaces[0]
                    y = spaces[1]                    
                placeBots = grid.MoveBots(x,y)   
                # Records all tiles that have been attempted
                self.cAtt.append((x,y))
                # Checks if current tile has been visited.
                #if it has, it skips it and adds to the number of duplicats
                if((x,y) not in self.cHit):              
                    placeBots.plotBots()
                    self.cHit.append((x,y))
                    num += 1
                    hits = len(self.cHit)
                    #Catches when there are more bots than tiles left to visit
                    remTiles = tiles - hits 
                    if (self.b >= remTiles and self.b != 1): 
                    #If there are too many bots, reduce them by 1
                        self.b -= 1                                                                          
                else:
                    #Adds duplicate coordinates to a list and keeps track 
                    #of how many there are
                    self.cDup.append((x,y))
                    self.numDup = len(self.cDup)  
            plt.show()
            #The following code updates how much of the grid has been covered
            #and where the bots have been
            tilesCovered = math.ceil(hits*oneTile)            
            plt.figure()
            plt.ion()
            myGrid = grid.GridPlotting(self.x,self.y)  
            myGrid.setup_grid() 
            increment = 0
            while (increment < len(self.cHit)):            
                hitSpots = grid.MarkSpace(self.cHit[increment][0],
                                          self.cHit[increment][1])
                hitSpots.fillBoxes()
                increment += 1
            #Shows the current grid and pauses to give time for "bot movement"
            plt.show()
            plt.pause(1)
        #After completion, sets how much was completed
        self.percentage = tilesCovered 
        #Calculates the amount of time it took 
        takenTime = time.time()-runTime
        self.time = takenTime
    #Randomizes the direction the tile can move
    def moveSpace(self,a,b):
        decision = random.randint(1,7)
        if (decision == 1 and a > 1):
            a = a- self.spaces
        elif(decision == 2 and b > 1):
            b = b- self.spaces
        elif (decision == 3 and a < self.x):
            a = a+ self.spaces
        elif (decision == 4 and b < self.y):
            b = b+ self.spaces
        elif (decision == 5 and a > 1 and b > 1 and a < self.x and b < self.y):
            a = a - self.spaces
            b = b - self.spaces
        elif (decision == 6 and b > 1 and a < self.x):
            a = a + self.spaces
            b = b - self.spaces
        elif (decision == 7 and a > 1 and b < self.y):
            a = a - self.spaces
            b = b + self.spaces
        elif (decision == 8 and a < self.x and b < self.y):
            a = a + self.spaces
            b = b + self.spaces
        return a,b
    #Returns percentage covered
    def get_percentage(self):
        return self.percentage
    #Returns time taken
    def get_time(self):
        return self.time
    #Returns the number of duplicates attempted
    def get_Num_Duplicate(self):
        return self.numDup
    #Return total spaces attempted
    def get_Attempted(self):
        return self.cAtt
    #Returns how many tiles a bot is allowed to move from original position
    def get_Spaces_Can_Move(self):
        return self.spaces