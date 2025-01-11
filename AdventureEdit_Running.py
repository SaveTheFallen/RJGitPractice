# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 08:04:51 2023

@author: Ryang
"""
import json

def main():
    loaded = False
    mainLoop = True
    while(mainLoop):
        menuChoice = getMenuChoice()
        if menuChoice == "0":
            print("Quitting...")
            mainLoop = False
        if menuChoice == "1":
            game = getDefaultGame()
            loaded = True
        if menuChoice == "2":
            game = loadGame()
            loaded = True
        
        if menuChoice == "3":
            if(loaded):
                playGame(game)
            else:
                print("Please load a game before attempting to play.")
    '''Runs the main loop
Calls a menu
Sends control to other parts of the program'''
def getMenuChoice():
    menuLoop = True
    while(menuLoop):
        print('''
              0) exit
              1) load default game
              2) load a game file
              3) play the current game
              ''')
        menuChoice = input("What will you do? ")
        if menuChoice in ("0","1","2","3"):
            menuLoop = False
        else:
            print(f"""Invalid Input Detected: "{menuChoice}."
            Please enter a value between 0-3.""")
        return menuChoice 
def getDefaultGame():
    game = {
        "start": ("This is a test", "start over", "start", "quit", "quit")
        }
    print("Loading preset... ")
    return game 
    '''prints a menu of user options
repeats if input is invalid
returns a valid menu choice'''
def playGame(game):
    keepgoing = True
    currentNode = ("start")
    while(keepgoing):
        currentNode = playNode(game, currentNode)
        print("picking adventure route...")
        
        if currentNode == "quit":
            keepgoing = False
    '''plays the game
Keeps going until next node is "quit"'''
def playNode(game, currentNode):
    (desc, menuA, nodeA, menuB, nodeB) = game[currentNode]
    print(f'''
          {desc}
          1. {menuA}
          2. {menuB}
          ''')
    userChoice = input("Your Choice: ")
    if userChoice == "1":
        currentNode = nodeA
    elif userChoice == "2":
        currentNode = nodeB
    else:
        print("Invalid input. redirecting...")
        currentNode = currentNode
    
    return currentNode
    '''given the game data and a node,
plays out the node
returns the next node'''

    '''given the current game structure...
list all the current node names
get a node name
if that node exists
copy that node to newNode
otherwise...
create newNode with empty data
use editField() to allow user to edit each node
return the now edited newNode'''

def loadGame():
        print("Loading Game Data...")
        file = open("Quiz.dat", "r")
        game = json.load(file)
        return game
    
'''presume there is a data file named 'game.dat' in the current directory
open that file
load the data into the game object
return that game object'''
main()
