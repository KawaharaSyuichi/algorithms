N = 1000
n = int(input())
s1 = str()
s2 = str()


def lcs(X, Y):
    c = []
    for i in range(N + 1):
        c.append([])
        for _ in range(N + 1):
            c[i].append(0)
    m = len(X)
    n = len(Y)
    maxl = 0
    X = ' ' + X  # Xの先頭に空白を挿入
    Y = ' ' + Y  # Yの先頭に空白を挿入

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i] == Y[j]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])

            maxl = max(maxl, c[i][j])

    return maxl


for _ in range(n):
    s1 = input()
    s2 = input()
    print(lcs(s1, s2))
