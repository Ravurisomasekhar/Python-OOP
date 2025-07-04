def leastFrequentLetters(s):
    s = s.lower()
    freq = {} 

    for ch in s:
        if ch.isalpha():  
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

    if not freq:
        return ""

   
    min_count = None
    for v in freq.values():
        if min_count is None or v < min_count:
            min_count = v


    result = ""
    for ch in "abcdefghijklmnopqrstuvwxyz":
        if ch in freq and freq[ch] == min_count:
            result += ch

    return result
