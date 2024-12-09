from util import getLinesFromFile
from itertools import product
from functools import reduce
import operator

def canCombine(value, operands, ops):
    #print(operands)
    for op_combo in product(ops,repeat = len(operands) - 1):
        result = int(operands[0])
        for i, op in enumerate(op_combo):
            result = reduce(op,[result,int(operands[i+1])])
        #print(result)
        if value == result:
            return True
    return False

equations_raw = [map(str.split, line.split(':')) for line in getLinesFromFile('input.txt')]

ops = [operator.add,operator.mul, lambda x,y: int(str(x) + str(y))]
result = 0
for val, operands in equations_raw:
    result = result + int(val[0]) if canCombine(int(val[0]), operands,ops) else result

print(result)
