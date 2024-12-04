import re
import operator
from functools import reduce

def execute(state, instr):
    if instr[0] == 'do()':
        return state[0], True
    elif instr[0] == 'don\'t()':
        return state[0], False
    else:
        return (state[0] + reduce(operator.mul, map(int, instr[1:])), state[1]) if state[1] else state

#part 1
with open('input.txt') as file:
    print(sum([reduce(operator.mul,map(int,match)) for match in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', file.read())]))

#part 2
with open('input.txt') as file:
    print(reduce(execute, re.findall(r'(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))', file.read()), (0,True))[0])