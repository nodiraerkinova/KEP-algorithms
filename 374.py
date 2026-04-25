n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] == min(a):
        print(i + 1, end=" ")
        break
