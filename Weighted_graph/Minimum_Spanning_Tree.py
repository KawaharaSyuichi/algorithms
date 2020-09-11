MAX = 100
INFTY = (1 << 21)
WHITE = 0
GRAY = 1
BLACK = 2

n = int(input())
M = []


def prim():
    u = int()
    minv = int()
    d = []  # d[v]にTに属する頂点とV-Tに属する頂点をつなぐ辺の中で、重みが最小の辺の重みを記録する
    p = []  # p[v]にMSTにおける頂点vの親を記録
    color = []  # 各頂点の訪問履歴

    for _ in range(n):
        d.append(INFTY)
        p.append(-1)
        color.append(WHITE)

    d[0] = 0

    while True:
        minv = INFTY
        u = -1

        for i in range(n):
            if (minv > d[i]) and (color[i] != BLACK):
                u = i
                minv = d[i]

        if u == -1:
            break

        color[u] = BLACK

        for v in range(n):
            if (color[v] != BLACK) and (M[u][v] != INFTY):
                if d[v] > M[u][v]:
                    d[v] = M[u][v]
                    p[v] = u
                    color[v] = GRAY

    sum = 0
    for i in range(n):
        if p[i] != -1:
            sum += M[i][p[i]]

    return sum


for i in range(n):
    M.append([])
    temp = list(map(int, input().split()))
    for e in temp:
        if e == -1:
            M[i].append(INFTY)
        else:
            M[i].append(e)

print(prim())
