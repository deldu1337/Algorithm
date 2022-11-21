s = input()
i = 0
result = ""
while True:
    if i == len(s)-1:
        result = result + s[i]
        break
    if s[i] == '0':
        result = result + s[i] + '+'
    else:
        result = result + s[i] + '*'
    i = i + 1
    
print(eval(result))
