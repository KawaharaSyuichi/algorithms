n = int(input())
A = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))
same_num_sum = 0


def binaryseach(A, n, key):
    left = 0
    right = n

    while left < right:
        mid = int((left + right) / 2)

        if A[mid] == key:
            return True
        elif key < A[mid]:
            right = mid
        else:
            left = mid + 1

    return False


for key in T:
    if binaryseach(A, n, key):
        same_num_sum += 1

print(same_num_sum)
