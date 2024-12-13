import numpy as np
import re
from util import getLinesFromFile

coeffs = [[],[]]
consts = []
tokens = 0
for linenum, text in enumerate(getLinesFromFile('input.txt')):
    # print(linenum, text)
    if linenum%4 == 0 or linenum%4 == 1:
        numbers = list(map(int,re.findall(r'\d+', text)))
        coeffs[0].append(numbers[0])
        coeffs[1].append(numbers[1])
    elif linenum%4 == 2:
        consts.extend(list(map(lambda a: int(a) + 10000000000000,re.findall(r'\d+', text))))
        solution = np.round(np.linalg.solve(coeffs, consts),3)
        # print(coeffs)
        # print(consts)
        print(solution)
        print(int(solution[0]), '==', solution[0], int(solution[0]) == solution[0])
        print(int(solution[1]), '==', solution[1], int(solution[1]) == solution[1])
        if int(solution[0]) > 0 and int(solution[1]) > 0:
            cost = solution[0] * 3 + solution[1] * 1
            print('this prize:', cost, int(cost) == cost)
            if int(cost) == cost:
                tokens += cost
            print('spent', tokens)
    else:
        coeffs = [[],[]]
        consts.clear()
print(int(tokens))
#86097067143304