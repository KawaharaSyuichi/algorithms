n = int(input())
R = []

for _ in range(n):
    R.append(int(input()))

maxv = -2000000000
minv = R[0]

for i in range(n - 1):
    if maxv < (R[i + 1] - minv):
        maxv = R[i + 1] - minv

    if minv > R[i + 1]:
        minv = R[i + 1]

print(maxv)
