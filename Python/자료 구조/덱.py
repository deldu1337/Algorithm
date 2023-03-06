from collections import deque
from sys import stdin
input = stdin.readline
n = int(input())
queue = deque()
for i in range(n):
    m = input().rstrip().split()
    if m[0] == 'push_front':
        queue.appendleft(int(m[1]))
    elif m[0] == 'push_back':
        queue.append(int(m[1]))
    elif m[0] == 'pop_front':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif m[0] == 'pop_back':
        if not queue:
            print(-1)
        else:
            print(queue.pop())
    elif m[0] == 'size':
        print(len(queue))
    elif m[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif m[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif m[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[len(queue)-1])
    
