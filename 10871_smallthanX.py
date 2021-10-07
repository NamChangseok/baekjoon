# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.

input_data = input().split()

N = int(input_data[0])
X = int(input_data[1])


a = list(map(int, input().split(' ')))

for i in a:
    if X > i:
        print(i)
