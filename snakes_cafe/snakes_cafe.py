
menu = ['wings', 'cookies', 'spring rolls', 'salmon', 'steak', 'meat Tornado', 'a literal garden', 'ice cream',
 'cake', 'pie', 'coffee', 'tea', 'unicorn tears']

meal = []


def order():
    '''This function doesn't take arguments and lets the customer order from the menu'''
    item = input(' ').lower()
    # item = 'Wings'
    if item in menu:
        meal.append(item)
        meal_length = len(meal)
        print(f'** order #{meal_length} : {item} has been added to your meal ** \n ')
        order()
    elif  item == 'quit':
        final_order = {}
        for i in meal:
            if not i in final_order:
                final_order[i] = 1
            else:
                final_order[i] +=1
        print(f' \n Your order is {final_order} \n')
    else:
        print("""
This item is not in the menu, 
please choose from our menu!!
""")
        order()


def customized_order():
    '''This function doesn't take arguments and lets the customer order any thing weather its included in the menu or not'''
    item = input(' ').lower()
    if item in menu:
        meal.append(item)
        meal_length = len(meal)
        print(f'** order #{meal_length} : {item} has been added to your meal ** \n')
        customized_order()
    elif  item == 'quit':
        final_order = {}
        for i in meal:
            if not i in final_order:
                final_order[i] = 1
            else:
                final_order[i] +=1
        print(f' \n Your order is {final_order} \n')
    else:
        print("""
This item is not in the menu, 
but dont worry, we will made it for you
""")
        meal.append(item)
        meal_length = len(meal)
        print(f'** order #{meal_length} : {item} has been added to your meal ** \n')
        customized_order()
        

def customizability():
    '''This function doesn't take arguments and let the customer choose between running the order and custom order functions'''
    is_custom = input('Do you want to order something that is not on the menu? (y/n)')
    if is_custom == 'n':
        print("""
Please strict with the inculed items in the menu

***********************************
** What would you like to order? **
***********************************
        """)
        order()
    elif is_custom == 'y':
        print("""
You can order items wether they are included in 
the menu or not, we will try our best :) 

***********************************
** What would you like to order? **
***********************************
        """)
        customized_order()
    else:
        print('Please enter (y) or (n)')
        customizability()


print("""
*************************************************
**          Welcome to the Snakes Cafe!        **
**          Please see our menu below.         **
**
** To submit and quit at any time, type "quit" **
*************************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
""")


customizability()
