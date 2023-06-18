def binary_sum(s, start, stop):
    if start >= stop:
        return 0
    elif start == stop - 1:
        return s[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(s, start, mid) + binary_sum(s, mid, stop)
    
s1 = list(range(10))
s2 = list(range(5))
s = s1 + s2
print(s)
print(binary_sum(s, 3, len(s)))
