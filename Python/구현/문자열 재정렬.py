n = input()

s = list(n)
s.sort()

result = ""
sum = 0

for i in s:
    if ord(i) < 65:
        sum += int(i)
    else:
        result += i

result += str(sum)
print(result)
