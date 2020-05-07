# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 12:25:13 2020
Rev. 1.4
@author: Ethan
"""

import backend    
def main():    
    userChoice = 'null'
    while(userChoice != 'q'):
        print("Welcome to the bot cleaning program!\n")
        print("This program will tell you one of two things: ")
        print("A) How many tiles in a room can be reached by the",
             "bots in a time you decide.")
        print("B) How long it takes to reach a percentage",
             "of tiles you decide.")
        print("Let's begin!\n")
        while True:
            try:
                xAxis = int(input("Enter how many tiles make up the width: "))
                break
            except ValueError:
                print("Please enter a number.")
        while True:
            try:
                yAxis = int(input("Enter how many tiles make up the height: "))
                break
            except ValueError:
                print("Please enter a number.")
        while True:
            try:
                numBots = int(input("Enter the number of robots you want to use: "))
                break
            except ValueError:
                print("Please enter an integer.")
        botMove = backend.FPB(xAxis,yAxis,numBots)        
        while(userChoice != 'a' or userChoice != 'b' or userChoice != 'q'):
            print("Enter 'a' for the first option or 'b' for the second",
                  "['q' to return to main menu]:")
            userChoice = str(input())
            if (userChoice == 'a'):
                print("You've chosen A - Coverage based on time\n")
                while True:
                    try:
                        userT = int(input("Enter the time you want the bots to run for: "))
                        break
                    except ValueError:
                        print("Please enter a number.")
                botMove.bots(userT,0) 
                print("Percentage covered: ",
                      format(botMove.get_percentage(),'.2f'),'%')
                break
            elif(userChoice == 'b'):
                print("You've chosen B - Time taken based on percentage")
                while True:
                    try:
                        userP = int(input("Enter the percentage you want to cover: "))
                        break
                    except ValueError:
                        print("Please enter a number.")
                botMove.bots(0,userP)
                print("Time it took: ",
                      format(botMove.get_time(),'.2f')," seconds")
                break
            elif (userChoice == 'q'):
                break
            else:
                print("Invalid choice.")
        print("Returning to main menu...[Any key to continue or 'q' to exit] ")
        userChoice = str(input())
    print("Have a wonderful day!")
main()    