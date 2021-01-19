def solution(h, q):
    # Your code here
    answer = []
    for each in q:
        node = each
        start = 1
        end = 2**h - 1
        parent = -1
        
        while node != end:
            parent = end
            mid = (start+end)/2
            if node < mid:
                end = mid - 1
            else:
                start = mid
                end = end - 1
        answer.append(parent)
    return answer
