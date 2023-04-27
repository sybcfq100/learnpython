def bad_fabonacci(n):
    if n <= 1:
        return n
    else:
        return bad_fabonacci(n-2) + bad_fabonacci(n-1)


def good_fabonacci(n):
    """ return pair of fibonacci numbers f(n) and f(n-1) """
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fabonacci(n-1)
        return (a+b, a)
    

print(good_fabonacci(7))
