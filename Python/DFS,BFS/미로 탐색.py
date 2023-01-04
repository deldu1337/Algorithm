from collections import deque
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))

dx = [-1, 0 ,1 ,0]
dy = [0, 1, 0, -1]

def bfs(a, b, num):
    queue = deque()
    queue.append((a,b))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 0:
                continue
            if nx == n-1 and ny == m-1:
                return arr[x][y] + 1
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx,ny))
        print(x,y)        

num = bfs(0,0,1)
print(num)
        
