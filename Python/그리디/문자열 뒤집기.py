s = input()

count = 0
result = s[0]
for i in range(1,len(s)):
    if result != s[i]:
        result = s[i]
        count = count + 1

print(count-1)
