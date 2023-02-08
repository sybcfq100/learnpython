def split(n):
    return n // 10, n % 10

def sum_digits(n):
    if n < 10: # base case
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

#  print(sum_digits(2013))

def fact(n):
    return 1 if n <= 0 else n * fact(n-1)

#  print(fact(3))


def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total

#  print(fact_iter(3))

def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2*last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

print(luhn_sum(362))
