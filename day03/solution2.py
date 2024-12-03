import re 

pattern1 = r'mul\((\d+),(\d+)\)'
pattern2 = r'don\'t\(\)'
pattern3 = r'do\(\)'
result = 0
isEnabled = True
with open('input.txt', 'r') as file:
  for line in file:
    for i in re.finditer(pattern1 + '|' + pattern2 + '|' + pattern3, line):
      print(i.group(0))
      if i.group(0).startswith('mul') and isEnabled:
        result += int(i.group(1)) * int(i.group(2))
      elif i.group(0).startswith("don"):
        isEnabled = False
      elif i.group(0).startswith('do'):
        isEnabled = True

print(result)