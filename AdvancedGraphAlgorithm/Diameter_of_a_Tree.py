# 木の直径(未完成。どこがダメか分からん)
"""
非負の重みを持つ無向の木Tの直径(木の最遠節点間の距離)

入力例1：
4
0 1 2
1 2 1
1 3 3

出力例1：
5

入力例2：
4
0 1 1
1 2 2
2 3 4

出力例2：
7
"""
import queue

n = int(input())

INFTY = (1 << 30)
G = []
d = [INFTY] * n


class Edge:
    def __init__(self, t, w):
        self.t = t
        self.w = w


def bfs(s):  # 幅優先探索
    Q = queue.Queue()  # キュー
    Q.put(s)
    d[s] = 0
    u = int()

    while not Q.empty():
        u = Q.get()
        for i in range(len(G[u])):
            e = G[u][i]
            if d[e.t] == INFTY:
                d[e.t] = d[u] + e.w
                Q.put(e.t)


def solve():
    # 適当な視点sから最も遠い節点tgtを求める
    bfs(0)

    maxv = 0
    tgt = 0

    for i in range(n):
        if d[i] == INFTY:
            continue
        if maxv < d[i]:
            maxv = d[i]
            tgt = i

    # tgtから最も遠い節点の距離maxvを求める
    bfs(tgt)
    maxv = 0
    for i in range(n):
        if d[i] == INFTY:
            continue
        maxv = max(maxv, d[i])

    print(maxv)


for _ in range(n):
    G.append([])

for _ in range(n - 1):
    s, t, w = map(int, input().split())

    G[s].append(Edge(t, w))
    G[t].append(Edge(s, w))

solve()
