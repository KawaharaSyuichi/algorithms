#最長増加部分列(理解できてない & バクあり)
"""
入力例:
5
5
1
3
2
4

出力例:
3
"""
import bisect
# C++のlower_boundはbisect.bisect_leftに該当

MAX = 100000
A = [0] * (MAX + 1)
L = [0] * MAX
n = int(input())


def lis():
    L[0] = A[0]
    length = 1

    for i in range(1, n):
        if L[length - 1] < A[i]:
            L[length] = A[i]
            length += 1
        else:
            input_index = bisect.bisect_left(L, A[i])
            A[input_index] = A[i]

    return length


for i in range(n):
    a = int(input())
    A[i] = a

print(lis())
