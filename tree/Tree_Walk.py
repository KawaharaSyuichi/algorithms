class Node:
    def __init__(self):
        self.p = NIL
        self.l = NIL
        self.r = NIL


def preParse(u):  # 先行順巡回
    if u == NIL:
        return
    print(" {}".format(u), end="")
    preParse(T[u].l)
    preParse(T[u].r)


def inParse(u):  # 中間順巡回
    if u == NIL:
        return
    inParse(T[u].l)
    print(" {}".format(u), end="")
    inParse(T[u].r)


def postParse(u):  # 後行順巡回
    if u == NIL:
        return
    postParse(T[u].l)
    postParse(T[u].r)
    print(" {}".format(u), end="")


NIL = -1
T = []
root = 0
n = int(input())

for _ in range(n):
    T.append(Node())

for i in range(n):
    v, l, r = map(int, input().split())
    T[v].l = l
    T[v].r = r
    if l != NIL:
        T[l].p = v
    if r != NIL:
        T[r].p = v

for i in range(n):
    if T[i].p == NIL:
        root = i

print("preParse")
preParse(root)
print("")
print("inParse")
inParse(root)
print("")
print("postParse")
postParse(root)
print("")
