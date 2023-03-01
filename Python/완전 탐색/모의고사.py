def solution(answers):
    result = []
    answer = [0] * 3
    one = []
    two = []
    three = []
    for i in range(2001):
        for j in range(5):
            one.append(j+1)
    for i in range(1251):
        for j in range(8):
            if j%2 == 0:
                two.append(2)
            else:
                if j == 1 or j == 3:
                    two.append(j)
                elif j == 5:
                    two.append(4)
                else:
                    two.append(5)
                    
    for i in range(1001):
        for j in range(10):
            if j==0 or j==1:
                three.append(3)
            elif j==2 or j==3:
                three.append(1)
            elif j==4 or j==5:
                three.append(2)
            elif j==6 or j==7:
                three.append(4)
            else:
                three.append(5)

    for i in range(len(answers)):
        if answers[i] == one[i]:
            answer[0] += 1
        if answers[i] == two[i]:
            answer[1] += 1
        if answers[i] == three[i]:
            answer[2] += 1
    for i in range(3):
        if answer[i] == max(answer):
            result.append(i+1)
    
    return result
