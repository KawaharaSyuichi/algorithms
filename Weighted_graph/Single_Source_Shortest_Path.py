MAX = 100
INFTY = (1 << 21)
WHITE = 0
GRAY = 1
BLACK = 2

n = int(input())
M = []


def dijkstra():
    minv = int()
    d = [INFTY] * MAX
    color = [WHITE] * MAX

    d[0] = 0
    color[0] = GRAY

    while True:
        minv = INFTY
        u = -1
        for i in range(n):
            if (minv > d[i]) and (color[i] != BLACK):
                u = i
                minv = d[i]

        if u == -1:
            break

        color[u] = BLACK

        for v in range(n):
            if (color[v] != BLACK) and (M[u][v] != INFTY):
                if (d[v] > d[u] + M[u][v]):
                    d[v] = d[u] + M[u][v]
                    color[v] = GRAY

    for i in range(n):
        dis = int()
        if d[i] == INFTY:
            dis = -1
        else:
            dis = d[i]
        print("{} {}".format(i, dis))


for i in range(MAX):
    M.append([])
    for _ in range(MAX):
        M[i].append(INFTY)

for _ in range(n):
    inputs = list(map(int, input().split()))
    u = inputs.pop(0)
    k = inputs.pop(0)
    for i in range(k):
        v = inputs[i * 2]
        c = inputs[i * 2 + 1]
        M[u][v] = c


dijkstra()
