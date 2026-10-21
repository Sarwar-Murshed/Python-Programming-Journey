list = [28,17,29,33]

# print(list.append(36))   prints none

# append method

list.append(36)   # append 36 in the last index
print(list)

# sort method

print(list.sort())  # none 
print("Ascending order : ",list)

print(list.sort(reverse = True))  # none 
print("Descending order : ",list)

# reverse method

print(list.reverse())  # none 
print("Reverse order : ",list)  # will reverse the updated list we got from descending order 

# updated list = 17, 28, 29, 33, 36

# insert method  --> insert(index,value)

list.insert(1,39)
print(list)

# [17, 39, 28, 29, 33, 36] updated list

list.append(39)   # [17, 39, 28, 29, 33, 36, 39]
print(list)

# remove(value) method

list.remove(39)   # remove the first occ of 39
print(list)

# pop(index) method --> removes the specific index of that value
# updated list [17, 28, 29, 33, 36, 39]

list.pop(2)    # removes 2nd idx (value 29)
print(list)

# copy method

x = list.copy()
print(x)

"""
summary 

list --> mutable which can be changed

1. append()
2. sort()
3. reverse()
4. insert()
5. remove()
6. pop()
7. copy()
"""