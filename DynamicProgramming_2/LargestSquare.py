# 最大正方形(理解できてない)
"""
入力例:
4 5
0 0 1 0 0
1 0 0 0 0
0 0 0 1 0
0 0 0 1 0

出力例:
4
"""

MAX = 1400
dp = []
G = []

for i in range(MAX):
    dp.append([])
    G.append([])
    for _ in range(MAX):
        dp[i].append(0)
        G[i].append(0)

H, W = map(int, input().split())


def getLargestSquare(H, W):
    maxWidth = 0

    for i in range(H):
        for j in range(W):
            dp[i][j] = (G[i][j] + 1) % 2
            maxWidth |= dp[i][j]

    for i in range(1, H):
        for j in range(1, W):
            if G[i][j]:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i - 1][j - 1],
                               min(dp[i - 1][j], dp[i][j - 1])) + 1
                maxWidth = max(maxWidth, dp[i][j])

    return maxWidth ** 2


for i in range(H):
    temp = list(map(int, input().split()))
    for j, k in enumerate(temp):
        G[i][j] = k

print(getLargestSquare(H, W))
