def sum_squares(a, b):
    return square(a) + square(b)

def f(x):
    return x * x

square = f
y = sum_squares(2, 3)
print(y)