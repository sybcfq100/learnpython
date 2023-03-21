def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


print(binary_search([2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37],34,0,15))
