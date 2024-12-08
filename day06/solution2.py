data = [list(line.strip()) for line in open('input.txt', 'r')]
directions = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}
next_direction = {'>': 'v', '<': '^', '^': '>', 'v': '<'}
startIdx = next((i, j) for i, row in enumerate(data) for j, char in enumerate(row) if char in directions)

def findLoops(data, rowIdx, colIdx):
  next = data[startIdx[0]][startIdx[1]]
  k, l = directions[next]
  path = set()
  while True:
    path.add((rowIdx, colIdx, k, l))
    if rowIdx+k < 0 or rowIdx+k >= len(data) or colIdx+l < 0 or colIdx+l >= len(data[0]):
      return False
    if data[rowIdx+k][colIdx+l] == "#":
      next = next_direction[next]
      k, l = directions[next][0], directions[next][1]
    else:
      rowIdx += k
      colIdx += l
    if (rowIdx, colIdx, k, l) in path:
      return True

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
      container.add((k, l))
      i, j = k, l
  else:
    break
count = 0
for pos in container:
  if data[pos[0]][pos[1]] != ".":
    continue
  data[pos[0]][pos[1]] = "#"
  if findLoops(data, startIdx[0], startIdx[1]):
    count += 1
  data[pos[0]][pos[1]] = "."

print(count)