def village(apple, t):
    def graft(t, bs):
         '''grafts the given branches bs onto each leaf of the given tree t, returning a new tree.'''
        if is_leaf(t):
            return tree(label(t), bs)
        new_branches = [graft(b, bs) for b in branches(t)]
        return tree(label(t), new_branches)
    base_t = apple(label(t))
    bs = [village(apple, b) for b in branches(t)]
    return graft(base_t, bs)


def tree(label, branches = []):
    '''construct a tree with the given label  value and a list of branches'''
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    '''return the label value of a tree.'''
    return tree[0]

t = tree[10, [tree(20), tree(30)]]
apple = lambda x: tree(x, [tree(x + 1), tree(x + 2)])
print_tree(village(apple, t))
