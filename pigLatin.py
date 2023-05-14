def pig_latin(word):

    if word == '':
        return

    if word[0] in 'aeiou':
        return f'{word}way'
    
    return word[1:] + word[0] + 'ay'


def pig_speak(sentence):

    translation = []
    for word in sentence.split():
        translation.append(pig_latin(word))

    return ' '.join(translation)


print(pig_latin('air'), 
      pig_latin('computer'))

print(pig_speak('all your base are belong to us'))
print(pig_speak('this is a test translation'))