#  Menu = {
# 'wings':  {
#    'category': 'Appetizers',
#    'inCart': 0
#  },
#  'cookies':  {
#    'category': 'Appetizers',
#    'inCart': 0
#  },
#  'spring rolls':  {
#    'category': 'Appetizers',
#    'inCart': 0
#  },

#  'Salmon': {
#    'category': 'Entrees',
#    'inCart': 0
#  },

#   'steak': {
#    'category': 'Entrees',
#    'inCart': 0
#  },

#   'salad': {
#    'category': 'Entrees',
#    'inCart': 0
#  },

#  'Ice Cream':  {
#    'category': 'Desserts',
#    'inCart': 0
#  },

#  'cake':  {
#    'category': 'Desserts',
#    'inCart': 0
#  },

#  'pie':  {
#    'category': 'Desserts',
#    'inCart': 0
#  },

#  'Coffee': {
#    'category': 'Drinks',
#    'Coffee': 0
#  },

#  'tea': {
#    'category': 'Drinks',
#    'inCart': 0
#  },

#  'apple juice': {
#    'category': 'Drinks',
#    'inCart': 0
#  }

#   }import sys

Menu = {
'Appetizers':  {
  #  'name': 'Appetizers',
   'wings': 0,
   'cookies': 0,
   'spring rolls': 0
 },

 'Entrees': {
  #  'name': 'Entrees',
   'Salmon': 0,
   'Steak': 0,
   'Meat Tornado': 0
 },

 'Desserts':  {
  #  'name': 'Desserts',
   'Ice Cream': 0,
   'Cake': 0,
   'Pie': 0
 },

 'Drinks': {
  #  'name': 'Drinks',
   'Coffee': 0,
   'Tea': 0,
   'Unicorn Tears': 0
 }

  }

appetizers = Menu['Appetizers']
drinks = Menu['Drinks']
desserts = Menu['Desserts']
entrees = Menu['Entrees']

categories = [appetizers, drinks, desserts, entrees]

def showMenu():
  
  print('*******************************')
  print('** Welcome to my janky code! **')
  print('** Please see menu below **')
  print('To quit at any time, type quit')
  print('*******************************')

  for key, val in Menu.items():
    print('------------')
    print(key) # Category
    print('------------')
    for key2, val2 in val.items():
        print(key2) # Food

def takeOrder(order):
    for category in categories:
      if order in category:
        category[order] +=1
        print(f"{category[order]} order of {order} has been added to your meal")
        done = input('type y to add more items, type quit to checkout')
        if done == 'y':
          takeOrder(order = input("type an item from the menu to order"))
        elif done == 'quit':
          sys.exit()
        else:
          print('invalid response, system crashing')



showMenu()
takeOrder(order = input("type an item from the menu to order"))
