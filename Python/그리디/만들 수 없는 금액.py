n = int(input())

coin = list(map(int, input().split()))
count = 1

coin.sort()

for i in coin:
    if count < i:
        break
    count += i

print(count)
