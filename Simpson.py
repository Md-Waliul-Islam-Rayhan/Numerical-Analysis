def f(x):
    return 1 / (1 + x ** 2)


def simpson13(x0, xn, n):
    h = (xn - x0) / n
    integration = f(x0) + f(xn)

    for i in range(1, n):
        xi = x0 + i * h

        if i % 2 == 0:
            integration = integration + 2 * f(xi)
        else:
            integration = integration + 4 * f(xi)
    integration = integration * h / 3

    return integration


lower_limit = float(input("Enter lower limit of integration: "))
upper_limit = float(input("Enter upper limit of integration: "))
sub_interval = int(input("Enter number of sub intervals: "))

result = simpson13(lower_limit, upper_limit, sub_interval)
print("Integration result by Simpson's 1/3 method is: %0.6f" % (result))
