from sys import stdin
input = stdin.readline
n,k = map(int, input().split())
arr = []
for i in range(n):
    coin = int(input())
    if coin <= k:
        arr.append(coin)

result = 0
i = len(arr)-1
while k!=0:
    if k >= arr[i]:
        result += k//arr[i]
        k -= (arr[i] * (k//arr[i]))
    i -= 1
    
print(result)
