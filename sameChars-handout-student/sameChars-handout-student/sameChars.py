def sameChars(s1, s2):
    if not isinstance(s1, str) or not isinstance(s2, str):
        return False
    if s1 == "" and s2 == "":
        return True

    
    unique1 = ""
    for c in s1:
        if c not in unique1:
            unique1 += c

    
    unique2 = ""
    for c in s2:
        if c not in unique2:
            unique2 += c


    for c in unique1:
        if c not in unique2:
            return False

    
    for c in unique2:
        if c not in unique1:
            return False

    return True

# Input and output
print(sameChars(input(), input()))
