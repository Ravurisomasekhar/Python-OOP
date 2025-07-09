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

def isprime(j):
	if j == 0 or j == 1:
		return False
	for i in range(2,j):
		if j%i ==0:
			return False
	return True
	
def hasNoPrimes(l):
	for i in l:
		for k in i:
			if isprime(k):
				return False
	return True		

print(hasNoPrimes(read2DArray()))


