from sys import stdin
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
tmp = list(set(arr))
tmp.sort()
dic = {}
for i in range(len(tmp)):
    dic[tmp[i]] = i
for i in arr:
    print(dic[i], end=' ')
