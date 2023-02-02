# def sum_squares(a, b):
#     return square(a) + square(b)

# def f(x):
#     return x * x

# square = f
# y = sum_squares(2, 3)
# print(y)

def view(re):
    ice = 4
    def k(means):
        return re(means)
    return k

def review(pr):
    return re(pr * 2)

ice = 3
re = view(lambda pr: pr * ice)
print(review(1))