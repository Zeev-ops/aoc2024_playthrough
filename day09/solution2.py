diskInfo = open('input.txt', 'r').read().strip()
files = {}
space = []
globalPos = 0

for i, length in enumerate(diskInfo):
  length = int(length)
  if i % 2 == 0:
    files[i//2] = (globalPos, length)
  else:
    space.append((globalPos, length))
  globalPos += length

for i in range(len(files)-1, 0, -1):
  for j in range(min(i, len(space))):
    if space[j][0] >= files[i][0]:
      space = space[:j]
      break
    diff = space[j][1] - files[i][1]
    if diff >= 0:
      files[i] = (space[j][0], files[i][1])
      if diff == 0:
        space.pop(j)
      else:
        space[j] = (space[j][0] + files[i][1], diff)
      break

result = 0
for fileNum, (startIdx, length) in files.items():
  for adder in range(length):
    result += fileNum * (startIdx + adder)
print(result)