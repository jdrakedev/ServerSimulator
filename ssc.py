import random
import os
import time

# TODO change the Theme to a CAFE!!! coffee, latte, espresso, americano

# Define the FoodItem class
class FoodItem:
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

# generate a random order based on the list called foodmenu
# append the randomized order to a new list and return it
def getorder():
    food = []
    for i in range(guests):
        i = random.choice(foodmenu)
        food.append(i)
        print(i, end=' ')
    return food

# this function is calculating the prices for each item in a given order based on the foodprices and foodmenu lists
# returns the prices dictionary, which contains the total cost for each item in the order
def getprice(order, foodprices):
    prices = {}
    for item in set(order):
        prices[item] = foodprices[foodmenu.index(item)] * order.count(item)
    return prices

# create food objects
HB = FoodItem('hamburger', 11)
NC = FoodItem('nachos', 8)
PZ = FoodItem('pizza', 20)
SA = FoodItem('salad', 10)

# create 2 lists that contain the menu and prices
foodmenu = [HB.get_name(), NC.get_name(), PZ.get_name(), SA.get_name()]
foodprices = [HB.get_price(), NC.get_price(), PZ.get_price(), SA.get_price()]    

# clear the screen
os.system("cls")

# global variable that stores the tips for the shift
MoneyMade = 0

print('\n\n')

# Header
print('Welcome to ServerSimulator,\nYou will receive a randomly generated order that will have to be entered correctly')
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
    print('|Pizza         20|')
    print('|Hamburger     11|')
    print('|Salad         10|')
    print('|Nachos         8|')
    print('|________________|')
    
    print('')
    print(f'You have been sat with {guests} guests')
    input('continue...\n')
    
    print('Be ready to take the Order')
    print('You will only have a few moments to memorize the order')
    input('continue...\n')
    
    print('Order: ')
    
    # get our randomized list
    order = getorder()
    
    # convert list to a string
    orderstring = ' '.join(order)
    
    # give the user an alloted time to memorize the order
    countdown = '\n12345'
    for c in countdown:
        time.sleep(1)
        print(c)

    # clear the screen
    os.system("cls")
    
    # user is prompted to enter the randomly generated order
    enterorder = input('\nWhat is the order?\n(add a space between each item) ')
    if enterorder == orderstring:
        print("\nOrder up!")
    else:
        print("\nWrong order! Youre fired!")
        print('\n\n')
        exit()
    
    print('Lets wait for the guests to finish their meal')
    input('continue...\n')
    
    print('Perfect! Now its time to get the bill ready')
    input('continue...\n')
        
    print('Here is the itemized order: ')
    for itemized in order:
        print(itemized)
    
    # get the correct prices for the order 
    prices = getprice(order, foodprices)
    
    # calculate the total price (use .values() [a dictionary function])
    totalprice = 0
    for price in prices.values():
        totalprice += price
    
    print('\nThe party is ready to pay, they hand over a $100 bill at the register')
    input('continue...\n')
    
    print('\nLooks like the register is down again, gonna have to calculate the bill by hand')
    input('continue...\n')
    
    # ask user to calculate the bill
    handcalc = int(input('Enter the total: '))
    
    # check if the bill is the correct amount
    if handcalc == totalprice: 
        print(f'The damage is ${totalprice}')
    else:
        print('Wrong total!')
        print('Youre fired!')
        print('\n\n')
        exit()
    
    input('continue...\n')
    
    #make change for the customer that is paying with a 100 dollar bill
    change = 100 - totalprice
    handcalcchange = int(input('What is the guests change? '))
    if handcalcchange == change:
        print('Guests change is $',change)
    else:
        print('Wrong change!')
        print('Youre fired!')
        print('\n\n')
        exit()
    
    # print the guests ticket
    print('\nThe guests ticket is printing,\nhand it to them along with their change')
    input('continue...\n')
    
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
    tip = random.randrange(1,20)
    print(f'\nThe guests hand you a tip of ${tip}')
    
    # calculate the total in tips for the shift
    MoneyMade += tip
    
    # take another table?
    another = input('\nTake another table? (y/n) ')
    if another == 'n':
        # return total tips after the shift is over
        print('')
        print(f'Total tips for this shift ${MoneyMade}')
        print('\n\n\n')
        break
    else:
        print('\n\n')
        continue


    # # calculate the price (use .items() [a tuple function])
    # totalprice = 0
    # for item, price in prices.items(): #TEST
        # #print(f"{item}: ${price}")
        # totalprice += price