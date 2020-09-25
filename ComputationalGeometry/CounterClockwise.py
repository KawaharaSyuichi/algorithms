# 半時計回り
"""
入力例:
0 0 2 0
5
-1 1
-1 -1
-1 0
0 0
3 0

出力例:
COUNTER_CLOCKWISE
CLOCKWISE
ONLINE_BACK
ON_SEGMENT
ONLINE_FRONT
"""

COUNTER_CLOCLWISE = 1
CLOCKWISE = -1
ONLINE_BACK = 2
ONLINE_FRONT = -2
ON_SEGMENT = 0

x_0, y_0, x_1, y_1 = map(int, input().split())
q = int(input())

for _ in range(q):
    x_2, y_2 = map(int, input().split())

    a_x = x_1 - x_0
    a_y = y_1 - y_0

    b_x = x_2 - x_0
    b_y = y_2 - y_0

    cross_product = a_x * b_y - a_y * b_x
    inner_product = a_x * b_x + a_y * b_y

    a_norm = a_x ** 2 + a_y ** 2
    b_norm = b_x ** 2 + b_y ** 2

    if cross_product > 0:
        print('COUNTER_CLOCLWISE')
    elif cross_product < 0:
        print('CLOCKWISE')
    elif inner_product < 0:
        print('ONLINE_BACK')
    elif a_norm < b_norm:
        print('ONLINE_FRONT')
    else:
        print('ON_SEGMENT')
