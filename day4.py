from util import buildGraph

def checkEast(node):
    try:
        ret = node.value == 'X' and node.east.value == 'M' and node.east.east.value == 'A' and node.east.east.east.value == 'S'
        if ret:
            node.visited = node.east.visited = node.east.east.visited = node.east.east.east.visited = True
        return ret
    except:
        return False

def checkWest(node):
    try:
        ret = node.value == 'X' and node.west.value == 'M' and node.west.west.value == 'A' and node.west.west.west.value == 'S'
        if ret:
            node.visited = node.west.visited = node.west.west.visited = node.west.west.west.visited = True
        return ret
    except:
        return False

def checkNorth(node):
    try:
        ret = node.value == 'X' and node.north.value == 'M' and node.north.north.value == 'A' and node.north.north.north.value == 'S'
        if ret:
            node.visited = node.north.visited = node.north.north.visited = node.north.north.north.visited = True
        return ret
    except:
        return False

def checkSouth(node):
    try:
        ret = node.value == 'X' and node.south.value == 'M' and node.south.south.value == 'A' and node.south.south.south.value == 'S'
        if ret:
            node.visited = node.south.visited = node.south.south.visited = node.south.south.south.visited = True
        return ret
    except:
        return False

def checkNorthEast(node):
    try:
        ret = node.value == 'X' and node.north_east.value == 'M' and node.north_east.north_east.value == 'A' and node.north_east.north_east.north_east.value == 'S'
        if ret:
            node.visited = node.north_east.visited = node.north_east.north_east.visited = node.north_east.north_east.north_east.visited = True
        return ret
    except:
        return False

def checkNorthWest(node):
    try:
        ret = node.value == 'X' and node.north_west.value == 'M' and node.north_west.north_west.value == 'A' and node.north_west.north_west.north_west.value == 'S'
        if ret:
            node.visited = node.north_west.visited = node.north_west.north_west.visited = node.north_west.north_west.north_west.visited = True
        return ret
    except:
        return False

def checkSouthEast(node):
    try:
        ret = node.value == 'X' and node.south_east.value == 'M' and node.south_east.south_east.value == 'A' and node.south_east.south_east.south_east.value == 'S'
        if ret:
            node.visited = node.south_east.visited = node.south_east.south_east.visited = node.south_east.south_east.south_east.visited = True
        return ret
    except:
        return False

def checkSouthWest(node):
    try:
        ret = node.value == 'X' and node.south_west.value == 'M' and node.south_west.south_west.value == 'A' and node.south_west.south_west.south_west.value == 'S'
        if ret:
            node.visited = node.south_west.visited = node.south_west.south_west.visited = node.south_west.south_west.south_west.visited = True
        return ret
    except:
        return False

graph = buildGraph('input.txt') 
xmasCount = 0
for i in range(len(graph)):
  #print('row', i)
  for j in range(len(graph[i])):
    #print('col', j)
    if j < len(graph[i])-3:
        xmasCount = (xmasCount + 1) if checkEast(graph[i][j]) else xmasCount
    if j < len(graph[i])-3 and i < len(graph)-3:
        xmasCount = (xmasCount + 1) if checkSouthEast(graph[i][j]) else xmasCount
    if i < len(graph)-3:
        xmasCount = (xmasCount + 1) if checkSouth(graph[i][j]) else xmasCount
    if j > 2 and i < len(graph)-3:
        xmasCount = (xmasCount + 1) if checkSouthWest(graph[i][j]) else xmasCount
    if j > 2:
        xmasCount = (xmasCount + 1) if checkWest(graph[i][j]) else xmasCount
    if j > 2 and i > 2:
        xmasCount = (xmasCount + 1) if checkNorthWest(graph[i][j]) else xmasCount
    if i > 2:
        xmasCount = (xmasCount + 1) if checkNorth(graph[i][j]) else xmasCount
    if j < len(graph[i])-3 and i > 2:
        xmasCount = (xmasCount + 1) if checkNorthEast(graph[i][j]) else xmasCount

print(xmasCount)
for i in range(len(graph)):
  row = ''
  for j in range(len(graph[i])):
      row = row + graph[i][j].value if graph[i][j].visited else row + '.'
  #print(row)
          