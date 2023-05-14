def first_last(sequence):
    # generic function that returns the first and last elements of a sequence
    return sequence[:1] + sequence[-1:] # sequence type preserved using slices - not indexes

print(first_last('abc'))
print(first_last([1, 2, 3, 4]))
print(first_last((1, 9.9, 'flp')))