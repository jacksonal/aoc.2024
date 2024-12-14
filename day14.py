from util import getLinesFromFile
from collections import Counter
import re
def parseBot(line):
    return list(map(lambda x: list(map(int, x.split(','))), re.findall(r'-?\d+,-?\d+',line)))

def updatePos(bot, ticks, w=101, h=103):
    pos, velocity = bot
    return ((pos[0] + velocity[0]*ticks)%w,(pos[1] + velocity[1]*ticks)%h)

def getQuadrant(pos, w=101, h=103):
    x,y = pos
    midw = w//2
    midh = h//2
    if x < midw:
        if y < midh:
            return 1 
        elif y > midh:
            return 3
    if x > midw:
        if y < midh:
            return 2 
        elif y > midh:
            return 4
def printgrid(grid, posList):
    posSet = set(map(tuple,posList))
    
    for i, row in enumerate(grid):
        rowstr = ''
        for j, c in enumerate(row):
            quad = getQuadrant((j,i), 11,7)
            rowstr += '.' if not quad else str(quad)
            #rowstr += '1' if (j,i) in posSet else '.'
        print(rowstr)

def printGridToFile(grid, posList, i):
    posSet = set(map(tuple,posList))
    with open(f'images\\{i}.txt','w') as f:
        for i, row in enumerate(grid):
            rowstr = ''
            for j, c in enumerate(row):
                quad = getQuadrant((j,i), 11,7)
                #rowstr += '.' if not quad else str(quad)
                rowstr += '#' if (j,i) in posSet else '.'
            f.write(rowstr+'\n')

# space is 101 wide, 103 tall
row = ['.'] * 101
space = []
for i in range(103):
    space.append(row)

ticks = 100
w = 101
h = 103
row = ['.'] * w
space = []
for i in range(h):
    space.append(row)

botPos = [updatePos(bot, 100,w,h) for bot in [parseBot(line) for line in getLinesFromFile('input.txt')]]
#print(botPos)
#printgrid(space, botPos)
botQuadrants = [getQuadrant(pos,w,h) for pos in botPos]

quadCounts = Counter(botQuadrants)
print(quadCounts)
print(quadCounts[1]*quadCounts[2]*quadCounts[3]*quadCounts[4])

bots = [parseBot(line) for line in getLinesFromFile('input.txt')]
for i in range(1000):
    botPos = [updatePos(bot, i,w,h) for bot in bots]
    printGridToFile(space, botPos, i)