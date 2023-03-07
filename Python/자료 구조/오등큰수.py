from collections import Counter
from sys import stdin
input = stdin.readline
n = int(input())
arr = list(map(int, input().split()))
stack = [0]
ans = [-1] * n
ans_count = Counter(arr)
for i in range(1,n):
    while stack and ans_count[arr[stack[-1]]] < ans_count[arr[i]]:
        ans[stack.pop()] = arr[i]
    stack.append(i)
print(*ans)
