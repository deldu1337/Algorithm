n, m = map(int, input().split())

ball = list(map(int, input().split()))

arr = []
count = 0
ball.sort()

for i in ball:
    for j in ball:
        if i != j and j not in arr:
            count += 1
    arr.append(i)

print(count)
