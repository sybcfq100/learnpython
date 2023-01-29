from operator import add, mul


# ''' Q1: Product '''
def product(n, term):
    result = 1
    for i in range(1, n + 1):
        result = mul(result, term(i))
    return result


# ''' Q2: Accumulate '''

identity = lambda x: x

square = lambda x: x * x

increment = lambda x: x + 1

triple = lambda x: 3 * x


def accumulate(combiner, base, n, term):
    result = base
    for i in range(1, n + 1):
        result = combiner(result, term(i))
    return result


print(accumulate(add, 0, 5, identity))
