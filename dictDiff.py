def dictDiff(dict1, dict2):
    # function returns new dict that expresses the difference between two dicts
    difference = {}
    all_keys = dict1.keys() | dict2.keys() # | => union - result set is a set containing the unique keys from both dicts

    for key in all_keys:
        if dict1.get(key) != dict2.get(key):
            difference[key] = [dict1.get(key), dict2.get(key)]

    return difference


print(dictDiff({'a': 1,'b': 2,'d': 3}, {'a': 1,'b': 2,'d': 3}))
print(dictDiff({'a': 1,'b': 2,'c': 3}, {'a': 1,'b': 2,'c': 4}))
print(dictDiff({'a': 1,'b': 2,'d': 3}, {'a': 1,'b': 2,'c': 4}))
print(dictDiff({'a': 1,'b': 2,'c': 3}, {'a': 1,'b': 2,'d': 4}))
# print(dictDiff({'a': 1,'b': 2, 'c':3}, {'d':1,'e':2,'g':0,'r':99}))