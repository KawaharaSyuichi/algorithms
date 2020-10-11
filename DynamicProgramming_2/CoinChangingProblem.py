# コイン問題
"""
入力例:
15 6
1 2 7 8 12 50

出力例:
2
"""
MMAX = 20  # 硬貨の種類
NMAX = 50000  # 求められる金額の最大値
INFTY = (1 << 29)
T = [INFTY] * (NMAX + 1)
T[0] = 0

n, m = map(int, input().split())  # 1<=n<=50000, 1<=m<=20
C = list(map(int, input().split()))  # 1<=額面<=10000:一枚の硬貨の金額の範囲
C.insert(0, 0)  # 調整(添字0の部分は使わない)

for i in range(1, m + 1):
    for j in range(n + 1):
        if j + C[i] > n:
            break
        T[j + C[i]] = min(T[j + C[i]], T[j] + 1)

print(T[n])
