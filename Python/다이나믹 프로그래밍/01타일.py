n = int(input())
arr = [0] * 2
arr[0] = 1
arr[1] = 2
sum = 0
if n <= 2:
    print(arr[n-1])
else:
    for i in range(3,n+1):
        sum = (arr[0] + arr[1])%15746
        arr[0] = arr[1]
        arr[1] = sum
    print(sum%15746)
