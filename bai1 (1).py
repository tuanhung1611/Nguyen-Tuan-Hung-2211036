import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Nhập số nguyên dương n: "))
print(f"{n} là số nguyên tố" if is_prime(n) else f"{n} không phải số nguyên tố")

