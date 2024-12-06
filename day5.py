from util import getFileContents
from collections import defaultdict
from functools import cmp_to_key

class UpdatePageComparator:
    def __init__(self, rules):
        self.rules = rules
    def compare(self,p1,p2):
        if p2 in self.rules[p1]: # p2 should come after p1
            return -1
        elif p1 in self.rules[p2]: #p1 should come after p2
            return 1
        else:
            return 0

input = getFileContents('input.txt')

ruleSection, updateSection = input.split('\n\n')

rules_raw = ruleSection.splitlines()
rules = defaultdict(list)
for r in rules_raw:
    first, second = r.strip().split('|')
    rules[first].append(second)

updates = [ line.strip().split(',') for line in updateSection.splitlines()]
validUpdates = updates.copy()
invalidUpdates = []
for u_index, update in enumerate(updates):
    #print(update)
    for i, pageNum in enumerate(update):
        rule = rules[pageNum]
        nextPages = update[i+1:]
        previousPages = update[:i]
        if len(set(previousPages).intersection(rule)) > 0:
            #print('\tINVALID')
            validUpdates.remove(update)
            invalidUpdates.append(update)
            break
print('valid updates', len(validUpdates))
print(sum([int(u[len(u)//2]) for u in validUpdates]))

comp = UpdatePageComparator(rules)
#part 2
print('fixing', len(invalidUpdates), 'invalid updates')
fixedUpdates = [sorted(update, key = cmp_to_key(comp.compare)) for update in invalidUpdates]

#print(fixedUpdates)
print(sum([int(u[len(u)//2]) for u in fixedUpdates]))
    