from collections import deque

n, k = map(int, input().split())
arr = []
data = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        if arr[i][j] != 0:
            data.append((arr[i][j], 0, i, j))
data.sort()
q = deque(data)
s, x, y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]

while q:
    virus, time, X, Y = q.popleft()
    if time == s:
        break
    for i in range(4):
        nx = X + dx[i]
        ny = Y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if arr[nx][ny] == 0:
                arr[nx][ny] = virus
                q.append((virus, time + 1, nx, ny))

print(arr[x-1][y-1])
                

