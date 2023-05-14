from random import randint

def guessingGame():
    
    x = randint(0, 100)
    print(f'{x}')
    
    while True:

        userGuess = int(input('Guess what number has been chosen. '))

        if userGuess > x:
            print('Too high')
        elif userGuess < x:
            print('Too low')
        elif userGuess == x:
            print('Just right')
            break
    

guessingGame()