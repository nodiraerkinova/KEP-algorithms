# for i in range(100, 1000):
#     a = i // 100
#     b = (i // 10) % 10
#     c = i % 10

#     y = a + b + c
#     k = a * b * c

#     if k % y == 0:
#         print(i)

# 2-usul 
# Algoritm:
# 1. Uch xonali sonlarni tekshirish uchun 100 dan 999 gacha bo'lgan sonlar ustida aylantiring.
# 2. Raqamlar ko'paytmasi 
# 3. yig'indisini hisoblang.
def calc(number):
    p, s = 1, 0
    for digit in str(number):
        p *= int(digit)
        s += int(digit)

    return p, s

for number in range(100, 1000):
    p, s = calc(number)

    if p % s == 0:
        print(number)
