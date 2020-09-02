MAX = 2000000
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


H = int(input())
A_temp = list(map(int, input().split()))


for i, a in enumerate(A_temp):
    A[i + 1] = a

for i in reversed(range(1, (int(H / 2)) + 1)):
    maxHeapify(i)

for i in range(1, H + 1):
    if i != H:
        print('{} '.format(A[i]), end='')
    else:
        print(A[i])
