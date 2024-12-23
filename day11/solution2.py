from functools import cache
from concurrent.futures import ThreadPoolExecutor

@cache
def newStones(number, steps):
  if steps == 0: return 1
  if number == 0: return newStones(1, steps - 1)
  numDigits = len(str(number))
  if numDigits % 2 == 0:
    divisor = 10 ** (numDigits // 2)
    return newStones(number // divisor, steps - 1) + newStones(number % divisor, steps - 1)
  return newStones(number * 2024, steps - 1)

def parallelProcessing(stone):
  return newStones(stone, 75)

data = [int(item) for line in open('input.txt', 'r') for item in line.strip().split()]
result = 0
with ThreadPoolExecutor() as executor:
  results = list(executor.map(parallelProcessing, data))

print(sum(results))