n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

start = 1
end = arr[n-1]
mid = (start+end)//2

while True:
    answer = 0
    if mid < arr[0]:
        end = mid -1
        mid = (start+end)//2
    else:
        for i in range(n):
            if mid < arr[i]:
                answer += (arr[i] - mid)
        if answer > m:
            mid += 1
        elif answer < m:
            mid -= 1
        else:
            print(mid)
            break
