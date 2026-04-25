n = int(input())
a = list(map(int, input().split()))
for x in a[::-1]:
    print(x, end=' ')
    