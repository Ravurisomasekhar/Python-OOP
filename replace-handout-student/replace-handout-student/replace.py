def replace(s1, s2, s3):
    s = ""
    i = 0
    while i < len(s1):
        if s1[i:i+len(s2)] == s2:
            s += s3
            i += len(s2)
        else:
            s += s1[i]
            i += 1
    return s

print(replace(input(), input(), input()))
