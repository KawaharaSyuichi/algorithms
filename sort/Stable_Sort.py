import copy


def bubble(C_B, N):
    flag = True
    i = 0

    while flag:
        flag = False

        for j in reversed(range(N)):
            if j < i + 1:
                break

            if C_B[j][1] < C_B[j - 1][1]:
                C_B[j], C_B[j-1] = C_B[j-1], C_B[j]
                flag = True

        i += 1


def selection(C_S, N):
    for i in range(N):
        minj = i

        for j in range(i, N):
            if C_S[j][1] < C_S[minj][1]:
                minj = j

        if minj != i:
            C_S[i], C_S[minj] = C_S[minj], C_S[i]


def isStable(C_B, C_S):
    if C_B == C_S:
        return True
    else:
        return False


C_Bubble = []
C_Select = []

N = int(input())
C_Bubble = list(input().split())
C_Select = copy.copy(C_Bubble)


bubble(C_Bubble, N)
selection(C_Select, N)

print(C_Bubble)
print("Stable")
print(C_Select)
if isStable(C_Bubble, C_Select):
    print("Stable")
else:
    print("Not stable")
