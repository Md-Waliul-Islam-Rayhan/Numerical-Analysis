def false_position(f, a, b, TOL, N0):
    if f(a) * f(b) >= 0:
        print("False position method fails.")
        return None
    i = 1
    FA = f(a)
    print('  n', '        a', '        b', '           p', '           f(p)', )
    while i <= N0:
        p = a - f(a) * (b - a) / (f(b) - f(a))
        FP = f(p)
        print(format(i, '3d'), '  ', format(a, 'f'), '  ', format(b, 'f'), '  ',
              format(p, '10.8f'), '  ', format(f(p), '10.2e'))
        if FP == 0 or abs(f(p)) < TOL:
            FP = f(p)
            return print('The solution is ', p)
        i = i + 1
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p
    print('The method fails after N0 iterations')
    return None


f = lambda x: x ** 3 + 4 * x ** 2 - 10
false_position(f, 1, 2, .0001, 25)
