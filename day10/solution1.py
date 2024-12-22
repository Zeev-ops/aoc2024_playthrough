def breathFirstSearch(x, y, map):
  pathwayCount = 0
  toCheck = [(x, y)]
  checkedHeads = set()

  while toCheck:
    x, y = toCheck.pop(0)
    if map[x][y] == 9 and (x, y) not in checkedHeads:
      pathwayCount += 1
      checkedHeads.add((x, y))
      continue
    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
      nx, ny = x + dx, y + dy
      if 0 <= nx < len(map) and 0 <= ny < len(map[0]) and map[nx][ny] - map[x][y] == 1:
        toCheck.append((nx, ny))
  return pathwayCount
        
map = [[int(i) for i in line.strip()] for line in open('input.txt', 'r')]
result = 0
for x in range(len(map)):
  for y in range(len(map[0])):
    if map[x][y] == 0:
      result += breathFirstSearch(x, y, map)
print(result)