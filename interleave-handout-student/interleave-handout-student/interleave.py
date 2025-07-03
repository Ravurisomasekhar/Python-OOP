def interleave(s1, s2):
    s = ""
    max_len = max(len(s1), len(s2))
    for i in range(max_len):
        if i < len(s1):
            s += s1[i]
        if i < len(s2):
            s += s2[i]
    return s

print(interleave(input(), input()))
