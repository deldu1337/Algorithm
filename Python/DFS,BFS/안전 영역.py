from collections import deque
n = int(input())
arr = []
max_num = 0
for i in range(n):
    low = list(map(int, input().split()))
    arr.append(low)

    for j in low:
        if j > max_num:
            max_num = j

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def bfs(a,b,c):
    queue = deque()
    queue.append((a,b))
    D[a][b] = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] > c and D[nx][ny] == 0:
                    D[nx][ny] = 1
                    queue.append((nx,ny))

result = []
for i in range(max_num):
    cnt = 0
    D = [[0] * n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if arr[j][k] > i and D[j][k] == 0:
                bfs(j,k,i)
                cnt += 1
    result.append(cnt)
    
print(max(result))
