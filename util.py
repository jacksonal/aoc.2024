def getFileContents(path):
  with open(path) as f:
    content = f.read()
    return content

def getLinesFromFile(path):
  with open(path) as f:
    lines = f.readlines()
    return [l.rstrip('\n') for l in lines]
  
def getRowsAsIntLists(path):
  with open(path) as f:
    lines = f.readlines()
    return [[int(c) for c in l.rstrip('\n')] for l in lines]

def getRowsAsLists(path):
  with open(path) as f:
    lines = f.readlines()
    return [[c for c in l.rstrip('\n').split()] for l in lines]

def getColsAsIntLists(path):
  with open(path) as f:
    lines = f.readlines()
    return [[int(l[i]) for l in lines] for i in range(len(lines[0])-1)]

def getColsAsLists(path):
  with open(path) as f:
    lines = f.readlines()
    return [[l[i] for l in lines] for i in range(len(lines[0])-1)]
  
def getColsAsStrings(path):
  with open(path) as f:
    lines = f.readlines()
    return [''.join([l[i] for l in lines]) for i in range(len(lines[0])-1)]

class Node:
  north = None
  north_east = None
  north_west = None
  south = None
  south_east = None
  south_west = None
  east = None
  west = None
  visited = False
  def __init__(self, value):
    self.value = value

def buildGraph(path):
  lines = getLinesFromFile(path)
  nodes = []
  for i in range(len(lines)):
    nodes.append([Node(lines[i][j]) for j in range(len(lines[i]))])
  for i in range(len(lines)):
    for j in range(len(lines[i])):
      if i > 0:
        nodes[i][j].north = nodes[i-1][j]
      if i > 0 and j < len(lines[i])-2:
        nodes[i][j].north_east = nodes[i-1][j+1]
      if i > 0 and j > 0:
        nodes[i][j].north_west = nodes[i-1][j-1]
      if i < len(lines)-2:
        nodes[i][j].south = nodes[i+1][j]
      if i < len(lines)-2 and j < len(lines[i])-2:
        nodes[i][j].south_east = nodes[i+1][j+1]
      if i < len(lines)-2 and j > 0:
        nodes[i][j].south_west = nodes[i+1][j-1]
      if j < len(lines[i])-2:
        nodes[i][j].east = nodes[i][j+1]
      if j > 0:
        nodes[i][j].west = nodes[i][j-1]
  return nodes