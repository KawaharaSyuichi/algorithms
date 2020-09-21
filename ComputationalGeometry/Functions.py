class Point:  # 点
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


"""
多角形の表現
Polygon = [Point, Point, Point, ...]
"""


class Vector(Point):  # ベクトル
    pass


class Segment:  # 線分
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2


class Line(Segment):  # 直線
    pass


class Circle:  # 円
    def __init__(self, c: Point, r: float):
        self.c = c
        self.r = r
