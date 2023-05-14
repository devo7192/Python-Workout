def how_many_different_numbers(numbers):
    unique_numbers = set(numbers)   # returns a set with unique elements from numbers
    # print(unique_numbers)
    return len(unique_numbers)

print(how_many_different_numbers([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]))
print(how_many_different_numbers([1, 2, 3, 1, 2, 3, 4, 1]))