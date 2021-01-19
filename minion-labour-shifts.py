def solution(data, n): 
    # Your code here
    # get unique values and count
    unique = []
    count = []
    for idx, each in enumerate(data):
        if each not in unique:
            unique.append(each)
            count.append([each, 0])
        if each in unique:
            for idx, every in enumerate(count):
                if count[idx][0] == each:
                    count[idx][1] += 1
                    
    # get values above n
    values = []
    for each in count:
        if each[1] > n:
            values.append(each[0])
    return list(filter(lambda a: a not in values, data))
