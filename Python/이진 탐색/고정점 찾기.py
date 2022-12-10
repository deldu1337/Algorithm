n = int(input())

arr = list(map(int, input().split()))

result = 0
start = 0
end = n-1
mid = (start+end)//2
while start <= end:
    if mid > arr[mid]:
        start = mid + 1
        mid = (start+end)//2
    elif mid < arr[mid]:
        end = mid - 1
        mid = (start+end)//2
    else:
        result = 1
        break

if result != 0:
    print(mid)
else:
    print(-1)

    
