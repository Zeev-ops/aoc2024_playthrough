import re 

pattern = re.compile(r'mul\((\d+),(\d+)\)')
result = 0
with open('input.txt', 'r') as file:
  for line in file:
    m = pattern.findall(line)
    for i in m:
      result += int(i[0]) * int(i[1])

print(result)