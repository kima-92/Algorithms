#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # Set a results array
  results = []
  # Set a highest variable, to hold the highest profit
  highest = 0

  # Loop through the entire array from right to left (x)
  for x in range(len(prices)-1, 0, -1):   # Not sure if need len(prices)-1
    # Loop again to get the number to it's left (y)
    for y in range(x-1, 0, -1):
      # current_item - adjacent_item
      result = prices[x] - prices[y]
      # add result to results list
      results.append(result)

      """
      # If current item is greater than it's adjacent
      if prices[x] > prices[y]:
        # current_item - adjacent_item
        result = prices[x] - prices[y]
        # add result to results list
        results.append(result)
      # else 
        # continue
        """

  # Set a higest base
  if results[0] > results[1]:
    highest = results[0]
  else:
    highest = results[1]

  # Loop through the results array (x)
  for x in range(0, len(results)-1):
    # Loop though the same array starting from the next item to the right (y)
    for y in range(x+1, len(results)-1):
      # If result != []:
      # If current_item is greater than adjacent_item
      if results[x] > results[y] and results[x] > highest:
        # Save in the highest variable
        highest = results[x]
      elif results[x] < results[y] and results[y] > highest:
        highest = results[y]
      # else:
        #highest = results[-2] - results[-1]

  # Return the highest variable
  print(f"\nThe results array is :\t{results}")
  return highest


a = [32, 456, 452, 7, 456, 23, 124, 576, 34, 2]

print(f"\nThe highest profit is:\t{find_max_profit(a)}")


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
 