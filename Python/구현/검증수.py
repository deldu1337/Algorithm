a = input().split()
def check(a):
    sum = 0
    for i in range(len(a)):
        sum += int(a[i])*int(a[i])
    return sum%10
print(check(a))
