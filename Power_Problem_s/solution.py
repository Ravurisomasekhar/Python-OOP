base,exponent= input().split(" ")
base = int(base)
exponent= int(exponent)
def Power(base,exponent):
    m=1
    if (exponent==0):
        return 1
    for i in range (exponent):
        m=m*base
    return m
print (Power(base,exponent))   

