from collections import deque
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(a, b):
    queue = deque()
    queue.append((a,b))
    result = 1
    arr[a][b] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                queue.append((nx,ny))
                result += 1

    return result

Arr=[]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            Arr.append(bfs(i,j))

print(len(Arr))
Arr.sort()
for i in Arr:
    print(i)
