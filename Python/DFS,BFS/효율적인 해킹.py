# pypy3 제출
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

def bfs(start):
    visited = [False] * (n+1)
    visited[start] = True
    queue = deque([start])
    cnt = 1

    while queue:
        a = queue.popleft()

        for v in arr[a]:
            if visited[v] == False:
                visited[v] = True
                queue.append((v))
                cnt += 1
    
    return cnt

arr = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    arr[b].append(a)

result = []

for i in range(1, n+1):
    result.append(bfs(i))

for i in range(len(result)):
    if max(result) == result[i]:
        print(i+1, end=' ')
