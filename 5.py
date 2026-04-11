import math

n = int(input())
y = 0

for i in range(1, n + 1):
    y += int(math.sqrt(i))

print(y) 