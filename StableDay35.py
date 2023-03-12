def stable(s, k, n):
    for i in range(len(s)):
        near = range(max(0, i-k), i)
        if any([abs(s[i]-s[j]) > n for j in near]):
            return False

    return True

print(stable([1,2,3,5,6], 1, 2))
print(stable([1,2,3,5,6], 2, 2))
print(stable([1,5,1,5,1], 2, 2))


def powers(n, k):
    def build(seed):
        if seed == 0:
            yield 0
        else:
            for x in build(seed // 10):
                yield x
                yield 10*x + seed %10

    yield from filter(curry2(is_power)(k, build(n)))


print(sorted(powers(12345,5)))
