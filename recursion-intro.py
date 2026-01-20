# Recursion - A function that calls itself
# Every recursive function has two parts
# 1. Base Case - (When to stop) -> Eg. if this is a file, don't go deeper
# 2. Recursive Case - (Call itself) -> eg. if this is a folder, scan it

# Example 1 (Recursion with  numbers)

def countdown(n):
    if n == 0: # Base Case
        return
    
    print(n)
    countdown(n-1) # Recursive Call
    
countdown(10)

