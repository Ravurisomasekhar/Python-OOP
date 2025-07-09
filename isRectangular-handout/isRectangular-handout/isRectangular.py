def read2DArray():
    a = []
    l = int(input())
    for i in range(l):
        s = input().split(" ")
        t = []
        for j in range(len(s)):
            t.append(int(s[j]))
        a.append(t)
    return a

def isRectangular(l):
    for i in l:
        if len(i)!=len(l[0]):
            return False
    return True

print(isRectangular(read2DArray()))


