from sys import stdin
input = stdin.readline
t = int(input())
for i in range(t):
    s = list(input().rstrip())
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:
                cnt = 1
                break
            cnt -= 1
    if cnt != 0:
        print('NO')
    else:
        print('YES')
