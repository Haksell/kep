def even_index_or_value(lst):
    return [x for i, x in enumerate(lst) if i & 1 == 0 or x & 1 == 0]
