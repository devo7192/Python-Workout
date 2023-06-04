import operator as op

def calc(to_solve):
    
    operations = {'+': op.add,
           '-': op.sub,
           '*': op.mul,
           '**': op.pow,
           '/': op.truediv,
           '%': op.mod }

    result = 0
    oper, first, second = to_solve.split(maxsplit=3)
            
    return operations[oper](int(first), int(second))
    

print(calc('- 3 44'))