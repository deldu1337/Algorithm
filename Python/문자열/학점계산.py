grade = list(input().rstrip())
if grade[0] == 'A':
    if grade[1] == '+':
        print(4.3)
    elif grade[1] == '0':
        print(4.0)
    else:
        print(3.7)
        
elif grade[0] == 'B':
    if grade[1] == '+':
        print(3.3)
    elif grade[1] == '0':
        print(3.0)
    else:
        print(2.7)
        
elif grade[0] == 'C':
    if grade[1] == '+':
        print(2.3)
    elif grade[1] == '0':
        print(2.0)
    else:
        print(1.7)
        
elif grade[0] == 'D':
    if grade[1] == '+':
        print(1.3)
    elif grade[1] == '0':
        print(1.0)
    else:
        print(0.7)
        
else:
    print(0.0)
    
