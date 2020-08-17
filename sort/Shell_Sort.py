n = int(input())
A = []
G = []
cnt = 0


def insertionSort(A, n, g):
    for i in range(g, n):
        v = A[i]
        j = i - g

        while (j >= 0 and A[j] > v):
            A[j + g] = A[j]
            j -= g
            global cnt
            cnt += 1

        A[j+g] = v


def shellSort(A, n):
    #　数列Gを生成
    h = 1
    while True:
        if h > n:
            break
        G.append(h)
        h = h * 3 + 1

    for i in reversed(range(len(G))):
        insertionSort(A, n, G[i])


for _ in range(n):
    A.append(int(input()))

shellSort(A, n)

print(len(G))
G.reverse()
print(G)
print(cnt)
for i in range(n):
    print(A[i])
