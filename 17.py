# 1 - usul
# for son in range(1000, 10000):
#     # Raqamlarni ajratish
#     ming = son // 1000
#     yuz = (son // 100) % 10
#     on = (son // 10) % 10
#     bir = son % 10
    
#     yigindi = ming + yuz + on + bir
    
#     # Shart: yig‘indi juft bo‘lsa
#     if yigindi % 2 == 0:
#         print(son, end=" ")

# 2 - usul
for son in range(1000, 10000):
    # Raqamlarni ajratish va yig‘indi hisoblash
    yigindi = (son // 1000) + ((son // 100) % 10) + ((son // 10) % 10) + (son % 10)
    
    # Shart: yig‘indi juft bo‘lsa
    if yigindi % 2 == 0:
        print(son, end=" ")