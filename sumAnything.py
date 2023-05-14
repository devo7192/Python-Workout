def mySum(*values): # splat operator accepts arbitrary number of arguments
    # generic function that sums n values together, regardless of data type - excluding sets and dicts 
    if not values:
        return values
    
    result = values[0]

    for item in values[1:]:
        result += item

    return result


print(mySum('abc', 'def'))
print(mySum(1, 2, 3, 4, 5))
print(mySum(1.89, 2.01, 3.21, 4.33, 5.6))
print(mySum([1, 2, 3], [4, 5, 6]))
print(mySum((1, 2, 3), (4, 5, 6)))

