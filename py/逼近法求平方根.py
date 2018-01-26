def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float

    returns the best guess when that guess is less than epsilon
    away from f(guess) or after 100 trials, whichever comes first.
    """
    guess = 1.0
    for i in range(100):
        if abs(f(guess) - guess) < epsilon:
            return guess
        else:
            guess = f(guess)
    return guess

'''a = fixedPoint(2.0, 0.001)
b = fixedPoint(0.0037475416347090202, 0.01)
c = fixedPoint(0.5001220703125, 0.0001)'''

def sqrt(a):
    def tryit(x):
        return 0.5 * (a/x + x)
    return fixedPoint(tryit, 0.0001)


def babylon(a):
    def test(x):
        return 0.5 * ((a / x) + x)
    return test


def sqrt(a):
    return fixedPoint(babylon(a), 0.000000000000001)
print(sqrt(1.4044068303877555394196723244008e-5))
print(sqrt(2))
print(sqrt(100))


