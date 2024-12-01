with open('input.txt', 'r') as file:
  left, right = zip(*[(int(x), int(y)) for x, y in (line.split("   ") for line in file)])

sum = 0
for i, j in zip(sorted(left), sorted(right)):
  sum += abs(i - j)
print(sum)