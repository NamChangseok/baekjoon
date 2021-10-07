
a = []

for i in range(9):
    a.append(int(input()))


max = max(a)
where = a.index(max)
print(max)
print(where+1)
