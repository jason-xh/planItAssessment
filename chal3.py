### Task ###
"""
Challenge 3:
Given two points on a grid, draw a line between them and print it as ASCII art
"""

### Functions ###
# grid print function
def prettyPrintGrid(grid):
    for line in grid:
        print(''.join(line))

# grid initialisation function
# returns 2D list grid of size width, height initialised with '.'
def initialiseGrid(width, height):
    grid = [['.' for i in range(width+1)] for j in range(height+1)]
    return grid

### Main Code ###
# input
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

# calculate width and height of grid
width = max(x1, x2)
height = max(y1, y2)

# initialise grid and add points
# NOTE: assuming grid (0, 0) is in the bottom left, we must subtract y value from the height
# everytime we index the 2D array to arrive at the correct point 
grid = initialiseGrid(width, height)
grid[height-y1][x1] = "1"
grid[height-y2][x2] = "2"


# calculating vertical and horizontal distances between points
# negative numbers are fine as we use addition/subtraction later
vertDist = y2 - y1
horiDist = x2 - x1 

# calculating increment distance
segmentLen = max(abs(vertDist), abs(horiDist)) # segment length must be positive
segmentHoriInc = horiDist/segmentLen
segmentVertInc = vertDist/segmentLen

# variables to track the line
linex = x1
liney = y1

# fill in the line and print grid
for i in range(0, segmentLen-1): # must subtract 1 so that we don't replace the second point with an x
    linex += segmentHoriInc
    liney += segmentVertInc
    grid[height-round(liney)][round(linex)] = 'x'
prettyPrintGrid(grid)

# should run in O(n)
# originally considered utilising gradient formula or general form of a line
# but I think the complexity may be worse than this current messier solution
