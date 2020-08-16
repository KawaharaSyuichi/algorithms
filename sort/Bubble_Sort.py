def bubblesort(A, N):
    sw = 0
    flag = True
    i = 0

    while flag:
        flag = False

        for j in reversed(range(N)):
            if j < i + 1:
                break

            if A[j] < A[j - 1]:
                A[j], A[j-1] = A[j-1], A[j]
                flag = True
                sw += 1

        i += 1

    return sw


N = int(input())
A = list(map(int, input().split()))

sw = bubblesort(A, N)

print(A)
print(sw, end='')
