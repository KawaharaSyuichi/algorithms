# 幅優先探索によるトポロジカルソート
"""
入力例：
6 6
0 1
1 2
3 1
3 4
4 5
5 2

出力例：
0
3
1
4
5
2
"""

MAX = 100000
INFTY = (1 << 29)

G = []
for _ in range(MAX):
    G.append([])

out = []
V = []
indeg = [0] * MAX


def bfs(s):
    q = []  # キュー
    q.append(s)
    V[s] = True

    while (len(q) != 0):
        u = q.pop(0)
        out.append(u)

        for i in range(len(G[u])):
            v = G[u][i]
            indeg[v] -= 1

            if indeg[v] == 0 and V[v] == False:
                V[v] = True
                q.append(v)


def tsort():
    for u in range(N):
        for i in range(len(G[u])):
            v = G[u][i]
            indeg[v] += 1

    for u in range(N):
        if indeg[u] == 0 and V[u] == False:
            bfs(u)

    for it in out:
        print(it)


N, M = map(int, input().split())


for _ in range(N):
    V.append(False)


for _ in range(M):
    s, t = map(int, input().split())
    G[s].append(t)

tsort()
