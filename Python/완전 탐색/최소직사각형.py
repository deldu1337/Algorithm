def solution(sizes):
    answer = 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        if i==0:
            max_w = sizes[i][0]
            max_h = sizes[i][1]
        else:
            if max_w < sizes[i][0]:
                max_w = sizes[i][0]
            if max_h < sizes[i][1]:
                max_h = sizes[i][1]
    
    answer = max_w * max_h
    
    return answer
