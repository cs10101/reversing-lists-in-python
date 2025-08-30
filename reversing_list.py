'''
This program is to demonstrate different ways in which we can reverse a list in Python.
This program was written by Christopher Scott on 30/08/2025.
'''

'''
Table of contents:
1. picking a method to reverse a list
2. using List slicing
3. using the reversed() function
4. using a loop (creating a new reversed list)
5. using a loop (in-place reverse)
6. using list comprehension
7. which method is best?
'''

def main():
    
    keep_going = True
    while keep_going:
        choose_method()
        again = input("Do you want to reverse another list? (yes/no): ").strip().lower()
        if again != 'yes':
            keep_going = False
            print("Exiting the program. Goodbye!")

# 1. picking a method to reverse a list
# There are several ways to reverse a list in Python. Here are three common methods:
def choose_method():
    
    users_choice = input("Choose a method to reverse a list:\n1. List slicing\n2. reversed() function\n3. Loop (creating a new reversed list)\n4. Loop (in-place reverse)\n5. List comprehension\nEnter 1, 2, 3, 4, or 5: ")

    if users_choice == '1':
        reverse_with_slicing()
    elif users_choice == '2':
        reverse_with_reversed_function()
    elif users_choice == '3':
        reverse_with_loop_new_list()
    elif users_choice == '4':
        reverse_with_loop_in_place()
    elif users_choice == '5':
        reverse_with_list_comprehension()
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        choose_method()

# 2. using List slicing
def reverse_with_slicing():
    # here is a static list of integers which we will reverse
    list_a = [1, 2, 3, 4, 5]
    
    # this 'rev' variable is assigned the reversed list using slicing
    rev = list_a[::-1]
    
    print("Reversed list using slicing:", rev)

# 3. using the reversed() function
def reverse_with_reversed_function():
    # here is a static list of integers which we will reverse
    list_a = [1, 2, 3, 4, 5]
    
    # the reversed() function returns an iterator that accesses the given sequence in the reverse order
    rev = list(reversed(list_a))
    
    print("Reversed list using reversed() function:", rev)

# 4. using a loop (creating a new reversed list)
def reverse_with_loop_new_list():
    # here is a static list of integers which we will reverse
    list_a = [1, 2, 3, 4, 5]
    
    rev = []
    for item in list_a:
        rev.insert(0, item)  # insert each item at the beginning of the new list
    
    print("Reversed list using loop (new list):", rev)

# 5. using a loop (in-place reverse)
def reverse_with_loop_in_place():
    # here is a static list of integers which we will reverse
    list_a = [1, 2, 3, 4, 5]
    
    left_index = 0
    right_index = len(list_a) - 1
    
    while left_index < right_index:
        # swap the elements at left_index and right_index
        list_a[left_index], list_a[right_index] = list_a[right_index], list_a[left_index]
        left_index += 1
        right_index -= 1
    
    print("Reversed list using loop (in-place):", list_a)

# 6. using list comprehension
def reverse_with_list_comprehension():
    # here is a static list of integers which we will reverse
    list_a = [1, 2, 3, 4, 5]
    
    rev = [list_a[i] for i in range(len(list_a)-1, -1, -1)]
    
    print("Reversed list using list comprehension:", rev)

# 7. which method is best?
# The best method depends on the specific use case:
# - For simplicity and readability, list slicing is often preferred.
# - For memory efficiency, the in-place loop method is best.
# - For creating a new reversed list, the reversed() function is a good choice.
# - List comprehension is also a good option for creating a new reversed list, but it may be less efficient than the reversed() function.
# - The loop method that creates a new list is generally less efficient and less Pythonic than the other methods.
# You can call the choose_method function to let the user pick a method
main()