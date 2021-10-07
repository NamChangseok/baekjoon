# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

N = int(input())
A = 1
for i in range(N):
    print('*' * A)
    A += 1
