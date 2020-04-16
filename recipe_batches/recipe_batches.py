#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # Set the batches variable to 0
  batches = 0
  # Set a variable to store the lowest number ( lowest_num )
  lowest_num = 0

  # If the length of both dictionaries are the same
  if len(recipe) == len(ingredients):
    # Set a list to store the results
    results = []

    # For each key in recipe
    for key in recipe:
      # Grab the value
      recipe_value = recipe.get(key)
      # Grab the value with the same key from ingredients
      ingredients_value = ingredients.get(key)

      # If the value of ingredients is greater than the value of recipe
      if ingredients_value >= recipe_value:
        # ingredients // recipe
        result = ingredients_value // recipe_value
        # append the result to the results array
        results.append(result)

    # Set lowest_num to a low number
    if results != []:
      lowest_num = results[0]

    # For left_item in results
    for x in range(0, len(results)-1):
      # For right_item in results
      for y in range(x+1, len(results)-1):

        # Compare to see which is the lowest

        # If left_item is less than right_item AND less than lowest_num
        if results[x] < results[y] and results[x] < lowest_num:
          # set lowest_num to left_item
          lowest_num = results[x]
        # elif right_item is less than left_item AND less than lowest_num: 
        elif results[y] < results[x] and results[y] < lowest_num:
          # set lowest_num to right_item
          lowest_num = results[y]

    # Set batches to lowest_num
    batches = lowest_num

  # Return batches
  return batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
