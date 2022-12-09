n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()
arr.reverse()

print(' '.join(map(str,arr)))
