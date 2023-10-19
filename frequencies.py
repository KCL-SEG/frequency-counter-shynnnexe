"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {} #creating empty list/dictionary

    for i in items:
        key = str(i) #turning inputs into string for consistency
        if key in frequencies: #check if key appears in frequency list
            frequencies[key] += 1 #if word has appeared, add 1 to the count
        else:
            frequencies[key] = 1 #else set count to 1

    return frequencies
