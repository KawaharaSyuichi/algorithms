def partition(p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]

    return i + 1


n = int(input())
A = list(map(int, input().split()))

q = partition(0, n - 1)

for i in range(n):
    if i:
        print(" ", end='')
    if i == q:
        print('[', end='')

    print(A[i], end='')

    if i == q:
        print(']', end='')
