n,m = map(int, input().split())
arr = []
result = []
for i in range(n+m):
    arr.append(input())

arr.sort()
for i in range(1,n+m):
    if arr[i-1] == arr[i]:
        result.append(arr[i])

print(len(result))
for i in result:
    print(i)
