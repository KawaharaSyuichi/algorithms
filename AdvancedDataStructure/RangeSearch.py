# 領域探索(作成途中)
"""
入力例：
6
2 1
2 2
4 2
6 2
3 3
5 4
2
2 4 0 4
4 10 2 5

出力例：
0
1
2
4

2
3
5
"""

MAX = 1000000
NIL = -1

P = []
T = []
N = int(input())

for i in range(N):
    x, y = map(int, input().split())
    P.append(Point(i, x, y))
    T.append(Node())

np = 0


class Node:
    def __init__(self):
        self.location = int()
        self.p = NIL
        self.l = NIL
        self.r = NIL


class Point:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y


def lessX(p1, p2):
    return p1.x < p2.x


def lessY(p1, p2):
    return p1.y < p2.y


def makeKDTree(l, r, depth):
    if not (l < r):
        return NIL

    mid = (l + r) / 2
    t = np
    np += 1

    if (depth % 2 == 0):
        reverse_flag = lessX(P[l], P[r - 1])
        P.sort(reverse=reverse_flag)
    else:
        reverse_flag = lessY(P[l], P[r - 1])
        P.sort(reverse=reverse_flag)

    T[t].location = mid
    T[t].l = makeKDTree(l, mid, depth + 1)
    T[t].r = makeKDTree(mid + 1, r, depth + 1)

    return t


def find(v, sx, tx, sy, ty, depth, ans):
    x = P[T[v].location].x
    y = P[T[v].location].y

    if (sx <= x and x <= tx and sy <= y and y <= ty):
        ans.append(P[T[v].location])

    if (depth % 2 == 0):
        if (T[v].l != NIL):
            if (sx <= x):
                find(T[v].l, sx, tx, sy, ty, depth + 1, ans)
        if (T[v].r != NIL):
            if (x <= tx):
                find(T[v].r, sx, tx, sy, ty, depth + 1, ans)
    else:
        if (T[v].l != NIL):
            if (sy <= y):
                find(T[v].l, sx, tx, sy, ty, depth + 1, ans)
        if (T[v].r != NIL):
            if (y <= ty):
                find(T[v].r, sx, tx, sy, ty, depth + 1, ans)


root = makeKDTree(0, N, 0)

q = int(input())
ans = []
for _ in range(q):
    sx, tx, sy, ty = map(int, input().split())
    ans.clear()
    find(root, sx, tx, sy, ty, 0, ans)
    ans.sort()

    for _ in range(len(ans)):
        print(ans[i].id)

    print('')
