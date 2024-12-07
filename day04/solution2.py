data = [[x for x in line.strip()] for line in open('input.txt', 'r')]

count = 0
for i in range(len(data)):
  for j in range(len(data[0])):
    xcount = 0
    if data[i][j] != 'A' or i-1 < 0 or j-1 < 0 or i+1 >= len(data) or j+1 >= len(data[i]):
      continue
    if data[i-1][j-1] == 'M' and data[i+1][j+1] == 'S':
      xcount += 1
    if data[i-1][j+1] == 'M' and data[i+1][j-1] == 'S':
      xcount += 1
    if data[i+1][j-1] == 'M' and data[i-1][j+1] == 'S':
      xcount += 1
    if data[i+1][j+1] == 'M' and data[i-1][j-1] == 'S':
      xcount += 1
    if xcount == 2:
      count += 1
print(count)