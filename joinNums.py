def join_numbers(interval):
    
    return ', '.join(str(x) for x in range(interval)) # join won't work on list of ints

print(join_numbers(15))