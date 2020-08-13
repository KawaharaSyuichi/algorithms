def trace(A, N):
    for i in range(N):
        if i > 0:
            print(' ', end='')
        print(A[i], end='')
    print('\n')


def insertionsort(A, N):
    for i in range(1, N):
        v = A[i]
        j = i - 1

        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j -= 1

        A[j + 1] = v
        trace(A, N)


N = int(input())
A = list(map(int, input().split()))

trace(A, N)
insertionsort(A, N)
