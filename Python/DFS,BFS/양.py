from sys import stdin
from collections import deque
input = stdin.readline
r,c = map(int, input().split())
arr = []
for i in range(r):
    arr.append(list(input().rstrip()))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(a,b,visited):
    visited[a][b] = 1
    queue = deque([])
    queue.append((a,b))

    cnt = [0] * 2
    if arr[a][b] == 'o':
        cnt[0] += 1
    if arr[a][b] == 'v':
        cnt[1] += 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]

            if X < 0 or X >= r or Y < 0 or Y >= c:
                continue
            if arr[X][Y] != '#' and visited[X][Y] == 0:
                if arr[X][Y] == 'o':
                    cnt[0] += 1
                if arr[X][Y] == 'v':
                    cnt[1] += 1
                visited[X][Y] = visited[x][y] + 1
                queue.append((X,Y))

    if cnt[0] > cnt[1]:
        cnt[1] = 0
    else:
        cnt[0] = 0
    return cnt

result = [0] * 2
visited = [[0] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if arr[i][j] != '#' and visited[i][j] == 0:
            a = bfs(i,j,visited)
            result[0] += a[0]
            result[1] += a[1]

print(result[0],result[1])
    
