'''
This program is to demonstrate different ways in which we can reverse a list in Python.
This program was written by Christopher Scott on 30/08/2025.
'''

'''
Table of contents:
1. using List slicing
2. using the reversed() function
3. using a loop (creating a new reversed list)
4. using a loop (in-place reverse)
5. using list comprehension
6. which method is best?
'''

# 1. using List slicing
def reverse_with_slicing():
    # here is a static list of integers which we will reverse
    list_a = [1, 2, 3, 4, 5]
    
    # this 'rev' variable is assigned the reversed list using slicing
    rev = list_a[::-1]
    
    print("Reversed list using slicing:", rev)

# 2. using the reversed() function