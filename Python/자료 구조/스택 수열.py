from sys import stdin
input = stdin.readline
n = int(input())
m = [0] * n
for i in range(n):
    m[i] = int(input())
stack = []
string = []
i = 1
while i<n+1:
    for v in m:
        if v >= i:
            for j in range(i,v+1):
                stack.append(i)
                string.append('+')
                i+=1
        if len(stack) > 0:
            if v == stack[len(stack)-1]:
                stack.pop()
                string.append('-')
            else:
                string.append('NO')
                i = 0
                break
    if i==0:
        break

if 'NO' in string:
    print('NO')
else:
    for i in range(len(string)):
        print(string[i])
