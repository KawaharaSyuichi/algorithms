n = int(input())
M = []
color = []
d = [0] * 100
f = [0] * 100
tt = [int()]
WHITE = 0
GRAY = 1
BLACK = 2


def dfs_visit(u, tt):  # スタックを用いた深さ優先探索
    color[u] = GRAY

    tt[0] += 1
    d[u] = tt[0]

    for v in range(n):
        if M[u][v] == 0:
            continue
        if color[v] == WHITE:
            dfs_visit(v, tt)

    color[u] = BLACK
    tt[0] += 1
    f[u] = tt[0]  # 訪問の完了


def dfs(tt):
    # 初期化
    for _ in range(n):
        color.append(WHITE)

    tt[0] = 0

    # 未訪問のuを始点として深さ優先探索
    for u in range(n):
        if color[u] == WHITE:
            dfs_visit(u, tt)
    for u in range(n):
        print('{} {} {}'.format(u + 1, d[u], f[u]))


for i in range(n):
    M.append([])
    for _ in range(n):
        M[i].append(0)

for _ in range(n):
    inputs = list(map(int, input().split()))
    u = inputs[0]
    k = inputs[1]

    u -= 1  # 0オリジンへ変換
    for j in range(2, k + 2):
        v = inputs[j]
        v -= 1  # 0オリジンへ変換
        M[u][v] = 1

dfs(tt)
