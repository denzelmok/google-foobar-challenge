from fractions import Fraction
import numpy as np

def solution(m):
    # markov chain problem, finding probability of absorbing states
    
    # check if s0 is an absorbing state, if yes, output 1
    if isinstance(m[0], list):
        if sum(m[0]) == 0:
            answer = [1]
            for idx, each in enumerate(m):
                if sum(each) == 0 and idx != 0:
                    answer.append(0)
            answer.append(1)
            return(answer)
    elif sum(m) == 1 or sum(m) == 0:
        return [1,1]
    
    # if absorbing state is marked by any, change to 0
    for idx, each in enumerate(m):
        if sum(each) == m[idx][idx]:
            m[idx][idx] = 0
    
    if sum(m[0]) == 0 and len(m) < 2:
        return 0
    elif sum(m[0]) == 0:
        answer = [1]
        for idx, each in enumerate(m):
            if sum(each) == 0 and idx != 0:
                answer.append(0)
        answer.append(1)
        return(answer)
    if len(m) == 2 and sum(m[1]) == 0:
        return 0
    if len(m) == 2:
        return 1
    
    # sort m into canonical form, with absorbing states at the end
    # introduce metadata of index location to m
    # rewrite swapping function
    # given m, if transient found between absorbing states, swap with first absorbing state
    for idx, each in enumerate(m):
        m[idx] = [each, idx]
    copy = m[:]
    swapped = []
    marker = 0
    for idx, each in enumerate(m):
        if sum(each[0]) == 0:
            for every in m[idx+1:]:
                if sum(every[0]) != 0 and every[1] not in swapped:
                    if len(swapped) != 0:
                        copy[idx+marker], copy[m.index(every)] = copy[m.index(every)], copy[idx+marker]
                        swapped.append(every[1])
                        swapped.append(each[1]+marker)
                        marker += 1
                    else:
                        copy[idx], copy[m.index(every)] = copy[m.index(every)], copy[idx]
                        swapped.append(every[1])
                        swapped.append(each[1])
                        marker += 1
    #print(swapped)
    # swap all elements in each list that have been swapped
    for i,k in zip(swapped[0::2], swapped[1::2]):
        for idx, each in enumerate(copy):
            copy[idx][0][k], copy[idx][0][i] = copy[idx][0][i], copy[idx][0][k]
    
    # get indexes of absorbing states
    need_swap = []
    for each in copy:
        if sum(each[0]) == 0:
            need_swap.append(each[1])
    
    # remove indexes
    m = [x[0] for x in copy]
    #print(m)
    # generate transition matrix
    probs = []
    for each in m:
        prob = []
        total = sum(each)
        if total != 0:
            for num in each:
                if num != 0:
                    proba = float(num) / float(total)
                else:
                    proba = 0
                prob.append(proba)
            probs.append(prob)
        else:
            probs.append(each)
    #print(probs)
    
    # split matrix into sections for probability calculation
    # Q is square matrix with probability of transitioning from one transient state to another
    sums = [sum(x) for x in m]
    num_trans = np.count_nonzero(sums)
    Q = []
    for i in range(num_trans):
        Q.append(probs[i][:num_trans])
    #print(Q)
    # R is probability of transitioning from one transient state to an absorbing state
    R = []
    for i in range(num_trans):
        R.append(probs[i][num_trans:])
    #print(R)
    O = []
    for i in range(num_trans):
        O.append(probs[i+2][:num_trans])
    #print(O)
    # I is the identity matrix
    I = np.identity(num_trans)
    #print(I)
    # N is the fundamental matrix, inverse of I-Q
    N = np.linalg.inv(np.subtract(I,Q))
    #print(N)
    # NR is the answer
    NR = np.matmul(N, R)
    #print(NR)
    
    # output answer as fraction with common denominator
    denom = []
    numer = []
    answer = []
    for each in NR[0]:
        if each != 0 and each != 1:
            frac = str(Fraction(each).limit_denominator()).split('/')
            numer.append(int(frac[0]))
            denom.append(int(frac[1]))
        elif each == 1:
            numer.append(1)
            denom.append(1)
        else:
            numer.append(0)
            denom.append(1)
    gcd = None
    check = []
    #print(numer)
    #print(denom)
    for idx, i in enumerate(denom):
        if gcd is None:
            gcd = i
        #print(gcd)
        check.append(len(str(float(gcd) / float(denom[idx]) * float(numer[idx]))) >= 5)
        #print(check)
        if False not in check:
            gcd = np.gcd(gcd,i)
            #print(gcd)
        elif idx != len(denom):
            gcd = np.lcm(gcd, i)
            #print(gcd)
    for idx, each in enumerate(numer):
        if denom[idx] != gcd and denom[idx] != 0:
            answer.append(int(gcd / denom[idx] * numer[idx]))
        else:
            answer.append(each)
    answer.append(gcd)
    #print(answer)
    
    # using need_swap, swap answers to correct order
    if len(need_swap) != 0:
        temp = []
        new = sorted(need_swap)
        for each in new:
            idx = need_swap.index(each)
            temp.append(answer[idx])
        temp.append(answer[-1])
        answer = temp
    return answer
