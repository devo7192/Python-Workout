from collections import Counter

WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']
    
def most_repeating_letter_count(word):
    # shows how often each item appears in the string, from most common to least common, in a list of tuples
    return Counter(word).most_common(1)[0][1]   # optional most_common() param

def most_repeating_word(wordList):
    # returns the string that contains the greatest number of repeated letters
    return max(wordList, key=most_repeating_letter_count)


print(most_repeating_word(WORDS))
print(most_repeating_word(['let', 'the', 'goood', 'times', 'roll']))