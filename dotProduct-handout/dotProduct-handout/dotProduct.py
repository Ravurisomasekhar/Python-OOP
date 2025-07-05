def readArray():
	a = []
	l = int(input())
	for i in range(l):
		a.append(int(input()))
	return a

def vectorSum(a,b):
	# your code goes here
	twosum = 0
	length = min(len(a),len(b))
	for i in range(length):
		h = a[i]*b[i]
		twosum += h
	return twosum



print(vectorSum(readArray(),readArray()))


