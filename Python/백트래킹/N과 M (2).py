def dfs(arr, idx):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(idx, N):
        arr.append(lst[i])
        dfs(arr, i+1)
        arr.pop()


N, M = map(int, input().split())
lst = [i for i in range(1, N+1)]
dfs([], 0)
