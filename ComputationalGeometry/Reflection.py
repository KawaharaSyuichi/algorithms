# 反射
"""
入力例：
0 0 3 4
3
2 5
1 4
0 3

出力例:
4.24 3.32
3.56 2.08
2.88 0.84
"""
import math

x_p1, y_p1, x_p2, y_p2 = map(int, input().split())
x_base = x_p2 - x_p1
y_base = y_p2 - y_p1
base_norm = math.sqrt(x_base ** 2 + y_base ** 2)


q = int(input())
for _ in range(q):
    x, y = map(int, input().split())
    x_hypo = x - x_p1
    y_hypo = y - y_p1

    rate = ((x_base * x_hypo + y_base * y_hypo) / base_norm) / base_norm
    x_projection = x_p1 + x_base * rate
    y_projection = y_p1 + y_base * rate

    x_projection_vector = (x_projection - x) * 2
    y_projection_vector = (y_projection - y) * 2

    x_ans = x + x_projection_vector
    y_ans = y + y_projection_vector

    print(x_ans)
    print(y_ans)
