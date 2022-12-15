n = int(input())
arr = list(map(int, input().split()))

count = 0
for i in range(1,n):
    if arr[i-1] < arr[i]:
        count += 1

print(count)
