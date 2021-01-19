import numpy as np
from fractions import Fraction

def solution(pegs):
    # Your code here
    # find possible distances between each peg
    def poss(first, second):
        return second - first
    
    # find all possible distances
    distances = []
    for idx, peg in enumerate(pegs):
        if idx+1 < len(pegs):
            distances.append(poss(peg, pegs[idx+1]))
    
    # function to find next radius
    def gen(radius, next_dist):
        b = abs(radius - next_dist)
        return b
    
    # maths
    # array generation
    a = []
    b = []
    # matrix entry generation
    for idx, distance in enumerate(distances):
        array = []
        for peg in pegs:
            array.append(0)
        array[idx] = 1
        array[idx+1] = 1
        a.append(array)
        array = []
    for idx, peg in enumerate(pegs):
        if idx == 0:
            array.append(1)
        elif idx == len(pegs) - 1:
            array.append(-2)
        else:
            array.append(0)
    a.append(array)
    # matrix known values
    for distance in distances:
        b.append(distance)
    b.append(0)
    
    if len(pegs) >= 2:
        a = np.array(a)
        b = np.array(b)
        x = np.linalg.solve(a, b)
        answer = str(Fraction(x[0]).limit_denominator()).split('/')
        if any(i<1 for i in x) == False:
            if len(answer) == 2:
                return int(answer[0]), int(answer[1])
            else:
                return int(answer[0]),1
    return (-1, -1)
