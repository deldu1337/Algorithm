n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()
result = [0 for _ in range(n-1)]
if n <= 1:
    print(arr[0])
elif n == 2:
    print(sum(arr))
else:
    result[0] = arr[0] + arr[1]
    for i in range(2, n):
        result[i-1] += (result[i-2]+arr[i])

    print(sum(result))

