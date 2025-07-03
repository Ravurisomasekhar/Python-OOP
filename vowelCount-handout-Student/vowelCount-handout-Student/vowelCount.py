
def vowelCount(s):
	vowels = "aeiouAEIOU"
	count = 0
	for i in s:
		if i in vowels:
			count+= 1
	return count

print(vowelCount(input()))