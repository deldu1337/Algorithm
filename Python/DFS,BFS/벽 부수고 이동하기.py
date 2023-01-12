from collections import deque
n,m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(a,b,z,visited,arr):
    queue = deque()
    queue.append((a,b,z))
    visited[a][b][z] = 1

    while queue:
        x,y,z = queue.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if arr[nx][ny] == 0 and visited[nx][ny][z] == 0:
                queue.append((nx,ny,z))
                visited[nx][ny][z] = visited[x][y][z] + 1
                
            if arr[nx][ny] == 1 and z == 0:
                queue.append((nx,ny,z+1))
                visited[nx][ny][z+1] = visited[x][y][z] + 1
                
    return -1

print(bfs(0,0,0,visited,arr))
