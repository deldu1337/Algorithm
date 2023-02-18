from collections import deque

n,m,k = map(int, input().split())

arr = [[0] * (m+1) for _ in range(n+1)]
for i in range(k):
    a,b = map(int, input().split())
    arr[a][b] = 1

visited = [False] * (n+1)
dx = [-1, 0 ,1, 0]
dy = [0, 1, 0 ,-1]
def bfs(arr, a, b):
    queue = deque()
    queue.append((a,b))
    cnt = 0

    while queue:
        x,y = queue.popleft()
    
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if X <= 0 or X > n or Y <= 0 or Y > m:
                continue
            if arr[X][Y] == 0:
                continue
            if arr[X][Y] == 1:
                arr[X][Y] = 0
                queue.append((X,Y))
                cnt += 1
    return cnt

cnt = 0
maxCnt = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if arr[i][j] != 0:
            cnt = bfs(arr, i,j)
            if cnt > maxCnt:
                maxCnt = cnt

print(maxCnt)
