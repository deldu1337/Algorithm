from collections import deque
from sys import stdin
input = stdin.readline
A,B = map(int, input().split())

global arr
arr=[]

def dfs(a,b,cnt):
    if a > b:
        return -1
    if a == b:
        arr.append(cnt)
        return cnt
    
    cnt += 1
    dfs(a*2,b,cnt)

    s = str(a)+'1'
    s = int(s)
    dfs(s,b,cnt)

dfs(A,B,1)
if len(arr) == 0:
    print(-1)
else:
    arr.sort()
    print(arr[0])
