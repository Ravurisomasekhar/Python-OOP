n  = int(input())
def fun(n): # type: ignore
    fact = 1
    for i in range(1,n+1): # type: ignore
        fact *= i
    return fact
print(fun(n))