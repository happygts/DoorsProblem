import argparse
import random
import numpy as np

def modifyArray(array, chosenIndex, indexPricelessGift):
  maskArray = np.ma.array(array, mask=False)
  otherIndex = chosenIndex

  if (chosenIndex == indexPricelessGift):
    otherIndex = random.choice([x for x in range(len(array)) if x != indexPricelessGift])

  for i in range(len(array)) :
    if i != otherIndex and i != chosenIndex :
      array[otherIndex] = 2
  
  return array

def simulate(doors):
  array = np.full(doors, 0, dtype=np.int)
  indexPricelessGift = random.choice([x for x in range(doors)])
  array[indexPricelessGift] = 1
  chosenIndex = random.choice([x for x in range(doors)])

  array = modifyArray(array, chosenIndex, indexPricelessGift)
  return array[chosenIndex] == 1

def run(doors, iteration) :
  totalSuccess = 0
  for i in range(iteration):
    if (simulate(doors)) :
      totalSuccess = totalSuccess + 1
  print(str(totalSuccess * 100 / iteration) + "%")

def parse():
  parser = argparse.ArgumentParser(description='Doors math problem.')
  parser.add_argument('-i', '--iteration', default=1000, help='Number of iteration', type=int)
  parser.add_argument('-d', '--doors', default=3, help='number of doors', type=int)

  args = parser.parse_args()

  doors = args.doors
  iteration = args.iteration
  run(doors, iteration)

parse()