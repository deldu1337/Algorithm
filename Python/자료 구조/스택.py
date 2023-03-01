from sys import stdin
input = stdin.readline
n = int(input())
stack = []
for i in range(n):
    m = input()
    if 'push' in m:
        spl = m.split(' ')
        stack.append(int(spl[1]))
    elif 'pop' in m:
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif 'size' in m:
        print(len(stack))
    elif 'empty' in m:
        if not stack:
            print(1)
        else:
            print(0)
    else:
        if not stack:
            print(-1)
        else:
            print(stack[len(stack)-1])
