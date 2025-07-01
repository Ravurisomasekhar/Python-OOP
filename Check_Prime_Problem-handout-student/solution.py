n = int(input())
def fun(n): # type: ignore
    if n == 0 or n == 1:
        return False
    for i in range(2,n+1): # type: ignore
        if n%i == 0:
            return False    
    return True
print(fun(n))