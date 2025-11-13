"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

def palindrome(x):
    l,r = 0, range(x)
    
    while l < r:
            l += 1
            r -= 1
    if(x < 0):
        return False
    return True

x = 121

print(palindrome(x))
    
