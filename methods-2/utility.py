# 19. Create Utility Module

# Create:

# utility.py

# Functions:

# even_or_odd()
# largest()

# Import and test.

def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def largest(*args):
    return max(args)