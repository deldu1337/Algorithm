n = int(input())
narr = list(map(int, input().split()))
m = int(input())
marr = list(map(int, input().split()))

narr.sort()
marr.sort()

result = ""

for i in range(m):
    start = 0
    end = n-1
    mid = (end+start)//2
    while True:
        if marr[i] > narr[mid]:
            start = mid + 1
            mid = (end+start)//2
            
        elif marr[i] < narr[mid]:
            end = mid - 1
            mid = (end+start)//2

        else:
            if i != m-1:
                result += "yes "
                break
            else:
                result += "yes"
                break
        if start > end:
            if i != m-1:
                result += "no "
                break
            else:
                result += "no"
                break

print(result)
                
