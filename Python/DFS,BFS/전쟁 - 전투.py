from collections import deque

n,m = map(int, input().split())
arr = []
for i in range(m):
    arr.append(list((map(str, input()))))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
visited = [[False] * n for _ in range(m)]
def bfs(a,b):
    visited[a][b] = True
    ans = arr[a][b]
    queue = deque()
    queue.append((a,b))
    cnt = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if X <= -1 or X >= m or Y <= -1 or Y >= n:
                continue
            if visited[X][Y] == True:
                continue
            if ans != arr[X][Y]:
                continue
            if visited[X][Y] == False:
                cnt += 1
                visited[X][Y] = True
                queue.append((X,Y))
    return (cnt*cnt)

W = 0
B = 0
cnt = 0
for i in range(m):
    for j in range(n):
        if visited[i][j] == False:
            cnt = bfs(i,j)
            if arr[i][j] == 'W':
                W += cnt
            else:
                B += cnt

print(W, B)
