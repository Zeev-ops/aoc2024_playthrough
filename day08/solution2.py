data = [list(line.strip()) for line in open('input.txt', 'r')]
antennaOccurences = {}
for i in range(len(data)):
  for j in range(len(data[0])):
    if data[i][j] == '.': continue
    if data[i][j] not in antennaOccurences:
      antennaOccurences[data[i][j]] = []
    antennaOccurences[data[i][j]].append((i, j))

antinodeOccurences = set() 
for signal, coord in antennaOccurences.items():
  if len(coord) == 1: continue
  for k in range(len(coord)):
    for l in range(k+1, len(coord)):
      diffI = coord[l][0] - coord[k][0]
      diffJ = coord[l][1] - coord[k][1]
      antinodeTop = (coord[k][0] - diffI, coord[k][1] - diffJ)
      while antinodeTop[0] >= 0 and antinodeTop[0] < len(data) and antinodeTop[1] >= 0 and antinodeTop[1] < len(data[0]):
        antinodeOccurences.add(antinodeTop)
        antinodeTop = (antinodeTop[0] - diffI, antinodeTop[1] - diffJ)
      antinodeBot = (coord[l][0] + diffI, coord[l][1] + diffJ)
      while antinodeBot[0] >= 0 and antinodeBot[0] < len(data) and antinodeBot[1] >= 0 and antinodeBot[1] < len(data[0]):
        antinodeOccurences.add(antinodeBot)
        antinodeBot = (antinodeBot[0] + diffI, antinodeBot[1] + diffJ)
for i in antennaOccurences:
  for j in antennaOccurences[i]:
    antinodeOccurences.add(j)
print(len(antinodeOccurences))