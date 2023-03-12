n = list(map(int, input().split()))
flag = 0
if n[0] == 1:
    Sum = n[0]
    for i in range(8):
        if Sum != n[i]:
            flag = 1
            break
        Sum += 1
    if flag == 1:
        print("mixed")
    else:
        print("ascending")
elif n[0] == 8:
    Sum = n[0]
    for i in range(8):
        if Sum != n[i]:
            flag = 1
            break
        Sum -= 1
    if flag == 1:
        print("mixed")
    else:
        print("descending")
else:
    print("mixed")
