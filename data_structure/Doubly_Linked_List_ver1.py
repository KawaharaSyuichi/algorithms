n = int(input())
Q = []

for _ in range(n):
    command, num = input().split()
    if command == 'insert':
        Q.append(int(num))
    else:
        for i in reversed(range(len(Q))):
            if Q[i] == int(num):
                Q.pop(i)
                break

for i in reversed(range(len(Q))):
    if i != 0:
        print('{} '.format(Q[i]), end='')
    else:
        print(Q[i])
