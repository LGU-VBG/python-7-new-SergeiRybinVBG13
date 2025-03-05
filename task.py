def merge_lists_to_dict(a=['tree', 'rock', 'river', 'cloud'], b=[300, 5, 100, 1]):
    zippyzap = zip(a, b)
    c = dict(zippyzap)
    return c
