import itertools

data = [line.strip().replace(':', '').split(' ') for line in open('input.txt', 'r')]
operators = ['+', '*', '||']
result = 0

for a, line in enumerate(data):
  print(a)
  if len(line) == 2:
    result += line[0]
  combinations = itertools.product(operators, repeat=len(line)-2)
  for combo in combinations:
    expression = line[1]
    for i in range(len(combo)):
      if combo[i] == '||': 
        expression = int(str(expression) + line[i+2])
      else: 
        expression = eval(f'{expression}{combo[i]}{line[i+2]}')
    if expression == int(line[0]):
      result += int(line[0])
      break
print(result)
