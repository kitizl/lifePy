#!python3

import numpy as np
import matplotlib.pyplot as plt

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

grid = np.zeros((10,10))

grid = setConditions(grid,opt="glider")

T = 15

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