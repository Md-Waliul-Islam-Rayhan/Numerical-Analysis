n = 5
x = [1.0, 1.3, 1.6, 1.9, 2.2]

y = [[0 for i in range(n)]
     for j in range(n)]

y[0][0] = 0.7651977
y[1][0] = 0.6200860
y[2][0] = 0.4554022
y[3][0] = 0.2818186
y[4][0] = 0.1103623

for i in range(1, n):
    for j in range(n - i):
        y[j][i] = (y[j + 1][i - 1] - y[j][i - 1]) / (x[j + i] - x[j])

for i in range(n):
    print(round(x[i], 7), end="\t")
    for j in range(n - i):
        print(format(round(y[i][j], 7), 'f'), end="\t")
    print(' ')

value = 1.5
sum = y[0][0]
product = 1
for i in range(1, n):
    product = product * (value - x[i - 1])
    sum = sum + product * y[0][i]
print('\nValue at', value, 'is :', round(sum, 7))
