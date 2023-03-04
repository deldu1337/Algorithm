from sys import stdin
input = stdin.readline
t = int(input())
for i in range(t):
    a = input().rstrip()
    print(a[0],end='')
    print(a[len(a)-1])
