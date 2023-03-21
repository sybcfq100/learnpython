def linear_sum(s, n):
    if n == 0:
        return 0
    else:
        return linear_sum(s, n-1) + s[len(s)-1] 
s = [4,3,6,7,5]
print(s[4])
print(linear_sum(s, len(s)))
