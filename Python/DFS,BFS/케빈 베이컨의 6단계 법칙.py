from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]

for i in range(m):
   a, b = map(int, input().split())
   arr[a].append(b)
   arr[b].append(a)

def bfs(start):
    num = [0] * (n+1)
    visited[start] = True
    queue = deque([start])
    while queue:
        a = queue.popleft()
        
        for v in arr[a]:
            if not visited[v]:
                visited[v] = True
                num[v] = num[a] + 1
                queue.append((v))
    return sum(num)
                
answer = [0] * (n)
for i in range(1,n+1):
    for j in range(1,n+1):
        if i != j:
            visited = [False] * (n+1)
            answer[i-1] += bfs(i)

print(answer.index(min(answer))+1)


