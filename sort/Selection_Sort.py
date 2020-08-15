def selectionsort(A, N):
    sw = 0

    for i in range(N):
        minj = i

        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j

        if minj != i:
            A[i], A[minj] = A[minj], A[i]
            sw += 1

    return sw


N = int(input())
A = list(map(int, input().split()))


sw = selectionsort(A, N)

print(A)
print(sw, end='')
