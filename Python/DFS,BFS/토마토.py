from collections import deque
m, n = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
queue = deque()

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == -1 or arr[nx][ny] == 1:
                continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] +1
                queue.append((nx,ny))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append((i,j))
            
bfs()

answer = 0
flag = False

for i in range(n):
    for j in range(m):

        if arr[i][j] == 0:
            flag = True
            break
        answer = max(answer, arr[i][j])

if flag:
    print(-1)
elif answer == -1:
    print(0)
else:
    print(answer-1)
            
