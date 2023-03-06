from sys import stdin
input = stdin.readline
t = int(input())
for i in range(t):
    s = input().rstrip().split(' ')
    for i in s:
        arr = list(i)
        print(''.join(reversed(arr)),end=' ')
    print()
