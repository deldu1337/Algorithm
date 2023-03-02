from sys import stdin
input = stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

result = [0,0]
def rec(x1, x2, y1, y2, cnt):
    if cnt == 0:
        result[arr[x1][y1]] += 1
        return
    flag = 0

    
    for i in range(x1,x2):
        for j in range(y1, y2):
            if arr[i][j] != arr[x1][y1]:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 1:
        rec(x1,x2-cnt,y1,y2-cnt,cnt//2)
        rec(x1,x2-cnt,y1+cnt,y2,cnt//2)
        rec(x1+cnt,x2,y1,y2-cnt,cnt//2)
        rec(x1+cnt,x2,y1+cnt,y2,cnt//2)
    else:
        result[arr[x1][y1]] += 1
    return

rec(0,n,0,n,n//2)
print(result[0])
print(result[1])

