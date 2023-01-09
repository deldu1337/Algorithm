from collections import deque
while True:
    w,h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = []
    dx = [-1,0,1,0,1,1,-1,-1]
    dy = [0,1,0,-1,1,-1,-1,1]
    count = 0
    for i in range(h):
        arr.append(list(map(int, input().split())))

    def bfs(a,b):
        queue = deque()
        queue.append((a,b))

        while queue:
            x,y = queue.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                if arr[nx][ny] == 0:
                    continue
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    queue.append((nx,ny))

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                bfs(i,j)
                count += 1
    print(count)
            
