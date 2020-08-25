import sys

SENTINEL = sys.maxsize
cnt = 0
n = int(input())
A = list(map(int, input().split()))


def merge(A, n, left, mid, right):
    L = []
    R = []
    n1 = mid - left
    n2 = right - mid

    for i in range(n1):
        L.append(A[left + i])
    for i in range(n2):
        R.append(A[mid + i])

    L.append(SENTINEL)
    R.append(SENTINEL)

    i = j = 0
    for k in range(left, right):
        global cnt
        cnt += 1

        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def mergeSort(A, n, left, right):
    if left + 1 < right:
        mid = int((left + right) / 2)
        mergeSort(A, n, left, mid)
        mergeSort(A, n, mid, right)
        merge(A, n, left, mid, right)


mergeSort(A, n, 0, n)

for i, j in enumerate(A):
    if i != n - 1:
        print('{} '.format(j), end='')
    else:
        print(j)

print(cnt)
