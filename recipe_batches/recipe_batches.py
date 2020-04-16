#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # Set the batches variable to 0
  # Set a variable to store the lowest number ( lowest_num )

  # While the length of both dictionaries are the same
  # While len(recipe) == len(ingredients)
    # Set a variable to store the results

    # For each key in recipe

      # Grab the value
      # Grab the value with the same key from ingredients
      # If the value of ingredients is greater than the value of recipe
        # ingredients // recipe
        # append the result to the results array

    # For left_item in results
      # For right_item in results

        # Set lowest_num to a low number

        # Compare to see which is the lowest

        # If left_item is less than right_item AND less than lowest_num
          # set lowest_num to left_item
        # elif right_item is less than left_item AND less than lowest_num: 
          # set lowest_num to right_item

    # Set batches to lowest_num

  # return batches
  pass 







a = {'foo': 1, 'bar': 2}
b = {'foo': 1, 'bar': 2}
c = {'bar': 2, 'foo': 1}
d = {'foo': 2, 'bar': 1}
e = {'foo': 1, 'bar': 2, 'baz':3}
f = {'foo': 1}

print(a.items() == b.items())
print(a.items() == c.items())
print(a.items() == d.items())
print(a.items() == e.items())
print(a.items() == f.items())

print(f"\na.item(): {a.items()}")


"""
if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
  """