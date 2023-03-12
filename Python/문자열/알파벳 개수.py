from sys import stdin
input = stdin.readline
s = input().rstrip()
arr = [0 for _ in range(26)]
for i in s:
    arr[ord(i)-97] += 1
for i in arr:
    print(i, end=' ')
