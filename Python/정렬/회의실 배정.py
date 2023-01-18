n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

count = 0
for i in range(n):
    work = arr[i]
    cnt = 1
    for j in range(i+1, n):
        if work[1] <= arr[j][0]:
            work = arr[j]
            cnt += 1
    if count <= cnt:
        count = cnt

print(count)
