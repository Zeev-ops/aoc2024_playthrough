def checkConditions(line):
  diff = all(1 <= abs(line[i] - line[i+1]) <= 3 for i in range(len(line)-1))
  return (line == sorted(line) or line == sorted(line, reverse=True)) and diff

def checkWithRemoval(line):
  if checkConditions(line):
    return True
  for i in range(len(line)):
    if checkConditions(line[:i] + line[i+1:]):
      return True
  return False

report = [[int(num) for num in line.strip().split()] for line in open('input.txt', 'r')]
correct = 0
for line in report:
  if checkWithRemoval(line):
    correct += 1
print(correct)