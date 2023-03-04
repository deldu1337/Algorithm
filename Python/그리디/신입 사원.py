from sys import stdin
input = stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    arr = []
    for j in range(n):
        arr.append(list(map(int, input().split())))
    if n == 1:
        print(n)
    else:
        arr.sort()
        cnt = 1
        top = 0
        for j in range(1,n):
            if arr[j][1] < arr[top][1]:
                top = j
                cnt += 1
        print(cnt)
