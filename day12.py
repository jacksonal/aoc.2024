from collections import Counter
from util import getLinesFromFile

def countPerimeter(pos, grid):
    i, j = pos
    veg = grid[i][j][0]
    perimeter = 0
    if i > 0:
        perimeter += 1 if grid[i-1][j][0] != veg else 0
    else:
        perimeter += 1
    if i < len(grid)-1:
        perimeter += 1 if grid[i+1][j][0] != veg else 0
    else:
        perimeter += 1
    if j > 0:
        perimeter += 1 if grid[i][j-1][0] != veg else 0
    else:
        perimeter += 1
    if j < len(grid[0])-1:
        perimeter += 1 if grid[i][j+1][0] != veg else 0
    else:
        perimeter += 1
    return perimeter

def getPlot(pos, veg, grid): # returns a list of all the positions in the plot
    plot = [pos]
    grid[pos[0]][pos[1]] = (grid[pos[0]][pos[1]][0], True) # mark visited
    plot.extend(getPlot((pos[0]-1, pos[1]), veg, grid) if pos[0] > 0 and not grid[pos[0]-1][pos[1]][1] and grid[pos[0]-1][pos[1]][0] == veg else [])
    plot.extend(getPlot((pos[0]+1, pos[1]), veg, grid) if pos[0] < len(grid)-1 and not grid[pos[0]+1][pos[1]][1] and grid[pos[0]+1][pos[1]][0] == veg else [])
    plot.extend(getPlot((pos[0], pos[1]-1), veg, grid) if pos[1] > 0 and not grid[pos[0]][pos[1]-1][1] and grid[pos[0]][pos[1]-1][0] == veg else [])
    plot.extend(getPlot((pos[0], pos[1]+1), veg, grid) if pos[1] < len(grid[0])-1 and not grid[pos[0]][pos[1]+1][1] and grid[pos[0]][pos[1]+1][0] == veg else [])
    return plot

def countSides(plot):
    # walk the perimeter of the plot and count the number of sides
    sides = 0



grid =[]
for line in getLinesFromFile('test.txt'):
    gridline = []
    for c in line:
        gridline.append((c, False))
    grid.append(gridline)
print(grid)
plots = []
for i, line in enumerate(grid):
    for j, c in enumerate(line):
        if not c[1]:
            plots.append(getPlot((i, j), c[0],grid))
price = 0
for p in plots:
    perimeter = sum(countPerimeter(pos, grid) for pos in p)
    print(len(p),perimeter, grid[p[0][0]][p[0][1]][0], p)
    price += perimeter * len(p)
print(price)
for p in plots:
    sides = countSides(p)


