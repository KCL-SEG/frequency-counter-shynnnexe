"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    for i in items:
        key = str(i)
        if key in frequencies:
            frequencies[key] += 1
        else:
            frequencies[key] = 1
                           
    return frequencies
