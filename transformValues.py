# Slight variation on map, one that that applies a function to each of the values of a dict

def transform_values(funct, dict):
    return {key: funct(value) for key, value in dict.items()}


simple = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(transform_values(lambda x: x*x, simple))