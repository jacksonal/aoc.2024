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
    return [[int(c) for c in l.rstrip('\n').split()] for l in lines]

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
