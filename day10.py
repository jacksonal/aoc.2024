from util import getRowsAsIntLists

# def score_trail(trailhead, pos_node, peak_pairs):
#     score = 0
#     #print('height', pos_node.value)
#     if pos_node.value == '9' :
#         if (trailhead,pos_node) not in peak_pairs:
#             score = 1
#             peak_pairs.add((trailhead,pos_node))
#     else:
#         if pos_node.north and pos_node.north.value == str(int(pos_node.value) + 1):
#             #print('going north')
#             score += score_trail(trailhead, pos_node.north, peak_pairs)
#         if pos_node.east and pos_node.east.value == str(int(pos_node.value) + 1):
#             #print('going east')
#             score += score_trail(trailhead, pos_node.east, peak_pairs)
#         if pos_node.south and pos_node.south.value == str(int(pos_node.value) + 1):
#             #print('going south')
#             score += score_trail(trailhead, pos_node.south, peak_pairs)
#         if pos_node.west and pos_node.west.value == str(int(pos_node.value) + 1):
#             #print('going west')
#             score += score_trail(trailhead, pos_node.west, peak_pairs)
#     return score

def findTrailheads(graph):
    trailheads = []
    for i,row in enumerate(graph):
        for j,node in enumerate(row):
            if node == 0:
                trailheads.append((i,j))
    return trailheads

def score_trail(trailhead, curpos, graph, trailhead_peak_pairs):
    if graph[curpos[0]][curpos[1]] == 9:# and (trailhead, curpos) not in trailhead_peak_pairs:
        #print('got to the top!')
        #trailhead_peak_pairs.add((trailhead, curpos))
        return 1
    else:
        score = 0
        curheight = graph[curpos[0]][curpos[1]]
        # up
        if curpos[0] > 0 and curheight == graph[curpos[0]-1][curpos[1]]-1:
            score = score_trail(trailhead, (curpos[0]-1, curpos[1]), graph, trailhead_peak_pairs)
        # down
        if curpos[0] < len(graph)-1 and curheight == graph[curpos[0]+1][curpos[1]]-1:
            score += score_trail(trailhead, (curpos[0]+1, curpos[1]), graph, trailhead_peak_pairs)
        # left
        if curpos[1] > 0 and curheight == graph[curpos[0]][curpos[1]-1]-1:
            score += score_trail(trailhead, (curpos[0], curpos[1]-1), graph, trailhead_peak_pairs)
        # right
        if curpos[1] < len(graph[0])-1 and curheight == graph[curpos[0]][curpos[1]+1]-1:
            score += score_trail(trailhead, (curpos[0], curpos[1]+1), graph, trailhead_peak_pairs)
        return score

graph = getRowsAsIntLists('input.txt')
print(graph[0][0])
print(len([node for row in graph for node in row]), 'positions on the map')
score = 0

trailhead_peak_pairs = set()

print(sum([score_trail(trailhead, trailhead, graph, trailhead_peak_pairs) for trailhead in findTrailheads(graph)]))

# trailhead_peak_pairs = set()
# for node in [node for row in graph for node in row]:
#     if node.value == '0':
#         trail_score = score_trail(node, node, trailhead_peak_pairs)
#         print(trail_score)
#         score += trail_score

# print(score)