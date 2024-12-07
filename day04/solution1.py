data = [[x for x in line.strip()] for line in open('input.txt', 'r')]
xmas = 'XMAS'

def countHorizontal(array):
  count = 0
  for k, line in enumerate(array):
    for i in range(len(line)):
      if i+3 < len(line) and xmas == "".join(line[i:i+len(xmas)]):
        count += 1
  return count

def countDiagonal2LeftBottom(array):
  count = 0
  for i in range(len(array)):
    for j in range(len(array[0])):
      if i+3 < len(array) and j-3 >= 0:
        if array[i][j] == 'X' and array[i+1][j-1] == 'M' and array[i+2][j-2] == 'A' and array[i+3][j-3] == 'S':
          count += 1
  return count

result = countHorizontal(data) #left -> right
result += countHorizontal([line[::-1] for line in data]) #right -> left
result += countHorizontal([list(row) for row in zip(*data)]) #top -> bottom
result += countHorizontal([list(row) for row in zip(*data[::-1])]) #bottom -> top
result += countDiagonal2LeftBottom(data) #left -> right
result += countDiagonal2LeftBottom([line[::-1] for line in data]) #right -> left
result += countDiagonal2LeftBottom([line[::-1] for line in data[::-1]]) #bottom left -> top right
result += countDiagonal2LeftBottom(data[::-1]) #bottom -> top
print(result)