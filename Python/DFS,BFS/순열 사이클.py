from collections import deque
from sys import stdin
input = stdin.readline
t = int(input())

def bfs(start, visited):
    visited[start] = True
    queue = deque([start])

    while queue:
        x = queue.popleft()

        for v in graph[x]:
            if not visited[v]:
                visited[v] = True
                queue.append((v))
        
for i in range(t):
    n = int(input())
    graph = [[] for _ in range(n+1)]
    arr = list(map(int, input().split()))
    for j in range(n):
        graph[j+1].append(arr[j])
    visited = [False] * (n+1)
    cnt = 0
    for j in range(1,n+1):
        if not visited[j]: 
            bfs(j,visited)
            cnt += 1
    print(cnt)
