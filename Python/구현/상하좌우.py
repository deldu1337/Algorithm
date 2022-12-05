n = int(input())

a = list(map(str, input().split(" ")))

x = 1
y = 1
for i in a:
    if i == 'R':
        if y + 1 <= n:
            y = y + 1

    if i == 'L':
        if y - 1 > 0:
            y = y - 1

    if i == 'D':
        if x + 1 > 0:
            x = x + 1

    if i == 'U':
        if x - 1 > 0:
            x = x - 1

print(x, y)
