# returns a set of all supervocalic words in a dict
# looser definition of what defines supervocalic - any word containing all five vowels (no order)
def get_sv(fileName):
    # with sets, the < operator returns true if vowels is a subset of word
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return {word.strip() for line in open(fileName) for word in line.split() if vowels < set(word.lower())} # strip removes whitespace to the left and right
    # word.lower() converts capital letters to lowercase letters


print(get_sv('sv.txt'))