n = int(input())
a = list(map(int, input().split()))
min_value = min(a)
position = a.index(min_value) + 1
print(position)

for i in range(n):
    if a[i] == min(a):
        print(i + 1, end=" ")
        break
