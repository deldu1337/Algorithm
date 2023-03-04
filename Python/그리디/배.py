from sys import stdin
input = stdin.readline
n = int(input())
crane = list(map(int, input().split()))
crane.sort(reverse=True)
m = int(input())
box = list(map(int, input().split()))
box.sort(reverse=True)

if box[0] > crane[0]:
    print(-1)
else:
    time = 0
    while True:
        flag = 0
        i = 0
        j = 0
        visited = [0] * len(crane)
        while True:
            if len(box) == 0:
                flag = 1
                break
            if i == len(crane):
                i = 0
            
            if crane[i] >= box[j]:
                if visited[i] == 0:
                    box.pop(j)
                    visited[i] = 1
                    i += 1
                else:
                    i += 1
            else:
                if visited[i] == 0:
                    j += 1
                else:
                    i += 1
                    j += 1
            if 0 not in visited or j == len(box):
                break
        if flag == 1:
            print(time)
            break
        else:
            time += 1
