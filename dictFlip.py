# Exchanges key and value data in a dict

def flip_dict(dict):
    return {value: key for key, value in dict.items()}

simple = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(flip_dict(simple))