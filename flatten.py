def flatten(listOfLists):
    # flatten([[1,2], [3,4]]) returns [1, 2, 3, 4]
    # use list comprehension!
    return [oneElement for oneSublist in listOfLists for oneElement in oneSublist]

print(flatten([[1,2], [3,4]]))