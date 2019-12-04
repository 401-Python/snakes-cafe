## Lab 01: Snakes Cafe

### Author: Alvian Joseph

### Links and Resources
* [PR](https://github.com/401-Python/snakes-cafe/pull/2)
* [![Build Status](https://www.travis-ci.com/alvian-401-advanced-javascript/lab-13-bearer-auth.svg?branch=master)](https://www.travis-ci.com/alvian-401-advanced-javascript/lab-13-bearer-auth)
* [front end]()

### Tasks
* When run, the program should print an intro message and the menu for the restaurant
* The restaurant’s menu should include appetizers, entrees, desserts, and beverages. At least 3 in each category
* The program should prompt the user for an order
* When a user enters an item, the program should print an acknowledgment of their input
* The program should tell the user how to exit

### Modules
#### snakes_cafe.py
  This file instantiates the ```Menu``` dictionary consisting of 4 keys representing a separate food category. The value of each key refers to an object with keys and values corresponding to a food, and an integer.

  Then, in order to more easily access the key/values within the Menu dictionary I create
  4 names, each corresponding to ```Menu[key]``` with key being one of the different food categories.

From here I define 2 simple functions, ```showMenu()``` and ```take_order()```
```showMenu()``` takes in no parameters and simply prints the items from the menu dictionary using 2 for loops. The outer for loop iterates through ```Menu.items()``` and prints the key for each, which correspond to a food category. The inner loop iterates through the values and prints the key for those, which correspond to a food item.

```take_order()``` takes in a single parameter, order, which will be a user input. This function loops through the list of keys(categories) created from the Menu dictionary. If the order is equal to any item on the menu, that menu item's int is incremented by 1 and the user is notified the item has been added to their cart.
The user is then prompted to either add another item, which calls the take_order() function again, or to checkout, which for now simply exits the program.
