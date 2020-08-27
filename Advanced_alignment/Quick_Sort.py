import sys
SENTINEL = sys.maxsize


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = int(value)


def merge(A, n, left, mid, right):
    L = []
    R = []
    n1 = mid - left
    n2 = right - mid

    for i in range(n1):
        L.append(A[left + i])

    for i in range(n2):
        R.append(A[mid + i])

    L.append(Card('None', SENTINEL))
    R.append(Card('None', SENTINEL))

    i = j = 0

    for k in range(left, right):
        if L[i].value <= R[j].value:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def mergeSort(A, n, left, right):
    mid = int()
    if left + 1 < right:
        mid = int((left + right) / 2)
        mergeSort(A, n, left, mid)
        mergeSort(A, n, mid, right)
        merge(A, n, left, mid, right)


def partition(B, n, p, r):
    x = B[r]
    i = p - 1

    for j in range(p, r):
        if B[j].value <= x.value:
            i += 1
            B[i], B[j] = B[j], B[i]

    B[i + 1], B[r] = B[r], B[i + 1]

    return i + 1


def quickSort(B, n, p, r):
    q = int()

    if p < r:
        q = partition(B, n, p, r)
        quickSort(B, n, p, q - 1)
        quickSort(B, n, q + 1, r)


n = int(input())
A = []
B = []

for i in range(n):
    suit, value = input().split()
    card = Card(suit, value)
    A.append(card)
    B.append(card)

mergeSort(A, n, 0, n)
quickSort(B, n, 0, n - 1)

if A == B:
    print('Stable')
else:
    print('Not Stable')

for i in range(n):
    print('{} {}'.format(B[i].suit, B[i].value))
