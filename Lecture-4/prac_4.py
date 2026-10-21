"""
Figure out a way to store 9 and 9.0 as separate values in a set.
(You can take help of built-in data types.)
"""

# way 1 using string

print("way 1 -\n")
x = {9,"9.00"}
print(x)

# way 2 using pair in the form of tuples

values = {
    ("float",9.00),
    ("int",9)
}

print("\nway 2 -\n")

print(values)

