n = 5
x = [1.0, 1.3, 1.6, 1.9, 2.2]
y = [0.7651977, 0.6200860, 0.4554022, 0.2818186, 0.1103623]

value = 1.5
p = 0
for i in range(n):
    L = 1
    for k in range(n):
        if i != k:
            L = L * (value - x[k]) / (x[i] - x[k])
    p = p + y[i] * L
print('\n Value at', value, 'is', round(p, 9))
