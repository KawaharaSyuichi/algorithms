# 射影
"""
入力例：
0 0 3 4
1
2 5

出力例:
3.12 4.16
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
    x_ans = x_p1 + x_base * rate
    y_ans = y_p1 + y_base * rate

    print(x_ans, y_ans)
