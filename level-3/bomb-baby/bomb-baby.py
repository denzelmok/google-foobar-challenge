def solution(x, y):
    # Your code here
    x, y = int(x), int(y)
    # x is mach bombs
    # y is facula bombs
    count = 0
    while x != 1 and y != 1:
        # if x and y are divisible, generation is impossible
        if x % y == 0:
            return "impossible"
        else:
            # add integer of max / min to count
            # to get how many times min fits into max
            count += int(max(x,y)/min(x,y))
            # x and y becomes the remainder of the division and the min number
            x, y = max(x,y) % min(x,y), min(x,y)
    return str(count+max(x,y) - 1)
