from sys import stdin
input = stdin.readline
a = list(input().rstrip())
for i in range(len(a)):
    if a[i].isupper():
        a[i] = a[i].lower()
    else:
        a[i] = a[i].upper()
print(''.join(a))
