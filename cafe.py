import random
import os

# TODO 
# make a random name generator so the player has to memorize those as well and call them out  

# Define the CafeItem class
class CafeItem:
    def __init__(self, name="", price=0):
        self.name = name
        self.price = price

    # Getter for the name attribute
    def get_name(self):
        return self.name
    
    # Setter for the name attribute
    def set_name(self, name):
        self.name = name
    
    # Getter for the price attribute
    def get_price(self):
        return self.price
    
    # Setter for the price attribute
    def set_price(self, price):
        self.price = price
#################################################### End Class

# prompt the user to continue
def go():
    input('\ncontinue...\n')

# generate a random order based on the list called cafe_menu
# append the randomized order to a new list and return it
def getorder():
    Cafe = []
    for i in range(guests):
        i = random.choice(cafe_menu)
        Cafe.append(i)
    return Cafe

# this function is calculating the prices for each item in a given order based on the cafe_prices and cafe_menu lists
# returns the prices dictionary, which contains the total cost for each item in the order
def getprice(order, cafe_prices):
    prices = {}
    for item in set(order):
        prices[item] = cafe_prices[cafe_menu.index(item)] * order.count(item)
    return prices

# create Cafe objects: coffee, latte, espresso, americano
COF = CafeItem('coffee', 2)
LAT = CafeItem('latte', 5)
ESP = CafeItem('espresso', 3)
AME = CafeItem('americano', 4)

# create 2 lists that contain the menu and prices
cafe_menu = [COF.get_name(), LAT.get_name(), ESP.get_name(), AME.get_name()]
cafe_prices = [COF.get_price(), LAT.get_price(), ESP.get_price(), AME.get_price()]    

# clear the screen
os.system("cls")

# global variable that stores the tips for the shift
MoneyMade = 0

# Header
print('Welcome to Python Cafe!')
print("\nIts your first day on the job so we are going to start you off on the register")
input("Press ENTER to continue...\n")

#main program
while True:
    #generates a random number of guests
    guests = 0
    guests = random.randrange(2,4)
    
    # clear the screen
    os.system("cls")
    print('Study the menu and prices, you will need this info when taking the order')
    go()
    
    os.system("cls")
    # print menu
    print(' ________________ ')
    print('|Menu            |')
    print('|                |')
    print('|Coffee         2|')
    print('|Latte          5|')
    print('|Espresso       3|')
    print('|Americano      4|')
    print('|________________|')
    go()
    os.system("cls")
    
    print(f'You have {guests} guests to attend to')
    go()
    os.system("cls")
    
    print('Be ready to take the Order')
    print('You will only have a few moments to memorize the order,\nso you can enter it into the system quickly')
    go()
    os.system("cls")
    
    
    # get our randomized list
    order = getorder()
    
    # print out the order
    print('Here is the itemized order: ')
    oidx = 0
    for itemized in order:
        oidx += 1
        print(f'{oidx}.{itemized}')
    go()
    os.system("cls")

    # prompt the user to enter each item and check if it matches each item in the list ()
    idx = 0
    for item in order:
        idx += 1
        enter_item = input(f"Enter item {idx}: ").strip().lower()
        if enter_item != item:
            print("Wrong order! You're fired!")
            exit()
    
    os.system("cls")
    print('Perfect! Now its time to get the bill ready')
    go()
    
    # get the correct prices for the order 
    prices = getprice(order, cafe_prices)
    
    # calculate the total price (use .values() [a dictionary function])
    totalprice = 0
    for price in prices.values():
        totalprice += price
    
    os.system("cls")
    print('The party is ready to pay,\nthey hand over a $50 bill at the register')
    go()
    os.system("cls")
    
    print('Looks like the register is down again!\nYoure gonna have to calculate the bill by hand')
    go()
    os.system("cls")
    
    # ask user to calculate the bill
    handcalc = input('Enter the total: ')

    # check if the bill is the correct amount
    if handcalc == str(totalprice): 
        print(f'The damage is ${totalprice}')
    elif len(handcalc.strip()) == 0:
        print('\nYou didnt even try!')
        print('Youre fired!')
        exit()
    else:
        print('\nWrong total!')
        print('Youre fired!')
        exit()


    go()
    os.system("cls")
    
    #make change for the customer that is paying with a 100 dollar bill
    change = 50 - totalprice
    handcalcchange = int(input('What is the guests change? '))
    if handcalcchange == change:
        print('Guests change is $',change)
    else:
        print('\nWrong change!')
        print('Youre fired!')
        exit()
    
    os.system("cls")
    # print the guests ticket
    print('\nThe guests ticket is printing,\nhand it to them along with their change')
    go()
    os.system("cls")
    
    print(' _______________')
    print('|Ticket         |')
    print('|               |')  
    print(f'|Total${totalprice}\t|')
    print('|               |')
    print(f'|Change${change}\t|')
    print('|               |')
    print('|Thnx!ComeAgain!|')
    print('|_______________|')
    
    # generate a random tip
    tip = random.randrange(1,10)
    print(f'The guests hand you a tip of ${tip}')
    
    # calculate the total in tips for the shift
    MoneyMade += tip
    
    # take another table?
    another = input('\nContinue the shift? (y/n) ')
    if another == 'n':
        os.system("cls")
        # return total tips after the shift is over
        print('Thats it? Well I hope this will cover your bills slacker! ')
        print(f'\nTotal tips for this shift ${MoneyMade}')
        break
    else:
        os.system("cls")
        continue
