menu = ['Wings', 'Cookies', 'Spring Rolls', 'Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden', 'Ice Cream', 'Cake', 'Pie', 'Coffee', 'Tea', 'Unicorn Tears']

meal = []
def order():
    item = input(' ')
    # item = 'Wings'
    if item in menu:
        meal.append(item)
        meal_length = len(meal)
        print(f'** {meal_length} order of {item} have been added to your meal **')
        order()
    elif  item == 'quit':
        print(f'Your order is {meal}')
    else:
        print("""
This item is not in the menu, 
please choose from our menu!!""")
        order()



def customized_order():
    item = input(' ')
    if item in menu:
        meal.append(item)
        meal_length = len(meal)
        print(f'** {meal_length} order of {item} have been added to your meal **')
        customized_order()
    elif  item == 'quit':
        print(f'Your order is {meal}')
    else:
        print("""
This item is not in the menu, 
but dont worry, we will made it for you""")
        meal.append(item)
        meal_length = len(meal)
        print(f'** {meal_length} order of {item} have been added to your meal **')
        customized_order()
        


print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

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



def customizability():
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

customizability()
