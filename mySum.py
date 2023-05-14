def mySum(*numbers):    # splat operator
    
    sumResult = 0
    for x in numbers:
        sumResult += x
    
    return sumResult


print(mySum(1, 2, 3, 4))