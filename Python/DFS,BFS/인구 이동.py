import math
from collections import deque
n,L,R = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
visited = [[0] * n for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    visited[a][b] = 1
    result = arr[a][b]
    cnt = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == 0 and abs(arr[nx][ny] - arr[x][y]) >= L and abs(arr[nx][ny] - arr[x][y]) <= R:
                result += arr[nx][ny]
                cnt += 1
                visited[nx][ny] = 1
                queue.append((nx,ny))

    result = result//cnt
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                arr[i][j] = result

    for i in range(n):
        print(arr[i])

    print()

count = 0
i = 0
j = 0
while True:
    while True:
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if abs(arr[nx][ny] - arr[i][j]) >= L and abs(arr[nx][ny] - arr[i][j]) <= R:
                bfs(i,j)
                i = -1
                j = -1
                count += 1
                visited = [[0] * n for _ in range(n)]
                break
        if j == -1:
            j = 0
            break
        else:
            j += 1
            break
    if i-1 >= n and j >= n:
        break
    elif i == -1:
        i = 0
        continue
    i += 1

print(count)
