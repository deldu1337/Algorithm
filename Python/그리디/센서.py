from sys import stdin
input = stdin.readline
n = int(input())
k = int(input())
arr = list(map(int, input().split()))
num = max(arr)
ar = [[] for _ in range(num+1)]
for i in range(n):
    ar[arr[i]].append(arr[i])
print(arr)
print(ar)
