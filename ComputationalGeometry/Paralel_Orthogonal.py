# 直線の直交・平行判定
"""
入力例：
3
0 0 3 0 0 2 3 2
0 0 3 0 1 1 1 4
0 0 3 0 1 1 2 2

出力例：
2
1
0
"""
q = int(input())

for _ in range(q):
    x0, y0, x1, y1, x2, y2, x3, y3 = map(int, input().split())

    p1_x = x1 - x0
    p1_y = y1 - y0

    p2_x = x3 - x2
    p2_y = y3 - y2

    if ((p1_x * p2_x + p1_y * p2_y) == 0):  # 二つの直線が直交
        print(1)
    elif ((p1_x * p2_y - p1_y * p2_x) == 0):  # 二つの直線が平行(外積が0、つまり、二つの直線が作る平行四辺形の面積が0)
        print(2)
    else:
        print(0)
