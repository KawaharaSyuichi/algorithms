S = input().split()
s = []

while True:
    operator = S.pop(0)

    if operator == '+':
        a = s.pop()
        b = s.pop()
        s.append(str(int(a) + int(b)))
    elif operator == '-':
        b = s.pop()
        a = s.pop()
        s.append(str(int(a) - int(b)))
    elif operator == '*':
        a = s.pop()
        b = s.pop()
        s.append(str(int(a) * int(b)))
    else:
        s.append(operator)

    if len(S) == 0:
        break


print(s[0])
