from collections import deque
from sys import stdin
input = stdin.readline
n,m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(a, b, visited):
    visited[a][b] = True
    queue = deque()
    queue.append((a,b))
    result = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]

            if X < 0 or X >= n or Y < 0 or Y >= m:
                continue
            if arr[X][Y] == 1 and visited[X][Y] == False:
                visited[X][Y] = True
                result += 1
                queue.append((X,Y))

    return result

visited = [[False] * m for _ in range(n)]
cnt = 0
result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == False:
            a = bfs(i,j,visited)
            cnt += 1
            if a > result:
                result = a


print(cnt)
print(result)
