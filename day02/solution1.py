report = [[int(num) for num in line.strip().split()] for line in open('input.txt', 'r')]

correct = 0
for r in report:
  if r == sorted(r) or r == sorted(r, reverse=True):
    diff = [abs(r[i] - r[i+1]) for i in range(len(r)-1)]
    if all(j >= 1 and j <= 3 for j in diff):
      correct += 1
print(correct)