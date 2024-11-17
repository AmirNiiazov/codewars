def same_structure_as(original, other):
    if not isinstance(original, list) or not isinstance(other, list) or len(original) != len(other):
        return False
    for x, y in zip(original, other):
        if type(x) != type(y) and x not in other:
            return False
        if isinstance(x, list) and isinstance(y, list):
            return same_structure_as(x, y)
    return True


print(same_structure_as([1, [1, 1], [1, 1], [1, 1], 2], [2, [2, 2], [2, 2], [2, 2], [2, 2]]))
