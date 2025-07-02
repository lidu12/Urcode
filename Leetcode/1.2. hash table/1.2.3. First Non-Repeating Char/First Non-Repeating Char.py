def first_non_repeating_char(string):
    counts = {}

    # First pass: count each character
    for char in string:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    # Second pass: find first char with count 1
    for char in string:
        if counts[char] == 1:
            return char

    return None




print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""