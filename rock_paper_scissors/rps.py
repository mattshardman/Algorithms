#!/usr/bin/python

import sys
from datetime import datetime

items = ['rock', 'paper', 'scissors']

def rock_paper_scissors(x):
  options = []

  def get_hand(arr, n):
    for i in range(len(items)): 
      arr.append(items[i])
      if x == n:
        options.append(arr[:])
      else:
        get_hand(arr, n + 1)
      arr.pop()
  get_hand([], 1)
  
  return options


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')