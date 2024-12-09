from util import getLinesFromFile
from collections import defaultdict
from itertools import combinations

def isInbounds(point, boundary):
    return point[0] > -1 and point[1] > -1 and point[0] < boundary[0] and point[1] < boundary[1]
def getInboundAntinodes(pair, boundary):
    rise = pair[1][1] - pair[0][1]
    run = pair[1][0] - pair[0][0]
    near_point,far_point = (pair[1],pair[0]) if pair[0][0] > pair[1][1] else (pair[0],pair[1])
    an = (far_point[0] + run, far_point[1] + rise)
    if isInbounds(an, boundary):
        yield an 
    an = (near_point[0] - run, near_point[1] - rise)
    if isInbounds(an, boundary):
        yield an

grid_raw = getLinesFromFile('test.txt')
row_count = len(grid_raw)
col_count = len(grid_raw[0])
print('grid is', row_count, 'rows by', col_count, 'cols')
antennae_locs = defaultdict(list)
for i,row in enumerate(grid_raw):
    for j, loc in enumerate(row):
        if loc != '.':
            antennae_locs[loc].append((i,j))

max_possible_antinodes = 0
for freq in antennae_locs:
    max_possible_antinodes += len(list(combinations(antennae_locs[freq],2))) * 2
print('max possible:', max_possible_antinodes)

antinodes = set()
for freq in antennae_locs:
    for ant_pair in combinations(antennae_locs[freq],2):
        for anti in getInboundAntinodes(ant_pair, (row_count,col_count)):
            antinodes.add(anti)
print(len(antinodes))
print(antinodes)
for i,row in enumerate(grid_raw):
    printrow = ''
    for j, loc in enumerate(row):
        printrow += '#' if (i,j) in antinodes else row[j]
    print(printrow)