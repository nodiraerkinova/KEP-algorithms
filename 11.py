n = int(input())
def is_prime(n):
    if n <= 1:
        return False
    
    for son in range(2, int(n**0.5) + 1):
        if n % son == 0:
            return False
    return True
#     if n < 1:
#         return False
    
#     # n = 15; 2, 3, 4, ... 14
#     for son in range(2, n):
#         if n % son == 0:
#             return False
#     return True

# print("YES" if is_prime(n) else "NO")
