# 円と直線の交点
"""
入力例:
2 1 1
2 
0 1 4 1
3 0 3 3

出力例:
1.000000 1.000000 3.000000 1.000000
3.000000 1.000000 3.000000 1.000000
"""

import math
c_x, c_y, r = map(int, input().split())
q = int(input())

for _ in range(q):
    x_p1, y_p1, x_p2, y_p2 = map(int, input().split())
    x_base = x_p2 - x_p1
    y_base = y_p2 - y_p1
    base_norm = math.sqrt(x_base ** 2 + y_base ** 2)

    x_hypo = c_x - x_p1
    y_hypo = c_y - y_p1

    rate = ((x_base * x_hypo + y_base * y_hypo) / base_norm) / base_norm
    cross_x = x_p1 + x_base * rate  # 円の中心から直線に垂線を引いたときの交点のx座標
    cross_y = y_p1 + y_base * rate  # 円の中心から直線に垂線を引いたときの交点のy座標

    e_x = x_base / base_norm  # 直線の単位ベクトルのx成分
    e_y = y_base / base_norm  # 直線の単位ベクトルのy成分

    pr_len_square = (cross_x - c_x) ** 2 + (cross_y - c_y) ** 2

    base = math.sqrt(r ** 2 - pr_len_square)

    x_ans_1 = cross_x + e_x * base
    y_ans_1 = cross_y + e_y * base

    x_ans_2 = cross_x - e_x * base
    y_ans_2 = cross_y - e_y * base

    if x_ans_1 <= x_ans_2:
        print('{} {} {} {}'.format(x_ans_1, y_ans_1, x_ans_2, y_ans_2))
    else:
        print('{} {} {} {}'.format(x_ans_2, y_ans_2, x_ans_1, y_ans_1))
