def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        arr = []
        start = commands[i][0]
        end = commands[i][1]
        result = commands[i][2]
        arr.append(array[start-1:end])
        arr[0].sort()
        print(arr)
        answer.append(arr[0][result-1])
        
    return answer
