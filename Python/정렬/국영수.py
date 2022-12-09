n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(str, input().split())))

for i in range(n):
    for j in range(i+1,n):
        if int(arr[i][1]) < int(arr[j][1]):
            arr[i], arr[j] = arr[j], arr[i]
        elif int(arr[i][1]) == int(arr[j][1]):
            if int(arr[i][2]) > int(arr[j][2]):
                arr[i], arr[j] = arr[j], arr[i]
            elif int(arr[i][2]) == int(arr[j][2]):
                if int(arr[i][3]) < int(arr[j][3]):
                    arr[i], arr[j] = arr[j], arr[i]
                elif int(arr[i][3]) == int(arr[j][3]):
                    for k in range(min(len(arr[i][0]), len(arr[j][0]))):
                        if ord(arr[i][0][k]) > ord(arr[j][0][k]):
                            arr[i], arr[j] = arr[j], arr[i]
                            break

for i in range(n):
    print(arr[i][0])
