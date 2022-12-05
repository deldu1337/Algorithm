n = input()

leng = len(n)
a = n[:leng//2]
b = n[leng//2:]

a = list(a)
b = list(b)

resultA = 0
resultB = 0
for i in a:
    resultA += int(i)

for i in b:
    resultB += int(i)

if resultA == resultB:
    print("LUCKY")
else:
    print("READY")
