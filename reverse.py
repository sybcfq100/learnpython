# def reverse(s, start, stop):
#     if start < stop - 1:
#         s[start], s[stop-1] = s[stop - 1], s[start]
#         reverse(s, start+1, stop -1)
#     return s
# a = [4,3,6,2,8,9,5]
# print(reverse(a, 0, len(a)))

def reverse_iterative(s):
    start, stop = 0, len(s)
    while start < stop - 1:
        s[start], s[stop-1] = s[stop-1], s[start]
        start, stop = start + 1, stop - 1
    return s
a = [4,3,6,2,8,9,5]
print(reverse_iterative(a))

