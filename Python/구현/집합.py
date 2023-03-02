from sys import stdin
input = stdin.readline
m = int(input())
s = []
for i in range(m):
    cal = input().rstrip()
    if 'add' in cal:
        spl = cal.split(' ')
        cal = int(spl[1])
        if cal not in s:
            s.append(cal)
    elif 'remove' in cal:
        spl = cal.split(' ')
        cal = int(spl[1])
        if cal in s:
            s.remove(cal)
    elif 'check' in cal:
        spl = cal.split(' ')
        cal = int(spl[1])
        if cal in s:
            print(1)
        else:
            print(0)
    elif 'toggle' in cal:
        spl = cal.split(' ')
        cal = int(spl[1])
        if cal in s:
            s.remove(cal)
        else:
            s.append(cal)
    elif 'all' in cal:
        s = []
        for j in range(1,21):
            s.append(j)
    else:
        s = []
