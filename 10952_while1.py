# 각 테스트 케이스마다 A+B를 출력한다.

while 1:
    input_data = (input().split(' '))
    a = int(input_data[0])
    b = int(input_data[1])

    if a == 0 and b == 0:
        break
    else:
        print(a+b)
