n = int(input())
time = []

for _ in range(n):
    start, end = map(int, input().split())
    time.append([start, end])

time = sorted(time, key=lambda a: a[0]) 
time = sorted(time, key=lambda a: a[1])
last = 0 
conut = 0

for i, j in time:
    if i >= last:
        conut += 1
        last = j

print(conut)
