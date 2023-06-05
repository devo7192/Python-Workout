# Pig latin translation of a file

def plword(word):
    if word[0] in 'aeiou':
        return f'{word}way'
    else:
        return f'{word[1:]}{word[0]}ay'


def pigLatin(fileName):
    return ' '.join(plword(word) for line in open(fileName) for word in line.split())


print(pigLatin('text.txt'))