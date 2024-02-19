def iteration(g, p0, TOL, N0):
    print('  n', '        p0', '        Error', )
    print('-----------------------------------')
    i = 1
    while i <= N0:
        p = g(p0)
        print(format(i, '3d'), '  ', format(p0, '10.8f'), '  ', format(abs(p - p0), '10.2e'))
        if abs(p - p0) < TOL:
            print('-----------------------------------')
            return print('The solution is ', p)
        i = i + 1
        p0 = p
    print('The method fails after N0 iterations')
    return None


g1 = lambda x: x - x ** 3 - 4 * x ** 2 + 10
g2 = lambda x: (10 / x - 4 * x) ** 0.5
g3 = lambda x: 0.5 * (10 - x ** 3) ** 0.5
g4 = lambda x: (10 / (4 + x) ** 0.5)
g5 = lambda x: x - (x ** 3 - 4 * x ** 2 - 10) / (3 * x ** 2 + 8 * x)

# iteration(g1,1.5,.0001,25)
# iteration(g2,1.5,.0001,35)
iteration(g3, 1.5, .0001, 250)
# iteration(g4,1.5,.0001,250)
# iteration(g5,1.5,.0001,250)
