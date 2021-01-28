def solution(l):
    # Your code here
    count = 0
    doubles = [0]*len(l)
    for m in range(1, len(l)):
        for n in range(m):
            if l[m] % l[n] == 0:
                doubles[m] += 1
                count += doubles[n]
    return count
