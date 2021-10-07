

N = int(input())
A = 1
M = N
for i in range(N):

    M -= 1
    print(' '*(M) + '*' * A)
    A += 1
