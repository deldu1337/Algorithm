from collections import deque
from sys import stdin
input = stdin.readline
X,Y = map(int, input().split())
arr = []
for i in range(X):
    arr.append(list(input()))
    
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(a, b, visited):
    queue = deque()
    visited[a][b] = 1
    queue.append((a,b))
    cnt = 0

    while queue:
        c,d = queue.popleft()

        for i in range(4):
            x = c + dx[i]
            y = d + dy[i]

            if x < 0 or x >= X or y < 0 or y >= Y:
                continue
            if arr[x][y] == 'L' and visited[x][y] == 0:
                visited[x][y] = visited[c][d] + 1
                cnt=max(cnt, visited[x][y])
                queue.append((x,y))
            
    return cnt-1

Max = 0
for i in range(X):
    for j in range(Y):
        if arr[i][j] == 'L':
            visited = [[0] * Y for _ in range(X)]
            Max = max(Max, bfs(i,j,visited))

print(Max)
