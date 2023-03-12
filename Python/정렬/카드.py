from collections import Counter
from sys import stdin
input = stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
count = Counter(arr)
result = list(count.most_common(1)[0])[0]
print(result)
