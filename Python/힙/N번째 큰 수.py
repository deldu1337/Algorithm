import heapq
from sys import stdin
input = stdin.readline
n = int(input())
heap = []
for i in range(n):
    a = list(map(int, input().split()))
    if i > 0:
        for j in a:
            b = heapq.heappop(heap)
            if b < j:
                heapq.heappush(heap, j)
            else:
                heapq.heappush(heap, b)
    else:
        for j in a:
            heapq.heappush(heap, j)

print(heap[0])
