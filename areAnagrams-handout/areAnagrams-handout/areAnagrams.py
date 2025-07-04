def areAnagrams(s1, s2):
	s1 = s1.lower()
	s2 = s2.lower()
	dict1 = {}
	dict2 = {}
	for i in s1:
		if i not in dict1:
			dict1[i] = 1
		else:
			dict1[i] +=1
	for i in s2:
		if i not in dict2:
			dict2[i] = 1
		else:
			dict2[i] +=1
	# print(dict1)
	# print(dict2)
	return dict1 == dict2

print(areAnagrams(input(), input()))
