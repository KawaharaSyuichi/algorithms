import math


class Point:
    def __init__(self):
        self.x = float()
        self.y = float()


def koch(n, a, b):
    if n == 0:
        return

    s = Point()
    t = Point()
    u = Point()

    th = math.pi * 60.0 / 180.0  # angle to radian

    s.x = (2.0 * a.x + 1.0 * b.x)/3.0
    s.y = (2.0 * a.y + 1.0 * b.y) / 3.0
    t.x = (1.0 * a.x + 2.0 * b.x) / 3.0
    t.y = (2.0 * a.y + 1.0 * b.y) / 3.0
    u.x = (t.x - s.x) * math.cos(th) - (t.y - s.y) * math.sin(th) + s.x
    u.y = (t.x - s.x) * math.sin(th) + (t.y - s.y) * math.cos(th) + s.y

    koch(n - 1, a, s)
    print('{0:.8f} {1:.8f}'.format(s.x, s.y))
    koch(n - 1, s, u)
    print('{0:.8f} {1:.8f}'.format(u.x, u.y))
    koch(n - 1, u, t)
    print('{0:.8f} {1:.8f}'.format(t.x, t.y))
    koch(n - 1, t, b)


a = Point()
b = Point()
n = int(input())

a.x = 0.0
a.y = 0.0
b.x = 100.0
b.y = 0.0

print('{0:.8f} {1:.8f}'.format(a.x, a.y))
koch(n, a, b)
print("{0:.8f} {1:.8f}".format(b.x, b.y))
