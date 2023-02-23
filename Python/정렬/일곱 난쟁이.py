from sys import stdin
input = stdin.readline
arr = []
for i in range(9):
    arr.append(int(input()))
a=-1
b=-1
for i in range(9):
    for j in range(9):
        if i != j:
            if (sum(arr) - 100) == (arr[i] + arr[j]):
                a = i
                b = j
                break
    if a > -1 and b > -1:
        break

answer = []
for i in range(9):
    if i == a or i == b:
        continue
    else:
        answer.append(arr[i])
answer.sort()
for i in range(7):
    print(answer[i])
