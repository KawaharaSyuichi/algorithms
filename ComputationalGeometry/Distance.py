# 距離(?)
"""
入力例:
3
0 0 1 0 0 1 1 1
0 0 1 0 2 1 1 2
-1 0 1 0 0 1 0 -1

出力例:
1.0000000000
1.4142135624
0.0000000000
"""
import math

q = int(input())
for _ in range(q):
    x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3 = map(int, input().split())

    a_x = x_1 - x_0
    a_y = y_1 - y_0

    b_x = x_2 - x_0
    b_y = y_2 - y_0

    d = (a_x * b_y - a_y * b_x) / math.sqrt(a_x ** 2 + a_y ** 2)

    print(d)
