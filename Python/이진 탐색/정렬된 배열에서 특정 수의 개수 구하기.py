from bisect import bisect_right, bisect_left

n, x = map(str, input().split())

arr = list(map(str, input().split()))

result = 0

right_index = bisect_right(arr, x)
left_index = bisect_left(arr, x)

result = right_index - left_index

if result != 0:
    print(result)
else:
    print(-1)
