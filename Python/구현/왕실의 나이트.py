n = input()

column = ['a','b','c','d','e','f','g','h']

c = n[0]
r = int(n[1:])
count = 0

if column.index(c) + 2 < len(column):
    if r + 1 <= 8:
        count += 1
    if r - 1 > 0:
        count += 1

if column.index(c) - 2 > 0:
    if r + 1 <= 8:
        count += 1
    if r - 1 > 0:
        count += 1

if r + 2 <= 8:
    if column.index(c) + 2 < len(column):
        count += 1
    if column.index(c) - 2 > 0:
        count += 1

if r - 2 > 0:
    if column.index(c) + 2 < len(column):
        count += 1
    if column.index(c) - 2 > 0:
        count += 1

print(count)
