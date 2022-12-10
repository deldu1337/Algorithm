n = int(input())

arr = list(map(int, input().split()))

arr.sort()
cnt = [0 for _ in range(2)]
count = 0
if n % 2 == 0:
    count = arr[n//2-1]
    for i in range(n):
        if i == n//2-1:
            cnt[0] += 0
        elif arr[i] < arr[n//2-1]:
            cnt[0] += (count - arr[i])
        elif arr[i] > arr[n//2-1]:
            cnt[0] += (arr[i] - count)
    
    count = arr[n//2]
    for i in range(n):
        if i == n//2:
            cnt[1] += 0
        elif arr[i] < arr[n//2]:
            cnt[1] += (count - arr[i])
        elif arr[i] > arr[n//2]:
            cnt[1] += (arr[i] - count)

    if cnt[0] < cnt[1]:
        print(arr[n//2-1])
    elif cnt[1] < cnt[0]:
        print(arr[n//2])
    else:
        print(arr[n//2-1])
    
elif n % 2 == 1:
    print(arr[n//2])
    
else:
    print(arr[0])
