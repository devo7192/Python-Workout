    
def sum_numbers(toAdd):
    # only sums numbers - even if string contains non-numbers
    return sum(int(x) for x in toAdd.split() if x.isnumeric())


print(sum_numbers('aaa 1000 bb cc 4'))