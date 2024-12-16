diskInfo = open('input.txt', 'r').read().strip()
files = [int(diskInfo[i]) for i in range(0, len(diskInfo), 2)]
space = [int(diskInfo[i]) for i in range(1, len(diskInfo), 2)]

result = 0
fileNumberFromLeft = 0
fileNumberFromRight = len(files)-1
globalPos = 0

while files:
  #add files from left
  result += sum(fileNumberFromLeft * (globalPos + i) for i in range(files[0]))
  globalPos += files[0]
  files.pop(0) 
  fileNumberFromLeft += 1 
  if not files: break

  #fill files from right in space
  while True:
    minResource = min(space[0], files[-1])
    result += sum(fileNumberFromRight * (globalPos + i) for i in range(minResource))
    globalPos += minResource

    diff = space[0] - files[-1]
    if diff < 0:
      space.pop(0)
      files[-1] = abs(diff)
      break
    elif diff > 0:
      files.pop()
      fileNumberFromRight -= 1
      space[0] = diff
    else:
      files.pop()
      fileNumberFromRight -= 1
      space.pop(0)
      break
print(result)