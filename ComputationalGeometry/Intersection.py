# 線分の交差判定
"""
入力例:
3
0 0 3 0 1 1 2 -1
0 0 3 0 3 1 3 -1
0 0 3 0 3 -2 5 0

出力例:
1(交差する場合)
1
0(交差しない場合)
"""


def ccw(x_0, y_0, x_1, y_1, x_2, y_2):
    COUNTER_CLOCLWISE = 1
    CLOCKWISE = -1
    ON_SEGMENT = 0

    a_x = x_1 - x_0
    a_y = y_1 - y_0
    b_x = x_2 - x_0
    b_y = y_2 - y_0

    cross_product = a_x * b_y - a_y * b_x

    a_norm = a_x ** 2 + a_y ** 2
    b_norm = b_x ** 2 + b_y ** 2

    if cross_product > 0:
        return COUNTER_CLOCLWISE
    elif cross_product < 0:
        return CLOCKWISE
    else:
        return ON_SEGMENT


q = int(input())
for _ in range(q):
    x0, y0, x1, y1, x2, y2, x3, y3 = map(int, input().split())

    if (ccw(x0, y0, x1, y1, x2, y2) * ccw(x0, y0, x1, y1, x3, y3) <= 0) and (ccw(x2, y2, x3, y3, x0, y0) * ccw(x2, y2, x3, y3, x1, y1) <= 0):
        print(1)
    else:
        print(0)
