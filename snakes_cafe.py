# data structures containing lists of the various menu items and customer name
appetizers = ['Wings', 'Cookies', 'Spring Rolls']
entrees = ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden']
desserts = ['Ice Cream', 'Cake', 'Pie']
drinks = ['Coffee', 'Tea', 'Unicorn Tears']

customer_name = input("Please enter your name: ")

# an intro message and restaurant menu that gets displayed when program is invoked
MENU = f"""
***********************************************
**   Welcome, {customer_name}, to the Snakes Cafe!    **
**   Please see our menu below.              **
**                                           **
**   To quit at any time, type "quit"        **
***********************************************

Appetizers
----------
{appetizers[0]}
{appetizers[1]}
{appetizers[2]}

Entrees
-------
{entrees[0]}
{entrees[1]}
{entrees[2]}
{entrees[3]}

Desserts
--------
{desserts[0]}
{desserts[1]}
{desserts[2]}

Drinks
------
{drinks[0]}
{drinks[1]}
{drinks[2]}
"""

print(MENU)

order_prompt = """
***********************************
** What would you like to order? **
** Enter 'quit' when done        **
***********************************
"""

# the user input is assigned to item identifier.  Initially, it is blank so that 
# while loop can be entered into
item = ' '

# a dictionary to contain the item key, value of times ordered
customer_order = {} 

# user is prompted for an order and the order(s) are added to dictionary and 
# printed to show what was entered 
item = input(order_prompt)
while (item != 'quit'):
  if item not in customer_order:
    customer_order[item] = 1
  else:
    customer_order[item] += 1

  # checks if order is in the dictionary and increments value.  Also formats the
  # order plurals for the output message.
  for order in customer_order:
    if customer_order[order] > 1:
      order_plural = 'orders'
      have_plural = 'have'
    else:
      order_plural = 'order'
      have_plural = 'has'

    print(f'** {customer_order[order]} {order_plural} of {order} {have_plural} been added to your meal **')

  # prompt user again for another item to order
  item = input(order_prompt)

print(f'Thank you {customer_name} for visiting Snakes Cafe.')