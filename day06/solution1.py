data = [list(line.strip()) for line in open('input.txt', 'r')]
directions = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}
next_direction = {'>': 'v', '<': '^', '^': '>', 'v': '<'}
startIdx = next((i, j) for i, row in enumerate(data) for j, char in enumerate(row) if char in directions)

container = set()
i, j = startIdx
nextDirection = data[i][j]

while True:
  di, dj = directions[nextDirection]
  k, l = i + di, j + dj
  if 0 <= k < len(data) and 0 <= l < len(data[i]):
    if data[k][l] == '#':
      nextDirection = next_direction[nextDirection]
      k, l = i, j
    else:
      container.add((k, l))  # Add to set
      i, j = k, l
  else:
    break
print(len(container))