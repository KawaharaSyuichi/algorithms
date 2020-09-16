# 全点対間最短経路
"""
入力例1：
4 6
0 1 1
0 2 5
1 2 2
1 3 4
2 3 1
3 2 7

出力例1：
0 1 3 4
INF 0 2 3
INF INF 0 1
INF INF 7 0

入力例2：
4 6
0 1 1
0 2 -5
1 2 2
1 3 4
2 3 1
3 2 7

出力例2：
0 1 -5 -4
INF 0 2 3
INF INF 0 1
INF INF 7 0

入力例3：
4 6
0 1 1
0 2 5
1 2 2
1 3 4
2 3 1
3 2 -7

出力例3：
NEGATIVE CYCLE

"""


MAX = 100
INFTY = (1 << 32)


def floyd():
    for k in range(n):
        for i in range(n):
            if d[i][k] == INFTY:
                continue
            for j in range(n):
                if d[k][j] == INFTY:
                    continue
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])


n, e = map(int, input().split())
d = []
for i in range(n):
    d.append([])
    for j in range(n):
        if i == j:
            d[i].append(0)
        else:
            d[i].append(INFTY)

for _ in range(e):
    u, v, c = map(int, input().split())
    d[u][v] = c

floyd()

negative = False
for i in range(n):
    if d[i][i] < 0:
        negative = True

if (negative):
    print('NEGATIVE CYCLE')
else:
    for i in range(n):
        for j in range(n):
            if j:
                print(' ', end='')
            if (d[i][j] == INFTY):
                print('INF', end='')
            else:
                print(d[i][j], end='')
        print()
