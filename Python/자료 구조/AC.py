from collections import deque
from sys import stdin
input = stdin.readline
t = int(input())
    
for i in range(t):
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1].split(',')
    queue = deque(arr)
    
    if n == 0:
        queue = []
        
    rev = 0
    flag = 0
    
    for j in p:
        if j == 'R':
            rev += 1
        else:
            if not queue:
                print('error')
                flag = 1
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if rev % 2 == 0:
            print('['+','.join(queue)+']')
        else:
            queue.reverse()
            print('['+','.join(queue)+']')
    
