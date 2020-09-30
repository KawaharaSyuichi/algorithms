# ナップザック問題
"""
入力例:
4 5
4 2
5 2
2 1
8 3

出力例:
13
"""

NMAX = 105
WMAX = 10005
DIAGONAL = 1  # 品物を選んだ場合
TOP = 0  # 品物を選ばない場合
maxValue = [0]
selection = []


class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def compute(maxValue, selection):
    for w in range(W + 1):
        C[0][w] = 0
        G[0][W] = DIAGONAL

    for i in range(1, N + 1):
        for w in range(1, W + 1):
            C[i][w] = C[i - 1][w]
            G[i][w] = TOP

            if items[i].weight > w:
                continue
            if (items[i].value + C[i - 1][w - items[i].weight] > C[i - 1][w]):
                C[i][w] = items[i].value + C[i - 1][w - items[i].weight]
                G[i][w] = DIAGONAL

    maxValue[0] = C[N][W]

    w = W
    for i in reversed(range(1, N + 1)):
        if G[i][w] == DIAGONAL:
            selection.append(i)
            w -= items[i].weight

    selection.reverse()


items = [0] * (NMAX + 1)  # 品物のリスト
C = []  # どの品物を選ぶかを探索するためのリスト
G = []  # 選んだ品物のリスト

for i in range(NMAX + 1):
    C.append([])
    G.append([])
    for _ in range(WMAX + 1):
        C[i].append(0)
        G[i].append(0)

N, W = map(int, input().split())

for i in range(1, N + 1):
    v, w = map(int, input().split())
    items[i] = Item(v, w)

compute(maxValue, selection)

print(maxValue[0])
