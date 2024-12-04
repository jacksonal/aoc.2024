from collections import Counter

def buildRecord(line):
    return [int(x) for x in line.split()]

def isDescending(records):
    for i in range(len(records))[1:]:
        diff = records[i-1] - records[i]
        if diff < 1 or diff > 3:
            print('\tNOT SAFELY DECREASING', records[i-1], records[i], 'decrease of', diff)
            return False
    print('\tSAFELY DECREASING')
    return True

def isIncreasing(records):
    for i in range(len(records))[1:]:
        diff = records[i] - records[i - 1]
        if diff < 1 or diff > 3:
            print('\tNOT SAFELY INCREASING', records[i-1], records[i], 'increase of', diff)
            return False
    print('\tSAFELY INCREASING')
    return True

def isSafe(records):
    print('checking', records)
    return isDescending(records) or isIncreasing(records)

def isSafeWithSkip(records):
    if isSafe(records):
        return True
    for i in range(len(records) - 1):
        if isSafe(records[:i] + records[i+1:]):
            return True
    
    return isSafe(records[:-1])


with open('input.txt') as file:
    records = [buildRecord(line) for line in file.readlines()]

#print(Counter([isSafe(r) for r in records]))
print(Counter([isSafeWithSkip(r) for r in records]))