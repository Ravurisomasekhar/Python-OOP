def readArray():
    s = input().split(" ")
    l = []
    for i in s:
        if len(i) != 0:
            l.append(int(i))
    return l

def smallestDifference(a):
    if len(a) < 2:
        return -1
    a.sort()
    min_diff = abs(a[1] - a[0])
    for i in range(1, len(a) - 1):
        diff = abs(a[i+1] - a[i])
        if diff < min_diff:
            min_diff = diff
    return min_diff

    
print(smallestDifference(readArray()))


