n = int(input())
x = list(map(int, input().split()))

x.sort()

count = 0
i = 0

while True:
    if i + x[i] >= n-1:
        break
    count = count + 1
    i = i + x[i]

print(count)
