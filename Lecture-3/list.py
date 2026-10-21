marks = [86.5, 41.33, 94.5, 67.8, 73.58]

print(marks)
print(type(marks)) # list type of marks
print(marks[0] , marks[3])   # prints 0th and 3rd index 
print(len(marks))

Student = ["Sarwar", "0112430410" , 3.60 , 23]
print(Student)

# After Changing the name

Student[0] = "Sajan"
print(Student)

# slicing 0 to 2 index

print("slicing 0 to 2 index : ",Student[ : 3])

# lists are mutable  that can be changed 
# arrays are immutable  that can not be changed 