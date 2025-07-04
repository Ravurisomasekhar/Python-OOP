
def hasBalancedParentheses(s):
	open = 0
	close = 0
	for i in s:
		if i == "(":
			open += 1
		elif i == ")":
			close += 1
	k = open+close
	return k%2 == 0
	

print(hasBalancedParentheses(input()))