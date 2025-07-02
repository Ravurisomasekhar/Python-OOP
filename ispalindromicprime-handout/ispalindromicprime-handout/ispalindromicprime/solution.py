def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def isPalindromicPrime(n):
    return is_prime(n) and is_palindrome(n)

n = int(input())
print(isPalindromicPrime(n))
