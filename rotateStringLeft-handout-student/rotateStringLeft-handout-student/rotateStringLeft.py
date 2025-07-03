def rotateStringLeft(s, n):
    if len(s) == 0:
        return s
    n = n % len(s)
    rotated = ""
    for i in range(n, len(s)):
        rotated += s[i]
    for i in range(n):
        rotated += s[i]
    return rotated

print(rotateStringLeft(input(), int(input())))
