# 2178 * 4 = 8712
# stringni kesish va teskari o'girish
text = "abcd"
print(text[1 : 3])  # "bc"
print(text[0 : 4]) # "abcd"
print(text[0:: ]) # abcd
print(text[::-1]) # dcba

def reverse_number(num):
    # Raqamlarni stringga aylantirish, teskari o'girish va qayta raqamga aylantirish
    return int(str(num)[::-1])

print(reverse_number(2178))  # 8712

for number in range(1000, 10000):
    if number == reverse_number(number) * 4:
        print(number)