n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(str, input().split())))

arr = sorted(arr, key=lambda arr: int(arr[1]))
for i in range(n):
    print(arr[i][0], end=' ')
