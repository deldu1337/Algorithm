from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(arr, a, b):
        queue = deque()
        queue.append((a,b))
        arr[a][b] = 0

        while queue:
            x,y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    queue.append((nx,ny))
            

t = int(input())
for i in range(t):
    n, m, k = map(int, input().split())
    arr=[[0] * m for _ in range(n)]
    count = 0
    visited = [False] * (n)
    
    for j in range(k):
        a, b = map(int, input().split())
        arr[a][b] = 1

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                bfs(arr, i, j)
                count += 1
    print(count)
