#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # while all ingredients are greater than recipe minus ingredient deduct recipe amount from ingreaient
  # keep looping until deducting an ingredient from another would make it negative
  loop = True
  count = 0
  while loop == True:
    for ing in recipe.items():
      if not ingredients.get(ing[0]):
        loop = False
        break 

      summer = ingredients.get(ing[0]) - ing[1]
      if summer < 0:
        loop = False
        break

    if loop == True:
      for ing in recipe.items():
        ingredients[ing[0]] = ingredients[ing[0]] - ing[1]
      count += 1
  return count



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))