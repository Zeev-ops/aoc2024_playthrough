from bisect import bisect_left, bisect_right

with open('input.txt', 'r') as file:
  left, right = zip(*[(int(x), int(y)) for x, y in (line.split("   ") for line in file)])

right = sorted(right)

checked = {}
sum = 0
for i in left:
  if i not in checked:
    lidx = bisect_left(right, i)
    ridx = bisect_right(right, i)
    counter = ridx - lidx
    checked[i] = i * counter
  sum += checked[i]
print(sum)