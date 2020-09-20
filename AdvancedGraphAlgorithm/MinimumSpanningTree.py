# 最小全域木
"""
クラスカルのアルゴリズム
1. グラフG=(V,E)の辺eiを、重みの昇順(比減少順)に整列する
2. 最小全域木の辺の集合をKとして、それを空に初期化する
3. i=1,2,3,...,|E|の順番に、|K|が|V-1|になるまで、K U {ei}が閉路を作らないようなeiをKに追加する
"""

"""
クラスカルのアルゴリズム(Union-Findを使う)

kruskal(V,E)
    Eの要素を整列//e1,e2,...
    Vに対応した互いに素な集合Sを生成する
    辺の集合Kを空にする

    for i=1 to |E|
        if S.findSet(e[i].source) != S.findSet(e[i].target) //not same(a,b)
            S.unite(e[i].source , e[i].target)
            K.push(e[i])

    return K
"""

"""
入力例:
6 9
0 1 1
0 2 3
1 2 1
1 3 7
2 4 1
1 4 3
3 4 1
3 5 1
4 5 6

出力例:
5
"""

MAX = 10000
INFTY = (1 << 29)


class DisjointSet:
    def __init__(self, size):
        self.rank = [0] * size  # rank[x]：ノードxを木の親としたときの木の高さ
        self.p = [0] * size  # p[x]：ノードxの親

        for i in range(size):
            self.makeSet(i)

    def makeSet(self, x):
        self.p[x] = x  # 自分自身を親
        self.rank[x] = 0  # 最初は自分だけなので木の高さは0

    def same(self, x, y):  # xとyが同じ集合に属しているのかどうかを確認
        return (self.findSet(x) == self.findSet(y))

    def unite(self, x, y):  # 結合
        self.link(self.findSet(x), self.findSet(y))

    def link(self, x_root, y_root):  # x_root(y_root):x(y)が属する集合の親
        if (self.rank[x_root] > self.rank[y_root]):
            self.p[y_root] = x_root
        else:
            self.p[x_root] = y_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[y_root] += 1

    def findSet(self, x):  # xが属する集合の親を返す
        if x != self.p[x]:
            self.p[x] = self.findSet(self.p[x])

        return self.p[x]


class Edge:
    def __init__(self, source, target, cost):
        self.source = source
        self.target = target
        self.cost = cost


def kruskal(N, edges):
    totalCost = 0
    edges.sort(key=lambda x: x.cost)  # 辺の重みを昇順で整列

    dset = DisjointSet(N + 1)

    for i in range(N):
        dset.makeSet(i)

    for i in range(len(edges)):
        e = edges[i]
        if not dset.same(e.source, e.target):
            # MST.append(e)
            totalCost += e.cost
            dset.unite(e.source, e.target)

    return totalCost


N, M = map(int, input().split())  # N:頂点の数 , M:辺の数
edges = []

for _ in range(M):
    source, target, cost = map(int, input().split())
    edges.append(Edge(source, target, cost))

print(kruskal(N, edges))
