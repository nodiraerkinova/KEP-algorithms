n = int(input())

s = 0

for _ in range(n):
    x = int(input()) 
    if x % 2 == 1:
        s += x

print(s) 