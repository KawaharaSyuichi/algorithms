n = int(input())
A = list(map(int, input().split()))
A_max = max(A)
B = [0] * (len(A))
C = [0] * (A_max + 1)


for i in A:
    C[i] += 1

for i in range(1, A_max + 1):
    C[i] = C[i] + C[i - 1]


for j in range(n):
    B[C[A[j]] - 1] = A[j]
    C[A[j]] -= 1

for k, i in enumerate(B):
    if k != len(B) - 1:
        print('{} '.format(i), end='')
    else:
        print(i)
