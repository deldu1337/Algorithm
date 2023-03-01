from collections import deque
from sys import stdin
input = stdin.readline
n = int(input())
queue = deque()
for i in range(n):
    m = input()
    if 'push' in m:
        spl = m.split(' ')
        queue.append((int(spl[1])))
    elif 'pop' in m:
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif 'size' in m:
        print(len(queue))
    elif 'empty' in m:
        if not queue:
            print(1)
        else:
            print(0)
    elif 'front' in m:
        if not queue:
            print(-1)
        else:
            print(queue[0])
    else:
        if not queue:
            print(-1)
        else:
            print(queue[len(queue)-1])
            
