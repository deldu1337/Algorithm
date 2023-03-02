from sys import stdin
input = stdin.readline
n = int(input())
alp = [0] * 26
arr = []
for i in range(n):
    a = input().rstrip()
    arr.append(a)
    cnt = len(a)-1
    
    for j in range(len(a)):
        if j != len(a)-1:
            alp[ord(a[j])-65] += (10 ** cnt)
            cnt -= 1
        else:
            alp[ord(a[j])-65] += 1

num = 9
for i in range(26-alp.count(0)):
    idx = alp.index(max(alp))
    for j in range(len(arr)):
        arr[j] = arr[j].replace(chr(idx+65),str(num))
    num -= 1
    alp[idx] = 0

for i in range(len(arr)):
    arr[i] = int(arr[i])

print(sum(arr))
