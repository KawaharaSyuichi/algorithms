NIL = -1
n = int(input())
T = []
D = [0] * n
H = [0] * n
root = 0


class Node:
    def __init__(self):
        self.parent = NIL
        self.left = NIL
        self.right = NIL


def setDepth(u, d):
    if u == NIL:
        return
    D[u] = d
    setDepth(T[u].left, d + 1)
    setDepth(T[u].right, d + 1)


def setHeight(u):
    h1 = h2 = 0
    if T[u].left != NIL:
        h1 = setHeight(T[u].left) + 1
    if T[u].right != NIL:
        h2 = setHeight(T[u].right) + 1

    if h1 > h2:
        H[u] = h1
    else:
        H[u] = h2

    return H[u]


def getSibling(u):  # 接点uの兄弟を返す
    if T[u].parent == NIL:  # 根の場合
        return NIL

    if T[T[u].parent].left != u and T[T[u].parent].left != NIL:  # 右にいるノードが左にいる兄弟の有無を調べる場合
        return T[T[u].parent].left

    if T[T[u].parent].right != u and T[T[u].parent].right != NIL:  # 左にいるノードが右にいる兄弟の有無を調べる場合
        return T[T[u].parent].right

    return NIL  # 兄弟がいない場合


def print_tree(u):
    print("node {}: ".format(u), end='')
    print("parent={}, ".format(T[u].parent), end='')
    print("sibling={}, ".format(getSibling(u)), end='')
    deg = 0
    if T[u].left != NIL:
        deg += 1
    if T[u].right != NIL:
        deg += 1
    print("degree={}, ".format(deg), end='')
    print("depth={}, ".format(D[u]), end='')
    print("height={}, ".format(H[u]), end='')

    if T[u].parent == NIL:
        print("root")
    elif T[u].left == NIL and T[u].right == NIL:
        print("leaf")
    else:
        print("internal node")


for _ in range(n):
    T.append(Node())

for _ in range(n):
    v, l, r = map(int, input().split())
    T[v].left = l
    T[v].right = r

    if l != NIL:
        T[l].parent = v
    if r != NIL:
        T[r].parent = v

for i in range(n):
    if T[i].parent == NIL:
        root = i

setDepth(root, 0)
setHeight(root)

for i in range(n):
    print_tree(i)
