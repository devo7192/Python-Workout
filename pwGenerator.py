import random

def create_password_generator(chars):

    def create_password(pwLength):
        output = []
        for i in range(pwLength):
            output.append(random.choice(chars))
        return ''.join(output)
    
    return create_password



alpha_password = create_password_generator('abcjhg')
print(alpha_password)
print(alpha_password(5))

symbol_password = create_password_generator('!@#$%')
print(symbol_password(10))
