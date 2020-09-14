"""
入力例：
5 12
0 1 4
0 2 3
1 1 2
1 3 4
1 1 4
1 3 2
0 1 3
1 2 4
1 3 0
0 0 4
1 0 2
1 3 0

出力：
0
0
1
1
1
0
1
1
"""


class DisjointSet:
    def __init__(self, size):
        self.rank = [0] * size  # rank[x]：ノードxを木の親としたときの木の高さ
        self.p = [0] * size  # p[x]：ノードxの親

        for i in range(n):
            self.p[i] = i  # 自分自身を親
            self.rank[i] = 0  # 最初は自分だけなので木の高さは0

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


n, q = map(int, input().split())
ds = DisjointSet(n)

for _ in range(q):
    com, a, b = map(int, input().split())
    if com == 0:  # uniteの場合
        ds.unite(a, b)  # 要素aと要素bを持つ集合を結合
    else:  # sameの場合
        if ds.same(a, b):
            print(1)
        else:
            print(0)
