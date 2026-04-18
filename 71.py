# n = input()
# s = 0
# for r in n[:3]:
#     son = int(r)
#     s += son 
# t = 0
# for r in n[3:6]:
#     raqam = int(r)
#     t += raqam
# if s == t:
#     print("True")
# else:
#     print("False")   

# 2 - usul
def sum_digits(number):
    s = 0
    for digit in str(number):
        s += int(digit)
    return s

# print(sum_digits(123)) --> 6
n = input() # 123456
start = n[0:3] # 123
end = n[3:6] # 456
print(sum_digits(start) == sum_digits(end))