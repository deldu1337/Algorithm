from sys import stdin
input = stdin.readline
n = int(input())
arr = [[] for _ in range(n)]
for i in range(n):
    name,a,b,c = map(str, input().rstrip().split())
    arr[i].append(name)
    arr[i].append(int(a))
    arr[i].append(int(b))
    arr[i].append(int(c))
arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in arr:
    print(i[0])
