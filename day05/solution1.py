data = [line.strip() for line in open('input.txt', 'r')]
splitidx = data.index('')
rules = [line.split('|') for line in data[:splitidx]]
order = [line.split(',') for line in data[splitidx+1:]]
result = 0
for o in order:
  expectedOrder = {}
  for page in o:
    for page in o:
      expectedOrder[page] = 0 
  for rule in rules:
    if rule[0] in o and rule[1] in o:
      expectedOrder[rule[0]] += 1
      expectedOrder[rule[1]] -= 1
  expectedOrder = dict(sorted(expectedOrder.items(), key=lambda item: item[1], reverse=True))
  isOrder = True
  for i, key in enumerate(expectedOrder.keys()):
    if o[i] != key:
      isOrder = False
      break
  if isOrder:
    result += int(o[len(o)//2])
print(result)
       
