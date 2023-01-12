from collections import deque
m,n,k = map(int, input().split())
arr = [[0] * n for _ in range(m)]
visited = [[0] * n for _ in range(m)]
for i in range(k):
    x1,y1,x2,y2 = map(int, input().split())

    for j in range(y1,y2):
        for l in range(x1,x2):
            arr[j][l] = 1
            visited[j][l] = 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def bfs(a,b,cnt):
    queue = deque()
    queue.append((a,b))
    visited[a][b] = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if arr[nx][ny] == 1:
                continue
            if arr[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny))
                cnt += 1
    return cnt

count = 0
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0 and visited[i][j] == 0:
            bfs(i,j,1)
            count += 1

answer = []
visited = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0 and visited[i][j] == 0:
            answer.append(bfs(i,j,1))

print(count)
answer.sort()
print(' '.join(map(str,answer)))
            


    
