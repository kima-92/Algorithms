#!/usr/bin/python

#import argparse

def find_max_profit(prices):
  # Set a results array
  results = []
  # Set a highest variable, to hold the highest profit
  highest = 0

  # Loop through the entire array from right to left (x)
  for x in range(len(prices)-1, 0, -1):   # Not sure if need len(prices)-1
    # Loop again to get the number to it's left (y)
    for y in range(x-1, 0, -1):
      # If current item is greater than it's adjacent
      if prices[x] > prices[y]:
        # current_item - adjacent_item
        result = prices[x] - prices[y]
        # add result to results list
        results.append(result)
      # else 
        # continue

  # Loop through the results array (x)
    # Loop though the same array starting from the next item to the right (y)
      # If current_item is greater than adjacent_item
        # Save in the highest variable

  # Return the highest variable

  return results


a = [32, 456, 452, 7, 456, 23, 124, 576, 34, 2]

print(find_max_profit(a))

"""
if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
  """