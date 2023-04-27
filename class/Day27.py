from math import gcd

def add_rational(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx*dy + ny*dx, dx*dy)

def mul_rational(x, y):
    return rational(numer(x)*numer(y), denom(x)*denom(y))

def rational_are_equal(x, y):
    return numer(x)*denom(y) == numer(y)*denom(x)

def print_rational(x):
    g = gcd(numer(x), denom(x))
    print(numer(x)//g, "/", denom(x)//g)

# Constructor and selectors

def rational(n, d): 
    def select(name):
        if name == 'n':
            return n
        elif name == 'd':
            return d
    return select
    #  return [n, d]

def numer(x):
    return x('n')
#  return x[0]

def denom(x):
    return x('d')
#  return x[1]
x, y = rational(2,3), rational(1,4)
print_rational(add_rational(x, y))
