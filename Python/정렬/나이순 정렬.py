n = int(input())
arr = [[] for _ in range(n)]
for i in range(n):
    a,b = map(str, input().split())
    arr[i].append(int(a))
    arr[i].append(b)

arr.sort(key=lambda x:x[0])

for i in range(len(arr)):
    print(arr[i][0], arr[i][1])
