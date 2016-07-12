"""
-------------------------------------------------------
basic_list_operations.py
A simple way to understand lists. 
Probably best suited for CP104.
-------------------------------------------------------
Author:  Rick Henderson
Email:   rhenderson@wlu.ca
__updated__ = "2016-05-26"
-------------------------------------------------------
"""

print("Lists in Python are indexed starting at 0.")

# A basic list for testing
data_test = [1, 2, 3]
print("The starting list we are using:")
print(data_test)

# Add an item to the List
print(
    "\nAdding 2 items to the list. Lists can contain mixed data types but we'll stick with just integers for now")
data_test.append(4)
data_test.append(6)

# Printing a List
print("\nNow the list contains:")
print(data_test)

# Removing an item from a list removes from the right/end of the list.
print("\nUse the pop() method to remove items from the list.")
value_removed = data_test.pop()
print("\nThe value removed is: {}.".format(value_removed))
print("\nSo a Python list is a LIFO object... like a Stack.")
print(
    "\nBut it is also more flexible because you can pop() or append() at any index position.")

# Remove the second item.
print("\nRemoving element at position/index 2...")
value_removed = data_test.pop(2)
print("\nThe value removed is: {}.".format(value_removed))
print("\nNow the list contains:")
print(data_test)

# Remove the "last item"
print(
    "You can also remove the last item in a list using the index [-1]. But it's the same as pop().")
value_removed = data_test.pop(-1)
print("\nNow the list contains:")
print(data_test)

# A way to print a list nicely. 
def a_print(a):
    # Author: David Brown
    for v in a[:-1]:
        print("{}".format(v), end=", ")
    print(a[-1])
    return
