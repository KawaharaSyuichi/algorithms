T = []
D = [0] * 100005
NIL = -1


class Node:
    def __init__(self):
        self.p = NIL
        self.l = NIL
        self.r = NIL


def rec(u, p):  # 再帰的に深さを求める
    D[u] = p
    if T[u].r != NIL:
        rec(T[u].r, p)  # 右の兄弟に同じ深さを設定
    if T[u].l != NIL:
        rec(T[u].l, p + 1)  # 最も左の子に自分の深さ+1を設定


def print_threes(u):
    print("node {}: parent = {}, depth = {}, ".format(u, T[u].p, D[u]), end='')

    if T[u].p == NIL:
        print("root, ", end='')
    elif T[u].l == NIL:
        print("leaf, ", end='')
    else:
        print("internal node, ", end='')

    print("[", end='')

    c = T[u].l
    i = 0
    while c != NIL:
        if i:
            print(", ", end='')
        print(c, end='')
        i += 1
        c = T[c].r

    print("]")


n = int(input())
for _ in range(n):
    T.append(Node())

for _ in range(n):
    temp = list(map(int, input().split()))
    v = temp[0]
    d = temp[1]

    for j in range(d):
        c = temp[2 + j]
        if j == 0:
            T[v].l = c
        else:
            T[l].r = c

        l = c
        T[c].p = v

for i in range(n):
    if T[i].p == NIL:
        r = i

rec(r, 0)

for i in range(n):
    print_threes(i)
