
MENU = {'chow mein': 12.99, 'beef and broccoli': 14.99, 'orange chicken': 11.99, 'egg rolls': 4.99}

def restaurant(menu):

    choice = ''
    total = 0

    while True:
        
        order = input('\nWhat would you like to order? ').strip() # removes leading and trailing whitespace
        if not order:
            break
        
        if order in menu:
            price = menu[order]
            total += price
            
        
        else:
            print(f'Sorry, we are all out of fresh {order}.\n')

restaurant(MENU)