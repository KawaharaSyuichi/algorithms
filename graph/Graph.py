N = 100
n = int(input())
M = []

for i in range(N):
    M.append([])
    for j in range(N):
        M[i].append(0)  # 0オリジンの隣接行列

for _ in range(n):
    inputs = list(map(int, input().split()))
    u = inputs[0]
    k = inputs[1]

    u -= 1  # 0オリジンへ変換
    for i in range(2, 2 + k):
        v = inputs[i]
        v -= 1  # 0オリジンへ変換
        M[u][v] = 1  # 今回は有向グラフ


for i in range(n):
    for j in range(n):
        if j:
            print(' ', end='')
        print(M[i][j], end='')

    print()
