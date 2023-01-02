def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    index_target = words.index(target)
    for i in range(len(words)):
        count = 0
        k = 0
                
        for j in range(len(begin)):
            if words[i][j] != begin[j]:
                count += 1
            if words[index_target][j] != begin[j]:
                k += 1
        if k == 1:
            begin = words[index_target]
            answer += 1
            break
        elif count == 1:
            begin = words[i]
            answer += 1
            print(words[i], end=' ')
        
    return answer
