import random
import os

# TODO change the Theme to a CAFE!!! coffee, latte, espresso, americano

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

# generate a random order based on the list called cafe_menu
# append the randomized order to a new list and return it
def getorder():
    Cafe = []
    for i in range(guests):
        i = random.choice(cafe_menu)
        Cafe.append(i)
        print(i, end=' ')
    return Cafe

# this fuLATtion is calculating the prices for each item in a given order based on the cafe_prices and cafe_menu lists
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
print("Its your first day on the job so we are going to start you off on the register")
input("enter to continue...\n")

#main program
while True:
    #generates a random number of guests
    guests = 0
    guests = random.randrange(2,4)
    
    print('Study the menu and prices, you will need this info when taking the order')
    input('continue...\n')
    
    # print menu
    print(' ________________ ')
    print('|Menu            |')
    print('|                |')
    print('|Coffee         2|')
    print('|Latte          5|')
    print('|Espresso       3|')
    print('|Americano      4|')
    print('|________________|')
    
    print('')
    print(f'You have {guests} to attend to')
    input('continue...\n')
    
    print('Be ready to take the Order')
    print('You will only have a few moments to memorize the order, so you can enter it into the system')
    input('continue...\n')
    os.system("cls")
    
    print('Order: ')
    # get our randomized list
    order = getorder()
    
    # convert list to a string
    orderstring = ' '.join(order)
    
    print("\n")
    input('continue...\n')

    # clear the screen
    os.system("cls")
    
    # user is prompted to enter the randomly generated order
    enterorder = input('\nWhat is the order? (add a space between each item)\n\nOrder: ')
    if enterorder == orderstring:
        print("\nOrder up!")
    else:
        print("\nWrong order! Youre fired!")
        exit()
        os.system("cls")
    
    print('Lets wait for the guests to finish their meal')
    input('continue...\n')
    os.system("cls")
    
    print('Perfect! Now its time to get the bill ready')
    input('continue...\n')
        
    print('Here is the itemized order: ')
    for itemized in order:
        print(itemized)
    
    # get the correct prices for the order 
    prices = getprice(order, cafe_prices)
    
    # calculate the total price (use .values() [a dictionary fuLATtion])
    totalprice = 0
    for price in prices.values():
        totalprice += price
    
    print('\nThe party is ready to pay, they hand over a $50 bill at the register')
    input('continue...\n')
    os.system("cls")
    
    print('\nLooks like the register is down again, gonna have to calculate the bill by hand')
    input('continue...\n')
    
    # ask user to calculate the bill
    handcalc = int(input('Enter the total: '))
    
    # check if the bill is the correct amount
    if handcalc == totalprice: 
        print(f'The damage is ${totalprice}')
    else:
        print('\nWrong total!')
        print('Youre fired!')
        exit()
    
    input('continue...\n')
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
    
    # print the guests ticket
    print('\nThe guests ticket is printing,\nhand it to them along with their change')
    input('continue...\n')
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
    print(f'\nThe guests hand you a tip of ${tip}')
    
    # calculate the total in tips for the shift
    MoneyMade += tip
    
    # take another table?
    another = input('\nTake another table? (y/n) ')
    if another == 'n':
        # return total tips after the shift is over
        print('')
        print(f'Total tips for this shift ${MoneyMade}')
        break
    else:
        os.system("cls")
        continue
