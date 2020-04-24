#!python3

import numpy as np
import matplotlib.pyplot as plt
import sys

"""
Usage:
    python main.py [-s N] [-t T] [-i INIT]
        -s : size of the (square) board (integer only)
        -t : time period of simulation
        -i : initial state, the available options are:
                - block
                - glider
                - blinker
    Example:
    python main.py -s 10 -t 10 -i GLIDER
"""

"""
TODO:
    * Change from plotting subplots to making animations (and saving them, if the option is chosen)
"""

def setConditions(grid,opt="block"):
    dummy = grid.copy()
    # creating a block
    if opt == "block":
        dummy[2,2] = 1
        dummy[2,3] = 1
        dummy[3,2] = 1
        dummy[3,3] = 1
    elif opt == "blinker":
        dummy[2,1] = 1
        dummy[2,2] = 1
        dummy[2,3] = 1
    elif opt == "glider":
        dummy[2,1] = 1
        dummy[3,2] = 1
        dummy[3,3] = 1
        dummy[2,3] = 1
        dummy[1,3] = 1
    else:
        print("That has not been implemented yet. Reverting to BLOCK")
        dummy = setConditions(grid)

    grid = dummy.copy()
    return grid

def countNeighbors(array, x, y):
    # a function that, given an index x,y counts how many neighbours it has
    hors = np.array([x-1,x,x+1])
    vers = np.array([y-1,y,y+1])

    # 0 borders
    hors = hors[hors>=0]
    vers = vers[vers>=0]

    # other edge border
    hors = hors[hors<array.shape[0]]
    vers = vers[vers<array.shape[1]]

    s = np.sum(array[hors][:,vers])
    s -= array[x][y]
    #print(f"({x},{y}) -> {s}")
    return s

args = sys.argv[1:]
argDict = dict()
i = 0

while i < len(args):
    argDict[args[i]] = args[i+1]
    if i+2 >= len(args):
        break
    else:
        i+=2

size = int(argDict["-s"])
time = int(argDict["-t"])
init = argDict["-i"].lower()

if size < 5:
    size = 5
if time < 2:
    time = 2



# setting up a grid
grid = np.zeros((size,size))

# setting initial conditions
grid = setConditions(grid,opt=init)

# Setting time period of simulation
T = time

fig, ax = plt.subplots(T,1)


t = 0
while t < T:
    y = np.zeros(grid.shape) # creating a duplicate
    # setting lives and deaths
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            nbors = countNeighbors(grid,i,j)
            if grid[i][j] == 1: # if alive
                if nbors < 2:
                    y[i][j] = 0 # underpopulation
                elif nbors > 3:
                    y[i][j] = 0 # overpopulation
                elif nbors == 2 or nbors == 3:
                    y[i][j] = 1
            elif grid[i][j] == 0: # if dead
                if nbors == 3:
                    y[i][j] = 1
                else:
                    y[i][j] = 0
    
    # plotting
    ax[t].imshow(grid)
            

    grid = y # updating the grid
    t+=1


plt.show()