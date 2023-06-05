from string import ascii_lowercase

def gematria():
    return {char: i for i, char in enumerate(ascii_lowercase, 1)}   # enumerate('abcdefghijklmnopqrstuv', start-> i=1)

print(gematria())