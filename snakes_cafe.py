# print('Hola')

appetizers = ['Wings', 'Cookies', 'Spring Rolls']
entrees = ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden']
desserts = ['Ice Cream', 'Cake', 'Pie']
drinks = ['Coffee', 'Tea', 'Unicorn Tears']

customerName = input("Please enter your name: ")

MENU = f"""

***********************************************
**    Welcome, {customerName}, to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
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

# item = input(order_prompt)
while (item != 'quit'):
  item = input(order_prompt)

  if (item == 'quit'):
    break

  if item not in customer_order:
    customer_order[item] = 1
  else:
    customer_order[item] += 1

  for k, v in (customer_order.items()):
    print(k, v)


  for order in customer_order:
      # for order, value in customer_order:

    # for order in customer_order:
    # if value > 1:
    if customer_order[order] > 1:
      orderPlural = 'orders'
    else:
      orderPlural = 'order'
    print(f'** {customer_order[order]} {orderPlural} of {order} have been added to your meal **')
    # print(f'** {customer_order[order]} {orderPlural} of {item} have been added to your meal **')

# for k,v in (word_dict.items()):
  # print(k, v)
  
# for key in sorted(election_results):
    # print("%s %s" % (key, election_results[key]))

# customer_order[]


# for i in range(0, int(wordPairs)):
#   s = input().split()
#   keys.append(s[0])
#   values.append(s[1])