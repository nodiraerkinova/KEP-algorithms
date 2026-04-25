n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    if (i + 1) % 2 == 1:
        print(a[i], end=' ') 