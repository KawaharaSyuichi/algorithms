n = int(input())
A = list(map(int, input().split()))
A.append(0)  # for sentinel
q = int(input())
T = list(map(int, input().split()))
same_num_sum = 0


def search(A, n, key):
    A[n] = key
    i = 0

    while A[i] != key:
        i += 1

    return i != n


for key in T:
    if search(A, n, key):
        same_num_sum += 1

print(same_num_sum)
