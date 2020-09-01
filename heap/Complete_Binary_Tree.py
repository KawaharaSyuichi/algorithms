MAX = 100000


def parent(i):
    return int(i / 2)


def left(i):
    return 2 * i


def right(i):
    return 2*i+1


H = int(input())
A_temp = list(map(int, input().split()))
A = [0]*(MAX+1)

for i, a in enumerate(A_temp):
    A[i+1] = a

for i in range(1, H + 1):
    print('node {}: key {}, '.format(i, A[i]), end='')

    if parent(i) >= 1:
        print('parent key = {}, '.format(A[parent(i)]), end='')
    if left(i) <= H:
        print('left key = {}, '.format(A[left(i)]), end='')
    if right(i) <= H:
        print('right key = {}, '.format(A[right(i)]), end='')

    print('')
