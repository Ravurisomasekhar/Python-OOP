def readArray():
	a = []
	l = int(input())
	for i in range(l):
		a.append(int(input()))
	return a

def alternatingSum(a):
	total = 0
	for i in range(len(a)):
		if i%2 ==0:
			total += a[i]
		else:
			total -= a[i]
	return total			


print(alternatingSum(readArray()))


