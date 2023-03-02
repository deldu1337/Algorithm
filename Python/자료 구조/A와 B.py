from collections import deque
from sys import stdin
input = stdin.readline

queue = deque(input().rstrip())
t = deque(input().rstrip())

for i in range(len(t)-len(queue)):
    if t[len(t)-1] == 'A':
        t.pop()
    else:
        t.pop()
        t.reverse()

flag = 0
for i in range(len(t)):
    if queue[i] != t[i]:
        flag = 1
        break

if flag == 0:
    print(1)
else:
    print(0)
