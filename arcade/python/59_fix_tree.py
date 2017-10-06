"""Fix the given tree by centering the asterisks in each line."""


def fix_tree(tree):
    return [x.strip().center(len(x)) for x in tree]
