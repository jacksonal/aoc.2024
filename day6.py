from util import buildGraph

def findGuardNode(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j].value == '^':
                return graph[i][j]
    return None

def getNext(node):
    if node.value == '^':
        return node.north
    elif node.value == '>':
        return node.east
    elif node.value == 'v':
        return node.south
    elif node.value == '<':
        return node.west

def rotate(direction):
    if direction == '^':
        return '>'
    elif direction == '>':
        return 'v'
    elif direction == 'v':
        return '<'
    elif direction == '<':
        return '^'
    
def guardStep(node):
    nextNode = getNext(node)
    if nextNode == None: # off the map
        #node.value = '.'
        return None
    elif nextNode.value != '#': # empty space
        nextNode.value = node.value
        #node.value = '.'
        return nextNode
    else: # blocked! turn right but don't move
        node.value = rotate(node.value)
        return node

def patrol(node):
    while(node):
        if not node.visited:
            print('visiting')
        node.visited = True
        node = guardStep(node)

def detectLoop(node):
    #print('detecting loop')
    guard = node
    fastGuard = node
    while guard:
        #print(guard, fastGuard)
        guard = guardStep(guard)
        fastGuard = guardStep(fastGuard)
        if guard == None or fastGuard == None:
            return False
        else:
            fastGuard = guardStep(fastGuard)
            if guard == fastGuard:
                return True
            elif guard == None or fastGuard == None:
                return False

minimap = buildGraph('test.txt')
start = findGuardNode(minimap)
patrol(start)
visited = [node for row in minimap for node in row if node.visited]
print(len(visited))

#part 2 placing an obstruction to create a loop
# only worry about placing the obstruction in the og path of the guard
# can only place 1 obstruction
# find the first node that the guard visits twice while moving in the same direction

#reset the map
for node in visited:
    node.visited = False
    node.value = '.'
start.value = '^'

obstructionCount = 0
for node in visited:
    if node != start:
        obstruction = node
        obstruction.value = '#'
        obstructionCount = (obstructionCount + 1) if detectLoop(start) else obstructionCount
        obstruction.value = '.'
        #reset the map
        for node in visited:
            node.visited = False
            node.value = '.'
        start.value = '^'
print(obstructionCount)