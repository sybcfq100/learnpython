def nats():
    curr = 0
    while True:
        curr += 1
        yield curr

def create_skip(n, gen):
    if n == 1:
        yield from gen
    curr, skip = 0, 1
    for elem in gen:
        if skip == n:
            skip = 1
        else:
            curr = curr + elem
            skip = skip + 1
            yield curr

def perfect_ngen(n):
    gen = create_skip(n, nats())
    while n > 1:
        n = n-1
        gen = create_skip(n , gen)

    return gen

two_gen = perfect_ngen(2)
three_gen = perfect_ngen(3)
print(next(two_gen))
print(next(two_gen))
print(next(two_gen))
print(next(three_gen))
print(next(three_gen))
print(next(three_gen))
