# data structures containing lists of the various menu items
appetizers = ['Wings', 'Cookies', 'Spring Rolls']
entrees = ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden']
desserts = ['Ice Cream', 'Cake', 'Pie']
drinks = ['Coffee', 'Tea', 'Unicorn Tears']

customer_name = input("Please enter your name: ")

# menu that get
MENU = f"""
***********************************************
**    Welcome, {customer_name}, to the Snakes Cafe!   **
**    Please see our menu below.             **
**
** To quit at any time, type "quit"          **
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

item = ' '
customer_order = {} # item key, value: # of times ordered

item = input(order_prompt)
while (item != 'quit'):
  if item not in customer_order:
    customer_order[item] = 1
  else:
    customer_order[item] += 1

  # for k, v in (customer_order.items()):
  #   print(k, v)

  for order in customer_order:
    if customer_order[order] > 1:
      order_plural = 'orders'
      have_plural = 'have'
    else:
      order_plural = 'order'
      have_plural = 'has'

    print(f'** {customer_order[order]} {order_plural} of {order} {have_plural} been added to your meal **')

  # prompt user again for another item
  item = input(order_prompt)

print(f'Thank you {customer_name} for visiting Snakes Cafe.')