# 線分の交点
"""
入力例:
3
0 0 2 0 1 1 1 -1
0 0 1 1 0 1 1 0
0 0 1 1 1 0 0 1

出力例:
1.0000000000 0.0000000000
0.5000000000 0.5000000000
0.5000000000 0.5000000000
"""

q = int(input())
for _ in range(q):
    x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3 = map(int, input().split())

    x_base = x_3 - x_2
    y_base = y_3 - y_2

    x_hypo_1 = x_0 - x_2
    y_hypo_1 = y_0 - y_2

    x_hypo_2 = x_1 - x_2
    y_hypo_2 = y_1 - y_2

    d1 = abs(x_base * y_hypo_1 - y_base * x_hypo_1)
    d2 = abs(x_base * y_hypo_2 - y_base * x_hypo_2)

    t = d1 / (d1 + d2)

    x_ans = x_0 + (x_1 - x_0) * t
    y_ans = y_0 + (y_1 - y_0) * t

    print('{} {}'.format(x_ans, y_ans))
