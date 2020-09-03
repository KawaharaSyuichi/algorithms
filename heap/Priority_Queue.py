MAX = 2000000
INFTY = 1 << 30
H = 0
A = [0] * (MAX + 1)


def maxHeapify(i):
    l = 2 * i
    r = 2 * i + 1
    largest = int()

    if (l <= H) and (A[l] > A[i]):
        largest = l
    else:
        largest = i
    if (r <= H) and (A[r] > A[largest]):
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(largest)


def extract():
    global H
    maxv = 0
    if H < 1:
        return - INFTY
    maxv = A[1]
    A[1] = A[H]
    H -= 1
    maxHeapify(1)

    print(maxv)


def increaseKey(i, key):
    if key < A[i]:
        return
    A[i] = key
    while (i > 1 and A[int(i / 2)] < A[i]):
        A[i], A[int(i / 2)] = A[int(i / 2)], A[i]
        i = i / 2


def insert(key):
    global H
    H += 1
    A[H] = -INFTY
    increaseKey(H, key)


while True:
    com = input().split()
    if com[0] == 'end':
        break
    if com[0] == 'insert':
        key = int(com[1])
        insert(key)
    else:
        extract()
