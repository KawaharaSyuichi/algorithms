n, q = map(int, input().split())
Q = []
time = 0

for _ in range(n):
    process_name, process_time = input().split()
    Q.append([process_name, int(process_time)])

while len(Q) != 0:
    if Q[0][1] > q:
        temp_name = Q[0][0]
        temp_time = Q[0][1] - q
        Q.pop(0)
        Q.append([temp_name, temp_time])
        time += q
    else:
        time += Q[0][1]
        print("{} {}".format(Q[0][0], time))
        Q.pop(0)
