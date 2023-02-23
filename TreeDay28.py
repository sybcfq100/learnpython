# Tree
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branch must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

t = tree(1, [tree(5, [tree(7)]), tree(6)])
#  print(t)
#  print(label(t))
#  print(branches(t)[0])
#  print(is_tree(branches(t)[0]))
#  print(label(branches(t)[0]))

def fib_tree(n):
    if  n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left)+label(right), [left, right])

#  print(fib_tree(4))

def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])

#  print(count_leaves(fib_tree(10)))
def leaves(tree):
    '''return a list containing the leaf labels of tree'''
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])

#  print(leaves(fib_tree(4)))

def increment_leaves(t):
    '''return a tree like t but with leaf labels incermented'''
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)

def increment(t):
    '''return a tree like t bunt with all labels incremented'''
    return tree(label(t)+1, [increment(b) for b in branches(t)])

def print_tree(t, indent=0):
    print('  '*indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent+2)

#  print_tree(fib_tree(4))

numbers = tree(3, [tree(4), tree(5, [tree(6)])])
haste = tree('h', [tree('a', [tree('s'), tree('t')]),tree('e')])

def print_sums(t, so_far):
    so_far = so_far + label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far)


print_sums(numbers, 0)
print_sums(haste, '')
