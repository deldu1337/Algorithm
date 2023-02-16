from collections import deque

n = int(input())
x, y = map(int, input().split())
m = int(input())
arr = [[] * 1 for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False] * (n+1)
def bfs(arr, visited, x, y):
    visited[y] = True
    queue = deque()
    cnt = 0
    queue.append((y))
    while queue:
        a = queue.popleft()
        if a == x:
            print(cnt)
            return
        for v in arr[a]:
            if not visited[v]:
                visited[v] = True
                queue.append((v))
        cnt += 1
    print(-1)

if x > y:
    bfs(arr, visited, x, y)
else:
    bfs(arr, visited, y, x)

    
