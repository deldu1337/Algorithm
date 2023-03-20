from collections import deque
from sys import stdin
input = stdin.readline
n = int(input())
arr = [i for i in range(1,n+1)]
queue = deque(arr)
if len(queue) == 1:
    print(queue[0])
else:
    while queue:
        queue.popleft()
        if len(queue) == 1:
            print(queue[0])
            break
        queue.append(queue.popleft())
    
