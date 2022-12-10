n = int(input())

arr = list(map(int, input().split()))

dp = [0 for _ in range(n-1)]
for i in range(n-1):
    dp[i] = arr[i]
    for j in range(i+2,n,2):
        dp[i] += arr[j]

print(max(dp))
