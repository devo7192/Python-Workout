from string import ascii_lowercase

def gematria_for(word):
    # returns gematria score for a word
    score = 0
    gematria = {char: i for i, char in enumerate(ascii_lowercase, 1)}
    return sum(gematria.get(char, 0) for char in word)
    

def gematria_equal_words(userWord):
    # opens a file and returns a list of words whose gematria scores match the current word's score
    curScore = gematria_for(userWord)
    return [word.strip() for line in open('text.txt') for word in line.split() if gematria_for(word) == curScore]


print(gematria_equal_words('cat'))