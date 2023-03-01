from sys import stdin
input = stdin.readline
t = int(input())
d = [0] * 101
d[1] = 1
d[2] = 1
d[3] = 1
for i in range(4,101):
    d[i] = d[i-3] + d[i-2]
for i in range(t):
    n = int(input())
    if n <= 3:
        print(1)
    else:
        print(d[n])
