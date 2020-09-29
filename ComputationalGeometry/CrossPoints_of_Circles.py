# 円と円の交点
"""
入力例:
0 0 2
2 0 2
出力例:
1.0000000 -1.7320508 1.0000000 1.7320508
"""

import math

c1_x, c1_y, c1_r = map(int, input().split())
c2_x, c2_y, c2_r = map(int, input().split())

d = math.sqrt((c2_x - c1_x) ** 2 + (c2_y - c1_y) ** 2)  # d:二つの円の中心間距離

# a:c1の中心から交点に向かうベクトルと二つの円が作る直線からなる角度
a = math.acos((c1_r ** 2 + d ** 2 - c2_r ** 2) / (2 * c1_r * d))  # 余弦定理

# t:x軸と二つの円の中心を結ぶ直線からなる角度
t = math.atan2((c2_y - c1_y), (c2_x - c1_x))

cross_x1 = math.cos(t + a) * c1_r
cross_y1 = math.sin(t + a) * c1_r

cross_x2 = math.cos(t - a) * c1_r
cross_y2 = math.sin(t - a) * c1_r

ans_x1 = c1_x + cross_x1
ans_y1 = c1_y + cross_y1

ans_x2 = c1_x + cross_x2
ans_y2 = c1_y + cross_y2

if ans_x1 < ans_x2:
    print('{} {} {} {}'.format(ans_x1, ans_y1, ans_x2, ans_y2))
elif ans_x1 > ans_x2:
    print('{} {} {} {}'.format(ans_x2, ans_y2, ans_x1, ans_y1))
else:
    if ans_y1 < ans_y2:
        print('{} {} {} {}'.format(ans_x1, ans_y1, ans_x2, ans_y2))
    else:
        print('{} {} {} {}'.format(ans_x2, ans_y2, ans_x1, ans_y1))
