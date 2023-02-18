import math
import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = []
plus = [0] * 4001
minus = [0] * 4001
count = []
for i in range(n):
    a = int(input())
    arr.append(a)
    if a > 0:
        plus[a] += 1
    else:
        minus[abs(a)] += 1
    

avg = round(sum(arr) / n)
arr.sort()
mid = arr[(n//2)]
ran = arr[n-1] - arr[0]
print(avg)
print(mid)
cnt_li = Counter(arr).most_common()
if len(cnt_li) > 1 and cnt_li[0][1]==cnt_li[1][1]:
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])
print(ran)
