n = input()
lst = map(int, input().split())
# s = 0
# for x in lst:
#     if x < 30 and x % 3 == 0:
#         print(x, end=" ")
#     else:
#         s += x

# print()
# print(s) 

for index in range(len(lst)):
    print(index, lst[index]) 