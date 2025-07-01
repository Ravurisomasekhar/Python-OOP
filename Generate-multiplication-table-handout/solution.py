n,m  = input().split(" ")
n =int(n)
m= int(m)
def Multiplication(n,m):
    for i in range(1,m+1):
        print(n,"*",i,"=",n*i)
Multiplication(n,m)        