N = 100
INFTY = (1 << 21)

d = []
for _ in range(N):
    d.append(0)

M = []
for i in range(N):
    M.append([])
    for _ in range(N):
        M[i].append(0)

n = int(input())


def bfs(s):
    q = []
    q.append(s)

    for i in range(n):
        d[i] = INFTY
    d[s] = 0

    while len(q) != 0:
        u = q.pop(0)
        for v in range(n):
            if M[u][v] == 0:
                continue
            if d[v] != INFTY:
                continue
            d[v] = d[u] + 1
            q.append(v)

    for i in range(n):
        dis = -1
        if d[i] != INFTY:
            dis = d[i]

        print('{} {}'.format(i + 1, dis))


for _ in range(n):
    inputs = list(map(int, input().split()))
    u = inputs[0]
    k = inputs[1]
    u -= 1  # 0オリジンへ変換

    for j in range(2, k + 2):
        v = inputs[j]
        v -= 1  # 0オリジンへ変換
        M[u][v] = 1

bfs(0)
