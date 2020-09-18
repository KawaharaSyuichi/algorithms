# 関節点(理解できてない)
"""
関節点とは：
連結グラフG=(V,E)において、頂点uとuから出ている全ての辺を削除して得られる部分グラフが、非連結になるとき、頂点uをグラフGの関節点(切断点)と言う。
"""

"""
入力例：
4 4
0 1
0 2
1 2
2 3

出力例：
2
"""

MAX = 100000
G = []
visited = [False] * MAX

prenum = [0] * MAX  # prenum[v]:幅優先探索(DFS)において、頂点vを何番目に訪問するか
parent = [0] * MAX  # parent[v]: DFSTreeにおける頂点vの親
lowest = [0] * MAX  # lowest[v]:DFSにおいて頂点vの訪問が完了する順番
timer = int()


def dfs(current, prev):
    # ノードcurrentを訪問した直後の処理
    global timer
    prenum[current] = lowest[current] = timer
    timer += 1

    visited[current] = True

    next_ = int()

    for i in range(len(G[current])):
        next_ = G[current][i]

        if (visited[next_] == False):
            # ノードcurrentからノードnext_へ訪問する直前の処理
            parent[next_] = current

            dfs(next_, current)
            # ノードnext_の探索が終了した直後の処理
            lowest[current] = min(lowest[current], lowest[next_])
        elif (next_ != prev):
            # エッジcurrent-->nextがBack-edgeの場合の処理
            lowest[current] = min(lowest[current], prenum[next_])

    # ノードcurrentの探索が終了した直後の処理


def art_points():
    timer = 1

    # lowestの計算
    dfs(0, -1)  # 0==root
    ap = []
    np = 0

    for i in range(1, N):
        p = parent[i]
        if p == 0:
            np += 1
        elif (prenum[p] <= lowest[i]):
            ap.append(p)

    if (np > 1):
        ap.insert(0)

    for i in ap:
        print(i)


N, m = map(int, input().split())

for _ in range(N):
    G.append([])

for _ in range(m):
    s, t = map(int, input().split())
    G[s].append(t)
    G[t].append(s)

art_points()
