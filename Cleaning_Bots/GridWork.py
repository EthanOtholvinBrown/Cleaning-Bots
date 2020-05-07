# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:14:37 2020
Rev 1.2
@author: Ethan
This super class is for building the grid and determining where the bots are
and where they have been.
"""
import matplotlib.pyplot as plt
# Class for building the grid based on the user's specifications
class GridPlotting():
    #Takes in the width and height of the grid to be built
    def __init__(self,dimx,dimy):        
        self.xAxis = dimx
        self.yAxis = dimy        
    def setup_grid(self):
        x=list()
        y=list()
        # Adds tiles for the width of the grid
        for num in range(self.xAxis):
            x.append(num)
        # Adds tiles for the height of the grid
        for num in range(self.yAxis):
            y.append(num)            
        plt.grid()# Creates the actual grid
        plt.xlim(xmin=0, xmax=self.xAxis)# Sets the width
        plt.ylim(ymin=0, ymax=self.yAxis)# Sets the height
        plt.xticks(x)# Creates the width markers
        plt.yticks(y)# Creates the height markers
        #Calculates how many tiles there are in total
    # Returns to call how many tiles there are
    def get_num_tiles(self):
        self.numOfTiles = self.xAxis * self.yAxis
        return self.numOfTiles  
#A class for determining the constantly updating bot location or "Movement" 
# of the bots
class MoveBots():
    def __init__(self,x,y):
        self.xc = x
        self.yc = y
    #Main function for bot "movement"
    #Visited tiles are represented by a diagonall slash through the tile
    def plotBots(self):
        self.particularBox_xCoord = [(self.xc-1),(self.xc)]
        self.particularBox_yCoord = [(self.yc-1),(self.yc)]
        plt.plot(self.particularBox_xCoord, self.particularBox_yCoord,'blue')
    #Returns Height and width of grid to call
    def get_x(self):
        return self.xc
    def get_y(self):
        return self.yc
#A class for marking where the bots have already visited, works the same as 
#MoveBots
class MarkSpace():
    def __init__(self,x,y):
        self.beenB = x
        self.beenA = y
    def fillBoxes(self):
        self.particularBox_xCoordFill = [(self.beenB-1),(self.beenB)]
        self.particularBox_yCoordFill = [(self.beenA-1), (self.beenA)]
        plt.plot(self.particularBox_xCoordFill, 
                 self.particularBox_yCoordFill,'red')