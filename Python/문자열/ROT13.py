from sys import stdin
input = stdin.readline
s = input().rstrip()
for i in s:
    if i == ' ':
        print(' ',end='')
    elif ord(i) >= 65 and ord(i) <= 90:
        if ord(i)+13 <= 90:
            print(chr(ord(i)+13),end='')
        else:
            print(chr(64+ord(i)+13-90),end='')
    elif ord(i) >= 97 and ord(i) <= 122:
        if ord(i)+13 <= 122:
            print(chr(ord(i)+13),end='')
        else:
            print(chr(96+ord(i)+13-122),end='')
    else:
        print(i,end='')
