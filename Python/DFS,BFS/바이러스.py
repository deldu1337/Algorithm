from collections import deque
num = int(input())
line = int(input())
arr = [[] for _ in range(num+1)]

for i in range(line):
    a,b=map(int,input().split())
    arr[a]+=[b]
    arr[b]+=[a]

visited = [False] * (num+1)

def bfs(arr, visited, start, result):
    queue = deque([start])
    
    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in arr[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                result += 1

    return result

print(bfs(arr, visited, 1, 0))

