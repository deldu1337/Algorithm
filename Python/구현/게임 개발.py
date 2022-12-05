n, m = map(int, input().split())
a, b, d = map(int, input().split())

count = 1
cnt = 0
arr = []
for i in range(n):
    arr.append([])
    r = list(map(int, input().split()))
    for j in range(m):
        arr[i].append(r[j])
arr[a][b] = 2
        
while True:
    if d + 1 >= 4:
        d = 0
    else:
        d = d + 1
    if d == 0:
        if arr[a-1][b] == 0 and a-1 >= 0:
            a = a - 1
            arr[a][b] = 2
            count += 1
        else:
            cnt += 1
            if cnt != 4:
                continue
            else:
                cnt = 0
                if a+1 < 4:
                    if arr[a+1][b] != 1:
                        a = a + 1
                    else:
                        break
                else:
                    break
        
    elif d == 1:
        if arr[a][b+1] == 0 and b+1 < 4:
            b = b + 1
            arr[a][b] = 2
            count += 1
        else:
            cnt += 1
            if cnt != 4:
                continue
            else:
                cnt = 0
                if b-1 >= 0:
                    if arr[a][b-1] != 1:
                        b = b - 1
                    else:
                        break
                else:
                    break
    elif d == 2:
        if arr[a+1][b] == 0 and a+1 < 4:
            a = a + 1
            arr[a][b] = 2
            count += 1
        else:
            cnt += 1
            if cnt != 4:
                continue
            else:
                cnt = 0
                if a-1 >= 0:
                    if arr[a-1][b] != 1:
                        a = a - 1
                    else:
                        break
                else:
                    break
    else:
        if arr[a][b-1] == 0 and b-1 >= 0:
            b = b - 1
            arr[a][b] = 2
            count += 1
        else:
            cnt += 1
            if cnt != 4:
                continue
            else:
                cnt = 0
                if b+1 < 4:
                    if arr[a][b+1] != 1:
                        b = b + 1
                    else:
                        break
                else:
                    break

print(count)
