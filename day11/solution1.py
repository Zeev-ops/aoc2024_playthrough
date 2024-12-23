data = [item for line in open('input.txt', 'r') for item in line.strip().split()]

for i in range(25):
  next = []
  for stone in data:
    if stone == '0':
      next.append('1')
    elif len(stone) % 2 == 0:
      next.append(stone[:len(stone)//2])
      next.append(str(int(stone[len(stone)//2:])))
    else:
      next.append(str(int(stone) * 2024))
  data = next
print(len(data))