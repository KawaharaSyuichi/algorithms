import heapq

MAX = 10000
INFTY = (1 << 20)
WHITE = 0
GRAY = 1
BLACK = 2

n = int(input())

# 重み付き有向グラフの隣接リスト表現(adj=[([int() , int()) , ([int() , int()) , ...] , [([int() , int()) , ([int() , int()) , ...])
adj = []


def dijkstra():
    PQ = []
    heapq.heapify(PQ)
    color = [WHITE] * MAX
    d = [INFTY] * MAX

    d[0] = 0
    heapq.heappush(PQ, [0, 0])
    color[0] = GRAY

    while (len(PQ) != 0):
        f = heapq.heappop(PQ)
        u = f[1]
        color[u] = BLACK

        # 最小値を取り出し、それが最短でなければ無視
        if (d[u] < f[0]):
            continue

        for j in range(len(adj[u])):
            v = adj[u][j][0]
            if color[v] == BLACK:
                continue
            if (d[v] > d[u] + adj[u][j][1]):
                d[v] = d[u] + adj[u][j][1]
                # priority_queueはデフォルトで大きい値を優先するため-1を掛ける
                heapq.heappush(PQ, [d[v], v])

                color[v] = GRAY

    for i in range(n):
        temp = int()
        if d[i] == INFTY:
            temp = -1
        else:
            temp = d[i]
        print('{} {}'.format(i, temp))


for i in range(MAX):
    adj.append([])

for _ in range(n):
    inputs = list(map(int, input().split()))
    u = inputs.pop(0)
    k = inputs.pop(0)
    for i in range(k):
        v = inputs[i * 2]
        c = inputs[i * 2 + 1]
        adj[u].append([v, c])


dijkstra()
