from collections import deque
n = int(input())
arr = []
d = [[0] * n for _ in range(n)]
for i in range(n):
    arr.append(list(map(str, input())))


dx = [-1,0,1,0]
dy = [0,1,0,-1]
def bfs(a,b,c,d):
    queue = deque()
    queue.append((a,b))
    if d[a][b] == 0:
        d[a][b] = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if len(c) == 2:
                if (arr[nx][ny] == c[0] or arr[nx][ny] == c[1]) and d[nx][ny] == 0:
                    d[nx][ny] = 1
                    queue.append((nx,ny))
            else:
                if arr[nx][ny] == c and d[nx][ny] == 0:
                    d[nx][ny] = 1
                    queue.append((nx,ny))

R = 0
G = 0
B1 = 0
B2 = 0
RG = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R' and d[i][j] == 0:
            bfs(i,j,'R',d)
            R += 1
        elif arr[i][j] == 'G' and d[i][j] == 0:
            bfs(i,j,'G',d)
            G += 1
        elif arr[i][j] == 'B' and d[i][j] == 0:
            bfs(i,j,'B',d)
            B1 += 1

d = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if (arr[i][j] == 'R' or arr[i][j] == 'G') and d[i][j] == 0:
            bfs(i,j,'RG',d)
            RG += 1
        elif arr[i][j] == 'B' and d[i][j] == 0:
            bfs(i,j,'B',d)
            B2 += 1

print((R+G+B1),(RG+B2))







            
