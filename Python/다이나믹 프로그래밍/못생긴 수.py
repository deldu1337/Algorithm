n = int(input())
d = [2,3,5]
count = 1
i=1
while True:
    if i % 2 == 0:
        if (i//2) % 2 == 0 or (i//2) % 3 == 0 or (i//2) % 5 == 0 or i == 2:
            count += 1
    elif i % 3 == 0:
        if (i//3) % 2 == 0 or (i//3) % 3 == 0 or (i//3) % 5 == 0 or i == 3:
            count += 1
    elif i % 5 == 0:
        if (i//5) % 2 == 0 or (i//5) % 3 == 0 or (i//5) % 5 == 0 or i == 5:
            count += 1
                
    if count == n:
        print(i)
        break
    i += 1
