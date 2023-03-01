from sys import stdin
input = stdin.readline
n = int(input())
d = []

for i in range(n):
    R, G, B = map(int, input().split())
    d.append([R, G, B])

for i in range(1,n):
    d[i][0] += min(d[i-1][1],d[i-1][2])
    d[i][1] += min(d[i-1][0],d[i-1][2])
    d[i][2] += min(d[i-1][0],d[i-1][1])

print(min(d[n-1]))
