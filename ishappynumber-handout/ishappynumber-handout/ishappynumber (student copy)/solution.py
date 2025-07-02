def isHappyNumber(n):
    seen_numbers = set()  

    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        digits = [int(d) for d in str(n)]
        total = 0
        for digit in digits:
            total += digit * digit
        n = total
    return n == 1
n = int(input())
print(isHappyNumber(n))
