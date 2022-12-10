n = int(input())

dp = [0 for _ in range(4)]

for i in range(n):
    if n == 1:
        print(sum(dp))
        break
    if n % 5 == 0:
        n //= 5
        dp[0] += 1
    elif n % 3 == 0:
        n //= 3
        dp[1] += 1
    else:
        if ((n - 1) % 5 == 0 or (n - 1) % 3 == 0) and n != 1:
            n -= 1
            dp[3] += 1
        elif n % 2 == 0 and n != 1:
            n //= 2
            dp[2] += 1
        else:
            n -= 1
            dp[3] += 1
