"""
WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with 
an empty dictionary and add one by one. Use subject name as key and marks as value.
"""

marks = {}

x = int(input("Enter OOP marks  : "))
marks.update({"OOP" : x})

x = int(input("Enter DBMS marks : "))
marks.update({"DBMS" : x})

x = int(input("Enter DSA marks  : "))
marks.update({"DSA" : x})

print(marks)