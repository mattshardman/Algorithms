#!/usr/bin/python

import sys

def making_change(amount, denominations):
  if amount == 0:
    return 1

  if amount < 0:
    return 0

  combinations = 0
  for coin in range(len(denominations)):
    if denominations[coin] > amount:
      break 
    combinations += making_change(amount - denominations[coin], denominations[coin:])
  
  return combinations

denominations = [1, 5, 10, 20, 50]

x = making_change(10, denominations)


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")