def readArray():
    a = []
    l = int(input())
    for i in range(l):
        a.append(int(input()))
    return a

def vectorSum(a,b):
    # your code goes here
    C = []
    for i in range (len(a)):
        C.append(a[i]+b[i])
    return C



print(vectorSum(readArray(),readArray()))


