def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def digit_sum(num):
    total = 0
    while num > 0:
        total += num % 10
        num = num // 10
    return total

def nthTenlyPrime(n):
    count = -1 
    current = 2

    while True:
        if is_prime(current):
            if digit_sum(current) == 10:
                count += 1
                if count == n:
                    return current
        current += 1
n = int(input())        
print(nthTenlyPrime(n))
