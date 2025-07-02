def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def isCarolPrime(n):
    m = 1
    while True:
        carol_number = (2 ** m - 1) ** 2 - 2
        if carol_number > n:
            break
        if carol_number == n and is_prime(n):
            return True
        m += 1
    return False

n = int(input())
print(isCarolPrime(n))
