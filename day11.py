from util import getFileContents
from itertools import chain
from collections import Counter

def replaceEmpty(stone):
    if stone == '':
        return '0'
    else:
        return stone
    
def blink(stone):
    if stone == '0':
        return ['1']
    elif len(stone) % 2 == 0:
        return [replaceEmpty(stone[:len(stone)//2].lstrip('0')), replaceEmpty(stone[len(stone)//2:].lstrip('0'))]
    else:
        return [str(int(stone) * 2024)]

stones = getFileContents('input.txt').split()
#part 1
for i in range(25):
    stones = list(chain.from_iterable([blink(stone) for stone in stones]))
    print(i, len(stones))

#part 2
def blinkandcount(stone, count):
    newvals = blink(stone)
    cnt = Counter()
    for v in newvals:
        cnt.update({v: count})
    return cnt

stones = Counter(getFileContents('test.txt').split())
print(stones)
for s in stones:
    print(s, stones[s])
for i in range(75):
    new_stones = Counter()
    for s in stones:
        new_stones.update(blinkandcount(s,stones[s]))
    stones = new_stones
    print(i, stones.total())
#print(stones)