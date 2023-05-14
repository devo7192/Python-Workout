def ubbi_dubbi(word):

    translation = []

    for letter in word:
        if letter in 'aeiou':
            translation.append(f'ub{letter}')
        else:
            translation.append(letter)

    return ''.join(translation)


print(ubbi_dubbi('milk'))
print(ubbi_dubbi('octopus'))
print(ubbi_dubbi('elephant'))
