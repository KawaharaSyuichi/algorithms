N = 100
n = int(input())
p = []
for _ in range(N + 1):
    p.append(0)

m = []
for i in range(N + 1):
    m.append([])
    for _ in range(N + 1):
        m[i].append(0)

for i in range(1, n + 1):
    p[i - 1], p[i] = map(int, input().split())

for l in range(2, n + 1):
    for i in range(1, (n - l + 1) + 1):
        j = i + l - 1
        m[i][j] = (1 << 21)

        for k in range(i, (j - 1) + 1):
            m[i][j] = min(m[i][j], m[i][k] + m[k + 1]
                          [j] + p[i - 1] * p[k] * p[j])

print(m[1][n])
