def richardson(f, x, n, h):
    d = [[0.0 for i in range(n+1)]for j in range(n+1)]
    for i in range(n + 1):
        d[i][0] = (f(x + h) - f(x)) / h
        powerOf4 = 1
        for j in range(1, i + 1):
            powerOf4 = 4 * powerOf4
            d[i][j] = d[i][j-1] + (d[i][j-1] - d[i-1][j-1]) / (powerOf4 - 1)
        h = 0.5 * h

    return d


def f(a): return (1+a**2)**-1
# math.log(a, math.e)


x = 1.8  # x- value of x to find derivative at
n = 22  # n- number of levels of extrapolation
h = 0.1  # h	- initial stepsize
d = richardson(f, x, n, h)


for i in range(n+1):
    for j in range(i+1):
        print(format(d[i][j], '.10f'), end="\t")
    print()